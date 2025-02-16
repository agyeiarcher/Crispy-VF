import os
import copy
import sys
import shutil
import itertools
import ufoLib2
import glyphsLib
import subprocess
from fontTools.designspaceLib import DesignSpaceDocument, AxisDescriptor, SourceDescriptor
from ufoProcessor import DesignSpaceProcessor
from fontTools.pens.basePen import BasePen
from ufoLib2.objects.component import Component
from fontTools.pens.pointPen import PointToSegmentPen  # ✅ Import correct outline copying method

def log(message):
    """Logs messages for debugging."""
    print(f"[LOG] {message}")

# Define parametric masters (6 core masters based on X-Transparency, X-Opacity, and Y-Opacity)
parametric_axes = {
    "X-Transparency": [94, 3330],
    "X-Opacity": [2, 1016],
    "Y-Opacity": [2, 462],
}

# Define derived masters (8 possible variations per parametric master)
derived_axes = {
    "Weight": [1, 900],
    "Width": [1, 100],
    "Grade": [-10, 10],
}

def generate_masters(input_glyphs, output_dir):
    """Generates the 64 master UFOs based on parametric and derived axes and ensures a valid default master."""
    
    if not os.path.exists(input_glyphs):
        log(f"🚨 ERROR: Glyphs file '{input_glyphs}' not found! Exiting.")
        return
    
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)
    os.makedirs(output_dir, exist_ok=True)
    
    designspace = DesignSpaceDocument()
    all_parametric_combinations = list(itertools.product(*parametric_axes.values()))
    all_derived_combinations = list(itertools.product(*derived_axes.values()))

    # Convert Glyphs file to UFOs
    log(f"📂 Loading Glyphs file: {input_glyphs}")
    ufos = glyphsLib.load_to_ufos(input_glyphs)

    if not ufos:
        log("🚨 ERROR: No UFOs were generated from Glyphs file. Exiting.")
        return

    # ✅ Ensure correct mapping of parametric masters
    parametric_masters = {}
    for i, ufo in enumerate(ufos):
        master_filename = f"master_{i}.ufo"  # Ensure correct naming
        ufo_path = os.path.join(output_dir, master_filename)
        ufo.save(ufo_path)

        # ✅ Map each master to its corresponding parametric key
        if i < len(all_parametric_combinations):  # Ensure index does not exceed range
            parametric_key = all_parametric_combinations[i]
            parametric_masters[parametric_key] = ufo_path
            log(f"✅ Saved parametric master: {ufo_path} with key {parametric_key}")
        else:
            log(f"⚠️ WARNING: More UFOs than expected parametric masters!")

    master_count = len(parametric_masters)  # Start count from number of parametric masters

    # ✅ Define the Default Master
    default_master_values = {
        "X-Transparency": (94 + 3330) / 2,
        "X-Opacity": (2 + 1016) / 2,
        "Y-Opacity": (2 + 462) / 2,
        "Weight": (1 + 900) / 2,
        "Width": (1 + 100) / 2,
        "Grade": (-10 + 10) / 2,
    }

    # Select the closest existing master for default
    closest_master = min(
        parametric_masters.items(),
        key=lambda item: sum(abs(item[0][i] - default_master_values[axis]) for i, axis in enumerate(parametric_axes.keys()))
    )
    base_ufo_path = closest_master[1]
    base_ufo = ufoLib2.Font.open(base_ufo_path)

    default_master_filename = "master_default.ufo"
    default_master_path = os.path.join(output_dir, default_master_filename)

    default_ufo = ufoLib2.Font()
    default_ufo.info = base_ufo.info
    default_ufo.lib = base_ufo.lib
    default_ufo.features.text = base_ufo.features.text
    default_ufo.kerning = base_ufo.kerning

    # ✅ Copy all glyphs and ensure outlines and components are correctly copied
    for glyph_name in base_ufo.keys():
        if glyph_name not in default_ufo:
            new_glyph = default_ufo.newGlyph(glyph_name)
        else:
            new_glyph = default_ufo[glyph_name]

        base_glyph = base_ufo[glyph_name]
        new_glyph.width = base_glyph.width
        new_glyph.unicodes = base_glyph.unicodes
        new_glyph.lib = base_glyph.lib

        # ✅ Copy glyph outlines using drawPoints() to ensure proper outline transfer
        if hasattr(base_glyph, "drawPoints"):
            pen = new_glyph.getPointPen()
            base_glyph.drawPoints(pen)

        # ✅ Copy components properly
        new_glyph.clearComponents()
        for component in base_glyph.components:
            new_component = Component(baseGlyph=component.baseGlyph, transformation=component.transformation)
            new_glyph.components.append(new_component)

        log(f"✅ Copied glyph: {glyph_name}")

    # ✅ Save the new default master UFO
    default_ufo.save(default_master_path, overwrite=True)
    log(f"✅ Successfully saved {default_master_path} with all glyphs")

    default_source = SourceDescriptor()
    default_source.filename = default_master_filename
    default_source.path = default_master_path
    default_source.location = default_master_values
    default_source.familyName = base_ufo.info.familyName
    default_source.styleName = "Regular"

    designspace.sources.append(default_source)
    log(f"✅ Added default master at {default_master_values}")

    # ✅ Generate additional interpolated masters
    for parametric_values in all_parametric_combinations:
        parametric_dict = dict(zip(parametric_axes.keys(), parametric_values))

        base_ufo_path = parametric_masters.get(parametric_values)
        if not base_ufo_path:
            log(f"🚨 ERROR: No parametric master found for {parametric_values}. Skipping...")
            continue

        base_ufo = ufoLib2.Font.open(base_ufo_path)

        for derived_values in all_derived_combinations:
            derived_dict = dict(zip(derived_axes.keys(), derived_values))
            combined_dict = {**parametric_dict, **derived_dict}

            master_filename = f"master_{master_count}.ufo"
            master_path = os.path.join(output_dir, master_filename)

            if os.path.exists(master_path):
                log(f"🛑 Skipping {master_filename}, already exists.")
                continue

            new_ufo = ufoLib2.Font()
            new_ufo.info = base_ufo.info
            new_ufo.lib = base_ufo.lib
            new_ufo.features.text = base_ufo.features.text
            new_ufo.kerning = base_ufo.kerning

            # ✅ Copy all glyphs correctly
            for glyph_name in base_ufo.keys():
                base_glyph = base_ufo[glyph_name]
                new_glyph = new_ufo.newGlyph(glyph_name)

                new_glyph.width = base_glyph.width
                new_glyph.unicodes = base_glyph.unicodes
                new_glyph.lib = base_glyph.lib

                # ✅ Properly copy outlines
                if hasattr(base_glyph, "drawPoints"):
                    pen = new_glyph.getPointPen()
                    base_glyph.drawPoints(pen)

                # ✅ Properly copy components
                new_glyph.clearComponents()
                for component in base_glyph.components:
                    new_component = Component(baseGlyph=component.baseGlyph, transformation=component.transformation)
                    new_glyph.components.append(new_component)

            new_ufo.save(master_path)
            log(f"✅ Created {master_filename} at {combined_dict}")

            source = SourceDescriptor()
            source.filename = master_filename
            source.path = master_path
            source.familyName = base_ufo.info.familyName
            source.styleName = f"Variation {master_count}"

            # ✅ Ensure each master is mapped to the correct axes and convert location values explicitly
            # ✅ Ensure each master is mapped to the correct axes explicitly
            source.location = {str(axis): float(combined_dict[axis]) for axis in combined_dict if axis in {**parametric_axes, **derived_axes}}

            designspace.sources.append(source)


            master_count += 1

    designspace_path = os.path.join(output_dir, "font.designspace")
    designspace.write(designspace_path)
    log(f"✅ DesignSpace file saved at {designspace_path}")

def main():
    if len(sys.argv) < 3 or len(sys.argv) > 4:
        print("Usage: python3 generate_64_masters.py /path/to/input_font.glyphs /path/to/output_masters [optional_output_ttf]")
        sys.exit(1)
    
    input_glyphs = sys.argv[1]
    output_dir = sys.argv[2]
    
    generate_masters(input_glyphs, output_dir)

if __name__ == "__main__":
    main()
