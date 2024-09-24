with open("0.Example file.txt","r") as file:
    all_lines=file.readlines()#returns list

    print(all_lines)#list with meta chars

    for line in all_lines:
        print(line,end="")