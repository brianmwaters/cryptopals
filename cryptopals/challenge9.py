"""Solution to Cryptopals Set 2, Challenge 9."""


def pkcs7_pad(bytes_, len_):
    """Pad a byte sequence with PKCS #7."""
    remainder = len_ % len(bytes_)
    pad_len = remainder if remainder != 0 else len_
    return bytes_ + bytes([remainder] * pad_len)


def pkcs7_unpad(bytes_, len_):
    """Unpad a byte sequence with PKCS #7."""
    remainder = bytes_[-1]
    pad_len = remainder if remainder != 0 else len_
    msg = bytes_[:-pad_len]
    pad = bytes_[-pad_len:]
    if remainder >= len_ or any(p != remainder for p in pad):
        raise ValueError("Invalid padding")
    return msg
