import legendre_nums

def legendre(x, p):
    """
    Determines wheter x is a quadratic residue modulo an odd prime p.

    Returns True if x is a quadratic residue, False otherwise.
    """
    return pow(x, (p - 1)//2, p) in [1, 0]

if __name__ == "__main__":
    p = legendre_nums.p
    residue = None
    for num in legendre_nums.ints:
        if legendre(num, p):
            residue = num
            break

    root = pow(residue, (p + 1)//4, p)
    roots = (root, -root % p)
    print(max(roots))
