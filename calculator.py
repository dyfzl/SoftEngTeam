def main():
    a = input()
    flag = True
    if not a.isdigit() :
        flag = False
        a = float(a)
    else : a = int(a)

    if a == 7532:
        print("[EVENT] Software Engineering Class")
        return
    elif a == 1015:
        print("[EVENT] 전북대 개교기념일입니다.")
        return
    elif a == 7503:
        print("[EVENT] 안녕! 7503은 사용할 수 없는 숫자야")
        return
    while True:
        operator = input()
        if operator == 7532:
            print("[EVENT] Software Engineering Class")
            return
        elif operator == 1015:
            print("[EVENT] 전북대 개교기념일입니다.")
            return
        elif operator == 7503:
            print("[EVENT] 안녕! 7503은 사용할 수 없는 숫자야")
            return
        elif operator == '=':
            if not flag:
                print('[SYSTEM] ERROR!')
            else:
                print(a)
            break
        elif operator == "-":
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

        elif operator == '!':
            if not flag:
                print('[SYSTEM] Input Error')
                a = None
                break
            else:
                a = facto(a)
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
        print("[EVENT] Software Engineering Class")
        return
    elif b == 1015:
        print("[EVENT] 전북대 개교기념일입니다.")
        return
    elif b == 7503:
        print("[EVENT] 안녕! 7503은 사용할 수 없는 숫자야")
        return
    else:
        return a - b

def add(a):
    b = input()
    if not b.isdigit() :
        return False
    else : b = int(b)

    if b == 7532:
        print("[EVENT] Software Engineering Class")
        return
    elif b == 1015:
        print("[EVENT] 전북대 개교기념일입니다.")
        return
    elif b == 7503:
        print("[EVENT] 안녕! 7503은 사용할 수 없는 숫자야")
        return
    else:
        return a + b

def mul(a):
    b = input()
    if not b.isdigit() :
        return False
    else : b = int(b)

    if b == 7532:
        print("[EVENT] Software Engineering Class")
        return
    elif b == 1015:
        print("[EVENT] 전북대 개교기념일입니다.")
        return
    elif b == 7503:
        print("[EVENT] 안녕! 7503은 사용할 수 없는 숫자야")
        return
    else:
        return a * b

def facto(a):
    if a == 0 or a == 1:
        return 1
    elif a < 0:
        print("[SYSTEM] Out Of Range")
        return None
    else:
        result = 1
        for i in range(2, a + 1):
            result *= i
        return result

if __name__ == "__main__" :
    main()
