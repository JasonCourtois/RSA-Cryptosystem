import rsa
import stdio
import sys


# Entry point.
def main():
    # Accepts (n and e) as command line arguments.
    n = int(sys.argv[1])
    e = int(sys.argv[2])
    # Sets the number of bits per character in (width) using rsa.bitLength(n).
    width = rsa.bitLength(n)
    # Sets (message) to all characters in standard input as a single string.
    message = stdio.readAll()
    # For every character in (message), encrypt and write it to standard output.
    for c in message:
        x = ord(c)
        x = rsa.encrypt(x, n, e)
        stdio.write(rsa.dec2bin(x, width))
    # Write a blank newline to standard output.
    stdio.writeln()


# If this program is run as an application, run main().
if __name__ == '__main__':
    main()
