'''
    Name: multiplexed_display.py
    Author: Benjamin Simmonds
    Date created: 2022-07-17
    Date last modified: 2022-10-22
    Python: 3.10
    What: Converts an integer (<256) to from its binary 
          to a decimal on four 7 segment displays.
          Supports both simple and 2's complement binary.
    How:  Each digit is displayed one at a time,
          reading from different regions of the EEPROM.
          The memory region to read from is determined using
          by toggling two high address bits with a 4-bit binary counter.
          In affect multiplexing the display of the four digits,
          using only one EEPROM.
          
        See https://eater.net/8bit/output
            https://www.bencode.io/posts/8bit/#two-complement
'''

class colors: # You may need to change color settings
    RED = '\033[31m'
    ENDC = '\033[m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'

digits = [b'\x7e', b'\x30', b'\x6d', b'\x79', b'\x33',
          b'\x5b', b'\x5f', b'\x70', b'\x7f', b'\x7b']


def write_bitmap_for_unsigned(buffer: list):
    '''
    Simple unsigned binary representation.
    Stored from address 0 upward.
    '''

    # ones place
    for i in range(256):
        buffer[i] = digits[i % 10]

    # tens place
    for i in range(256):
        buffer[i + 256] = digits[int(i / 10) % 10]

    # hundreds place
    for i in range(256):
        buffer[i + 512] = digits[int(i / 100) % 10]

    # sign
    for i in range(256):
        buffer[i + 768] = b'\x00'


def get_address_for_twos_value(value: int) -> int:
    '''
    The twos complement for an 8bit value supports -128 to 127.
    The negatives need to be stored in the EEPROM address that 
    corresponds to its unsigned value, for example:
    5 (00000101) should be stored in address 5.
    -5 (11111011) should be stored in address 251.
    '''
    if value < 0:
        return value + 2**8
    return value


def write_bitmap_for_twos_complement(buffer: list):
    '''
    Two complement is the best way to represent signed integers as binary.
    Twos complement mappings are stored from address 1024 upward.
    This way a simple toggle switch that turns on the 1024 address bit in the EEPROM
    can be used, as a way to switch from simple mode to two complement mode.
    '''
    # ones place for twos complement
    for i in range(-128, 128):
        buffer[get_address_for_twos_value(i) + 1024] = digits[abs(i) % 10]

    # tens place for twos complement
    for i in range(-128, 128):
        buffer[get_address_for_twos_value(i) + 1280] = digits[abs(int(i / 10)) % 10]

    # hundreds place for twos complement
    for i in range(-128, 128):
        buffer[get_address_for_twos_value(i) + 1536] = digits[abs(int(i / 100)) % 10]

    # sign for twos complement
    for i in range(-128, 128):
        if i < 0:
            buffer[get_address_for_twos_value(i) + 1792] = b'\x01'  # 0x01 = g segment (negative symbol)
        else:
            buffer[get_address_for_twos_value(i) + 1792] = b'\x00'


def print_bytes(buffer: list):
    '''Prints binary list as hex, 16 bytes per line.'''
    for i, byte in enumerate(buffer):

        line_break = (i + 1) % 16 == 0

        byte_printable = byte.hex()
        if line_break == False:
            byte_printable += '-'
        print(byte_printable, end='')

        if byte_printable == '30783030':
            print(colors.RED + str(i) + colors.ENDC + ' ' + colors.GREEN + str(byte_printable) + colors.ENDC)

        if line_break:
            print('')


def write_bytes(buffer: list):
    '''
    Binary to decimal mapping for simple binary and twos complement.
    '''
    write_bitmap_for_unsigned(buffer)
    write_bitmap_for_twos_complement(buffer)


if __name__ == '__main__':
    buffer = [b'\x00'] * 2048
    write_bytes(buffer)
    print_bytes(buffer)
    with open("seven-segment-bin2dec-map.bin", "wb") as out_file:
        for byte in buffer:
            out_file.write(byte)
