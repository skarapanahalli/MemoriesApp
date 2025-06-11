import os
import datetime
import random
import numpy as np
from moviepy.editor import ImageClip, concatenate_videoclips, AudioFileClip
from config_manager import ConfigManager
from music_downloader import MusicDownloader

from PIL import Image
from pkg_resources import parse_version

# Handle Pillow 10.0.0+ compatibility for Image.ANTIALIAS
if parse_version(Image.__version__) >= parse_version("10.0.0"):
    Image.ANTIALIAS = Image.LANCZOS

class SlideshowGenerator:
    def __init__(self, config_file_path):
        self.config_manager = ConfigManager(config_file_path)
        self.photo_folder_path = self.config_manager.get_config("AppConfig", "photo_folder_path")
        self.years_back = [int(y) for y in self.config_manager.get_config("AppConfig", "years_back").split(",")]
        self.random_photos_limit = int(self.config_manager.get_config("AppConfig", "random_photos_limit"))
        self.photo_display_seconds = int(self.config_manager.get_config("AppConfig", "photo_display_seconds"))
        self.slideshow_output_folder = self.config_manager.get_config("AppConfig", "slideshow_output_folder")
        self.video_format = self.config_manager.get_config("VideoConfig", "video_format")
        self.video_codec = self.config_manager.get_config("VideoConfig", "video_codec")
        self.video_fps = int(self.config_manager.get_config("VideoConfig", "video_fps"))
        self.video_bitrate = self.config_manager.get_config("VideoConfig", "video_bitrate")
        resolution_str = self.config_manager.get_config("VideoConfig", "video_resolution").split("x")
        self.video_resolution = (int(resolution_str[0]), int(resolution_str[1]))
        self.music_downloader = MusicDownloader(config_file_path)
        
        # Configure MoviePy temporary directory
        self.moviepy_temp_dir = self.config_manager.get_config("MoviePyConfig", "moviepy_temp_dir")
        if not self.moviepy_temp_dir:
            # Default to a subfolder in slideshow_output_folder if not specified
            self.moviepy_temp_dir = os.path.join(self.slideshow_output_folder, "MoviePy_temp")
        os.makedirs(self.moviepy_temp_dir, exist_ok=True)
        os.environ["TMPDIR"] = self.moviepy_temp_dir
        os.environ["TEMP"] = self.moviepy_temp_dir
        os.environ["TMP"] = self.moviepy_temp_dir

        # Build the photo index once upon initialization
        self.photo_index = self._build_photo_index()

    def _build_photo_index(self):
        """Scans the photo directory and builds an in-memory index of photos and their dates."""
        index = []
        print("Building photo index...")
        for root, _, files in os.walk(self.photo_folder_path):
            for file in files:
                try:
                    # Check for common image file extensions
                    if file.lower().endswith((".png", ".jpg", ".jpeg", ".bmp", ".gif")):
                        file_path = os.path.join(root, file)
                        timestamp = os.path.getmtime(file_path)
                        file_date = datetime.datetime.fromtimestamp(timestamp).date()
                        index.append((file_path, file_date))
                except Exception as e:
                    print(f"Error processing file {file} for index: {e}")
        print(f"Photo index built with {len(index)} items.")
        return index

    def get_photos_for_date(self, target_date):
        """Gets photos for a specific date by querying the in-memory index."""
        photos = []
        for file_path, file_date in self.photo_index:
            if file_date.year == target_date.year and file_date.month == target_date.month and file_date.day == target_date.day:
                photos.append(file_path)
        return photos

    def select_photos_for_year(self, year_offset):
        selected_photos = []
        today = datetime.date.today()

        target_date = today.replace(year=today.year - year_offset)
        photos_found = []
        days_offset = 0
        while not photos_found and days_offset < 7: # Try up to 7 previous days for fallback
            current_target_date = target_date - datetime.timedelta(days=days_offset)
            photos_found = self.get_photos_for_date(current_target_date)
            if not photos_found:
                days_offset += 1

        if photos_found:
            random.shuffle(photos_found)
            selected_photos.extend(photos_found[:self.random_photos_limit])
        return selected_photos

    def create_slideshow(self, photo_paths, output_filename, audio_query="popular tune"):
        if not photo_paths:
            print("No photos to create slideshow.")
            return

        clips = []
        for photo_path in photo_paths:
            try:
                # Load image using PIL for more control
                img = Image.open(photo_path)
                img_width, img_height = img.size

                # Calculate aspect ratios
                video_aspect_ratio = self.video_resolution[0] / self.video_resolution[1]
                img_aspect_ratio = img_width / img_height

                # Determine new dimensions and padding
                if img_aspect_ratio > video_aspect_ratio: # Image is wider than video frame
                    new_width = self.video_resolution[0]
                    new_height = int(new_width / img_aspect_ratio)
                    padding_top = (self.video_resolution[1] - new_height) // 2
                    padding_bottom = self.video_resolution[1] - new_height - padding_top
                    padding_left = 0
                    padding_right = 0
                else: # Image is taller than or same aspect ratio as video frame
                    new_height = self.video_resolution[1]
                    new_width = int(new_height * img_aspect_ratio)
                    padding_left = (self.video_resolution[0] - new_width) // 2
                    padding_right = self.video_resolution[0] - new_width - padding_left
                    padding_top = 0
                    padding_bottom = 0
                
                # Resize image while maintaining aspect ratio
                img = img.resize((new_width, new_height), Image.ANTIALIAS)

                # Create a new blank image with the target video resolution (black background)
                background = Image.new("RGB", self.video_resolution, (0, 0, 0))
                background.paste(img, (padding_left, padding_top))

                # Convert PIL Image to MoviePy ImageClip using numpy array
                clip = ImageClip(np.array(background)).set_duration(self.photo_display_seconds)

                # Add pan/zoom animation
                # Randomly choose pan direction or zoom
                animation_type = random.choice(["zoom_in", "zoom_out", "pan_left", "pan_right", "pan_up", "pan_down"])
                
                if animation_type == "zoom_in":
                    clip = clip.resize(lambda t: 1 + 0.05 * t / clip.duration)
                elif animation_type == "zoom_out":
                    clip = clip.resize(lambda t: 1.05 - 0.05 * t / clip.duration)
                elif animation_type == "pan_left":
                    clip = clip.set_position(lambda t: (
                        -clip.w * 0.05 * t / clip.duration, 
                        "center"
                    ))
                elif animation_type == "pan_right":
                    clip = clip.set_position(lambda t: (
                        clip.w * 0.05 * t / clip.duration, 
                        "center"
                    ))
                elif animation_type == "pan_up":
                    clip = clip.set_position(lambda t: (
                        "center", 
                        -clip.h * 0.05 * t / clip.duration
                    ))
                elif animation_type == "pan_down":
                    clip = clip.set_position(lambda t: (
                        "center", 
                        clip.h * 0.05 * t / clip.duration
                    ))

                clips.append(clip)
            except Exception as e:
                print(f"Error processing image {photo_path}: {e}")

        if not clips:
            print("No valid clips to create slideshow.")
            return

        final_clip = concatenate_videoclips(clips, method="compose")

        audio_path = self.music_downloader.get_music_file_path()
        if audio_path and os.path.exists(audio_path):
            audio_clip = AudioFileClip(audio_path)
            final_clip = final_clip.set_audio(audio_clip.set_duration(final_clip.duration))
        else:
            print("Could not find or download audio, creating slideshow without music.")

        output_dir = os.path.join(self.slideshow_output_folder, datetime.date.today().strftime("%d-%m-%Y"))
        os.makedirs(output_dir, exist_ok=True)
        output_path = os.path.join(output_dir, output_filename)

        final_clip.write_videofile(output_path, fps=self.video_fps, codec=self.video_codec, audio_codec="aac", bitrate=self.video_bitrate, logger=None)
        print(f"Slideshow created at: {output_path}")


# Example Usage (for testing)
if __name__ == "__main__":
    # Create a dummy config.ini for testing if it doesn\"t exist
    if not os.path.exists("config.ini"):
        with open("config.ini", "w") as f:
            f.write("[AppConfig]\n")
            f.write("photo_folder_path = ./dummy_photos\n")
            f.write("years_back = 1,2,3\n")
            f.write("random_photos_limit = 3\n")
            f.write("photo_display_seconds = 2\n")
            f.write("slideshow_output_folder = ./Memories\n")
            f.write("schedule_time = 18:00\n")
            f.write("pixabay_api_key = YOUR_DUMMY_API_KEY\n")
            f.write("\n[VideoConfig]\n")
            f.write("video_format = mp4\n")
            f.write("video_codec = libx264\n")
            f.write("video_fps = 24\n")
            f.write("video_bitrate = 5000k\n")
            f.write("video_resolution = 1080x1920\n")
            f.write("\n[AudioConfig]\n")
            f.write("music_file_path = \n")

    # Create dummy photos for testing
    dummy_photos_dir = ".\\dummy_photos"
    os.makedirs(dummy_photos_dir, exist_ok=True)
    from PIL import Image
    today = datetime.date.today()
    for i in range(5):
        # Create photos for today, and 1, 2, 3 years back
        for year_offset in [0, 1, 2, 3]:
            target_date = today.replace(year=today.year - year_offset)
            img = Image.new("RGB", (1920, 1080), color = (random.randint(0,255), random.randint(0,255), random.randint(0,255)))
            img.save(os.path.join(dummy_photos_dir, f"photo_{target_date.strftime("%Y%m%d")}_{i}.png"))
            # Set modification time to simulate creation date
            os.utime(os.path.join(dummy_photos_dir, f"photo_{target_date.strftime("%Y%m%d")}_{i}.png"), (target_date.timestamp(), target_date.timestamp()))

    generator = SlideshowGenerator("config.ini")
    
    # Test for a specific year
    photos_1_year_back = generator.select_photos_for_year(1)
    print(f"Selected {len(photos_1_year_back)} photos for 1 year back:")
    for p in photos_1_year_back:
        print(p)
    generator.create_slideshow(photos_1_year_back, output_filename="test_slideshow_1_year_back.mp4")

    photos_2_years_back = generator.select_photos_for_year(2)
    print(f"Selected {len(photos_2_years_back)} photos for 2 years back:")
    for p in photos_2_years_back:
        print(p)
    generator.create_slideshow(photos_2_years_back, output_filename="test_slideshow_2_years_back.mp4")


