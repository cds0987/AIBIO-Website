import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from AI_Model.Multilanguage import translator
import torch
ENG=translator.translate("Chào mọi người", "vi_VN")
print(ENG)