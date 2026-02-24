import os

folder_path = input("Enter folder path: ")

if not os.path.isdir(folder_path):
    print("Invalid folder path")
else:
    extensions = {}

    for file in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, file)):
            ext = os.path.splitext(file)[1]
            if ext:
                extensions[ext] = extensions.get(ext, 0) + 1

    print("\nFile Extension Count:")
    for ext, count in extensions.items():
        print(f"{ext} : {count}")
