import subprocess


def isFfmpegInstalled():
    try:
        # Attempt to run ffmpeg -version and capture its output
        # stdout=subprocess.PIPE and stderr=subprocess.PIPE prevent output to console
        # check=True will raise a CalledProcessError if the command returns a non-zero exit code
        subprocess.run(['ffmpeg', '-version'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except FileNotFoundError:
        return False
    except subprocess.CalledProcessError:
        return False
    except Exception as e:
        print(f"An error occured when looking for ffmpeg: {e}")
        return False