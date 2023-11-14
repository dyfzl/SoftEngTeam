def main():
    a = int(input())
    flag = True
    if a == 7532:
        print("Software Engineering Class")
        return
    while True:
        operator = input()
        if operator == '=':
            if not flag:
                print('ERROR!')
            else:
                print(a)
            break
        if operator == "-" :
            a = sub(a)
        elif operator == "+":
            a = add(a)
        elif operator == '*':
            a = mul(a)
        else:
            flag = False

def sub(a):
    b = int(input())
    return a - b

def add(a):
    b = int(input())
    return a + b

def mul(a):
    b = int (input())
    return a * b


if __name__ == "__main__" :
    main()
