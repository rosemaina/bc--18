def find_missing(list_1,list_2):

    difference= set(list_1) ^ set(list_2)

    if list_1 ==[] and list_2==[]: 

        return 0

    elif len(list_1) == len(list_2): 

        return 0

    else:

        return (list(difference)[0])

print(find_missing([1,3,6,7], [1,2,3,6,7]))