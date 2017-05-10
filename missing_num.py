def find_missing(x,y):

    difference= set(x) ^ set(y)

    if x ==[] and y==[]: 

        return 0

    elif len(x) == len(y): 

        return 0

    else:

        return (list(difference)[0])

print(find_missing([1,3,6,7], [1,2,3,6,7]))
print(find_missing([31,79,11,99], [31,79,0,11,99]))
print(find_missing([17,35,6,7], [17,35,47,6,7]))
print(find_missing([57,93,76,55], [57,12,93,76,55]))
