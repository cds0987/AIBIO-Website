import torch
from transformers import T5Tokenizer, T5ForConditionalGeneration
import torch.nn as nn
import os
#AI_Model/AI_model_cache
# Set cache directories programmatically
#Backend/Store/Hugging Face cache
os.environ["TRANSFORMERS_CACHE"] = "AI_Model/AI_model_cache/HuggingFace"
os.environ["HF_DATASETS_CACHE"] = "AI_Model/AI_model_cache/HuggingFace"
os.environ["HF_METRICS_CACHE"] = "AI_Model/AI_model_cache/HuggingFace"
class CaptionMOLT5(nn.Module):
    def __init__(self):
        super(CaptionMOLT5, self).__init__()
        self.caption_model = T5ForConditionalGeneration.from_pretrained('laituan245/molt5-small-smiles2caption',
    cache_dir="AI_Model/AI_model_cache/HuggingFace")
        self.caption_tokenizer=T5Tokenizer.from_pretrained("laituan245/molt5-small-smiles2caption", model_max_length=512,
    cache_dir="AI_Model/AI_model_cache/HuggingFace")
        self.device=torch.device("cpu" if torch.cuda.is_available() else "cpu")
        self.caption_model.to(self.device)
    def forward(self,smiles):
        input_ids = self.caption_tokenizer(smiles, return_tensors="pt").input_ids
        input_ids = input_ids.to(self.device)
        outputs = self.caption_model.generate(input_ids, num_beams=7, max_length=512)
        return self.caption_tokenizer.decode(outputs[0], skip_special_tokens=True)

