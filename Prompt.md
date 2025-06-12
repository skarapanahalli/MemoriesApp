# Memories App

I have huge collection of photos on my computer, which is running windows 11 Operating System. 

I want to create an app which will allow me to relive memories like 'on this day X years back ' feature from google photos

## Programming Language and other choices:
- Use python as your primary language
- Use schtasks for creating Scheduled Tasks in windows

## Slide Show Generation:
- The App should create a slideshow video of the photos from same day X, Y, Z back, where X, Y, Z represents years in time and are configurable
 
- Keep the newly created slide show video in a folder called  'Memories'

- Each day create a new current day folder inside the 'Memories' with day month and year format as in DD-MM-YYYY

- If the same day does on X,Y,Z years back does not have any photos try going back till about 7 days to find photos

- Inside the current day folder create the slide show video with names [Memories_this_week_X-year(s)_back] [Memories_this_week_Y-years_back], [Memories_this_week_Z-years_back] where X, Y, Z  are configurable

- The input photos folder path from my computer should be configurable

- Choose a slideshow video file format which is playable across devices such as iPhones and Android phones in portrait mode, make the video codec configurable

- Add a little annimation for each photo, such as pan or zoom to make it more creative

- Limit to C random photos, where C is configurable

- Each photo in the video should displayed for S seconds, where S is configurable

- Include a license free popular tune or music clipping available from internet as audio background for the created video**

## Background music
- To make the slideshow more lively, add some background music. Download royalty free music from the internet and include the same into the slideshow
- Choose some pleasing instrumental music without being intimidating. The focus should be on the Photo display and not the music

## Configuration GUI
- All configurations should be present in an INI file 
- Give me a simple GUI for editing all the configuration options
- Create a default config.ini file for first time use with reasonable assumptions
- Give me a text box option to input the back in time years X,Y,Z
- Give me a text box to configure the maximum random photos number C 
- Give me a text box to indicate the number of seconds S for each photo should be displayed 
- Give me a checkbox to Create Scheduled Task, create or update the task if this checkbox is checked and delete the task if this checkbox is unchecked
- Give me a checkbox to create a startup folder entry for showing the today's slideshow folder
- If this checkbox is checked, create an entry in startup folder, so that the folder is opened everytime I login into my PC
- If this checkbox is un-checked remove the startup folder entry
- Give me an option to select the input photos folder. Give me a browse button to select the input folder
- Give me an option to select the output photos folder. Give me a browse button to select the output folder
- Give me a save button to save all the configurations

## Slideshow display
-Every time I login to my computer, I want the windows explorer to open the current day folder inside the Memories folder which will show me the slideshow videos that are created for that day. This will allow me to share the files to my friends and family

## Scheduling:
- This app should run once in a day at time T, where T is configurable
- Create a scheduled task in windows which will run the installed executable
- The Scheduled Task should be updated everytime there is change in relevant configuration options 

## Packaging and Installation
- Package the application with once click installation which includes all python dependencies
- Make sure this is compatible with both Windows 10 and Windows 11 devices
- Give me an easy to use Installer with Instalation wizard used for typical windows application
- Group appropriate python and configuration files in folders to organize the project
- Generate a nice and relevant icon file with .ico extention for my memories App executable
- Use this icon for the final MemoriesApp.exe and setup executable file 

## Help file
- Create a simple step-by-step help file on how to install and use this application from an end user perspective
- Create documentation for a developer to follow step by step to compile and create the final output installable
- I am using Visual studio code and Github, so I need the help files in markdown mark up language

## Training
- I want to test the App and I need data, so can you create for me about 50 random photos or images which will have the same day (modified file date) as today, but will be 1,2,3,5,10,15 years back
- Create these images with standard aspect ratios and resolutions that you will see in everyday photos from DSLR and mobile phones