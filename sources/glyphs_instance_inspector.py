import sys
import logging
import subprocess
import shutil
from pathlib import Path
from ufoLib2 import Font
from vanilla import Window, List, Button, TextBox
from AppKit import NSApplication

logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')


def inspect_H_width(glyphs_file_path):
    export_dir = Path("export")
    instances_dir = export_dir / "instances"
    export_dir.mkdir(exist_ok=True)
    instances_dir.mkdir(exist_ok=True)

    results = []

    try:
        subprocess.run([
            "fontmake",
            "-g", str(glyphs_file_path),
            "-o", "ufo",
            "--interpolate",
            "--instance-dir", str(instances_dir)
        ], check=True)
        logging.info("Instance UFOs generated successfully.")

        for ufo_path in instances_dir.glob("*.ufo"):
            instance_name = ufo_path.stem
            logging.info(f"Processing instance: {instance_name}")

            try:
                ufo = Font.open(ufo_path)

                H_glyph = ufo.get("H")
                if H_glyph is None:
                    raise ValueError(f"Missing 'H' glyph in instance '{instance_name}'.")

                width = H_glyph.width
                logging.info(f"'H' width in instance '{instance_name}': {width}")
                results.append({"Instance": instance_name, "H Width": width})
            except Exception as e:
                logging.error(f"Failed to process instance '{instance_name}': {e}")

    except subprocess.CalledProcessError as e:
        logging.error(f"fontmake failed: {e}")
    except Exception as e:
        logging.error(f"Error during processing: {e}")
    finally:
        shutil.rmtree(export_dir)
        logging.info("Export folder cleaned up.")

    return results


class InspectorUI:
    def __init__(self, glyphs_file_path):
        self.glyphs_file_path = glyphs_file_path
        self.w = Window((400, 300), "Instance Width Inspector")
        self.w.list = List((10, 40, -10, -40), [], columnDescriptions=[{"title": "Instance"}, {"title": "H Width"}])
        self.w.button = Button((10, -30, -10, 20), "Run Check", callback=self.run_check)
        self.w.status = TextBox((10, 10, -10, 20), "Ready")
        self.w.open()

    def run_check(self, sender):
        self.w.status.set("Running...")
        results = inspect_H_width(self.glyphs_file_path)
        self.w.list.set(results)
        self.w.status.set("Completed")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python glyphs_instance_inspector.py path/to/font.glyphs")
        sys.exit(1)

    glyphs_file_path = sys.argv[1]
    app = NSApplication.sharedApplication()
    InspectorUI(glyphs_file_path)
    app.run()
