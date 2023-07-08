import streamlit as st
from PIL import Image

def main():
    st.title("Interactive Image Gallery")
    uploaded_files = st.file_uploader("Upload Images", accept_multiple_files=True, type=["png", "jpg", "jpeg"])

    if uploaded_files:
        images = [Image.open(file) for file in uploaded_files]

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
