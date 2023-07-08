
import streamlit as st
from PIL import Image

def main():
    st.title("Interactive Image Gallery")
    uploaded_files = st.file_uploader("Upload Images", accept_multiple_files=True, type=["png", "jpg", "jpeg"])

    if uploaded_files:
        images = [Image.open(file) for file in uploaded_files]

        operation = st.selectbox("Select an Operation", ["None", "Rotate", "Resize"])
        if operation == "Rotate":
            angle = st.slider("Rotation Angle", -180, 180, 0)
            images = [image.rotate(angle) for image in images]
        elif operation == "Resize":
            width = st.slider("New Width", 100, 1000, 300)
            height = st.slider("New Height", 100, 1000, 300)
            images = [image.resize((width, height)) for image in images]

        # Display images in a grid layout
        col_num = 3  # Number of columns in the grid
        image_width = 200  # Width of each image
        for i, image in enumerate(images):
            if i % col_num == 0:
                col = st.columns(col_num)
            with col[i % col_num]:
                st.image(image, use_column_width=True)
                st.caption(f"Image {i+1}")

if __name__ == "__main__":
    main()
