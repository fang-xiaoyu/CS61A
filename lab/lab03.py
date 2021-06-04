""" Lab 3: Recursion and Python Lists """
#%%
def skip_add(n):
    """ Takes a number x and returns x + x-2 + x-4 + x-6 + ... + 0.

    >>> skip_add(5)  # 5 + 3 + 1 + 0
    9
    >>> skip_add(10) # 10 + 8 + 6 + 4 + 2 + 0
    30
    >>> # Do not use while/for loops!
    >>> from construct_check import check
    >>> check('lab03.py', 'skip_add',
    ...       ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return skip_add(n - 2) + n

from doctest import run_docstring_examples
run_docstring_examples(skip_add, globals(), True) 
#%%
this_file = __file__
def hailstone(n):
    """Print out the hailstone sequence starting at n, and return the
    number of elements in the sequence.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    >>> # Do not use while/for loops!
    >>> from construct_check import check
    >>> check(this_file, 'hailstone',
    ...       ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    print(n)
    list1.append(n)
    if n == 1:    
        return 1
    elif n % 2 == 0:
        return hailstone(n // 2) + 1
    else:
        return hailstone(3 * n + 1) + 1
run_docstring_examples(hailstone, globals(), True) 
#%%
def summation(n, term):

    """Return the sum of the first n terms in the sequence defined by term.
    Implement using recursion!

    >>> summation(5, lambda x: x * x * x) # 1^3 + 2^3 + 3^3 + 4^3 + 5^3
    225
    >>> summation(9, lambda x: x + 1) # 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10
    54
    >>> summation(5, lambda x: 2**x) # 2^1 + 2^2 + 2^3 + 2^4 + 2^5
    62
    >>> # Do not use while/for loops!
    >>> from construct_check import check
    >>> check(this_file, 'summation',
    ...       ['While', 'For'])
    True
    """
    assert n >= 1
    "*** YOUR CODE HERE ***"
    if n == 1:
        return term(n)
    else:
        return summation(n - 1, term) + term(n)

run_docstring_examples(summation, globals(), True) 
# %%


""" Optional problems for Lab 3 """
#%%
def is_prime(n):
    """Returns True if n is a prime number and False otherwise.

    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    "*** YOUR CODE HERE ***"
    def helper(m = 2):
        if m == n:
            return True
        elif n % m == 0:
            return False
        else:
            return helper(m + 1)
    return helper()

from doctest import run_docstring_examples
run_docstring_examples(is_prime, globals(), True) 
#%%
def gcd(a, b):
    """Returns the greatest common divisor of a and b.
    Should be implemented using recursion.

    >>> gcd(34, 19)
    1
    >>> gcd(39, 91)
    13
    >>> gcd(20, 30)
    10
    >>> gcd(40, 40)
    40
    """
    "*** YOUR CODE HERE ***"
    max_num = max(a, b)
    min_num = min(a, b)
    if min_num == 1:
        return 1
    elif max_num % min_num == 0:
        return min_num
    else:
        return gcd(min_num, max_num % min_num)

run_docstring_examples(gcd, globals(), True) 
#%%
def ten_pairs(n):
    """Return the number of ten-pairs within positive integer n.

    >>> ten_pairs(7823952)
    3
    >>> ten_pairs(55055)
    6
    >>> ten_pairs(9641469)
    6
    """
    "*** YOUR CODE HERE ***"
    n_list = []
    while n >= 10:
        res = n % 10
        n_list.append(res)
        n = n // 10
    n_list.append(n)
    def digit_num(digit, n_list):
        q = 0
        for _ in n_list:
            if _ == digit:
                q += 1
        return q
    ten_times = 0
    for digit in n_list:
        num = digit_num(digit, n_list)
        oppose_digit = 10 - digit
        oppose_num = digit_num(oppose_digit, n_list)
        if digit == 5:
            ten_times += (num - 1) / 2
        else:
            ten_times += oppose_num / 2
    return int(ten_times)

from doctest import run_docstring_examples
run_docstring_examples(ten_pairs, globals(), True) 
# %%
