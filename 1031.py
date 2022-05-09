#Josephus Problem
def CriseEn(n , m):
    if n==1:
        return 1
    else:
        return (CriseEn(n-1 , m) + m-1) % n +1

while True:
    n = int(input())
    if n == 0:
        break
    else:
        c = 1
        while True:
            r = CriseEn(n-1, c)
            if r == 12:
                print(c)
                break
            else:
                c+=1
