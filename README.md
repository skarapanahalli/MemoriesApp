# Memories App - Developer/User Guide

## Introduction
This app was created to test new age Gen AI tools. You are welcome to try it out yourself, just use the `Prompt.md` 
But do note that depending on the AI tool you use, you many have to resolve by interacting with AI chat bot
If you just want to use the output, look at the installation section

## About Memories App
Welcome to Memories App! This application helps you relive your cherished memories by automatically creating daily slideshows from photos taken on the same day in previous years. Similar to the "On This Day" feature in Google Photos, Memories App brings your past moments back to life with beautiful slideshows set to music.

## Installation

### System Requirements
- Windows 10 or Windows 11 operating system
- At least 4GB of RAM
- At least 100MB of free disk space
- Python 3.8 or higher (included in the installer)
- Multiple Python packages are required (not an exhausive list)
  - moviepy
  - PyQt5
  - pillow

### Installation Steps (for Developer)
1. Clone the Github project to your PC 
2. Switch to your python environment
3. Use the requirements.txt to download the necessary python libraries
3. Open a command prompt and run installer\installer.bat
4. You should see the `MemoriesApp_Setup.exe` created
5. Double-click the `MemoriesApp_Setup.exe` on the target PC
6. Follow the on-screen instructions to complete the installation.
7. DO NOT LAUNCH the Memories App Configuration tool immediately after installation.
8. From the shortcuts created, open the Configuration as ADMINISTRATOR
9. Save the Configurations, it should create the scheduler job as well
10. Run the MemoriesApp from the shortcut as ADMINISTRATOR whenever you want to rescan your photos
10. Everytime you login, it should openup the newly created memories folder with subfolders containing slideshow for different days
11. Share the video files with friends & family
12. Share the `MemoriesApp_Setup.exe` with others
13. Note - This app has been tested only on Windows 11 OS

### Important Notes
1. `Running the app as Administrtor is mandatory, it will not work with regular user priviliges, as it tries to create windows scheduler task`
2. `This has been tested only on windows 11 with 24H2 updates`

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
- **Default Audio**: A default audio is included in the setup
- **Music File Path**: Select a music file to use as background music for the slideshows. You can use any MP3 or WAV file.

3. Click "Save Configuration" to save your settings.

## Using Memories App

### Automatic Operation

Once configured, Memories App will run automatically at the scheduled time each day:

1. The app will search for photos taken on the same day in previous years (based on your "Years Back" setting).
2. It will create a slideshow for each year specified, including random photos from that day.
3. The slideshows will be saved in the specified output folder, in a subfolder named with the current date (DD-MM-YYYY format).
4. Each time you log in to your computer, Windows Explorer will automatically open the current day's folder so you can view your memories.


### Changing Configuration

To change your configuration at any time:

1. Launch "Memories App Configuration" from the Start Menu.
2. Update your settings as needed.
3. Click "Save Configuration" to apply the changes.
4. Always remember to launch the App as ADMINISTRATOR

## Troubleshooting

### No Slideshows Generated

- Ensure your photo folder path is correct and contains photos.
- Check that the file dates on your photos are correctly set.
- If no photos are found for the exact date in previous years, the app will look up to 7 days earlier.
- Depending on the number of photos in your collection and the number of photos matching the configured criteria, the App may take several minutes to complete

### Video Playback Issues

- Ensure you have a compatible video player installed.
- Try changing the video format or codec in the configuration.
- Note, this is tested only on Windows 11 and Android phone(s)

### Scheduling Issues

- Make sure your computer is turned on at the scheduled time.
- Check the Windows Task Scheduler to ensure the Memories App task is properly registered.
- You should see a cmd window pop up everytime the scheduler is run - this is expected
- Always remember to launch and use the app as ADMINISTRATOR

## Uninstallation

To uninstall Memories App:

1. Open the Windows Control Panel.
2. Go to "Programs and Features" or "Apps & features".
3. Find "Memories App" in the list of installed programs.
4. Click "Uninstall" and follow the on-screen instructions.

## Support
If you encounter any issues or have questions about Memories App, log issues in github
`https://github.com/skarapanahalli/MemoriesApp`

## Manus.ai referal
If you want to try Manus.ai and need a referal, connect me in LinkedIn and message me your email Id and I can refer. 
My linkedIn profile is here
https://www.linkedin.com/in/skarapanahalli/


