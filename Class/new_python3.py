def fun():
    print('this is functions file')

def even_odd(n):
    
    ''' this is function to check even odd'''

    if n%2==0:
        print(n,'is even')
    else:
        print(n,'is odd')


def prime_num(n):
    ''' this is function for prime number'''
    if n<=1:
        print('not prime')
    for i in range(2,n):
        if n%i==0:
            print('not prime')
            break
        
    else:
        print('prime')

from random import *
def pop(guess_num):
    ''' this is function guess number in set'''
    s=[]
    i=0
    while i<=10:
        s.append(randint(1,100))
        i+=1
    
    
    if guess_num == s:
        print('you win')
    else:
        print('try again')