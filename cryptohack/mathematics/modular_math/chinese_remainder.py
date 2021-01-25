import operator, functools

def crt(ints, modulii):
    """
    Given two lists of numbers [a_1, ..., a_n] and [n_1, ..., n_n], find
    the unique solution to the system
        x == a_1 mod n_1
        ...
        x == a_n mod n_n
    where x == a mod N and N = n_1 * ... * n_n.

    Input:  ints, a list of numbers a_1 through a_n, and
            modulii, a list of modulii n_1 through n_n
    Output: the unique solution x guaranteed by the Chinese Remainder Theorem
    """
    
    n_tot = functools.reduce(operator.mul, modulii, 1)

    # Calculate the Chinese Remainder Theorem coefficients, where
    # c_i is (n_tot / n_i) * (n_tot / n_i)^-1 mod n_i
    c = [(n_tot // n_i) * pow(n_tot // n_i, n_i - 2, n_i) for n_i in modulii]

    # Compute a_1 * c_1 + ... + a_n * c_n
    return sum(i[0] * i[1] for i in zip(ints, c)) % n_tot

if __name__ == "__main__":
    print(crt([2, 3, 5], [5, 11, 17]))
    
    
