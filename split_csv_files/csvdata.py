import os
from parameters import output_lines


def split_file(input_file):
    input_folder = os.path.dirname(input_file)
    input_file_name = os.path.basename(input_file)
    output_files = []
    csv_file = open(os.path.join(input_folder, input_file_name), "r")
    first_line = csv_file.readlines(1)[0]
    print(first_line)
    i = 1
    j = 1
    for data_line in csv_file.readlines():
        if i == 1:
            output_filename = os.path.join(input_folder, str(j) + "-" + input_file_name);
            print(output_filename)
            output_files.append(output_filename)
            output_file = open(output_filename, "w")
            output_file.writelines(first_line)
            output_file.writelines(data_line)
            i += 1
        elif i == output_lines:
            output_file.writelines(data_line)
            i = 1
            output_file.close()
            j += 1
        else:
            output_file.writelines(data_line)
            i += 1
    csv_file.close()
    output_file.close()
    return output_files
