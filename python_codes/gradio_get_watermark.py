import gradio as gr
from blind_watermark import WaterMark


# Function to extract watermark
def extract_watermark(image_path):
    # Initialize the WaterMark object with passwords
    bwm1 = WaterMark(password_img=1, password_wm=1)
    len_wm = 39  # Length of the watermark

    # Extract the watermark
    extracted_watermark = bwm1.extract(image_path, wm_shape=len_wm, mode='str')

    # Return the extracted watermark
    return f'Extracted Watermark: {extracted_watermark}'


# Gradio interface
with gr.Blocks() as demo:
    gr.Markdown("### Upload an image to extract the watermark")
    with gr.Row():
        image_input = gr.Image(type="filepath", label="Upload Image")
        watermark_output = gr.Textbox(label="Extracted Watermark")
    extract_button = gr.Button("Extract Watermark")
    extract_button.click(
        fn=extract_watermark, inputs=image_input, outputs=watermark_output
    )

# Launch the app
demo.launch(share=True)
