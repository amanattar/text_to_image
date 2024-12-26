import streamlit as st
from diffusers import StableDiffusionPipeline
import torch
from PIL import Image
import io

# Set up the Streamlit interface
st.title("Text-to-Image Generator")
st.write("Enter a description, and the AI will generate an image based on your input.")

# Sidebar instructions
st.sidebar.title("Instructions")
st.sidebar.write(
    """
    1. Enter a detailed description of the image you want to generate in the text box.
    2. Click 'Generate Image' to see the result.
    """
)

# Load the Stable Diffusion model
@st.cache_resource
def load_model():
    st.write("Loading model... Please wait.")
    pipe = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5")
    pipe.to("cuda" if torch.cuda.is_available() else "cpu")  # Use GPU if available
    return pipe

pipe = load_model()

# Input for text description
prompt = st.text_input("Describe the image you want to generate:")

if st.button("Generate Image"):
    if prompt:
        with st.spinner("Generating image..."):
            try:
                # Generate the image
                image = pipe(prompt).images[0]
                
                # Display the generated image
                st.image(image, caption="Generated Image", use_container_width=True)
                
                # Download option
                buf = io.BytesIO()
                image.save(buf, format="PNG")
                byte_im = buf.getvalue()
                st.download_button(
                    label="Download Image",
                    data=byte_im,
                    file_name="generated_image.png",
                    mime="image/png"
                )
            except Exception as e:
                st.error(f"Error generating image: {str(e)}")
    else:
        st.warning("Please enter a description before generating an image.")


