import random as r

a=r.randint(1,100)
b=r.randint(1,100)

print(a,'+' ,b,'=')
x=input('------>')
c=int(x)

if a+b==c:
    print('정답')
else:
    print('틀림')
