# QRCode-Generator
Python script generates QR codes using the segno library, a tool for creating QR codes. Here's a breakdown of what the script is doing:

Library Import:
The script starts by importing the segno library, which is used to generate QR codes.

Generating QR Codes:

Three different QR codes are generated, each with a unique purpose:
Portfolio Website QR Code (darkblue_qrcode.png):

URL: https://aviyasingh.wixsite.com/analyst
QR Code color settings:
Dark color: Dark blue
Light color: Light blue (for the background)
LinkedIn QR Code (maroonblue_qrcode.png):

URL: https://www.linkedin.com/in/aviya-singh-055562114/
QR Code color settings:
Dark color: Dark blue
Quiet zone color: Green
GitHub QR Code (datagreen_qrcode.png):

URL: https://github.com/Aviya-Singh
QR Code color settings:
Dark color: Dark blue
Light color: Light blue (for the background)
Quiet zone color: Maroon
Data dark color: Green
Data light color: Light green
Saving QR Codes:

After configuring the settings for each QR code, they are saved as PNG image files with specified filenames (darkblue_qrcode.png, maroonblue_qrcode.png, datagreen_qrcode.png) in the specified directory (/Users/aviyasingh/Documents/Python/).
The scale of each QR code is set to 5 (which determines the size of the QR code).
The script essentially creates QR codes for different URLs and customizes their appearance by setting colors for different components like dark color, light color, quiet zone color, etc., providing distinct visual identities for each QR code.
