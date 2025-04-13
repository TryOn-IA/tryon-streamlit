import os
from PIL import Image, ImageDraw

# Crée le dossier de sortie s'il n'existe pas
output_path = "results/streamlit_tryon/try-on/"
os.makedirs(output_path, exist_ok=True)

# Crée une image fictive avec texte
image = Image.new("RGB", (512, 640), color=(230, 230, 230))
draw = ImageDraw.Draw(image)
draw.text((20, 300), "Essayage IA simulé 👗", fill=(0, 0, 0))

# Sauvegarde l'image
image.save(os.path.join(output_path, "user.jpg"))

print("Image générée (fictive) avec succès.")

