'''this is the program to print fibonacci sequence, this is the most 
easiest way to print this sequence. I implimented this
by understanding simultanious assignment.'''

n=int(input("enter: "))
a,b=0,1
while(n>=0):
    n-=1
    print(a)
    a,b=b,a+b
