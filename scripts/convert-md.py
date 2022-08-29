import os
import sys
directory = os.fsencode(sys.argv[1])
    
for file in os.listdir(directory):
     filename = os.fsdecode(file)
     if filename.endswith(".md") or filename.endswith(".py"): 
         file_name, ext = os.path.splitext(file)
         print(file_name)
         empty_str = ""
         file_name = file_name.decode('utf-8') + empty_str
         os.system("markdown-pdf "+sys.argv[1]+"/" + file_name + ".md -o " + file_name + ".pdf")         
         continue
     else:
         continue
