import numpy as np

def AND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b=-0.7
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1 

def OR(x1, x2):
    x=np.array([x1,x2])
    w=np.array([0.5,0.5])
    b=-0.2
    tmp = np.sum(x*w)+b
    if tmp <= 0:
        return 0
    else:
        return 1

def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    b = 0.7
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

def XOR(x1,x2):
    ORres = OR(x1,x2)
    NANDres = NAND(x1,x2)
    return AND(ORres, NANDres)

if __name__ == '__main__':
    print("AND Gate")
    for xs in [(0,0),(0,1),(1,0),(1,1)]:
        y = AND(xs[0],xs[1])
        print(str(xs)+"->"+str(y))

    print("\nOR Gate")
    for xs in [(0,0),(0,1),(1,0),(1,1)]:
        y = OR(xs[0],xs[1])
        print(str(xs)+"->"+str(y))
        
    print("\nNAND Gate")
    for xs in [(0, 0), (1, 0), (0, 1), (1, 1)]:
        y = NAND(xs[0], xs[1])
        print(str(xs) + " -> " + str(y))
        
    print("\nXOR Gate")
    for xs in [(0, 0), (1, 0), (0, 1), (1, 1)]:
        y = XOR(xs[0], xs[1])
        print(str(xs) + " -> " + str(y))