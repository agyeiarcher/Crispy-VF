import sys
import csv
import glyphsLib
from collections import defaultdict

def find_matched_masters(glyphs_file_path):
    """Finds matched master pairs with the minimum X-Opacity and same X-Transparency."""
    
    # Load the font
    font = glyphsLib.load(glyphs_file_path)

    # Step 1: Extract Available Axes
    axes = {axis.name: axis.axisTag for axis in font.axes}
    
    # Step 2: Extract X-Opacity Values from Masters
    masters_data = {}
    x_opacity_values = []

    for master in font.masters:
        if len(master.axes) < 3:
            continue

        x_transparency = master.axes[0]  # Assuming first axis is X-Transparency
        x_opacity = master.axes[1]       # Assuming second axis is X-Opacity
        y_opacity = master.axes[2]       # Assuming third axis is Y-Opacity

        # Store both master name and UUID
        masters_data[master.id] = {
            "name": master.name,
            "uuid": master.id,  # Store UUID instead of ID
            "X-Transparency": x_transparency,
            "X-Opacity": x_opacity,
            "Y-Opacity": y_opacity
        }

        x_opacity_values.append(x_opacity)

    # Step 3: Find Minimum X-Opacity
    min_x_opacity = min(x_opacity_values) if x_opacity_values else None

    # Step 4: Group Masters by X-Transparency that have Min X-Opacity
    grouped_by_x_transparency = defaultdict(list)

    for master_id, data in masters_data.items():
        if data["X-Opacity"] == min_x_opacity:
            grouped_by_x_transparency[data["X-Transparency"]].append((master_id, data))

    # Step 5: Pair Masters with Same X-Transparency
    matched_pairs = []

    for x_transparency, masters in grouped_by_x_transparency.items():
        for i in range(len(masters) - 1):
            matched_pairs.append((masters[i], masters[i + 1]))

    print(f"\n🔍 Found {len(matched_pairs)} matched master pairs.")

    return font, matched_pairs

def find_layer(glyph, master_uuid):
    """Find the correct layer for a given master UUID."""
    for layer in glyph.layers:
        if layer.associatedMasterId == master_uuid:
            return layer
    return None  # No matching layer found

def analyze_glyph_widths(font, matched_pairs, output_csv_path):
    """Evaluates glyph width data for matched master pairs and writes to CSV."""

    csv_data = []

    for (master_A, data_A), (master_B, data_B) in matched_pairs:
        master_A_uuid = data_A["uuid"]
        master_B_uuid = data_B["uuid"]

        for glyph in font.glyphs:
            # Debugging: Print available layers for this glyph
            print(f"\n🔍 Checking glyph '{glyph.name}' in matched masters: {data_A['name']} & {data_B['name']}")
            print(f"  - Master A UUID: {master_A_uuid}, Master B UUID: {master_B_uuid}")
            print(f"  - Available layers: {[layer.associatedMasterId for layer in glyph.layers]}")

            # Find the correct layers using associatedMasterId
            layer_A = find_layer(glyph, master_A_uuid)
            layer_B = find_layer(glyph, master_B_uuid)

            if not layer_A or not layer_B:
                print(f"⚠️ Glyph '{glyph.name}' does not have layers for {data_A['name']} & {data_B['name']}")
                continue

            print(f"✅ Found layers for '{glyph.name}' - Processing widths.")

            # Extract glyph metrics
            advance_width_A = layer_A.width
            advance_width_B = layer_B.width

            # Handle missing outlines gracefully
            if layer_A.bounds:
                left_sb_A = layer_A.bounds.origin.x
                right_sb_A = layer_A.width - (layer_A.bounds.origin.x + layer_A.bounds.size.width)
            else:
                left_sb_A = 0  # Assume LSB is 0 if no outline
                right_sb_A = layer_A.width  # Assume RSB is the full advance width

            if layer_B.bounds:
                left_sb_B = layer_B.bounds.origin.x
                right_sb_B = layer_B.width - (layer_B.bounds.origin.x + layer_B.bounds.size.width)
            else:
                left_sb_B = 0  # Assume LSB is 0 if no outline
                right_sb_B = layer_B.width  # Assume RSB is the full advance width

            # Check if values match
            match_status = "Yes" if (
                advance_width_A == advance_width_B and 
                left_sb_A == left_sb_B and 
                right_sb_A == right_sb_B
            ) else "No"

            # Append data for this matched pair
            csv_data.append([
                glyph.name, data_A["name"], left_sb_A, right_sb_A, advance_width_A,
                data_B["name"], left_sb_B, right_sb_B, advance_width_B,
                match_status
            ])

    # Step 7: Save CSV Output
    with open(output_csv_path, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            "Glyph Name", "Master A", "Master A LSB", "Master A RSB", "Master A Adv Width",
            "Master B", "Master B LSB", "Master B RSB", "Master B Advance Width", "Match?"
        ])
        writer.writerows(csv_data)

    print(f"✅ CSV file generated: {output_csv_path} ({len(csv_data)} rows)")


# Command-line execution
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python check_widths_for_grade.py /path/to/font.glyphs /path/to/output.csv")
        sys.exit(1)

    glyphs_file = sys.argv[1]
    output_csv_path = sys.argv[2]

    font, matched_pairs = find_matched_masters(glyphs_file)
    analyze_glyph_widths(font, matched_pairs, output_csv_path)
