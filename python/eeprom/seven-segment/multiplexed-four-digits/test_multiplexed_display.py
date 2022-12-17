import pytest
import multiplexed_display


@pytest.fixture
def buffer():
    b = [b'\x00'] * 2048
    multiplexed_display.write_bytes(b)
    return b


def test_silly():
    assert multiplexed_display.get_address_for_twos_value(0) == 0
    assert multiplexed_display.get_address_for_twos_value(5) == 5
    assert multiplexed_display.get_address_for_twos_value(-5) == 251


def test_unsigned_ones_place_bits(buffer):
    assert buffer[123] == b'\x79'


def test_unsigned_tens_place_bits(buffer):
    assert buffer[123 + 256] == b'\x6d'


def test_unsigned_hundreds_place_bits(buffer):
    assert buffer[123 + 512] == b'\x30'


def test_twos_complement_ones_place_for_negative(buffer):
    address = multiplexed_display.get_address_for_twos_value(-123)
    assert buffer[address + 1024] == b'\x79'


def test_twos_complement_tens_place_for_negative(buffer):
    address = multiplexed_display.get_address_for_twos_value(-123)
    assert buffer[address + 1280] == b'\x6d'


def test_twos_complement_hundreds_place_for_negative(buffer):
    address = multiplexed_display.get_address_for_twos_value(-123)
    assert buffer[address + 1536] == b'\x30'


def test_twos_complement_thousands_place_for_negative(buffer):
    address = multiplexed_display.get_address_for_twos_value(-123)
    assert buffer[address + 1792] == b'\x01'


def test_twos_complement_ones_place_for_postive(buffer):
    address = multiplexed_display.get_address_for_twos_value(123)
    assert buffer[address + 1024] == b'\x79'


def test_twos_complement_tens_place_for_postive(buffer):
    address = multiplexed_display.get_address_for_twos_value(123)
    assert buffer[address + 1280] == b'\x6d'


def test_twos_complement_hundreds_place_for_postive(buffer):
    address = multiplexed_display.get_address_for_twos_value(123)
    assert buffer[address + 1536] == b'\x30'


def test_twos_complement_thousands_place_for_postive(buffer):
    address = multiplexed_display.get_address_for_twos_value(123)
    assert buffer[address + 1792] == b'\x00'
