def swap(a, b):
    c = a
    print(a, b, c)
    a = b
    print(a, b, c)
    b = c
    print(a, b, c)

def drawLine(screen, a, b, color):
    if(b[0] < a[0]):
        swap(a, b)
    x = a[0]
    y = a[1]
    B = -1 * (b[0] - a[0])
    if b[1] <= a[1]:
        A = a[1] - b[1]
        if abs(A) >= abs(B):
            d = A + (2 * B)
            while(y >= b[1]):
                plot(screen, x, y, color)
                if(d < 0):
                    x = x + 1
                    d = d + (2*A)
                y = y - 1
                d = d + (2*B)
        else:
            d = (2 * A) + B
            while(x <= b[0]):
                plot(screen, x, y, color)
                if(d > 0):
                    y = y - 1
                    d = d + (2*B)
                x = x + 1
                d = d + (2*A)
    else:
        A = a[1] - b[1]
        if abs(A) >= abs(B):
            d = A - (2 * B)
            while(y <= b[1]):
                plot(screen, x, y, color)
                if(d > 0):
                    x = x + 1
                    d = d + (2*A) 
                y = y + 1
                d = d - (2*B)
        else:
            d = (2 * A) - B
            while(x <= b[0]):
                plot(screen, x, y, color)
                if(d < 0):
                    y = y + 1
                    d = d - (2*B)
                x = x + 1
                d = d + (2*A)

def main():
    a = 5
    b = 3
    swap(a, b)
    print(a, b)

main()
