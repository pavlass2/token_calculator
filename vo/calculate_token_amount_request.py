from typing import List

from pydantic import BaseModel

from vo.ai_model import AiModel


class CalculateTokenAmountRequest(BaseModel):
    ai_model: AiModel
    content: List[dict]
