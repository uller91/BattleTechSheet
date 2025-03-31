import os.path
import os
import ast


def read_mech_list():   
    # reading the file with the explicit file path
    mechs_dict = {}
    
    file_path = os.path.join("data", "mech_list.csv")
    f = open(file_path, "r")
    content = f.readlines()

    for i in range(len(content)):
        if i == 0:
            continue #skiping the first line
        line = (content[i].strip("\n")).split("; ")
        if line[1] in mechs_dict.keys():
            mechs_dict[line[1]].update({line[2] : line[0]})
        else:
            mechs_dict[line[1]] = {line[2] : line[0]}

    f.close()
    return mechs_dict


def read_mech_data(line_number, variant, model):
    mech_list = {}

    file_path = os.path.join("data", "mech_data.csv")
    f = open(file_path, "r")
    content = f.readlines()
    if int(line_number) >= len(content):
        raise Exception(f"{line_number} line doesn't exist in DB")

    titles = (content[0].strip("\n")).split("; ")
    mech = (content[int(line_number)].strip("\n")).split("; ")

    if mech[1] != variant or mech[2] != model:
        raise Exception(f"Mech is not found in the DB on {line_number} line!")
    
    for i in range(len(titles)):    #assuming all the plain text goes in the columns 0-5
            if i > 5:
                mech_list[titles[i]] = ast.literal_eval(mech[i])    #text to dictionary conversion
            else:
                mech_list[titles[i]] = mech[i]

    f.close()
    return mech_list