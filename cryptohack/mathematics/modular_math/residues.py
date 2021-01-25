def find_modular_roots(x, p):
    """
    Find the square roots of x modulo p, if they exist.

    This function applies a brute force approach and is inefficient
    for large p.

    Returns the square roots as a tuple if x is a quadratic residue,
    None otherwise.
    """
    for i in range(1, p):
        if pow(i, 2, p) == x:
            return (i, -i % p)
    return None

if __name__ == "__main__":
    p = 29
    ints = [14, 6, 11]
    for x in ints:
        roots = find_modular_roots(x, p)
        if roots is not None:
            print(min(roots))

