#Read-in script for WIPO technology fields for all patents

# Importing necessary packages.
import os
import zipfile as zip
import pandas as pd
import csv
# Set up file path:
# Please include the folder path of the file you are reading. Ex: os.chdir("C:/Users/johnsmith/Downloads")
os.chdir("")
# Selecting the zip file.
file_name = "g_wipo_technology.tsv.zip"
f_name = "g_wipo_technology.tsv"
zf = zip.ZipFile(file_name)
chunksize = 10 ** 6
count = 1
n_obs = 0
for df in pd.read_csv(zf.open(f_name), delimiter="\t", chunksize=chunksize, quoting=csv.QUOTE_NONNUMERIC):
    print('processing chunk: ' + str(count))
    n_obs += len(df)
    count += 1
# Print summary of data: number of observations, columns, and each variable data type
print(n_obs)
print(df.dtypes)



