
[Setup]
AppName=Memories App
AppVersion=1.0
DefaultDirName={pf}\MemoriesApp
DefaultGroupName=Memories App
OutputDir=.
OutputBaseFilename=MemoriesApp_Setup
Compression=lzma
SolidCompression=yes
SetupIconFile=icon.ico

[Files]
Source: "..\dist\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "config.ini"; DestDir: "{app}"; Flags: ignoreversion
Source: "DefaultAudio.mp3"; DestDir: "{app}"; Flags: ignoreversion
Source: "MemoriesApp.bat"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\Memories App"; Filename: "{app}\MemoriesApp.exe"; IconFilename: "{app}\icon.ico"
Name: "{group}\Memories App Configuration"; Filename: "{app}\MemoriesApp.exe"; Parameters: "--gui"; IconFilename: "{app}\icon.ico"
Name: "{commondesktop}\Memories App"; Filename: "{app}\MemoriesApp.exe"; IconFilename: "{app}\icon.ico"


[Run]
Filename: "{app}\MemoriesApp.exe"; Description: "Run Memories App Configuration"; Parameters: "--gui"; Flags: nowait postinstall skipifsilent
