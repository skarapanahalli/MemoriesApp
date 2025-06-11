# Memories App - User Guide

## Introduction

Welcome to Memories App! This application helps you relive your cherished memories by automatically creating daily slideshows from photos taken on the same day in previous years. Similar to the "On This Day" feature in Google Photos, Memories App brings your past moments back to life with beautiful slideshows set to music.

## Installation

### System Requirements

- Windows 10 or Windows 11 operating system
- At least 4GB of RAM
- At least 100MB of free disk space
- Python 3.8 or higher (included in the installer)

### Installation Steps

1. Download the `MemoriesApp_Setup.exe` installer from the provided link.
2. Double-click the installer file to start the installation process.
3. Follow the on-screen instructions to complete the installation.
4. When prompted, you can choose to launch the Memories App Configuration tool immediately after installation.

## Initial Configuration

When you first run Memories App, you'll need to configure it according to your preferences:

1. Launch the Memories App Configuration tool from the Start Menu or Desktop shortcut.
2. Configure the following settings:

### App Configuration

- **Photo Folder Path**: Select the folder where your photos are stored. This can be any folder on your computer, including external drives.
- **Years Back**: Enter the number of years to look back for memories, separated by commas (e.g., "1,2,3" to create slideshows from 1, 2, and 3 years ago).
- **Random Photos Limit**: Set the maximum number of photos to include in each slideshow.
- **Photo Display Seconds**: Set how long each photo should be displayed in the slideshow.
- **Slideshow Output Folder**: Select the folder where the generated slideshows will be saved.
- **Schedule Time**: Set the time of day when the slideshow generation should run automatically.

### Video Configuration

- **Video Format**: Choose the format for the slideshow videos (MP4 recommended for best compatibility).
- **Video Codec**: Select the video codec (H.264/libx264 recommended for best compatibility).
- **Video FPS**: Set the frames per second for the video.
- **Video Bitrate**: Set the video quality (higher bitrate = better quality but larger file size).
- **Video Resolution**: Set the resolution of the video (1080x1920 recommended for portrait mode on mobile devices).

### Audio Configuration

- **Music File Path**: Select a music file to use as background music for the slideshows. You can use any MP3 or WAV file.

3. Click "Save Configuration" to save your settings.

## Using Memories App

### Automatic Operation

Once configured, Memories App will run automatically at the scheduled time each day:

1. The app will search for photos taken on the same day in previous years (based on your "Years Back" setting).
2. It will create a slideshow for each year specified, including random photos from that day.
3. The slideshows will be saved in the specified output folder, in a subfolder named with the current date (DD-MM-YYYY format).
4. Each time you log in to your computer, Windows Explorer will automatically open the current day's folder so you can view your memories.

### Manual Operation

You can also run Memories App manually:

1. Launch Memories App from the Start Menu or Desktop shortcut.
2. The app will immediately generate slideshows based on your configuration.

### Changing Configuration

To change your configuration at any time:

1. Launch "Memories App Configuration" from the Start Menu.
2. Update your settings as needed.
3. Click "Save Configuration" to apply the changes.

## Troubleshooting

### No Slideshows Generated

- Ensure your photo folder path is correct and contains photos.
- Check that the file dates on your photos are correctly set.
- If no photos are found for the exact date in previous years, the app will look up to 7 days earlier.

### Video Playback Issues

- Ensure you have a compatible video player installed.
- Try changing the video format or codec in the configuration.

### Scheduling Issues

- Make sure your computer is turned on at the scheduled time.
- Check the Windows Task Scheduler to ensure the Memories App task is properly registered.

## Uninstallation

To uninstall Memories App:

1. Open the Windows Control Panel.
2. Go to "Programs and Features" or "Apps & features".
3. Find "Memories App" in the list of installed programs.
4. Click "Uninstall" and follow the on-screen instructions.

## Support

If you encounter any issues or have questions about Memories App, please contact support at support@memoriesapp.example.com.

---

Thank you for using Memories App! We hope it brings joy as you rediscover your cherished memories.

