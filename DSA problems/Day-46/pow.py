#striver
#https://takeuforward.org/plus/dsa/recursion/implementation-problems/pow(x,n)
#recursion-easy

def rec(x,n):
    if n==0:
        return 1
    if n < 0:
        return 1 / rec(x, -n)
    if n%2==0:
        return rec(x*x,n//2)
    else:
        return x * rec(x,n-1)

x = 2.5000
n = 2
print(rec(x,n))