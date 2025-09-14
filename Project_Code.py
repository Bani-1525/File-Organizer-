import os
import shutil

# Dictionary for file type categories
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".pptx", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi"],
    "Music": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Code": [".py", ".cpp", ".java", ".js", ".html", ".css"],
    "Others": []
}

def organize_files(folder_path):
    if not os.path.exists(folder_path):
        print("❌ Folder not found. Please check the path.")
        return

    # Create category folders if they don't exist
    for category in FILE_CATEGORIES.keys():
        category_path = os.path.join(folder_path, category)
        if not os.path.exists(category_path):
            os.makedirs(category_path)

    # Scan files and move them to appropriate folders
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)

        if os.path.isfile(file_path):
            moved = False
            for category, extensions in FILE_CATEGORIES.items():
                if any(file_name.lower().endswith(ext) for ext in extensions):
                    shutil.move(file_path, os.path.join(folder_path, category, file_name))
                    moved = True
                    break
            if not moved:
                shutil.move(file_path, os.path.join(folder_path, "Others", file_name))

    print("✅ Files organized successfully!")

# Example usage
if __name__ == "__main__":
    folder = input("Enter the folder path you want to organize: ")
    organize_files(folder)