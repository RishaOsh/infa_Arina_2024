
from math import *

def color(H, n):
    L = 0.5
    S = 1
    a = S * min(L, 1-L)
    k = (n + (H/30)) % 12
    f = L - a * max(-1, min(k-3, 9-k, 1))
    return(f)
    

def RGB(H):
    R = color(H,0)
    G = color(H,8)
    B = color(H,4)
    return(R,G,B)
    
def intRGB(H):
    return list(map(lambda x: int(255*x), RGB(H)))