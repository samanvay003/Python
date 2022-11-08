import os,sys,datetime

maxAge=50
abs_path=input("Please enter the absolute path")

if not os.path.exists(abs_path) or os.path.isfile(abs_path):
    print(f"The path {abs_path} is invalid")
    sys.exit(0)

all_files = []

tdate=datetime.datetime.now()
for i in os.listdir(abs_path):
    abs_name = os.path.join(abs_path,i)
    if(os.path.isfile(abs_name)):
        cdate=datetime.datetime.fromtimestamp(os.path.getctime(abs_name))
        if (tdate-cdate).days>maxAge:
            print(i,"is deleted now")
            os.remove(abs_name)
