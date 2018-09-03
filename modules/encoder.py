import json
from bson import ObjectId
import isodate
from datetime import datetime, date


class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        elif isinstance(o, (datetime, date)):
            return isodate.datetime_isoformat(o)
        return json.JSONEncoder.default(self, o)