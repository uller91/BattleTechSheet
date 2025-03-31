import random


def get_random_crit():
    value = random.randint(1,6) + random.randint(1,6)
    if value <= 7:
        return 0
    elif value <= 9:
        return 1
    elif value <=11:
        return 2
    else:
        return 3


def get_random_position():
    value = random.randint(1,4)
    if value == 1:
        return "front"
    elif value == 2:
        return "rear"
    elif value == 3:
        return "left"
    else:
        return "right"


def get_random_part(position):
    value = random.randint(1,6) + random.randint(1,6)
    part = "CRIT" 
    match position:
        case "front":
            if value == 2:
                part = "CRIT"
            elif value == 7:
                part = "CT"
            elif value == 3 or value == 4:
                part = "RA"
            elif value == 5:
                part = "RL"
            elif value == 6:
                part = "RT"
            elif value == 8:
                part = "LT"
            elif value == 9:
                part = "LL"
            elif value == 10 or value == 11:
                part = "LA"
            else:
                part = "H"
            return part
        
        case "rear":
            if value == 2:
                part = "CRIT"
            elif value == 7:
                part = "RCT"
            elif value == 3 or value == 4:
                part = "RA"
            elif value == 5:
                part = "RL"
            elif value == 6:
                part = "RRT"
            elif value == 8:
                part = "RLT"
            elif value == 9:
                part = "LL"
            elif value == 10 or value == 11:
                part = "LA"
            else:
                part = "H"
            return part
        
        case "left":
            if value == 2:
                part = "CRIT"
            elif value == 8:
                part = "CT"
            elif value == 10:
                part = "RA"
            elif value == 11:
                part = "RL"
            elif value == 9:
                part = "RT"
            elif value == 7:
                part = "LT"
            elif value == 3 or value == 6:
                part = "LL"
            elif value == 4 or value == 5:
                part = "LA"
            else:
                part = "H"
            return part
        
        case "right":
            if value == 2:
                part = "CRIT"
            elif value == 8:
                part = "CT"
            elif value == 10:
                part = "LA"
            elif value == 11:
                part = "LL"
            elif value == 9:
                part = "LT"
            elif value == 7:
                part = "RT"
            elif value == 3 or value == 6:
                part = "RL"
            elif value == 4 or value == 5:
                part = "RA"
            else:
                part = "H"                 
    return part