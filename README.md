# 8bit-cpu

Code used to assist with the build of my [8-bit CPU](https://eater.net/8bit).

Organised by language then category of problem domain.


## Binary to decimal decoder

The bitmap to flash onto an [AT28C64B EEPROM](https://bencode.io/blob/datasheet-atmel-eeprom-at28c64b.pdf) that will translate a binary number (e.g. `101`) into its decimal representation on a seven segment display (e.g. `5`)

Seven segment displays generally work the same in terms of pinout. The main difference in types is their polarity, either +V is used to activate segments (called common cathode), or -V are used (called common anode). For my output module, are using four bright green (Gallium Phosphide Green) common cathode [Kingbright SC56-11GWA](https://bencode.io/blob/datasheet-kingbright-7-segment-SC56-11GWA.pdf).

Here's the basic topology for most seven segments displays:

```
   a
  ---
f| g |b
  ---
e|   |c
  ---
   d
```

Pinout:

- a = pin 7
- b = pin 6
- c = pin 4
- d = pin 2
- e = pin 1
- f = pin 9
- g = pin 10

As an example, to activate the top segment (labelled a), need to push power through pin 7.

How you wire the displays up to the EEPROM is totally up to you, but you need to come up with a scheme and use it consistently.

For example, here is the schema Ben Eater came up with.

| 0d  | dp  | a   | b   | c   | d   | e   | f   | g   | 0x  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0   | 0   | 1   | 1   | 1   | 1   | 1   | 1   | 0   | 7e  |
| 1   | 0   | 0   | 1   | 1   | 0   | 0   | 0   | 0   | 30  |
| 2   | 0   | 1   | 1   | 0   | 1   | 1   | 0   | 1   | 6d  |
| 3   | 0   | 1   | 1   | 1   | 1   | 0   | 0   | 1   | 79  |
| 4   | 0   | 0   | 1   | 1   | 0   | 0   | 1   | 1   | 33  |
| 5   | 0   | 1   | 0   | 1   | 1   | 0   | 1   | 1   | 5b  |
| 6   | 0   | 1   | 0   | 1   | 1   | 1   | 1   | 1   | 5f  |
| 7   | 0   | 1   | 1   | 1   | 0   | 0   | 0   | 0   | 70  |
| 8   | 0   | 1   | 1   | 1   | 1   | 1   | 1   | 1   | 7f  |
| 9   | 0   | 1   | 1   | 1   | 1   | 0   | 1   | 1   | 7b  |

Notes:

- The `g` pin (the middle segment) is represented by least significant bit (LSB)
- `dp` is the decimal point, which given are displaying integers don't have a need for
