import json


class Json:

    @staticmethod
    def is_json(value):
        try:
            json.loads(value)
            return True
        except json.JSONDecodeError:
            return False
        
    @staticmethod
    def decode(value):
        if Json.is_json(value):
            return json.loads(value)
        return value