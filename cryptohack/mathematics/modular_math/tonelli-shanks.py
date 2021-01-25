from legendre import legendre
import tonelli_nums

def modular_root(x, p):
    """
    Find the square root of a quadratic residue x modulo a prime p using the
    Tonelli-Shanks algorithm.

    Input: quadratic residue x, prime p
    Output: r in Z/pZ such that r^2 = x, None if no such root exists
    """

    # Check that x is a quadratic residue mod p
    if not legendre(x, p):
        return None

    # Find q and s such that p - 1 = q * 2^s with q odd
    q = p - 1
    s = 0
    while q % 2 == 0:
        q = q // 2
        s += 1

    # Find a quadratic non-residue z
    z = 2 
    while legendre(z, p):
        z += 1
    
    # Set initial parameters
    m = s
    c = pow(z, q, p)
    t = pow(x, q, p)
    r = pow(x, (q + 1)//2, p)

    # Find successive pairs of r and t that satisfy r^2 == n * t (mod p)
    # and t is a 2^(m-1) root of 1. Once t == 1 (mod p), we have found 
    # r to be the square root of x.
    while True:
        if t == 0:
            return 0
        elif t == 1:
            return r
        else:
            for i in range(1, m + 1):
                if i == m:
                    return None
                if pow(t, 2**i, p) == 1:
                    break
            b = pow(c, 2**(m - i - 1), p)
            m = i
            c = pow(b, 2, p)
            t = (t * c) % p
            r = (r * b) % p

if __name__ == "__main__":
    root = modular_root(tonelli_nums.a, tonelli_nums.p)
    roots = (root, -root % tonelli_nums.p)
    print(min(roots))

