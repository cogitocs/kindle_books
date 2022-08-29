import os
import sys

current_dir=os.getcwd() 
target_dir=sys.argv[2]
def mv_files(dir):
    r = []
    for root, dirs, files in os.walk(dir):
        for name in files:
            if name.endswith(".pdf") or name.endswith(".py"): 
                print("source:"+root +"/" + name)
                print("target file name:"+"[" + root.replace(current_dir+"/","") + "]" +"-"+name)
                print("target dir:"+target_dir)
                newfilename="[" + root.replace(current_dir+"/","") + "]" +"-"+name
                os.system("cp "+ root +"/" + name +" "+target_dir+"/" + newfilename)


def main():
    mv_files(sys.argv[1])

if __name__ == "__main__":
    main()
