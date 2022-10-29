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


def test_ones_place_bits_for_decimal_123_is_mapping_for_3(buffer):
    assert buffer[123] == b'\x79'


def test_tens_place_bits_for_decimal_123_is_mapping_for_2(buffer):
    assert buffer[123 + 256] == b'\x6d'


def test_hundreds_place_bits_for_decimal_123_is_mapping_for_1(buffer):
    assert buffer[123 + 512] == b'\x30'
