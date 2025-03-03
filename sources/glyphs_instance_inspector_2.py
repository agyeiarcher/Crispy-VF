import sys
import logging
import subprocess
import shutil
from pathlib import Path
from ufoLib2 import Font
from vanilla import Window, List, Button, TextBox
from AppKit import NSApplication
from fontTools.designspaceLib import DesignSpaceDocument

logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')


def inspect_H_width(glyphs_file_path):
    export_dir = Path("export")
    instances_dir = export_dir / "instances"
    export_dir.mkdir(exist_ok=True)
    instances_dir.mkdir(exist_ok=True)

    results = []
    axis_names = []

    try:
        subprocess.run([
            "fontmake",
            "-g", str(glyphs_file_path),
            "-o", "ufo",
            "--output-dir", str(export_dir)
        ], check=True)
        logging.info("Masters and Designspace exported successfully.")

        designspace_files = list(export_dir.glob("*.designspace"))
        if len(designspace_files) == 1:
            designspace_path = designspace_files[0]
            designspace = DesignSpaceDocument.fromfile(designspace_path)
            axis_names = [axis.name for axis in designspace.axes]
            instance_locations = {inst.name: inst.location for inst in designspace.instances}
        elif len(designspace_files) == 0:
            raise FileNotFoundError("No Designspace file found in export folder.")
        else:
            raise FileNotFoundError("Multiple Designspace files found in export folder.")

        subprocess.run([
            "fontmake",
            "-m", str(designspace_path),
            "-o", "ufo",
            "--output-dir", str(instances_dir)
        ], check=True)
        logging.info("Instance UFOs generated successfully.")

        ufo_files = {ufo.stem: ufo for ufo in instances_dir.glob("*.ufo")}

        for instance in designspace.instances:
            instance_name = instance.name
            sanitized_name = instance_name.replace(" ", "").replace("-", "").lower()

            matched_ufo = None
            for ufo_name, ufo_path in ufo_files.items():
                if sanitized_name in ufo_name.replace(" ", "").replace("-", "").lower():
                    matched_ufo = ufo_path
                    break

            if not matched_ufo:
                logging.error(f"UFO file for instance '{instance_name}' not found.")
                continue

            axes = instance.location
            logging.info(f"Processing instance: {instance_name} with axes {axes}")

            try:
                ufo = Font.open(matched_ufo)

                H_glyph = ufo.get("H")
                if H_glyph is None:
                    raise ValueError(f"Missing 'H' glyph in instance '{instance_name}'.")

                width = H_glyph.width
                result = {"Instance": instance_name}
                result.update({axis: axes.get(axis, "-") for axis in axis_names})
                result["H Width"] = width
                logging.info(f"'H' width in instance '{instance_name}': {width}")
                results.append(result)
            except Exception as e:
                logging.error(f"Failed to process instance '{instance_name}': {e}")

    except subprocess.CalledProcessError as e:
        logging.error(f"fontmake failed: {e}")
    except Exception as e:
        logging.error(f"Error during processing: {e}")
    finally:
        pass  # Cleanup moved to after UI closes

    return results, axis_names


class InspectorUI:
    def __init__(self, glyphs_file_path):
        self.export_dir = Path("export")
        self.glyphs_file_path = glyphs_file_path
        self.w = Window((800, 400), "Instance Width Inspector")
        self.w.list = List((10, 40, -10, -40), [], columnDescriptions=[])
        self.w.button = Button((10, -30, -10, 20), "Run Check", callback=self.run_check)
        self.w.status = TextBox((10, 10, -10, 20), "Ready")
        self.w.open()

    def run_check(self, sender):
        self.w.status.set("Running...")
        results, axis_names = inspect_H_width(self.glyphs_file_path)
        columns = [{"title": "Instance"}] + [{"title": axis} for axis in axis_names] + [{"title": "H Width"}]
        self.w.list.setColumnDescriptions(columns)
        self.w.list.set(results)
        self.w.status.set("Completed")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python glyphs_instance_inspector.py path/to/font.glyphs")
        sys.exit(1)

    glyphs_file_path = sys.argv[1]
    app = NSApplication.sharedApplication()
    InspectorUI(glyphs_file_path)
    try:
        app.run()
    finally:
        shutil.rmtree("export")
        logging.info("Export folder cleaned up.")
