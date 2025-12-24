def armstrong_number(n):     
    total=0
    a=n
    while n>0:
        rem=n%10
        fact=1
        while rem>0:
            fact=fact*rem
            rem=rem-1
        total=total+fact
        n=n//10
    if a==total:
        return("armstrong number")
    else:
        return("not an armstrong number")
n=int(input("enter a number:"))
print(armstrong_number(n))
    
