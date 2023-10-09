import streamlit as st
from PIL import Image
from ultralytics import YOLO
import cv2

st.set_page_config(page_title="Computer vision", page_icon="🖥️")

model = YOLO("models/final.pt")

def main():
    st.title("Object Detection App")
    
    dict_names = {"Type 1": "https://www.alanmichelson.com/handagayas", "Type 2": "https://www.aperture.org/editorial/kimowan-metchewaiss-search-for-visual-sovereignty/", "Type 3": "https://www.aperture.org/editorial/kimowan-metchewaiss-search-for-visual-sovereignty/", "Type 4": "https://www.guadalupemaravilla.com/retablos", "Type 5": "https://www.koyoltzintli.com/project/meda"}
    artist_names = {"Type 1": "Alan Michelson", "Type 2": "Kimowan Metchewaiss", "Type 3": "Kimowan Metchewaiss", "Type 4": "Guadalupe Maravilla", "Type 5": "Koyoltzintli"}
    

    choice = st.radio("Select an option", ("Upload an image", "Use webcam", "Provide image URL"))
    
    if choice == "Upload an image":
        uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

        if uploaded_file is not None:
            img = Image.open(uploaded_file)
            names = model.names

            results = model(source=img)

            
            for r in results:
                for c in r.boxes.cls:
                    artist = names[int(c)]
            col1, col2 = st.columns(2)
            
            link = dict_names[artist]
            artist_name = artist_names[artist]
            
                        
            st.write("Artist: [%s](%s)" % (artist_name, link))
                        

            res_plotted = results[0].plot()
            cv2.imwrite('images/test_image_output.jpg', res_plotted)
            
            col1.image(img, caption="Uploaded Image", use_column_width=True)
            col2.image('images/test_image_output.jpg', caption="Predicted Image", use_column_width=True)

if __name__ == '__main__':
    main()
