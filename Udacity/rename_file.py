import os
from string import maketrans

def rename_files():
        #1) get file name in list
	file_list=os.listdir(r"C:\00_Workspace\03_python_code\prank\prank")
	#print file_list
	#print os.getcwd()

	os.chdir(r"C:\00_Workspace\03_python_code\prank\prank")
        lect_table=maketrans('0123456789','          ')
 
        #2) for each file, rename file
	for filename in file_list:
            new_filename=filename.translate(lect_table).replace(" ","")
            #print new_filename
            os.rename(filename,new_filename)
                        	
rename_files()
print os.listdir(r"C:\00_Workspace\03_python_code\prank\prank")
