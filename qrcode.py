# Daarkblue qrcode.py

import segno

#QR Code for Portfolio Website in dark blue and background in lightblue color.
qrcode = segno.make_qr('https://aviyasingh.wixsite.com/analyst')
qrcode.save(
    "/Users/aviyasingh/Documents/Python/darkblue_qrcode.png",
    scale=5,
    dark="darkblue",
    light="lightblue",
)

#QR Code for LinkedIn in dark blue and qyuietzone in green color.
qrcode = segno.make_qr('https://www.linkedin.com/in/aviya-singh-055562114/')
qrcode.save(
    "/Users/aviyasingh/Documents/Python/maroonblue_qrcode.png",
    scale=5,
    dark="darkblue",
    quiet_zone="green",
)

#QR Code for GitHub in dark blue, background in lightblue color, quiet zone in maroon and data in green.
qrcode = segno.make_qr('https://github.com/Aviya-Singh')
qrcode.save(
    "/Users/aviyasingh/Documents/Python/datagreen_qrcode.png",
    scale=5,
    dark="darkblue",
    light="lightblue",
    quiet_zone="maroon",
    data_dark="green",
    data_light="lightgreen",
)


