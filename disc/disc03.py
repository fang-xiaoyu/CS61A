#%%
def multiply(m, n):
    """
    >>> multiply(5, 3)
    15
    """
    if n >= 1:
        return m + multiply(m, n-1)
    else:
        return 0

from doctest import run_docstring_examples
run_docstring_examples(multiply, globals(), True)
# %%
def is_prime(n):
    """
    >>> is_prime(7)
    True
    >>> is_prime(9)
    False
    >>> is_prime(1)
    False
    """
    def prime_helper(m = 2):
        if m == n:
            return True
        elif n % m == 0 or n == 1:
            return False
        else:
            return prime_helper(m + 1)
    return prime_helper()
run_docstring_examples(is_prime, globals(), True)
# %%
def make_func_repeater(f, x):
    """
    >>> incr_1 = make_func_repeater(lambda x: x + 1, 1)
    >>> incr_1(2) #same as f(f(x))
    3
    >>> incr_1(5)
    6
    """
    def repeat(m):
        if m == 0:
            return x
        else:
            return make_func_repeater(f, f(x))(m - 1)
            #return f(repeat(m - 1))
    return repeat
run_docstring_examples(make_func_repeater, globals(), True)
# %%
def count_stair_ways(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return count_stair_ways(n - 1) + count_stair_ways(n - 2)
count_stair_ways(1)
# %%
def count_k(n, k):
    """
    >>> count_k(3, 3) # 3, 2 + 1, 1 + 2, 1 + 1 + 1
    4
    >>> count_k(4, 4)
    8
    >>> count_k(10, 3)
    274
    >>> count_k(300, 1) # Only one step at a time
    1
    """
    #count_k(n, k) = count_k(n, k - 1) + count_k(n - k, k)
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        i, total = 1, 0
        while i <= k:
            total += count_k(n - i, k)
            i += 1     
        return total
run_docstring_examples(count_k, globals(), True)

