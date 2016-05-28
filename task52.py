def task52(n):
    i=0
    res=1
    while i<n:
        i+=1
        res=res*i
    return res
if __name__=="__main__":
    print task52(input())
