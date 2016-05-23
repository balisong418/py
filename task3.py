def dubleseven():
    number =  float(input())
    if (number/7 == number//7):
        return int(number*2)
    else:
        return "exeption"

if __name__ == "__main__":
    print dubleseven()
