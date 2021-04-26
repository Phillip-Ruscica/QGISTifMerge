import glob
import os
# Change the data_path to the folder containing the tifs

################################
data_path = "c:\data\....\*.tif"
################################





file_list = glob.glob(data_path)

files_string = " ".join(file_list)

command = "gdal_merge.py -o output.tif -of gtiff " + files_string

os.system(command)
