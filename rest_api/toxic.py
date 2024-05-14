import os
import numpy as np

from typing import List, Dict, Union
from tokenizers import Tokenizer
from src.onnx_model import OnnxTransformer


class CustomDetoxify:
    """Detoxify
    Easily predict if a comment or list of comments is toxic.
    Returns:
        results(dict): dictionary of output scores for each class
    """

    def __init__(self, model_path=None, **kwargs):
        self.model = OnnxTransformer(
            model_path,
            providers=["CPUExecutionProvider"],
        )

        self.tokenizer = Tokenizer.from_file(os.path.join(model_path, "tokenizer.json"))
        self.tokenizer.enable_padding()
        self.tokenizer.enable_truncation(max_length=256)

        self.class_names = [
            "toxicity",
            "severe_toxicity",
        ]

    def predict(self, text):
        if isinstance(text, str):
            text = [text]
        inputs = self.tokenizer.encode_batch(text)

        inputs = {
            "input_ids": np.vstack([inp.ids for inp in inputs], dtype=np.int64),
            "attention_mask": np.vstack(
                [inp.attention_mask for inp in inputs], dtype=np.int64
            ),
            "token_type_ids": np.vstack(
                [inp.type_ids for inp in inputs], dtype=np.int64
            ),
        }

        output = self.model.predict(inputs)
        scores = 1 / (1 + np.exp(-output))  # Sigmoid
        results = {}
        for i, cla in enumerate(self.class_names):
            results[cla] = (
                scores[0][i]
                if isinstance(text, str)
                else [scores[ex_i][i].tolist() for ex_i in range(len(scores))]
            )
        return results


def get_labels_above_threshold(
    toxicity: Dict[str, List[float]], threshold: float = 0.5
) -> List[str]:
    return [
        label for label, probability in toxicity.items() if probability[0] >= threshold
    ]


def get_task_user_agent_toxic(
    llm_input: str, llm_output, model: CustomDetoxify
) -> Dict[str, Union[str, int]]:
    user_toxicity = model.predict(llm_input)
    agent_toxicity = model.predict(llm_output)

    return {
        "user_toxic": 1 if user_toxicity["toxicity"][0] >= 0.5 else 0,
        "user_severe_toxic": 1 if user_toxicity["severe_toxicity"][0] >= 0.5 else 0,
        "agent_toxic": 1 if agent_toxicity["toxicity"][0] >= 0.5 else 0,
        "agent_severe_toxic": 1 if agent_toxicity["severe_toxicity"][0] >= 0.5 else 0,
    }
