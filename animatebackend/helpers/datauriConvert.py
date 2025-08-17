import base64
import os

def ClearFolder(folderPath):
    current_directory = os.getcwd()
    for filename in os.listdir(current_directory+folderPath):
        filePath = os.path.join(current_directory+folderPath, filename)
        os.remove(filePath)
        print(f"Deleted: {filePath}")

def SaveDataUriToPng(uris, folderPath, format,zeroPadding):
  
    for index in range(len(uris)):
        value= uris[index]
        if not value.startswith("data:image/png;base64,"):
            print("Error: The provided Data URI does not appear to be a PNG image.")
            return

        base64_data = value.split("data:image/png;base64,")[1]

        try:
            binary_data = base64.b64decode(base64_data)
        except base64.binascii.Error as e:
            print(f"Error decoding Base64 data: {e}")
            return

        os.makedirs(folderPath, exist_ok=True)

        file_path = os.path.join(folderPath, format+str(index+1).zfill(zeroPadding)+".png")

        try:
            with open(file_path, "wb") as f:
                f.write(binary_data)
            print(f"Image successfully saved to: {file_path}")
        except IOError as e:
            print(f"Error saving image to file: {e}")


