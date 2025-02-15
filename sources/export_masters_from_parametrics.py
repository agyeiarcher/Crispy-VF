import os
import sys
import shutil
import itertools
import ufoLib2
import glyphsLib
from fontTools.designspaceLib import DesignSpaceDocument, AxisDescriptor, SourceDescriptor
from ufoProcessor import DesignSpaceProcessor

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
    """Generates the 64 master UFOs based on parametric and derived axes."""
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
    log(f"Converting {input_glyphs} to UFOs")
    log(f"📂 Attempting to load Glyphs file: {input_glyphs}")
    ufos = glyphsLib.load_to_ufos(input_glyphs)
    
    master_count = 0
    
    for parametric_values in all_parametric_combinations:
        parametric_dict = dict(zip(parametric_axes.keys(), parametric_values))
        
        # Use an existing master as a template
        base_ufo = ufos[0]
        
        # Generate derived variations for each parametric master
        for derived_values in all_derived_combinations:
            derived_dict = dict(zip(derived_axes.keys(), derived_values))
            combined_dict = {**parametric_dict, **derived_dict}
            
            master_filename = f"master_{master_count}.ufo"
            master_path = os.path.join(output_dir, master_filename)
            
            # Duplicate parametric master and assign axis values
            new_ufo = ufoLib2.Font()
            new_ufo.layers = base_ufo.layers
            new_ufo.info = base_ufo.info
            new_ufo.lib = base_ufo.lib
            new_ufo.features.text = base_ufo.features.text
            new_ufo.save(master_path)
            
            source = SourceDescriptor()
            source.filename = master_filename
            source.path = master_path
            source.location = combined_dict
            designspace.sources.append(source)
            
            log(f"✅ Created {master_filename} at {combined_dict}")
            master_count += 1
    
    # Define axes in designspace
    for axis_name, (min_value, max_value) in {**parametric_axes, **derived_axes}.items():
        axis = AxisDescriptor()
        axis.name = axis_name
        axis.tag = axis_name[:4].upper()
        axis.minimum = min_value
        axis.maximum = max_value
        axis.default = (min_value + max_value) / 2
        designspace.axes.append(axis)
        log(f"✅ Added axis: {axis_name}, Min: {min_value}, Max: {max_value}, Default: {(min_value + max_value) / 2}")
    
    designspace_path = os.path.join(output_dir, "font.designspace")
    designspace.write(designspace_path)
    log(f"✅ DesignSpace file saved at {designspace_path}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 generate_64_masters.py /path/to/input_font.glyphs /path/to/output_masters")
        sys.exit(1)
    
    input_glyphs = sys.argv[1]
    output_dir = sys.argv[2]
    generate_masters(input_glyphs, output_dir)
