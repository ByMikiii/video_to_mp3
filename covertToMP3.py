import os
from moviepy.editor import *

def convert_video_to_mp3(video_path, output_path, bitrate='192k'):
    video = VideoFileClip(video_path)
    audio = video.audio
    audio.write_audiofile(output_path, bitrate=bitrate)

current_folder = os.getcwd()

for file_name in os.listdir(current_folder):
    if file_name.endswith(('.mp4', '.avi', '.mov', '.mkv')):
        
        video_path = os.path.join(current_folder, file_name)
        
        mp3_file_name = file_name.rsplit('.', 1)[0] + '.mp3'
        
        mp3_output_path = os.path.join(current_folder, mp3_file_name)
        
        convert_video_to_mp3(video_path, mp3_output_path)
        
        # os.remove(video_path)
        print(f"Converted {file_name} to MP3 and removed the video file.")

print("Conversion and removal process completed.")
