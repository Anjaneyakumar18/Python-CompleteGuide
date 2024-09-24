try:
    
    f=open("0.Example file.txt","rb")
    cont=f.read()
    #print(cont)
    byte_list=[]
    for ch in cont:
        ele="".join(format(ch,'b'))
        byte_list.append(ele)
    print(byte_list)
    char_list=[]
    for binary_num in byte_list:
        deci_num=int(binary_num,2)
        letter=bytes([deci_num])
        char_list.append(letter)
    #print(char_list)

    cont=''
    for letter in char_list:
        letter=str(letter)[2:-1]
        cont+=letter

    print(cont)


except FileNotFoundError as e:
    print(f"Error message: {e}")