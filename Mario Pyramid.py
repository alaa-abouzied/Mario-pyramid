star = ""
num = input("Enter number: ")
for i in range(int(num)):
    for j in range(i+1):
        if j < (int(num)-1):
            star += "*"
        else:
            star += " "
    star += "\n"
print(star)
