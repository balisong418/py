def py3(n):
    a = n%10==(n//10)%10==(n//100)%10
    b = n%10==(n//10)%10 or (n//10)%10==(n//100)%10 or n%10==(n//100)%10
    return a,b
if __name__=="__main__":
    print py3(input())
