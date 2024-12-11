from rdkit import Chem
from rdkit.Chem import Draw
import os

class Visualize:
    def __init__(self):
        # Ensure a directory exists to store temporary images
        self.image_dir = "static/temp_images"
        os.makedirs(self.image_dir, exist_ok=True)

    def smileImage(self, smile):
        try:
            mol = Chem.MolFromSmiles(smile)
            if not mol:
                return None
            
            # Generate image
            img_path = os.path.join(self.image_dir, f"{smile}.png")
            Draw.MolToFile(mol, img_path)
            return img_path  # Return the file path of the image
        except Exception as e:
            print(f"Error generating image: {e}")
            return None
