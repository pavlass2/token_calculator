from typing import List

from pydantic import BaseModel

from vo.result import Result


class CalculateTokenAmountResponse(BaseModel):
    result: Result
    messages: List[str]
    amount: int
