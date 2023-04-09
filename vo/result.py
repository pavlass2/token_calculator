from enum import Enum


class Result(str, Enum):
    OK = "OK"
    INFO = "INFO"
    WARN = "WARN"
    FAILURE = "ERROR"