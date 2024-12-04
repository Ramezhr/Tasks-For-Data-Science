import script_calc as sc

while True:
    op = str(input("enter the operation(add/sub/mult/div):"))
    a = int(input("enter the first number:"))
    b = int(input("enter the second number:"))
    if op.lower() == 'add':
        result = sc.add(a, b)
        print(result)
        ask = str(input("do you want to make another operation? (ok or stop):"))
        if ask == 'stop':
            break
    elif op.lower() == 'sub':
        result = sc.sub(a, b)
        print(result)
        ask = str(input("do you want to make another operation? (ok or stop):"))
        if ask == 'stop':
            break
    elif op.lower() == 'mult':
        result = sc.mult(a, b)
        print(result)
        ask = str(input("do you want to make another operation? (ok or stop):"))
        if ask == 'stop':
            break
    elif op.lower() == 'div':
        result = sc.div(a, b)
        print(result)
        ask = str(input("do you want to make another operation? (ok or stop):"))
        if ask == 'stop':
            break
    else:
        print("the operation is wrong write it again!")

