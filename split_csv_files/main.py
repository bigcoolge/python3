import os
import gzip
import shutil
from csvdata import split_file
from parameters import root_folder

print("======get all gz files")
gz_files = set()
for dirpath, dirnames, filenames in os.walk(root_folder):
    for filename in filenames:
        if(filename.endswith(".gz")):
            gz_files.add(os.path.join(dirpath, filename))
print(gz_files)
print("DONE!======get all gz files")

print("=====unzip files")
for gz_file in gz_files:
    with gzip.open(gz_file, 'rb') as f_in:
        output_file = gz_file[:-3]
        print(output_file)
        with open(output_file, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)
print("DONE!=====unzip files")

print("=====get unzipped csv files")
csv_files = set()
for dirpath, dirnames, filenames in os.walk(root_folder):
    for filename in filenames:
        if(filename.endswith(".csv")):
            csv_files.add(os.path.join(dirpath, filename))
print(csv_files)
print("DONE=====get unzipped csv files")

print("=======split and gzip files")
for csv_file in csv_files:
    output_files = split_file(csv_file)
    print(output_files)
    for output_file in output_files:
        with open(output_file, 'rb') as f_in, gzip.open(output_file + ".gz", 'wb') as f_out:
            f_out.writelines(f_in)
        os.remove(output_file)
    os.remove(csv_file)
print("DONE=======split and gzip files")