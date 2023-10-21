import stdio
import stdrandom
import sys


# Generates and returns the public/private keys as a tuple (n, e, d). Prime numbers p and q
# needed to generate the keys are picked from the interval [lo, hi).
def keygen(lo, hi):
    # Create a list(pqprimes) of two samples of prime numbers from the range [lo, hi}.
    pqprimes = _sample(_primes(lo, hi), 2)

    # Set (q) to the first value in the list and (p) to the second value.
    q = pqprimes[0]
    p = pqprimes[1]

    # Set (n) equal to (p * q) and (m) equal to (p - 1) * (q - 1).
    n = p * q
    m = (p - 1) * (q - 1)

    # Create a list(mprimes) of primes from the range [2, m).
    mprimes = _primes(2, m)

    # Set (e) to a random single value from the list (mprimes).
    e = _choice(mprimes)

    # While (e) divides (m) without a remainder, choose a new number.
    while m % e == 0:
        e = _choice(mprimes)

    # Generate a random number from the range [1, m) in variable (d).
    d = stdrandom.uniformInt(1, m)

    # While (e * d) mod (m) does not equal 1, generate a new number.
    while (e * d) % m != 1:
        d = stdrandom.uniformInt(1, m)

    # Return n, e, and d.
    return n, e, d


# Encrypts x (int) using the public key (n, e) and returns the encrypted value.
def encrypt(x, n, e):
    # Returns encrypted value using given equation: x^e mod n.
    return (x ** e) % n


# Decrypts y (int) using the private key (n, d) and returns the decrypted value.
def decrypt(y, n, d):
    # Returns decrypted value using given equation: y^d mod n.
    return (y ** d) % n


# Returns the least number of bits needed to represent n.
def bitLength(n):
    return len(bin(n)) - 2


# Returns the binary representation of n expressed in decimal, having the given width, and padded
# with leading zeros.
def dec2bin(n, width):
    return format(n, '0%db' % (width))


# Returns the decimal representation of n expressed in binary.
def bin2dec(n):
    return int(n, 2)


# Returns a list of primes from the interval [lo, hi).
def _primes(lo, hi):
    # Creates an empty list to store prime values.
    primes = []

    # If low value is less than 2, set low to 2 because
    # function doesn't properly define 1 as not prime.
    if lo < 2:
        lo = 2

    # Iterates over the range [Low, high) and checks if each number is a prime.
    for p in range(lo, hi):
        j = 2
        prime = True
        while j <= (p / j):
            if p % j == 0:
                prime = not prime
                break
            j += 1

        # If prime is true, then add (p) to the list of primes.
        if prime:
            primes += [p]

    # Return the list of primes.
    return primes


# Returns a list containing a random sample (without replacement) of k items from the list a.
def _sample(a, k):
    # Creates a complete duplicate of list (a) in list (b).
    b = a[:]

    # Will shuffle the first (k) items in list (b) using range(k).
    for i in range(k):
        # Generate a random index from the range [i, len(b)).
        r = stdrandom.uniformInt(i, len(b))
        # Store the ith value of (b) in temp and swap the values with b[r].
        temp = b[i]
        b[i] = b[r]
        b[r] = temp

    # Return the first (k) items of (b).
    return b[:k]


# Returns a random item from the list a.
def _choice(a):
    # Generate a random index from range [0, len(a)).
    r = stdrandom.uniformInt(0, len(a))

    # Return a[r].
    return a[r]


# Unit tests the library [DO NOT EDIT].
def _main():
    x = ord(sys.argv[1])
    n, e, d = keygen(25, 100)
    encrypted = encrypt(x, n, e)
    stdio.writef('encrypt(%c) = %d\n', x, encrypted)
    decrypted = decrypt(encrypted, n, d)
    stdio.writef('decrypt(%d) = %c\n', encrypted, decrypted)
    width = bitLength(x)
    stdio.writef('bitLength(%d) = %d\n', x, width)
    xBinary = dec2bin(x, width)
    stdio.writef('dec2bin(%d) = %s\n', x, xBinary)
    stdio.writef('bin2dec(%s) = %d\n', xBinary, bin2dec(xBinary))


if __name__ == '__main__':
    _main()
