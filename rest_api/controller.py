import logging
import os
import numpy as np

from typing import Dict, List, Union
from fastapi import APIRouter
from src.onnx_model import OnnxTransformer
from tokenizers import Tokenizer
from pydantic import BaseModel

logger = logging.getLogger(__name__)
router = APIRouter()


class Request(BaseModel):
    texts: Union[str, List[str]]


# Toxic cfg
toxic_model_name = "MiniLM-L6-toxic-all-labels-onnx"
toxic_model = OnnxTransformer(
    toxic_model_name,
)

t_tokenizer = Tokenizer.from_file(os.path.join(toxic_model_name, "tokenizer.json"))
t_tokenizer.enable_padding(
    pad_token="<pad>",
    pad_id=1,
)
t_tokenizer.enable_truncation(max_length=256)


@router.post("/toxicity", response_model=List[Dict])
def conversation_toxicity(request: Request):

    class_names = [
        "toxicity",
        "severe_toxicity",
        "obscene",
        "threat",
        "insult",
        "identity_hate",
    ]
    output = toxic_model.predict(t_tokenizer, request.texts, batch_size=16)
    output = np.concatenate(output, axis=0)

    scores = 1 / (1 + np.exp(-output))  # Sigmoid
    results = []

    for item in scores:
        labels = []
        scores = []
        for idx, s in enumerate(item):
            labels.append(class_names[idx])
            scores.append(float(s))
        results.append({"labels": labels, "scores": scores})

    return results
