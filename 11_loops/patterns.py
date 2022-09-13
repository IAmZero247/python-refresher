#pattern 1
# *
# * *
# * * *
# * * * *
# * * * * *

def pattern1(ival):
    for i in range(1,ival+1):
        for j in range( i):
            print(i , end=' '  )
        print()
    return None

print("pattern1:")
pattern1(5)

#pattern 2
#         *
#       * *
#     * * *
#   * * * *
# * * * * *

def pattern2(ival):
    for i in range(1,ival+1):
        for j in range( ival):
            if j<ival-i:
                print(' ', end=' ')
            else:
                print(i, end=' ')
        print()
    return None

print("pattern2:")
pattern2(5)


#pattern 3
# * * * * *
# * * * *
# * * *
# * *
# *
def pattern3(ival):
    for i in range(1,ival+1):
        for j in range( ival+1-i):
            print(ival+1-i , end=' '  )
        print()
    return None

print("pattern3:")
pattern3(5)

#pattern 4
# * * * * *
#   * * * *
#     * * *
#       * *
#         *
def pattern4(ival):
    space =0
    for i in range(1,ival+1):
        for k in range(0, space):
            print(' ', end=' ')
        for j in range( ival+1-i ,0 ,-1):
            print(ival+1-i, end=' ')
        space = space +1
        print()
    return None

print("pattern4:")
pattern4(5)


