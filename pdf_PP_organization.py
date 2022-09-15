import os, re, shutil
from glob import glob
import comtypes.client

# Function that saves the file as pdf

def PPTtoPDF(inputFileName, outputFileName, formatType = 32):
    powerpoint = comtypes.client.CreateObject("Powerpoint.Application")
    powerpoint.Visible = 1

    if outputFileName[-3:] != 'pdf':
        outputFileName = outputFileName + ".pdf"
    deck = powerpoint.Presentations.Open(inputFileName)
    deck.SaveAs(outputFileName, formatType) # formatType = 32 for ppt to pdf
    deck.Close()
    powerpoint.Quit()
    
# Read folders from a particular folder in the path1
path1 = r"D:\OneDrive - University of Bristol\University of Bristol\FTGP 2022-2023\BB"
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
    pattern = '*.pptx'
    copy_path2 = os.path.join(copy_path, pattern)
    files_with_patterns=sorted(glob(copy_path2))

    # Getting the folder where you want the pdf files to be created 
    folder_to_be_pasted= os.path.join(path2, "Week"+str(new_list2[k]),"Lectures")

    # Go through each file that is a powerpoint file
    for value in files_with_patterns:
        # Get the name of the pp lecture but in pdf format
        Lecture_name= os.path.basename(value)[:-5]+".pdf"
        
        # Set the new path of the file
        file_path_paste=os.path.join(folder_to_be_pasted, Lecture_name)
        
        # Create pdf files from Powerpoint
        PPTtoPDF(value, file_path_paste, formatType = 32)
    