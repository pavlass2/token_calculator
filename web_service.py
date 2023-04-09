import json
from typing import List

from fastapi import FastAPI, HTTPException, status, Request, Body
from fastapi.openapi.utils import get_openapi

import token_calculator
from vo.ai_model import AiModel
from vo.calculate_token_amount_request import CalculateTokenAmountRequest
from vo.calculate_token_amount_response import CalculateTokenAmountResponse
from vo.settings import Settings
from vo.result import Result

settings = Settings()
app = FastAPI()


# nastav docker build a docker container, commitni image i kod


def authenticate(request: Request):
    api_key = request.headers.get(settings.API_KEY_HEADER)
    if api_key != settings.API_KEY_VALUE:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)


@app.post("/calculate_token_amount", response_model=CalculateTokenAmountResponse)
def calculate_token_amount(
        request: Request,
        calculate_token_amount_request: CalculateTokenAmountRequest = Body(..., example={
            "ai_model": "gpt-3.5-turbo-0301",
            "content": [
                {"role": "system", "content": "You are helpful assistant."},
                {"role": "user", "content": "What is the capital of Czech Republic?"},
                {"role": "assistant", "content": "The capital of Czech Republic is Prague."}
            ]
        })
):
    """Returns the number of tokens of the content"""
    authenticate(request)

    ai_model: AiModel = calculate_token_amount_request.ai_model
    # Ensure that ai_model is a non-empty string
    if not ai_model or not isinstance(ai_model, str):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="ai_model parameter is required and must be a non-empty string")

    content: List[dict] = calculate_token_amount_request.content
    # Ensure that content is a non-empty JSON array
    if not content or not isinstance(content, list):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="content parameter is required and must be a non-empty JSON array")

    messages = list()
    try:
        amount = token_calculator.calculate_token_amount(ai_model, content, messages)
        if len(messages) == 0:
            result = Result.OK
        else:
            result = Result.WARN

    except Exception as e:
        messages.append(str(e))
        amount = 0
        result = Result.FAILURE

    calculate_token_amount_response = CalculateTokenAmountResponse(result=result, messages=messages, amount=amount)
    return calculate_token_amount_response


# OPEN API JSON
openapi_schema = get_openapi(
    title="Token Calculator",
    version="1.0.0",
    description="Token counting JSON API for Aaia based on tiktoken",
    routes=app.routes,
)
# Save the OpenAPI specification to a file
with open("target/open_api/openapi.json", "w") as f:
    json.dump(openapi_schema, f, indent=4)
