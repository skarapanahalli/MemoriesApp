# Memories App

A Windows application that creates daily slideshows from photos taken on the same day in previous years, similar to the "On This Day" feature in Google Photos.

## Features

- **Automatic Slideshow Generation**: Creates slideshows from photos taken on the same day in previous years.
- **Configurable Settings**: Customize years to look back, number of photos, display duration, and more.
- **Background Music**: Add your music to your slideshows.
- **Scheduled Execution**: Runs automatically once a day at a configurable time.
- **Auto-Display**: Opens the memories folder automatically when you log in.
- **User-Friendly GUI**: Easy-to-use interface for configuration.
- **One-Click Installation**: Simple installer for Windows 10 and Windows 11.

## Project Structure

- `config.ini`: Configuration file for all app settings.
- `config_manager.py`: Handles reading and writing to the configuration file.
- `slideshow_generator.py`: Core logic for selecting photos and creating slideshows.
- `music_downloader.py`: Handles music file management.
- `gui.py`: Graphical user interface for configuration.
- `scheduler.py`: Windows Task Scheduler integration.
- `main.py`: Main entry point for the application.
- `installer.py`: Creates the installer package.
- `help.md`: User guide and documentation.

## Requirements

- Windows 10 or Windows 11
- Python 3.8 or higher
- Required Python packages:
  - moviepy
  - PyQt5
  - pillow

## Installation

1. Download the `MemoriesApp_Setup.exe` installer.
2. Run the installer and follow the on-screen instructions.
3. Launch the Memories App Configuration tool to set up your preferences.

## Usage

See the `help.md` file for detailed usage instructions.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- MoviePy for video creation
- PyQt5 for the GUI
- PyInstaller for packaging

