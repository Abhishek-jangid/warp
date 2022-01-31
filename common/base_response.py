from common.constants import STATUS_KEY, MESSAGE_KEY, ERROR_KEY, DATA_KEY


def set_error_response(msg: str = "Something went wrong", error: dict = None):
    return {
        STATUS_KEY: False,
        MESSAGE_KEY: msg,
        ERROR_KEY: error
    }

def set_success_response(data: dict = {}, msg: str = "Success"):
    return {
        STATUS_KEY: True,
        MESSAGE_KEY: msg,
        DATA_KEY: data
    }
