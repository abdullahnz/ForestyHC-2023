#!/usr/bin/env python3

def xor(x, y):
    return bytes([a ^ b for a, b in zip(x, y)])

banner_enc = open('banner.png.enc', 'rb').read()
banner_png = open('banner.png', 'rb').read()

keystream = xor(banner_enc, banner_png)

flag_enc = open('flag.png.enc', 'rb').read()
flag_png = xor(flag_enc, keystream)

open('recover_flag.png', 'wb').write(flag_png)