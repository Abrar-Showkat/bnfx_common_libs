from urllib.parse import urlparse
import datetime


class MandatoryFieldValidation:

    def __init__(self, dictData):
        self.my_dict = dictData

    def validate(self, key):
        value = self.my_dict
        for key in key.split('.'):
            value = value.get(key)
            if value is None:
                return {"message": f"{key} key is required", "status": False}
        if isinstance(value, list):
            if all(value):
                return {"status": True}
            else:
                return {"message": f"{key} key can't have empty values", "status": False}

        else:
            if str(value) is not None and not str(value).isspace() and str(value) != 'null' and str(value) != '':

                return {"status": True}
            else:
                return {"message": f"{key} key is required", "status": False}


class FormatValidation:

    def __init__(self, dictData):

        self.my_dict = dictData

    def urlValidation(self, key):

        value = self.my_dict

        for key in key.split('.'):
            value = value.get(key)
            if value is None:
                return {"message": f"{key} is not found", "status": False}

        try:
            url = urlparse(value)
            if all([url.scheme, url.netloc]):
                return {"Value": value, "status": True}
            else:
                return {"message": "url is not valid", "status": False}

        except ValueError:
            return {"message": "Url is not valid", "status": False}

    def dateValidation(self, key):
        value = self.my_dict

        for key in key.split('.'):
            value = value.get(key)
            if value is None:
                return {"message": f"{key} is not found", "status": False}
        try:
            datetime.datetime.strptime(value, "%Y/%m/%d")
            return {"Value": value, "status": True}
        except ValueError:
            return {"message": "Date is not in correct format", "status": False}

    def timeValidation(self, key):
        value = self.my_dict

        for key in key.split('.'):
            value = value.get(key)
            if value is None:
                return {"message": f"{key} is not found"}
        try:
            datetime.datetime.strptime(value, "%H:%M:%S")
            return {"Value": value, "status": True}
        except ValueError:
            return {"message": "Time is not in correct format", "status": False}

    def dateTimeValidation(self, key):
        value = self.my_dict

        for key in key.split('.'):
            value = value.get(key)
            if value is None:
                return {"message": f"{key} key is required"}
        try:
            datetime.datetime.strptime(value, "%Y/%m/%d %H:%M:%S")
            return {"Value": value, "status": True}
        except ValueError:
            return {"message": "Datetime is not in correct format", "status": False}
