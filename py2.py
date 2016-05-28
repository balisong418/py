def py2(a,b,c):
    list=[a,b,c]
    list2=[]
    for i in list:
        if i>0:
            i=i**3
        else:
            i=0
        list2.append(i)
    return list2
if __name__=="__main__":
    print py2(input(),input(),input())
