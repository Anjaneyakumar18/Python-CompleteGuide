with open("0.Example file.txt",'w') as file:
    lines=["I am Ak\n","Leetcode\n","DSA\n",'DBMS\n',"PYTHON"]
    file.writelines(lines)
    file.close()