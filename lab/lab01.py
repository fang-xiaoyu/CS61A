"""Lab 1: Expressions and Control Structures"""
#%%
def sum_naturals(n):
    '''
    >>> sum_naturals(10)
    55
    >>> sum_naturals(100)
    5050
    '''
    total, k = 0, 1
    while k <= n:
        total, k = total+k, k+1
    return total

from doctest import run_docstring_examples
run_docstring_examples(sum_naturals, globals(), True)

#%%
# 'if a' : 'if a != 0'
# 'not a' : 'if a is False, then True, else False'
def kk(positive, negative):
    while negative:
        if positive == 0:
                print(negative)
        positive += 3
        negative += 3
kk(-9,-12)

#%%
def both_positive(x, y):
    """Returns True if both x and y are positive.

    >>> both_positive(-1, 1)
    False
    >>> both_positive(1, 1)
    True
    """
    return (x > 0) and (y > 0) # You can replace this line!
from doctest import run_docstring_examples
run_docstring_examples(both_positive, globals(), True)

#%%
def sum_digits(n):
    """Sum all the digits of n.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> x = sum_digits(123) # make sure that you are using return rather than print
    >>> x
    6
    """
    "*** YOUR CODE HERE ***"
    # '%' : '取模，返回除法的余数'
    # '//' : '地板除法，返回整除结果的整数部分'
    total = 0
    while n // 10 != 0:
        total += n % 10
        n = n // 10
    total += n
    return total
from doctest import run_docstring_examples
run_docstring_examples(sum_digits, globals(), True)

### extra practice ###
"""Optional questions for Lab 1"""

#%%
def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 0)
    1
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    """
    "*** YOUR CODE HERE ***"
    total = 1
    if k == 0:
        return total
    else:
        while k != 0:
            total *= n
            n, k = n-1, k-1
        return total

from doctest import run_docstring_examples
run_docstring_examples(falling, globals(), True) 

#%%
def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"
    while n // 10 != 0:
        if n % 10 == 8 and (n // 10) % 10 == 8:
            return True
        else:
            n = n // 10  
    return False

from doctest import run_docstring_examples
run_docstring_examples(double_eights, globals(), True) 

# %%
