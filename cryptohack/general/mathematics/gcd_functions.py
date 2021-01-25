def gcd(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    
    return a

def gcd_extended(a, b):
    s0 = 1
    s1 = 0
    t0 = 0
    t1 = 1
    while b != 0:
        r = a % b
        q = a // b

        s = s0 - (q * s1)
        t = t0 - (q * t1)

        a = b
        b = r

        s0 = s1
        s1 = s

        t0 = t1
        t1 = t

    return (a, s0, t0)
