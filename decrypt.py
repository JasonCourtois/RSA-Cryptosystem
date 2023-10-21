import rsa
import stdio
import sys


# Entry point.
def main():
    # Accept (n and d) as command line arguments.
    n = int(sys.argv[1])
    d = int(sys.argv[2])
    # Sets the number of bits per character in (width) using rsa.bitLength(n).
    width = rsa.bitLength(n)
    # Read all characters in standard input and store them in the string (message).
    message = stdio.readAll()
    # Iterates over the range [0, len(message -1) and in increments of (width).
    for i in range(0, len(message) - 1, width):
        # Set (s) to the substring from character [i to i + width).
        s = message[i:i+width]
        # Convert the binary value in (s) to decimal using rsa.bin2dec(s) and store it in (y).
        y = rsa.bin2dec(s)
        # Decrypt (y) using rsa.decrypt(y, n, d) and write chr(y) to standard output.
        y = rsa.decrypt(y, n, d)
        stdio.write(chr(y))


# If this program is run as an application, run main().
if __name__ == '__main__':
    main()
