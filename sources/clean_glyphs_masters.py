import sys
import os
import datetime
import shutil
import glyphsLib
import ufoLib2
import itertools
from fontTools.designspaceLib import DesignSpaceDocument, AxisDescriptor, SourceDescriptor, InstanceDescriptor
from ufoProcessor import DesignSpaceProcessor

def log(message):
    """Logs messages with timestamps."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] {message}")

# Define the parametric axes with proper tags, min/max values, and default positions
axes = {
    "Weight": ("WGHT", 1, 900, 450),
    "Width": ("WDTH", 1, 100, 50),
    "Grade": ("GRAD", -10, 10, 0),
    "X-Opacity": ("XOPQ", 2, 1016, 509),
    "Y-Opacity": ("YOPQ", 2, 462, 232),
    "X-Transparency": ("XTRA", 94, 3330, 1712),
}

def remove_existing_temp_ufo(output_dir):
    """Deletes the temp_ufo directory if it exists."""
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)
        log(f"Deleted existing {output_dir} directory.")

def convert_glyphs_to_ufo(input_path, output_dir):
    """Converts a Glyphs file to UFO + DesignSpace format and properly tags sources."""
    remove_existing_temp_ufo(output_dir)
    os.makedirs(output_dir, exist_ok=True)

    log(f"Converting {input_path} to UFO + DesignSpace")
    ufos = glyphsLib.load_to_ufos(input_path)
    designspace = DesignSpaceDocument()

    # Define axes in the DesignSpace
    for axis_name, (tag, min_value, max_value, default_value) in axes.items():
        axis = AxisDescriptor()
        axis.name = axis_name
        axis.tag = tag
        axis.minimum = min_value
        axis.maximum = max_value
        axis.default = default_value
        designspace.axes.append(axis)
        log(f"Added axis: {axis_name}, Tag: {tag}, Min: {min_value}, Max: {max_value}, Default: {default_value}")

    # ✅ Ensure all sources are properly appended
    source_list = []
    for i, ufo in enumerate(ufos):
        source = SourceDescriptor()
        source.filename = f"master_{i}.ufo"
        source.path = os.path.join(output_dir, source.filename)

        # Extract family name and style
        family_name = ufo.info.familyName or "UnnamedFont"
        style_name = ufo.info.styleName or f"Master{i}"

        source.familyName = family_name
        source.styleName = style_name
        source.name = f"{family_name}-{style_name}"

        source.copyLib = True
        source.copyGroups = True
        source.copyInfo = True
        source.copyFeatures = True

        # Assign axis locations
        source.location = {
            axis_name: default_value for axis_name, (_, _, _, default_value) in axes.items()
        }

        # Ensure UFO is saved
        if os.path.exists(source.path):
            os.chmod(source.path, 0o777)
            os.remove(source.path)
        ufo.save(source.path)

        log(f"✅ Adding source: Name={source.name}, File={source.filename}, Path={source.path}")
        log(f"📌 Location={source.location}")

        source_list.append(source)  # ✅ Append source to local list

    # ✅ Append all sources in one go to avoid incomplete writes
    designspace.sources.extend(source_list)

    # Debugging: Print sources to verify before writing
    log(f"✅ Final sources count: {len(designspace.sources)}")
    for src in designspace.sources:
        log(f"📌 Source in DesignSpace: {src.name}, File: {src.filename}, Location: {src.location}")

    # Save the DesignSpace file
    designspace_path = os.path.join(output_dir, "font.designspace")
    designspace.write(designspace_path)

    # ✅ Verify the saved file
    if os.path.exists(designspace_path):
        log(f"✅ DesignSpace file saved successfully at: {designspace_path}")
    else:
        log("🚨 Error: DesignSpace file was not written!")

    log("Conversion complete.")


def modify_designspace(output_dir):
    """Ensures sources are retained when modifying DesignSpace."""
    ds_path = os.path.join(output_dir, "font.designspace")
    log(f"Modifying DesignSpace: {ds_path}")

    if not os.path.exists(ds_path):
        log("Error: DesignSpace file not found. Skipping modification.")
        return

    # ✅ Load the existing DesignSpace file
    ds = DesignSpaceDocument.fromfile(ds_path)

    # ✅ Preserve existing sources instead of overwriting
    if not ds.sources:
        log("⚠️ Warning: No sources found in DesignSpace, re-adding masters.")
        for ufo_filename in os.listdir(output_dir):
            if ufo_filename.endswith(".ufo"):
                ufo_path = os.path.join(output_dir, ufo_filename)
                ufo = ufoLib2.Font.open(ufo_path)

                source = SourceDescriptor()
                source.filename = ufo_filename
                source.path = ufo_path
                source.familyName = ufo.info.familyName or "UnnamedFont"
                source.styleName = ufo.info.styleName or "Master"
                source.name = f"{source.familyName}-{source.styleName}"
                source.location = {
                    axis_name: (min_value + max_value) / 2
                    for axis_name, (_, min_value, max_value, _) in axes.items()
                }

                ds.sources.append(source)
                log(f"✅ Re-added missing source: {source.name}")

    # ✅ Debug: Print sources
    log(f"✅ Final sources count after modification: {len(ds.sources)}")
    for src in ds.sources:
        log(f"📌 Source: {src.name} → {src.filename}")

    # ✅ Save the DesignSpace file with preserved sources
    ds.write(ds_path)
    log(f"✅ DesignSpace file updated. Sources count: {len(ds.sources)}")


def convert_ufo_to_glyphs(output_dir, output_file):
    """Converts UFO + DesignSpace back into a Glyphs file."""
    log("Converting modified UFO + DesignSpace back to Glyphs format.")
    designspace_path = os.path.join(output_dir, "font.designspace")

    ds = DesignSpaceDocument.fromfile(designspace_path)
    
    font = glyphsLib.to_glyphs(ds)
    font.save(output_file)


def calculate_missing_masters(output_dir, designspace):
    """Calculates missing masters and generates interpolated UFOs."""
    ds_path = os.path.join(output_dir, "font.designspace")
    log(f"Checking for missing masters in: {ds_path}")

    # Ensure the designspace file exists before proceeding
    if not os.path.exists(ds_path):
        log("🚨 ERROR: DesignSpace file not found. Skipping interpolation.")
        return

    num_axes = len(designspace.axes)
    expected_masters = 2 ** num_axes  # 2^n masters required
    existing_masters = len(designspace.sources)

    log(f"✅ Expected Masters: {expected_masters}, Existing Masters: {existing_masters}")

    if existing_masters >= expected_masters:
        log("✅ All required masters exist. No interpolation needed.")
        return

    missing_masters = expected_masters - existing_masters
    log(f"⚠️ Missing {missing_masters} masters. Interpolating...")

    # Initialize the DesignSpaceProcessor
    processor = DesignSpaceProcessor()
    processor.read(ds_path)

    # Generate missing masters
    axis_ranges = {
        axis.name: [axis.minimum, axis.maximum] for axis in designspace.axes
    }

    missing_locations = list(itertools.product(*axis_ranges.values()))

    for i, location_values in enumerate(missing_locations):
        if i < existing_masters:
            continue  # Skip existing masters

        location_dict = {axis.name: value for axis, value in zip(designspace.axes, location_values)}

        # ✅ Generate interpolated glyph data
        interpolated_glyphs = processor.makeInstance(location_dict)

        if not interpolated_glyphs:
            log(f"🚨 ERROR: Interpolation failed at {location_dict}. Skipping...")
            continue

        # ✅ Create a new UFO font
        new_ufo = ufoLib2.Font()

        # ✅ Copy glyph data manually
        for glyph_name, glyph_data in interpolated_glyphs.items():
            new_glyph = new_ufo.newGlyph(glyph_name)
            new_glyph.width = glyph_data.get("width", 0)
            new_glyph.unicode = glyph_data.get("unicode", None)

            if "outline" in glyph_data:
                new_glyph.setData(glyph_data["outline"])

        # ✅ Save the interpolated master UFO
        master_filename = f"master_{existing_masters + i}.ufo"
        master_path = os.path.join(output_dir, master_filename)
        new_ufo.save(master_path)
        log(f"✅ Interpolated new master: {master_filename} at {location_dict}")

        # ✅ Add this new master to the DesignSpace
        new_source = SourceDescriptor()
        new_source.filename = master_filename
        new_source.path = master_path
        new_source.location = location_dict
        designspace.sources.append(new_source)

    # ✅ Save updated DesignSpace file
    designspace.write(ds_path)
    log(f"✅ DesignSpace updated with interpolated masters. Total sources: {len(designspace.sources)}")


def main(input_file, output_dir, output_file):
    """Main function to automate master generation using UFO and DesignSpace processing."""
    try:
        log(f"Starting process for: {input_file}")
        
        # Ensure the output directory exists
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
            log(f"Created output directory: {output_dir}")
        
        # Step 1: Convert Glyphs to UFO + DesignSpace
        convert_glyphs_to_ufo(input_file, output_dir)
        
        # Verify that the DesignSpace file exists
        ds_path = os.path.join(output_dir, "font.designspace")
        if not os.path.exists(ds_path):
            log("🚨 ERROR: DesignSpace file not found after conversion. Exiting.")
            return

        # Step 2: Modify the DesignSpace file to ensure sources are retained
        modify_designspace(output_dir)

        # Step 3: Load the DesignSpace and calculate missing masters
        designspace = DesignSpaceDocument.fromfile(ds_path)
        calculate_missing_masters(output_dir, designspace)

        # Save the updated DesignSpace file with new interpolated masters
        designspace.write(ds_path)
        log(f"✅ DesignSpace updated and saved at: {ds_path}")

        # Step 4: Convert the UFOs back to a Glyphs file
        convert_ufo_to_glyphs(output_dir, output_file)
        log(f"✅ Process complete. Modified Glyphs file saved at: {output_file}")

        # List the contents of the output directory for verification
        log("📁 Output directory contents:")
        for filename in os.listdir(output_dir):
            log(f" - {filename}")

    except Exception as e:
        log(f"🚨 ERROR: An unexpected error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 generate_glyphs_masters.py /path/to/input_file.glyphs /path/to/output_dir /path/to/output_file.glyphs")
        sys.exit(1)
    
    input_file_path = sys.argv[1]
    output_directory = sys.argv[2]
    output_file_path = sys.argv[3]
    
    main(input_file_path, output_directory, output_file_path)

