def triangle(h, depth=1,symbol='.'):
    if h%2!=0 and depth==h//2+1:
        print(symbol*depth)
        return
    print(symbol*depth)
    triangle(h,depth = depth+1)
    print(symbol*depth)
    return
triangle(int(input()))
