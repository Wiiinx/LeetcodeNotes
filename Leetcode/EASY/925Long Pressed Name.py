def isLongPressedName(name, typed):
    i = 0
    for j in range(len(typed)):
        if i < len(name) and name[i] == typed[j]:
            i += 1
        elif j == 0 or typed[j] != typed[j-1]:
            return False
    return i == len(name)



def main():

    #print(isLongPressedName("alex", "aaleex")) #True
    #print(isLongPressedName("saeed", "ssaaedd"))
    #print(isLongPressedName("alex", "aaleexa")) # False
    #print(isLongPressedName("vtkgn", "vttkgnn"))
    #print(isLongPressedName("vtkgn", "vttkgnnnnnnnn"))
    #print(isLongPressedName("alexd", "ale"))
    print(isLongPressedName("pyplrz", "ppyypllr"))
    #print(isLongPressedName("a", "b"))

main()