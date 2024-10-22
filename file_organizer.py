import os
import shutil

# Path of the folder to be organized
path = "./"
# path = "Unorganized_Files"

# Dictionary with file types and their respective folder names
folders = {
    "doc":  "Documents",
    "txt":  "Text Files",
    "pdf":  "PDFs",

    "mp3":  "Music",

    "mp4":  "Videos",
    "mkv":  "Videos",

    "jpg":  "Images",
    "jpeg": "Images",
    "png":  "Images/PNG",
    "svg":  "Images/SVG",
    "gif":  "Images/GIF",
    "webp":  "Images/WEBP",

    "less":  "Codes/CSS",
    "scss":  "Codes/SCSS",
    "css":  "Codes/CSS",
    "php":  "Codes/PHP",
    "html":  "Codes/HTML",
    "xml":  "Codes/XML",
    "js":  "Codes/JS",
    "json":  "Codes/JSON",
    
    "sql":  "SQL",

    "zip":  "Archive",
    "gz":  "Archive/GZ",
    "rar":  "Archive/RAR",

    "exe":  "Software",
    "msi":  "Software",
    "iso":  "Software",
}

# Loop through each file in the folder
for filename in os.listdir(path):
    # Get the extension of the file
    ext = os.path.splitext(filename)[1][1:]
    
    # If the file type is in our dictionary, move the file to its respective folder
    if ext in folders:
        folder_name = folders[ext]
        folder_path = os.path.join(path, "Organiged", folder_name)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        old_path = os.path.join(path, filename)
        new_path = os.path.join(folder_path, filename)
        shutil.move(old_path, new_path)
