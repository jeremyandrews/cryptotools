
from pathlib import Path
from bisect import bisect_left

from transformations import int_to_bin, bin_to_bytes, bytes_to_bin, sha256

HERE = Path(__file__).absolute().parent

with open(HERE / 'wordlist.txt') as file:
    WORDS = file.read().split('\n')


def binary_search(word):
    hi, lo = len(WORDS), 0
    pos = bisect_left(WORDS, word, lo, hi)  # find insertion position
    if pos != hi and WORDS[pos] == word:
        return pos
    raise LookupError(f'{word} not in list')


def check(mnemonic):
    mnemonic = mnemonic.lower().split()

    if len(mnemonic) not in {12, 15, 18, 21, 24}:
        return False

    try:
        indexes = [binary_search(word) for word in mnemonic]
    except LookupError:
        return False

    bits = ''.join(int_to_bin(idx).zfill(11) for idx in indexes)
    checksum_length = len(mnemonic)//3
    data, checksum = bin_to_bytes(bits[:-checksum_length]), bits[-checksum_length:]
    return bytes_to_bin(sha256(data)).zfill(256)[:checksum_length] == checksum
