import sys
import os
import io

if len(sys.argv) != 2:
    sys.stderr.write("Arguments error. Usage:\n")
    sys.stderr.write("\tpython3 fill_na.py data-file\n")
    sys.exit(1)

f_input = sys.argv[1]
f_output = os.path.join("data", "stage2", "train.csv")
os.makedirs(os.path.join("data", "stage2"), exist_ok=True)

def process_data(fd_in, fd_out):
    arr_action = []
    arr_resource = []
    arr_role_deptname = []
    arr_role_code = []

    for line in fd_in:
        line = line.rstrip('\n').split(',')
        arr_action.append(line[0])
        arr_resource.append(line[1])
        arr_role_deptname.append(line[2])
        arr_role_code.append(line[3])

    for action, resource, role_deptname, role_code in zip(arr_action, arr_resource, arr_role_deptname, arr_role_code):
        fd_out.write("{},{},{},{}\n".format(action, resource, role_deptname, role_code))


with io.open(f_input, encoding="utf8") as fd_in:
    with io.open(f_output, "w", encoding="utf8") as fd_out:
        process_data(fd_in, fd_out)
