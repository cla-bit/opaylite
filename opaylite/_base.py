from decouple import config


OPAY_SECRET_KEY = config("OPAY_SECRET_KEY")


class OpayBaseClientAPI:
    """Base Client API for Opay API"""

    _OPAY_BASE_URL = "https://testapi.opaycheckout.com/api/"

    _VALID_HTTP_METHODS = {"GET", "POST", "PUT", "DELETE"}
