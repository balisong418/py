def task53(n):
    i=0
    while n>1:
        if n%10==8:
            i+=1
        n=n//10
    return i
if __name__=="__main__":
    print task53(input())
