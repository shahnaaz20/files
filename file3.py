banks_list = ["Kotak", "HDFC", "RBL", "SBI", "Bank of Baroda"]
i = 0
my_file = open("question3.txt","w")
while i < len(banks_list):
    my_file.write(banks_list[i])
    my_file.write("\n")
    i = i + 1
my_file.close()
    