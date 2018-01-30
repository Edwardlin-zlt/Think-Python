def Exercise(x,y):
    if x>y:
        return 1
    elif x == y:
        return 0
    else:
        return -1

x = int(raw_input())
y = int(raw_input())

print Exercise(x,y)
