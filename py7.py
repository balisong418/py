def py6(a):
    if 12>a>0:
        if 3>=a>=5:
            return 'spring'
        elif 6>=a>=8:
            return 'summer'
        elif 9>=a>=11:
            return 'fall'
        else:
            return 'winter is comming'
    else:
        return 'exeption'
if __name__=="__main__":
    print py6(input())
