my_file = open("file4.txt", "r")
for x in my_file:
    if "delhi" in x:
        my_file = open("delhi.txt", "a")
        my_file.write(x)
    elif "shimla" in x:
        my_file = open("shimla.txt","a")
        my_file.write(x)
    else:
        my_file = open("others.txt","a")
        my_file.write(x)
        
