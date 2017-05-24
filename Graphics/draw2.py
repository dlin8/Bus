def helper():
    d = A + (2 * B)
    while(y >= b[1]):
        plot(screen, x, y, color)
        if(d < 0):
            x = x + 1
            d = d + (2*A)
        y = y - 1
        d = d + (2*B)
    

def drawLine(screen, a, b, color):
    if(b[0] < a[0]):   #Swap if b is to the right of a.
        c = a
        a = b
        b = c
        
    x = a[0]   #Starting pixel.
    y = a[1]
    
    B = -1 * (b[0] - a[0])
    
    if b[1] <= a[1]:   #b is higher than a. Octants: 1, 2.
        if abs(A) >= abs(B):   #Slope >= 1. Octant 2.
            d = A + 2 * B
        else:   #Octant 1.
            d = B + 2 * A
    else: #Octants: 8, 7.
        if abs(A) >= abs(B):   #Slope <= -1. Octant 7.
            d = A - 2 * B
        else:   #Octant 8.
            d = 2 * A - B

def main():
    a = 5
    b = 3
    tmp = swap(a, b)
    a = tmp[0]
    b = tmp[1]
    print(a, b)

main()
