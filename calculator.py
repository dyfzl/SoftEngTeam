def main():
    a = int(input())
    flag = True
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
            if sub(a) is None:
                break
            a = sub(a)
        elif operator == "+":
            if add(a) is None:
                break
            a = add(a)
        elif operator == '*':
            if mul(a) is None:
                break
            a = mul(a)
        else:
            flag = False

def sub(a):
    b = int(input())
    if b == 7532:
        print("Software Engineering Class")
        return None
    return a - b

def add(a):
    b = int(input())
    if b == 7532:
        print("Software Engineering Class")
        return None
    return a + b

def mul(a):
    b = int(input())
    if b == 7532:
        print("Software Engineering Class")
        return None
    return a * b


if __name__ == "__main__" :
    main()
