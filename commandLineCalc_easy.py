'''
make a command line calculator

DIFFICULTY = MEDIUM
TOPICS = strings, variables, lists

your task is to write a command line calculator
this task is easy since we can use the eval function to do most of the legwork
however, we need to parse possible invalid user input. This is your task

return None if invalid input. Otherwise return the result
'''

def calculate(s):
    '''
    >>> calculate("1+3")
    4
    >>> calculate("1+3*4/3")
    5.0
    >>> calculate("(1+3)*5")
    20
    >>> calculate("-----1")
    -1
    >>> calculate("-+-1")
    1
    >>> calculate(\'print("bad guy coming to hack")\')
    '''
    # TODO = fill in this function
    true =1
    for i in range (len(s)):
        if((ord(s[i])<40 or ord(s[i])>57)):
            true = 0

    if (true==0):
        return
    return eval(s)

    pass

if __name__ == '__main__':
    import doctest
    doctest.testmod()
