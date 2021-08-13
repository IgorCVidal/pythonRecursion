A = []
B = []
C = []
K = []
count = 0

# Filling the initial array with number.
def fill_A(n):
    i=0
    while n > len(A):
       i = i+1
       A.append(i)
    print("A: ", A, "B: ",B, "C: ",C)

# Move numbers from stacks and count each move.
def move(x,y):
    global count
    ix=x[len(x)-1]
    y.append(x[len(x)-1])
    x.pop(len(x)-1)
    count +=1
    print('Moved {}, Result = {} and {} and {}!'.format(ix,A,B,C))

# The moving recursion logic. 
def hanoi(n,f,h,t):
    
    if n==0:
        pass
    else:
        hanoi(n-1,f,t,h)
        move(f,t)
        hanoi(n-1,h,f,t)

fill_A(4)
hanoi(4,A,B,C)
print(count, '  moves to complete!')
print("A: ", A, "B: ",B, "C: ",C)
