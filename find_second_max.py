if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    c=0
    for a in arr:
        if c > a:
            c=a
    
    print(c)