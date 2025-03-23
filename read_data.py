import os.path
import os

def read_mech_list():   
    # reading the file with the explicit file path
    # (!!!) possible improvement - write the number of the line into the dict to improve the reading from the file in the read_mech_data function
    mechs_dict = {}
    
    file_path = os.path.join("data", "mech_list.csv")
    f = open(file_path, "r")
    content = f.readlines()

    for i in range(len(content)):
        if i == 0:
            continue #skiping the first line
        line = (content[i].strip("\n")).split(", ")
        if line[0] in mechs_dict.keys():
            mechs_dict[line[0]].append(line[1])
        else:
            mechs_dict[line[0]] = [line[1]]

    f.close()
    #print(mechs_dict)
    return mechs_dict

def read_mech_data(variant, model):
    # can be improved according to the idea on the line 6
    # should I rewrite it as a dictionary instead of the list? hm...

    mech_list = []

    file_path = os.path.join("data", "mech_data.csv")
    f = open(file_path, "r")
    content = f.readlines()

    found = False
    for i in range(len(content)):
        if i == 0:
            continue #skiping the first line
        line = (content[i].strip("\n")).split(", ")
        if variant == line[0] and model == line[1]:
            print("Mech is found!")
            found = True
            mech_list = line
            break
    
    if not found:
        raise Exception("Mech is not found in the DB!")

    f.close()
    #print(mech_list)
    return mech_list