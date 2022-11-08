import os
abs_path = input("Please enter the absolute path: ")

if(os.path.isfile(abs_path)):
    print(f"The path {abs_path} is not a directory ")
else:
    all_files_dir = os.listdir(abs_path)
    if (len(all_files_dir) == 0):
        print(f"There are no files in {abs_path} path")
    else:
        ext = input("Plese enter the extension")
        result=[]
        for i in all_files_dir:
            if(i.endswith(ext)):
                result.append(i)
        print(result)
