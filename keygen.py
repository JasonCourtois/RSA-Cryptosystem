import rsa
import stdio
import sys


# Entry point.
def main():
    # Accept (lo and hi) as command line arguments.
    lo = int(sys.argv[1])
    hi = int(sys.argv[2])
    # Use rsa.keygen() to generate (n, e, and d) values.
    n, e, d = rsa.keygen(lo, hi)
    # Write generated values to standard output.
    stdio.writef("%d %d %d", n, e, d)


# If this program is run as an application, run main().
if __name__ == '__main__':
    main()
