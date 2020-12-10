UNICODE_MALAYALAM = 29
_unicode_blocks = [
    (UNICODE_MALAYALAM, 0x0D00, 0x0D7F)
]

NUM_BLOCKS = len(_unicode_blocks)


def unicode_block(ch):
    '''Return the Unicode block name for ch, or None if ch has no block.'''
    cp = ord(ch)
    # special case basic latin
    # binary search for the correct block
    be, en = 0, NUM_BLOCKS - 1
    while be <= en:
        mid = (be+en) >> 1
        name, start, end = _unicode_blocks[mid]
        if start <= cp <= end:
            return name
        if cp < start:
            en = mid-1
        else:
            be = mid+1
