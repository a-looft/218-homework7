import os
import qrcode

url = os.getenv('QR_DATA_URL', 'https://github.com/a-looft')
filename = os.getenv('QR_CODE_FILENAME', 'myQR.png')
output_dir = os.getenv('QR_CODE_DIR', 'qr_codes')
fill_color = os.getenv('FILL_COLOR', 'black')
back_color = os.getenv('BACK_COLOR', 'white')

os.makedirs(output_dir, exist_ok=True)

img = qrcode.make(url)
img.save(os.path.join(output_dir, filename))

print(f"QR Code generated for {url} and saved to {output_dir}/{filename}")
