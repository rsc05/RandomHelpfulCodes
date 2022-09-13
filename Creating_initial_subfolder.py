import os

# Create Folders and sub-folders in the path
path=r"D:\OneDrive - University of Bristol\University of Bristol\FTGP 2022-2023 BB"
SubFolders=["Labs", "Lectures"]
for i in range(1,8):
    # Create weeks
    full_path = os.path.join(path, "Week"+str(i))
    os.mkdir(full_path)
    
    # In the newly created folder create two folders
    for j in SubFolders:
        full_path2 = os.path.join(full_path, j)
        os.mkdir(full_path2)
