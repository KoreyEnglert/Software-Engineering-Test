import random

def password(a): #commit 1
    p = "";
    for x in range(a):
        a = random.randint(0, 61);
        a += 48;
        if(a > 57):
            a += 7
        if(a > 90):
            a += 6
        p += chr(a)
    print(p);

password(10)
print(" ")
password(20)
print(" ")
password(5)
