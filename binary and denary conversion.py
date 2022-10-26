a=0
while a>=0:
    a = int(input('press 1 for binary to denary, press 2 for denary to binary: '))
    if a == 1:
        binary1 = input("input binary number here: ")
        denary1 = 0
        for digit in binary1:
            denary1 = denary1 * 2 + int(digit)
        print("number: ", str(denary1))
        a=-1
    elif a == 2:
        denary2 = int(input("input denary number here: "))
        binary2 = ""
        while denary2 > 0:
            binary2 = str(denary2%2) + binary2
            denary2 =  denary2//2
        print(binary2)
        a=-1
    else:
        print('not 1 or 2, try again')
        a=0


