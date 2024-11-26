from blind_watermark import WaterMark

# Initialize the WaterMark object with passwords
bwm1 = WaterMark(password_img=1, password_wm=1)

# Read the original image
bwm1.read_img('pic.jpg')

# Define the watermark text
watermark_text = 'Xperi'

# Read the watermark text
bwm1.read_wm(watermark_text, mode='str')

# Embed the watermark into the image and save the result
bwm1.embed('webpage_image/output.jpg')

# Output the length of the watermark bits
len_wm = len(bwm1.wm_bit)
print(f'Watermark embedded. Length of watermark bits: {len_wm}')
