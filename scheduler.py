import subprocess
import os
import sys
import datetime

class Scheduler:
    def __init__(self, config_file_path):
        self.config_file_path = config_file_path

    def create_or_update_task(self, task_name, script_path, schedule_time):
        # Ensure the script_path is quoted to handle spaces
        quoted_script_path = f"\"{script_path}\""
        
        # The command to run the main script without the GUI
        action_command = f"{quoted_script_path} --run-slideshow"

        # Extract hour and minute from schedule_time (HH:MM)
        try:
            hour, minute = map(int, schedule_time.split(":"))
            if not (0 <= hour <= 23 and 0 <= minute <= 59):
                raise ValueError("Invalid time format")
        except ValueError:
            raise ValueError("Schedule time must be in HH:MM format (e.g., 18:00).")

        # Create or update the daily task
        command = [
            "schtasks",
            "/create",
            "/tn", task_name,
            "/tr", action_command,
            "/sc", "daily",
            "/st", schedule_time,
            "/f", 
            "/rl", "HIGHEST"
        ]
        
        try:
            result = subprocess.run(command, capture_output=True, text=True, check=True, shell=True)
            print(f"Task scheduling output: {result.stdout}")
            if result.stderr:
                print(f"Task scheduling error: {result.stderr}")
        except subprocess.CalledProcessError as e:
            raise Exception(f"Error scheduling task: {e.stderr}")
        except FileNotFoundError:
            raise Exception("schtasks command not found. This feature is only available on Windows.")

    def delete_task(self, task_name):
        command = [
            "schtasks",
            "/delete",
            "/tn", task_name,
            "/f"
        ]
        
        try:
            result = subprocess.run(command, capture_output=True, text=True, check=True, shell=True)
            print(f"Task deletion output: {result.stdout}")
            if result.stderr:
                print(f"Task deletion error: {result.stderr}")
        except subprocess.CalledProcessError as e:
            if "ERROR: The system cannot find the file specified." in e.stderr or "ERROR: The specified task name does not exist." in e.stderr:
                print(f"Task {task_name} does not exist, no need to delete.")
            else:
                raise Exception(f"Error deleting task: {e.stderr}")
        except FileNotFoundError:
            raise Exception("schtasks command not found. This feature is only available on Windows.")

    def create_startup_script(self, app_executable_path, slideshow_output_folder):
        # Get the Windows Startup folder path
        startup_folder = os.path.join(os.environ["APPDATA"], "Microsoft", "Windows", "Start Menu", "Programs", "Startup")
        
        # Create a batch file to open the current day's folder
        script_name = "OpenMemoriesFolder.bat"
        script_path = os.path.join(startup_folder, script_name)
        
        today_folder = datetime.date.today().strftime("%d-%m-%Y")
        full_path_to_open = os.path.join(slideshow_output_folder, today_folder)

        # Ensure the path exists before trying to open it
        # The script will try to open the folder, if it doesn't exist, it will just fail silently
        batch_content = f"@echo off\n"
        batch_content += f"start \"\" \"{full_path_to_open}\"\n"

        try:
            with open(script_path, "w") as f:
                f.write(batch_content)
            print(f"Startup script created at: {script_path}")
        except Exception as e:
            raise Exception(f"Error creating startup script: {e}")

    def delete_startup_script(self):
        startup_folder = os.path.join(os.environ["APPDATA"], "Microsoft", "Windows", "Start Menu", "Programs", "Startup")
        script_name = "OpenMemoriesFolder.bat"
        script_path = os.path.join(startup_folder, script_name)

        try:
            if os.path.exists(script_path):
                os.remove(script_path)
                print(f"Startup script deleted from: {script_path}")
            else:
                print("Startup script not found, no need to delete.")
        except Exception as e:
            raise Exception(f"Error deleting startup script: {e}")

