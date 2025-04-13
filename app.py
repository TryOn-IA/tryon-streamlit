import os
import streamlit as st
import subprocess

st.set_page_config(page_title="TryOn IA", page_icon="👗")
st.title("Essayage IA 👚 avec Streamlit + TryOn++")

# Création des dossiers nécessaires
data_img_path = "data/image"
data_cloth_path = "data/cloth"
os.makedirs(data_img_path, exist_ok=True)
os.makedirs(data_cloth_path, exist_ok=True)

# Upload photo utilisateur
user_img = st.file_uploader("🧑 Upload une photo de toi (portrait)", type=["jpg", "jpeg", "png"])
# Upload photo vêtement
cloth_img = st.file_uploader("👕 Upload une image du vêtement à plat", type=["jpg", "jpeg", "png"])

if user_img and cloth_img:
    with open(f"{data_img_path}/user.jpg", "wb") as f:
        f.write(user_img.read())
    with open(f"{data_cloth_path}/cloth.jpg", "wb") as f:
        f.write(cloth_img.read())

    st.info("Lancement de l'essayage virtuel... 🚀")

    # Appel du script TryOn++ (assure-toi que test.py est présent)
    result = subprocess.run(
        ["python", "test.py", "--name", "streamlit_tryon", "--datasetting", "unpaired", "--warp", "clothflow"],
        capture_output=True, text=True
    )

    if result.returncode == 0:
        output_path = "results/streamlit_tryon/try-on/user.jpg"
        if os.path.exists(output_path):
            st.success("Voici le résultat généré :")
            st.image(output_path, caption="Essayage réussi 😎") 
        else:
            st.error("Image générée introuvable.")
    else:
        st.error("Erreur pendant l'exécution du modèle :")
        st.text(result.stderr)
else:
    st.warning("Upload une photo de toi ET une photo de vêtement pour commencer.")
