def fromto():
    number = float(input())
    if (number <= 1) & (number >= 0):
        return "true"
    else:
        return "false"

if __name__ == "__main__":
    print fromto()
