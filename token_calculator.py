from typing import List

import tiktoken

from vo.ai_model import AiModel

DEFAULT_ENCODING: str = "cl100k_base"


def calculate_token_amount(ai_model: AiModel, content: List[dict], return_messages: List[str]):
    """Returns the number of tokens of the content.
    Based on OpenAI cookbook .
    https://github.com/openai/openai-cookbook/blob/main/examples/How_to_count_tokens_with_tiktoken.ipynb"""
    try:
        encoding = tiktoken.encoding_for_model(ai_model)
    except KeyError:
        return_messages.append("Warning: model not found. Using cl100k_base encoding.")
        encoding = tiktoken.get_encoding(DEFAULT_ENCODING)
    if ai_model == AiModel.GPT_3_5_TURBO:
        return_messages.append(
            "Warning: gpt-3.5-turbo may change over time. Returning num tokens assuming gpt-3.5-turbo-0301."
        )
        return calculate_token_amount(AiModel.GPT_3_5_TURBO_0301, content)
    elif ai_model == AiModel.GPT_4:
        return_messages.append("Warning: gpt-4 may change over time. Returning num tokens assuming gpt-4-0314.")
        return calculate_token_amount(AiModel.GPT_4.GPT_4_0314, content)
    elif ai_model == AiModel.GPT_3_5_TURBO_0301:
        tokens_per_message = 4  # every message follows <|start|>{role/name}\n{content}<|end|>\n
        tokens_per_name = -1  # if there's a name, the role is omitted
    elif ai_model == AiModel.GPT_4.GPT_4_0314:
        tokens_per_message = 3
        tokens_per_name = 1
    else:
        raise NotImplementedError(
            f"""num_tokens_from_messages() is not implemented for model {ai_model}. See https://github.com/openai/openai-python/blob/main/chatml.md for information on how messages are converted to tokens.""")
    num_tokens = 0
    for message in content:
        num_tokens += tokens_per_message
        for key, value in message.items():
            num_tokens += len(encoding.encode(value))
            if key == "name":
                num_tokens += tokens_per_name
    num_tokens += 3  # every reply is primed with <|start|>assistant<|message|>
    return num_tokens
