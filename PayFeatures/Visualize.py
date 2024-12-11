import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from AI_Model.CaptionSmiles import CaptionMOLT5
from rdkit import Chem
from rdkit.Chem import Draw
import matplotlib.pyplot as plt
class Visualize():
    def __init__(self):
        self.caption=CaptionMOLT5()
    def smileImage(self,smile):
        try:
            mol=Chem.MolFromSmiles(smile)
        except:
            return None
        img=Draw.MolToImage(Chem.MolFromSmiles(smile))
        return img
    def caption(self,smile):
        try:
            mol=Chem.MolFromSmiles(smile)
        except:
            return None
        caption=self.caption(smile)
        return caption
