def py4(a,b):
    if a*1000/360>b:
        return a
    else:
        return b
if __name__=="__main__":
    print py4(input(),input())
