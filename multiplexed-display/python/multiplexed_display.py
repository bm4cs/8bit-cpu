
digits = [b'\x7e', b'\x30', b'\x6d', b'\x79', b'\x33',
          b'\x5b', b'\x5f', b'\x70', b'\x7f', b'\x7b']


def print_bytes_list(buffer: list):
    for i, byte in enumerate(buffer):

        line_break = (i + 1) % 16 == 0

        byte_printable = byte.hex()
        if line_break == False:
            byte_printable += '-'
        print(byte_printable, end='')

        if line_break:
            print('')


def write_bytes(buffer: list):
    print('Programming ones place')
    for i in range(256):
        buffer[i] = digits[i % 10]

    print('Programming tens place')
    for i in range(256):
        buffer[i + 256] = digits[int(i / 10) % 10]

    print('Programming hundreds place')
    for i in range(256):
        buffer[i + 512] = digits[int(i / 100) % 10]


if __name__ == '__main__':
    buffer = [b'\x00'] * 2048
    write_bytes(buffer)
    print_bytes_list(buffer)
