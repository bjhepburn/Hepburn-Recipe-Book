import streamlit as st
import os
import base64

st.set_page_config(page_title="Brad's Bakery Recipes", layout="wide")

st.title("👨‍🍳 Brad's Bakery Recipe Box")

# 1. Path to your PDF library
# Ensure this points to the folder containing your "Cookies", "Pies" folders
PDF_ROOT = "PDFs" 

# 2. Get Categories (Folder Names)
if os.path.exists(PDF_ROOT):
    categories = [f for f in os.listdir(PDF_ROOT) if os.path.isdir(os.path.join(PDF_ROOT, f))]
    
    # Sidebar for Category Selection
    category = st.sidebar.selectbox("Select Category", sorted(categories))

    if category:
        # Get Recipes in that category
        cat_path = os.path.join(PDF_ROOT, category)
        recipes = [f for f in os.listdir(cat_path) if f.endswith(".pdf")]
        
        # Dropdown for Recipe Selection
        recipe_selection = st.selectbox("Choose a Recipe", sorted(recipes))

        if recipe_selection:
            file_path = os.path.join(cat_path, recipe_selection)
            
            # 3. Display the PDF
            with open(file_path, "rb") as f:
                base64_pdf = base64.b64encode(f.read()).decode('utf-8')
            
            # Embedding the PDF in an iframe
            pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="800" type="application/pdf"></iframe>'
            st.markdown(pdf_display, unsafe_allow_html=True)
else:
    st.error(f"Could not find the '{PDF_ROOT}' folder. Please make sure it's in the same directory as this script.")