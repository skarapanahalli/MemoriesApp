import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QFileDialog, QMessageBox, QCheckBox
from config_manager import ConfigManager
from scheduler import Scheduler

class MemoriesAppGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.config_manager = ConfigManager("config.ini")
        self.scheduler = Scheduler("config.ini")
        self.init_ui()
        self.load_config()

    def init_ui(self):
        self.setWindowTitle("Memories App Configuration")
        self.setGeometry(100, 100, 600, 400)

        main_layout = QVBoxLayout()

        # AppConfig Section
        app_config_layout = QVBoxLayout()
        app_config_layout.addWidget(QLabel("<h2>Application Settings</h2>"))

        self.photo_folder_path_input = self._create_file_input_row("Photo Folder Path:", "photo_folder_path")
        app_config_layout.addLayout(self.photo_folder_path_input)

        self.years_back_input = self._create_text_input_row("Years Back (comma-separated):", "years_back")
        app_config_layout.addLayout(self.years_back_input)

        self.random_photos_limit_input = self._create_text_input_row("Random Photos Limit:", "random_photos_limit")
        app_config_layout.addLayout(self.random_photos_limit_input)

        self.photo_display_seconds_input = self._create_text_input_row("Photo Display Seconds:", "photo_display_seconds")
        app_config_layout.addLayout(self.photo_display_seconds_input)

        self.slideshow_output_folder_input = self._create_file_input_row("Slideshow Output Folder:", "slideshow_output_folder")
        app_config_layout.addLayout(self.slideshow_output_folder_input)

        self.schedule_time_input = self._create_text_input_row("Schedule Time (HH:MM):", "schedule_time")
        app_config_layout.addLayout(self.schedule_time_input)

        self.enable_scheduling_checkbox = QCheckBox("Enable Daily Slideshow Scheduling")
        app_config_layout.addWidget(self.enable_scheduling_checkbox)

        self.enable_startup_folder_open_checkbox = QCheckBox("Open Daily Memories Folder on Startup")
        app_config_layout.addWidget(self.enable_startup_folder_open_checkbox)

        main_layout.addLayout(app_config_layout)

        # VideoConfig Section
        video_config_layout = QVBoxLayout()
        video_config_layout.addWidget(QLabel("<h2>Video Settings</h2>"))

        self.video_format_input = self._create_text_input_row("Video Format:", "video_format", section="VideoConfig")
        video_config_layout.addLayout(self.video_format_input)

        self.video_codec_input = self._create_text_input_row("Video Codec:", "video_codec", section="VideoConfig")
        video_config_layout.addLayout(self.video_codec_input)

        self.video_fps_input = self._create_text_input_row("Video FPS:", "video_fps", section="VideoConfig")
        video_config_layout.addLayout(self.video_fps_input)

        self.video_bitrate_input = self._create_text_input_row("Video Bitrate:", "video_bitrate", section="VideoConfig")
        video_config_layout.addLayout(self.video_bitrate_input)

        self.video_resolution_input = self._create_text_input_row("Video Resolution (WxH):", "video_resolution", section="VideoConfig")
        video_config_layout.addLayout(self.video_resolution_input)

        main_layout.addLayout(video_config_layout)

        # AudioConfig Section
        audio_config_layout = QVBoxLayout()
        audio_config_layout.addWidget(QLabel("<h2>Audio Settings</h2>"))

        self.music_file_path_input = self._create_file_input_row("Music File Path:", "music_file_path", section="AudioConfig")
        audio_config_layout.addLayout(self.music_file_path_input)

        main_layout.addLayout(audio_config_layout)

        # MoviePyConfig Section
        moviepy_config_layout = QVBoxLayout()
        moviepy_config_layout.addWidget(QLabel("<h2>MoviePy Settings</h2>"))

        self.moviepy_temp_dir_input = self._create_file_input_row("MoviePy Temp Directory:", "moviepy_temp_dir", section="MoviePyConfig")
        moviepy_config_layout.addLayout(self.moviepy_temp_dir_input)

        main_layout.addLayout(moviepy_config_layout)

        # Save Button
        save_button = QPushButton("Save Configuration")
        save_button.clicked.connect(self.save_config)
        main_layout.addWidget(save_button)

        self.setLayout(main_layout)

    def _create_text_input_row(self, label_text, config_key, section="AppConfig"):
        layout = QHBoxLayout()
        label = QLabel(label_text)
        line_edit = QLineEdit()
        line_edit.setObjectName(f"{section}_{config_key}") # Set object name for easy access
        layout.addWidget(label)
        layout.addWidget(line_edit)
        return layout

    def _create_file_input_row(self, label_text, config_key, section="AppConfig"):
        layout = QHBoxLayout()
        label = QLabel(label_text)
        line_edit = QLineEdit()
        line_edit.setObjectName(f"{section}_{config_key}") # Set object name for easy access
        browse_button = QPushButton("Browse")
        browse_button.clicked.connect(lambda: self._browse_file_or_folder(line_edit, config_key))
        layout.addWidget(label)
        layout.addWidget(line_edit)
        layout.addWidget(browse_button)
        return layout

    def _browse_file_or_folder(self, line_edit, config_key):
        if "path" in config_key or "dir" in config_key:
            folder_path = QFileDialog.getExistingDirectory(self, "Select Folder")
            if folder_path:
                line_edit.setText(folder_path)
        elif "file" in config_key:
            file_path, _ = QFileDialog.getOpenFileName(self, "Select File")
            if file_path:
                line_edit.setText(file_path)

    def load_config(self):
        # AppConfig
        self.findChild(QLineEdit, "AppConfig_photo_folder_path").setText(self.config_manager.get_config("AppConfig", "photo_folder_path"))
        self.findChild(QLineEdit, "AppConfig_years_back").setText(self.config_manager.get_config("AppConfig", "years_back"))
        self.findChild(QLineEdit, "AppConfig_random_photos_limit").setText(self.config_manager.get_config("AppConfig", "random_photos_limit"))
        self.findChild(QLineEdit, "AppConfig_photo_display_seconds").setText(self.config_manager.get_config("AppConfig", "photo_display_seconds"))
        self.findChild(QLineEdit, "AppConfig_slideshow_output_folder").setText(self.config_manager.get_config("AppConfig", "slideshow_output_folder"))
        self.findChild(QLineEdit, "AppConfig_schedule_time").setText(self.config_manager.get_config("AppConfig", "schedule_time"))
        self.enable_scheduling_checkbox.setChecked(self.config_manager.get_config("AppConfig", "enable_scheduling").lower() == "true")
        self.enable_startup_folder_open_checkbox.setChecked(self.config_manager.get_config("AppConfig", "enable_startup_folder_open").lower() == "true")

        # VideoConfig
        self.findChild(QLineEdit, "VideoConfig_video_format").setText(self.config_manager.get_config("VideoConfig", "video_format"))
        self.findChild(QLineEdit, "VideoConfig_video_codec").setText(self.config_manager.get_config("VideoConfig", "video_codec"))
        self.findChild(QLineEdit, "VideoConfig_video_fps").setText(self.config_manager.get_config("VideoConfig", "video_fps"))
        self.findChild(QLineEdit, "VideoConfig_video_bitrate").setText(self.config_manager.get_config("VideoConfig", "video_bitrate"))
        self.findChild(QLineEdit, "VideoConfig_video_resolution").setText(self.config_manager.get_config("VideoConfig", "video_resolution"))

        # AudioConfig
        self.findChild(QLineEdit, "AudioConfig_music_file_path").setText(self.config_manager.get_config("AudioConfig", "music_file_path"))

        # MoviePyConfig
        self.findChild(QLineEdit, "MoviePyConfig_moviepy_temp_dir").setText(self.config_manager.get_config("MoviePyConfig", "moviepy_temp_dir"))

    def save_config(self):
        # AppConfig
        self.config_manager.set_config("AppConfig", "photo_folder_path", self.findChild(QLineEdit, "AppConfig_photo_folder_path").text())
        self.config_manager.set_config("AppConfig", "years_back", self.findChild(QLineEdit, "AppConfig_years_back").text())
        self.config_manager.set_config("AppConfig", "random_photos_limit", self.findChild(QLineEdit, "AppConfig_random_photos_limit").text())
        self.config_manager.set_config("AppConfig", "photo_display_seconds", self.findChild(QLineEdit, "AppConfig_photo_display_seconds").text())
        self.config_manager.set_config("AppConfig", "slideshow_output_folder", self.findChild(QLineEdit, "AppConfig_slideshow_output_folder").text())
        self.config_manager.set_config("AppConfig", "schedule_time", self.findChild(QLineEdit, "AppConfig_schedule_time").text())
        self.config_manager.set_config("AppConfig", "enable_scheduling", str(self.enable_scheduling_checkbox.isChecked()))
        self.config_manager.set_config("AppConfig", "enable_startup_folder_open", str(self.enable_startup_folder_open_checkbox.isChecked()))

        # VideoConfig
        self.config_manager.set_config("VideoConfig", "video_format", self.findChild(QLineEdit, "VideoConfig_video_format").text())
        self.config_manager.set_config("VideoConfig", "video_codec", self.findChild(QLineEdit, "VideoConfig_video_codec").text())
        self.config_manager.set_config("VideoConfig", "video_fps", self.findChild(QLineEdit, "VideoConfig_video_fps").text())
        self.config_manager.set_config("VideoConfig", "video_bitrate", self.findChild(QLineEdit, "VideoConfig_video_bitrate").text())
        self.config_manager.set_config("VideoConfig", "video_resolution", self.findChild(QLineEdit, "VideoConfig_video_resolution").text())

        # AudioConfig
        self.config_manager.set_config("AudioConfig", "music_file_path", self.findChild(QLineEdit, "AudioConfig_music_file_path").text())

        # MoviePyConfig
        self.config_manager.set_config("MoviePyConfig", "moviepy_temp_dir", self.findChild(QLineEdit, "MoviePyConfig_moviepy_temp_dir").text())

        QMessageBox.information(self, "Configuration Saved", "Configuration has been saved successfully!")

        # Handle scheduling based on checkbox
        if self.enable_scheduling_checkbox.isChecked():
            try:
                # Pass the path to the main.py script (or the executable path if packaged)
                # sys.argv[0] gives the path of the current script/executable
                bat_file_path = os.path.splitext(os.path.abspath(sys.argv[0]))[0] + ".bat"
                self.scheduler.create_or_update_task("MemoriesAppDailySlideshow", 
                                                     bat_file_path, 
                                                     self.findChild(QLineEdit, "AppConfig_schedule_time").text())
                QMessageBox.information(self, "Scheduler", "Daily task scheduled successfully!")
            except Exception as e:
                QMessageBox.critical(self, "Scheduler Error", f"Failed to schedule task: {e}")
        else:
            try:
                self.scheduler.delete_task("MemoriesAppDailySlideshow")
                QMessageBox.information(self, "Scheduler", "Daily task unscheduled successfully!")
            except Exception as e:
                QMessageBox.critical(self, "Scheduler Error", f"Failed to unschedule task: {e}")

        # Handle startup folder open based on checkbox
        if self.enable_startup_folder_open_checkbox.isChecked():
            try:
                slideshow_output_folder = self.findChild(QLineEdit, "AppConfig_slideshow_output_folder").text()
                self.scheduler.create_startup_script(os.path.abspath(sys.argv[0]), slideshow_output_folder)
                QMessageBox.information(self, "Startup Folder", "Startup folder script created successfully!")
            except Exception as e:
                QMessageBox.critical(self, "Startup Folder Error", f"Failed to create startup folder script: {e}")
        else:
            try:
                self.scheduler.delete_startup_script()
                QMessageBox.information(self, "Startup Folder", "Startup folder script deleted successfully!")
            except Exception as e:
                QMessageBox.critical(self, "Startup Folder Error", f"Failed to delete startup folder script: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MemoriesAppGUI()
    window.show()
    sys.exit(app.exec_())

