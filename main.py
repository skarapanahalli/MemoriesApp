import os
import sys
import datetime
from PyQt5.QtWidgets import QApplication
from config_manager import ConfigManager
from slideshow_generator import SlideshowGenerator
from gui import MemoriesAppGUI

def run_gui():
    """
    Run the GUI application for configuration.
    """
    app = QApplication(sys.argv)
    window = MemoriesAppGUI()
    window.show()
    sys.exit(app.exec_())

def generate_slideshows_for_years():
    """
    Generate slideshows based on the current configuration for each year back.
    """
    config_manager = ConfigManager("config.ini")
    generator = SlideshowGenerator("config.ini")
    
    years_back = [int(y) for y in config_manager.get_config("AppConfig", "years_back").split(",")]
    today = datetime.date.today()

    for year_offset in years_back:
        photos = generator.select_photos_for_year(year_offset)
        if photos:
            # New Naming convention: [Memories_This_Week_X_year(s)_back]
            year_suffix = "year" if year_offset == 1 else "years"
            output_filename = f"Memories_This_Week_{year_offset}_{year_suffix}_back.mp4"
            generator.create_slideshow(photos, output_filename=output_filename)
        else:
            print(f"No photos found for {year_offset} year(s) back.")

def main():
    """
    Main entry point for the application.
    """
    # Check if config.ini exists
    if not os.path.exists("config.ini"):
        print("Configuration file not found. Running GUI for initial setup.")
        run_gui()
        return

    # Check command line arguments
    if len(sys.argv) > 1 and sys.argv[1] == "--gui":
        run_gui()
    elif len(sys.argv) > 1 and sys.argv[1] == "--run-slideshow":
        generate_slideshows_for_years()
    else:
        # Default behavior if no specific argument is given, run slideshows
        # This is for when the scheduler calls it without arguments
        generate_slideshows_for_years()

if __name__ == "__main__":
    main()

