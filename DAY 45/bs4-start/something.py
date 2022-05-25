n = [4,4,4,11,4,4,11,4,4,4,4,4]

space = []
for i in range(0,len(n)-1) :
    if n[i] != n[-(-1)]:
        home =  abs (0 -((-i)+11))
        space.append(home)
for i in range(1,len(n)) :
    if n[0] != n[-(i)]:
        home =  abs (i -((-i)+11))
        space.append(home)

print(max(space))

def maxDistance(self, A):
        i, j = 0, len(A) - 1
        while A[0] == A[j]: j -= 1
        while A[-1] == A[i]: i += 1
        return max(len(A) - 1 - i, j)



        
    # elif n[i] != n[len(n)-2]:
    #     home =  abs(i - (len(n)-2))
    # elif n[i] != n[len(n)-3]:
    #     home =  abs(i - (len(n)-3))
    # elif n[i] != n[len(n)-4]:
    #     home =  abs(i - (len(n)-4))
    # elif n[i] != n[len(n)-5]:
    #     # home =  abs(i - (len(n)-5))
