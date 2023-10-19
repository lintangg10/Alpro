import sys
sys.setrecursionlimit(10000)

def hello_world(n):
    for i in range(n):
        print('Hello world!')

def hello_world_rekrusif(n):
    if n == 0: #base case n=0
        return #exit dari fungsi
    else:
        print('Hello World!') #print sekali
        hello_world_rekrusif(n-1) #sisanya

hello_world(10)
