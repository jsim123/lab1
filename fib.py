'''
task = produce list of fibonacci numbers of length n

DIFFICULTY = EASY
TOPICS = lists, variables, loops

1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...
'''

def produceFibsList(n):
    '''
    >>> produceFibsList(0)
    []
    >>> produceFibsList(1)
    [1]
    >>> produceFibsList(2)
    [1, 1]
    >>> produceFibsList(3)
    [1, 1, 2]
    >>> produceFibsList(5)
    [1, 1, 2, 3, 5]
    '''
    # TODO = fill in the code here, and return the correct result using the return keyword
    list = []
    hold = 1
    first = 1
    second = 1

    if(n==0):
        return list

    if ( n==1):
        list.append(1)
        return list

    elif (n==2):
        list.append(1)
        list.append(1)
        return list
    list.append(1)
    list.append(1)
    for i in range (2,n):
        hold=first+second
        first=second
        second=hold
        list.append(hold)
    return list
    pass

if __name__ == '__main__':
    import doctest
    doctest.testmod()
