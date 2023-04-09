from enum import Enum


class AiModel(str, Enum):
    GPT_3_5_TURBO = "gpt-3.5-turbo"
    GPT_3_5_TURBO_0301 = "gpt-3.5-turbo-0301"
    GPT_4 = "gpt-4"
    GPT_4_0314 = "gpt-4-0314"
