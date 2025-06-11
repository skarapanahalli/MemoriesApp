pyinstaller -F -w --add-data "installer\config.ini;." --add-data "installer\DefaultAudio.mp3;." --add-data "installer\icon.ico;." --icon=installer\icon.ico --name=MemoriesApp main.py 
"C:\Program Files (x86)\Inno Setup 6\ISCC.exe" "installer\MemoriesApp.iss"
