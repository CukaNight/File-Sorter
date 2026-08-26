import os
import shutil

class sort():
    def move_by_extension(self, source_folder, extension, destination):
        folder = source_folder
        
        files = [
            os.path.join(folder, f)
            for f in os.listdir(folder)
            if os.path.isfile(os.path.join(folder, f)) and f.lower().endswith(extension.lower())
        ]
        
        for file_path in files:
            filesname = os.path.basename(file_path)
            dst_path = os.path.join(destination, filesname)
            shutil.move(file_path, dst_path)



    RULES = {
        "Изображения": {
            "dest": "C:/Users/user/Pictures/Фото",
            "extensions": [".jpeg",".jpg",".png",".webp",".gif"]
        },
        "Видео": {
            "dest": "C:/Users/user/Videos/Видео",
            "extensions": [".mp4",".mov",".mkv",".avi"]
        },
        "Код и данные": {
            "dest": "C:/Users/user/Documents/Код и данные",
            "extensions": [".py",".json",".csv",".xml"]
        },
        "Программы": {
            "dest": "C:/Users/user/Documents/Программы",
            "extensions": [".exe",".msi"]
        },
        "Архивы": {
            "dest": "C:/Users/user/Documents/Архивы",
            "extensions": [".zip",".rar",".7z",".tar.gz"]
        },
        "Аудио": {
            "dest": "C:/Users/user/Music/Аудио",
            "extensions": [".mp3",".wav",".flac"]
        },
        "Документы": {
            "dest": "C:/Users/user/Documents/Документы",
            "extensions": [".pdf",".docx",".txt",".xlsx",".pptx"]
        }
    }

    def run(self):
        source_folder = "C:/Users/user/Downloads"

        for category_name, rule in self.RULES.items():
            dest_folder = rule['dest']
            extensions = rule['extensions']

            os.makedirs(dest_folder, exist_ok=True)

            for ext in extensions:
                self.move_by_extension(source_folder, ext, dest_folder)

if __name__ == "__main__":
    s = sort()  # Создаем объект класса
    s.run() 

print("Успешно")