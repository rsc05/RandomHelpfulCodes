import os, re, shutil
from glob import glob
import comtypes.client

    
# Read folders from a particular folder in the path1
path1 = r"D:\OneDrive - University of Bristol\University of Bristol\FTGP 2022-2023\BB"

# Setting the intial part of the path where you want to save the file
path2= r"D:\OneDrive - University of Bristol\University of Bristol\FTGP 2022-2023 BB"


# Select the folder with only number names
# Get the list of folders in that path
list1=next(os.walk(path1))[1]

# Remove all elements in the list that do not have number
r = re.compile(".*\d")
new_list1 = list(filter(r.match, list1)) # Read Note below

# Get the numbers of each element in new_list1
new_list2=[re.search('.*(\d)', x, re.IGNORECASE).group(1) for x in new_list1]


for k in range(len(new_list1)):
    i=new_list1[k]
    copy_path= os.path.join(path1, i)

    # Find specific flies in the folder
    pattern = '*.docx'
    copy_path2 = os.path.join(copy_path, pattern)
    files_with_patterns=sorted(glob(copy_path2))

    # Getting the folder where you want the pdf files to be created 
    folder_to_be_pasted= os.path.join(path2, "Week"+str(new_list2[k]),"Lectures")

    # Copy these files to specific folder
    folder_to_be_copied= os.path.join(path2, "Week"+str(new_list2[k]),"Labs")

    # Go through each file that is a powerpoint file
    for value in files_with_patterns:
    # print(value)
        shutil.copy(value, folder_to_be_copied)