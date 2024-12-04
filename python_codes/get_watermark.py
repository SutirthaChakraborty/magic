from blind_watermark import WaterMark

# Initialize the WaterMark object with passwords
bwm1 = WaterMark(password_img=1, password_wm=1)

len_wm = 39

# Extract the watermark from the embedded image
extracted_watermark = bwm1.extract(
    'magic/images/output.jpg', wm_shape=len_wm, mode='str'
)


# Print the extracted watermark
print(f'Extracted Watermark: {extracted_watermark}')
