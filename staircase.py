
def print_staircase(length):
    for n in range(1,length+1):
        print(' '*(length-n)+'#'*(n))
        # print('#'*n+' '*(length-n))
        
    

if __name__=='__main__':
    length=int(input())
    print_staircase(length)