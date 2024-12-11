import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from AI_Model.QuestionAnswerModel import QsAsDBert
import torch
class QsAsD:
    def __init__(self):
        self.model = QsAsDBert()
    def get_answer(self,question,top=3,take_content=False):
        return self.model.get_answer(question,top,take_content)

model=QsAsD()
qs='Who is at risk for Lymphocytic Choriomeningitis (LCM)? ?'
print(model.get_answer(qs,3,True))