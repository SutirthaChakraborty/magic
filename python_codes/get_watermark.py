from blind_watermark import WaterMark

# Initialize the WaterMark object with passwords
bwm1 = WaterMark(password_img=1, password_wm=1)

# Length of watermark bits must match the embedded watermark
# Replace `len_wm` with the value from the embedding process
len_wm = 32  # Example length (replace with actual value)

# Extract the watermark from the embedded image
extracted_watermark = bwm1.extract(
    'magic/images/output.jpg', wm_shape=len_wm, mode='str'
)

# Print the extracted watermark
print(f'Extracted Watermark: {extracted_watermark}')
