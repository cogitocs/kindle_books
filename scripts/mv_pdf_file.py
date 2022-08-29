import os
import sys

current_dir=os. getcwd() 
def mv_files(dir):
    r = []
    for root, dirs, files in os.walk(dir):
        for name in files:
            if name.endswith(".pdf") or name.endswith(".py"): 
                print(root +"/" + name)
                print("[" + root.replace(current_dir,"") + "]" +"-"+name)
                newfilename="[" + root.replace(current_dir,"") + "]" +"-"+name
                os.system("cp "+ root +"/" + name +" "+current_dir+"category/" + newfilename)

def main():
    mv_files(sys.argv[1])

if __name__ == "__main__":
    main()