#!/usr/bin/python3
"""UTF8 Validation Module"""


def validUTF8(data):
    """validates data to be utf8 encoded
    -Check if the first bit of the byte is 0. If it is,
    then it's a 1-byte character.
    -If the first bit is 1,
    count how many consecutive 1s there are from the start.
    This will tell you how many bytes the character takes up.
    -For the next n-1 bytes
    (where n is the number of bytes the character takes up),
    check if the first two bits are 10. If they're not,
    then it's not a valid UTF-8 character.

    # init vars then check if the first bit of byte is 0
    i = 0
    data_shifted = []
    while (i < len(data)):
        if data[i] & 0b10000000 == 0:
            i += 1
            continue  # skips if its 0,, meaning its a byte is 1
        else:
            count = 0
            # if its not 0
            while (data[i] & 0b10000000) != 0:
                count += 1
                data_shifted.append(data[i] << 1)
                i += 1
        # use a loop to check the next n-1 bytes
        if (i + count) > len(data_shifted):
            return False
        for j in range(1, count):
            if (data_shifted[i+j] & 0b11000000) != 0b10000000:
                return False
        i += count
    return True
"""
    number_bytes = 0

    mask_1 = 1 << 7
    mask_2 = 1 << 6

    for i in data:

        mask_byte = 1 << 7

        if number_bytes == 0:

            while mask_byte & i:
                number_bytes += 1
                mask_byte = mask_byte >> 1

            if number_bytes == 0:
                continue

            if number_bytes == 1 or number_bytes > 4:
                return False

        else:
            if not (i & mask_1 and not (i & mask_2)):
                return False

        number_bytes -= 1

    if number_bytes == 0:
        return True

    return False
