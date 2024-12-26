**Text-to-Image Generator**
===========================

**Overview**
------------

This project is a **Text-to-Image Generator** web application built using **Streamlit** and the **Stable Diffusion v1.4** model from Hugging Face. It allows users to generate images from textual descriptions easily.

* * *

**Features**
------------

*   **Text-to-Image Generation**: Converts textual prompts into high-quality images.
*   **Interactive Interface**: Powered by Streamlit, providing a simple and user-friendly experience.
*   **Download Option**: Generated images can be downloaded directly from the app.

* * *

**Requirements**
----------------

To run this project locally, you need:

*   Python 3.10 or later
*   GPU (optional but recommended for faster image generation)

Install the required libraries:

```bash
pip install torch torchvision transformers diffusers streamlit Pillow
```

* * *

**Usage**
---------

### **1\. Run Locally**

1.  Clone the repository:
    
    ```bash
    git clone https://github.com/amanattar/text_to_image.git
    cd text_to_image
    ```
    
2.  Install dependencies:
    
    ```bash
    pip install -r requirements.txt
    ```
    
3.  Run the Streamlit app:
    
    ```bash
    streamlit run app.py
    ```
    
4.  Open your browser and navigate to `http://localhost:8501`.
    

* * *

### **2\. Hosted Version**

You can also access this app online via **Hugging Face Spaces**:

*   **URL**: https://huggingface.co/spaces/amanattar/text_to_image
* * *

**How It Works**
----------------

1.  Enter a detailed text prompt into the input box. Example prompts:
    *   `"A majestic lion in a sunset savannah"`
    *   `"A futuristic cityscape at night with neon lights"`
2.  Click the **Generate Image** button.
3.  The app processes the input and displays the generated image.
4.  Optionally, download the image using the provided button.

* * *

**Project Structure**
---------------------

```bash
.
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── README.md              # Documentation
```

* * *

**Model Used**
--------------

*   **Stable Diffusion v1.4**: A powerful text-to-image generation model provided by Hugging Face. It balances quality and performance for a variety of prompts.

* * *

**Optimizations**
-----------------

*   **Reduced Inference Steps**: The app uses 20 inference steps for faster image generation while maintaining good quality.
*   **GPU Support**: Automatically detects GPU for faster performance.

* * *

**Future Enhancements**
-----------------------

*   Add style customization options (e.g., photorealistic, cartoon, watercolor).
*   Allow multiple images to be generated for a single prompt.
*   Include advanced parameters (e.g., guidance scale sliders) for more control over image generation.

* * *

**Contributors**
----------------

*   **Aman Attar** ([GitHub](https://github.com/amanattar))

* * *

**License**
-----------

This project is licensed under the MIT License. See the `LICENSE` file for more details.
