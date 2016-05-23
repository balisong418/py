def minmax():
    num1 = input()
    num2 = input()
    num3 = input()
    print "max"
    if num1 >= num2:
        if num1 >= num3:
            print num1
        elif num3 >= num2:
            print num3
        else:
            print num2
    elif num2 >= num3:
        print num2
    else:
        print num3
    print "min"
    if num1 <= num2:
        if num1 <= num3:
            print num1
        elif num3 <= num2:
            print num3
        else:
            print num2
    elif num2 <= num3:
        print num2
    else:
        print num3

if __name__ == "__main__":
    minmax()
