import subprocess
import os

def createVideoFromPngs(inputFolder, outputVideoPath, imagePattern="image%03d.png"):
  
    current_directory = os.getcwd()
    input = current_directory+inputFolder
    output = current_directory+outputVideoPath
    input_image_path = os.path.join(input, imagePattern)

    command = [
        'ffmpeg',
        '-y',  
        '-i', input_image_path,
        '-c:v', 'libx264', 
        output
    ]

    try:
        subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"Video created successfully at: {outputVideoPath}")
    except subprocess.CalledProcessError as e:
        print(f"Error during FFmpeg execution: {e}")
        print(f"FFmpeg stderr: {e.stderr.decode()}")
    except FileNotFoundError:
        print("FFmpeg not found. Please ensure it is installed and in your system's PATH.")

