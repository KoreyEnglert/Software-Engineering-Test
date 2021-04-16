import random

def password(a): #commit 1
    list = [];
    for x in range(a):
        a = random.randint(0, 61) + 48;
        if(a > 57):
            a += 8
        if(a > 90):
            a += 7
            list.append(chr(a))
    print(list);

password(60)
print(" ")
password(20)
print(" ")
password(9)
