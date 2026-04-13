import streamlit as st
import os
from streamlit_pdf_viewer import pdf_viewer

st.set_page_config(page_title="Brad's Bakery", layout="wide")

st.title("👨‍🍳 Hepburn Recipe Book")

PDF_ROOT = "PDFs" 

if os.path.exists(PDF_ROOT):
    categories = sorted([f for f in os.listdir(PDF_ROOT) if os.path.isdir(os.path.join(PDF_ROOT, f))])
    category = st.sidebar.selectbox("Select Category", categories)

    if category:
        cat_path = os.path.join(PDF_ROOT, category)
        recipes = sorted([f for f in os.listdir(cat_path) if f.endswith(".pdf")])
        recipe_selection = st.selectbox("Choose a Recipe", recipes)

        if recipe_selection:
            file_path = os.path.join(cat_path, recipe_selection)
            
            # --- The New Display Method ---
            with open(file_path, "rb") as f:
                binary_pdf = f.read()
            
            # 1. Provide a Download Button (Great for offline use in the bakery)
            st.download_button(
                label="💾 Download/Print Recipe",
                data=binary_pdf,
                file_name=recipe_selection,
                mime="application/pdf"
            )

            # 2. View the PDF directly on the page
            pdf_viewer(input=binary_pdf, width=700)
            
else:
    st.error("PDF folder not found.")
