def py6(a):
    if 12>a>0:
        if 5>=a>=3:
            return 'spring'
        elif 8>=a>=6:
            return 'summer'
        elif 11>=a>=9:
            return 'fall'
        else:
            return 'winter is comming'
    else:
        return 'exeption'
if __name__=="__main__":
    print py6(input())
