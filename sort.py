import os
import shutil

class sort():
    def sort():
        folder = r"C:/Users/user/Downloads"
        phot = "C:/Users/user/Pictures/Рабочие Фото/Разобрать по папкам"
        os.makedirs(phot, exist_ok=True)
        dst_folder = r"C:/Users/user/Pictures/Рабочие Фото/Разобрать по папкам"
        ext = ".jpg"

        photo = [
            os.path.join(folder, f)
            for f in os.listdir(folder)
            if os.path.isfile(os.path.join(folder, f)) and f.lower().endswith(ext.lower())
        ]

        for file_path in photo:
            photoname = os.path.basename(file_path)
            dst_path = os.path.join(dst_folder, photoname)
            shutil.move(file_path, dst_path)

        ext2 = ".png"

        photo = [
            os.path.join(folder, f)
            for f in os.listdir(folder)
            if os.path.isfile(os.path.join(folder, f)) and f.lower().endswith(ext2.lower())
        ]

        for file_path2 in photo:
            photoname2 = os.path.basename(file_path2)
            dst_path = os.path.join(dst_folder, photoname2)
            shutil.move(file_path2, dst_path)

        ext9 = ".webp"
        
        photo = [
            os.path.join(folder, f)
            for f in os.listdir(folder)
            if os.path.isfile(os.path.join(folder, f)) and f.lower().endswith(ext9.lower())
        ]
        
        for file_path9 in photo:
            photoname3 = os.path.basename(file_path9)
            dst_path = os.path.join(dst_folder, photoname3)
            shutil.move(file_path9, dst_path) 

        ext10 = ".jpeg"
        
        photo = [
            os.path.join(folder, f)
            for f in os.listdir(folder)
            if os.path.isfile(os.path.join(folder, f)) and f.lower().endswith(ext10.lower())
        ]
        
        for file_path10 in photo:
            photoname4 = os.path.basename(file_path10)
            dst_path = os.path.join(dst_folder, photoname4)
            shutil.move(file_path10, dst_path)

    def sort2():
        folder = r"C:/Users/user/Downloads"
        pyth = "C:/Users/user/Documents/Файлы програмирования"
        os.makedirs(pyth, exist_ok=True)
        dst_folder2 = r"C:/Users/user/Documents/Файлы програмирования"
        ext3 = ".py"

        python = [
            os.path.join(folder, f)
            for f in os.listdir(folder)
            if os.path.isfile(os.path.join(folder, f)) and f.lower().endswith(ext3.lower())
        ]

        for file_path3 in python:
            pythonname = os.path.basename(file_path3)
            dst_path2 = os.path.join(dst_folder2, pythonname)
            shutil.move(file_path3, dst_path2)

        ext4 = ".json"

        python = [
            os.path.join(folder, f)
            for f in os.listdir(folder)
            if os.path.isfile(os.path.join(folder, f)) and f.lower().endswith(ext4.lower())
        ]

        for file_path4 in python:
            pythonname = os.path.basename(file_path4)
            dst_path2 = os.path.join(dst_folder2, pythonname)
            shutil.move(file_path4, dst_path2)

    def sort3():
        folder = r"C:/Users/user/Downloads"
        ex = "C:/Users/user/Documents/.exe"
        os.makedirs(ex, exist_ok=True)
        dst_folder3 = r"C:/Users/user/Documents/.exe"
        ext5 = ".exe"

        exe = [
            os.path.join(folder, f)
            for f in os.listdir(folder)
            if os.path.isfile(os.path.join(folder, f)) and f.lower().endswith(ext5.lower())
        ]

        for file_path5 in exe:
            exename = os.path.basename(file_path5)
            dst_path3 = os.path.join(dst_folder3, exename)
            shutil.move(file_path5, dst_path3)

    def sort4():
        folder = r"C:/Users/user/Downloads"
        zi = "C:/Users/user/Documents/.zip"
        os.makedirs(zi, exist_ok=True)
        dst_folder4 = r"C:/Users/user/Documents/.zip"
        ext6 = ".zip"

        zip = [
            os.path.join(folder, f)
            for f in os.listdir(folder)
            if os.path.isfile(os.path.join(folder, f)) and f.lower().endswith(ext6.lower())
        ]

        for file_path6 in zip:
            zipname = os.path.basename(file_path6)
            dst_path4 = os.path.join(dst_folder4, zipname)
            shutil.move(file_path6, dst_path4)

    def sort5():
        folder = r"C:/Users/user/Downloads"
        vide = "C:/Users/user/Videos/Разобрать по папкам"
        os.makedirs(vide, exist_ok=True)
        dst_folder5 = r"C:/Users/user/Videos/Разобрать по папкам"
        ext7 = ".mp4"

        video = [
            os.path.join(folder, f)
            for f in os.listdir(folder)
            if os.path.isfile(os.path.join(folder, f)) and f.lower().endswith(ext7.lower())
        ]

        for file_path7 in video:
            videoname = os.path.basename(file_path7)
            dst_path5 = os.path.join(dst_folder5, videoname)
            shutil.move(file_path7, dst_path5)

        ext8 = ".mkv"
        
        video = [
            os.path.join(folder, f)
            for f in os.listdir(folder)
            if os.path.isfile(os.path.join(folder, f)) and f.lower().endswith(ext8.lower())
        ]
        
        for file_path8 in video:
            videoname = os.path.basename(file_path8)
            dst_path5 = os.path.join(dst_folder5, videoname)
            shutil.move(file_path8, dst_path5)

        ext10 = ".mov"
        
        video = [
            os.path.join(folder, f)
            for f in os.listdir(folder)
            if os.path.isfile(os.path.join(folder, f)) and f.lower().endswith(ext10.lower())
        ]
        
        for file_path11 in video:
            videoname = os.path.basename(file_path11)
            dst_path5 = os.path.join(dst_folder5, videoname)
            shutil.move(file_path11, dst_path5)    
    sort()
    sort2()
    sort3()
    sort4()
    sort5()

print("Успешно")