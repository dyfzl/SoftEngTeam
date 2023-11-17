def main():
    a = input()
    flag = True
    if not a.isdigit() :
        flag = False
        a = float(a)
    else : a = int(a)

    if a == 7532:
        print("Software Engineering Class")
        return
    while True:
        operator = input()
        if operator == 7532:
            print("Software Engineering Class")
            return
        elif operator == '=':
            if not flag:
                print('ERROR!')
            else:
                print(a)
            break

        if operator == "-":
            a = sub(a)
            if a is None:
                break
            elif a is False:
                flag = False
        elif operator == "+":
            a = add(a)
            if a is None:
                break
            elif a is False:
                flag = False
        elif operator == '*':
            a = mul(a)
            if a is None:
                break
            elif a is False:
                flag = False
        else:
            flag = False

def sub(a):
    b = input()
    if not b.isdigit() :
        return False
    else : b = int(b)
    if b == 7532:
        print("Software Engineering Class")
        return None
    else:
        return a - b

def add(a):
    b = input()
    if not b.isdigit() :
        return False
    else : b = int(b)
    if b == 7532:
        print("Software Engineering Class")
        return None
    else:
        return a + b

def mul(a):
    b = input()
    if not b.isdigit() :
        return False
    else : b = int(b)
    if b == 7532:
        print("Software Engineering Class")
        return None
    else:
        return a * b


if __name__ == "__main__" :
    main()
