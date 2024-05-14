import logging

from typing import Dict, List, Union
from fastapi import APIRouter
from pydantic import BaseModel
from rest_api.toxic import CustomDetoxify, get_task_user_agent_toxic
from rest_api.schema import TaskInput


logger = logging.getLogger(__name__)
router = APIRouter()


class Request(BaseModel):
    texts: Union[str, List[str]]


toxic_model_name = "MiniLMv2-toxic-jigsaw-lite-onnx"
toxic_model = CustomDetoxify(toxic_model_name)


@router.post("/conversation_toxicity_plugin", response_model=Dict[str, Union[str, int]])
async def task_toxic(request: TaskInput):
    return get_task_user_agent_toxic(request.llm_input, request.llm_output, toxic_model)
