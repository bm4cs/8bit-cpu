'''
    File name: multiplexed_display.py
    Author: Benjamin Simmonds
    Date created: 2022-07-17
    Date last modified: 2022-08-24
    Python Version: 3.10
    Description: Converts an integer (<256) to its binary 
                 represention, for use on 7 segment displays.
                 See https://eater.net/8bit
'''


def print_bytes(buffer: list):
    '''Prints binary list as hex, 16 bytes per line.'''
    for i, byte in enumerate(buffer):

        line_break = (i + 1) % 16 == 0

        byte_printable = byte.hex()
        if line_break == False:
            byte_printable += '-'
        print(byte_printable, end='')

        if line_break:
            print('')


def write_bytes(buffer: list):
    '''Binary to decimal (7 segment) mapping.'''

    digits = [b'\x7e', b'\x30', b'\x6d', b'\x79', b'\x33',
              b'\x5b', b'\x5f', b'\x70', b'\x7f', b'\x7b']

    # ones place
    for i in range(256):
        buffer[i] = digits[i % 10]

    # tens place
    for i in range(256):
        buffer[i + 256] = digits[int(i / 10) % 10]

    # hundreds place
    for i in range(256):
        buffer[i + 512] = digits[int(i / 100) % 10]


if __name__ == '__main__':
    buffer = [b'\x00'] * 2048
    write_bytes(buffer)
    print_bytes(buffer)
    with open("7seg-decoder.bin", "wb") as out_file:
        for byte in buffer:
            print(byte.hex())
            out_file.write(byte)
