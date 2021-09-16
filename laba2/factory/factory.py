from pickle_serializer.pickle_serializer import Pickle
from my_json_serializer.json_serializer import Json
from my_toml_serializer.toml_serializer import Toml
from my_yaml_serializer.yaml_serializer import Yaml

class Factory:
    def create_serializer(format):
        if format == ".pickle":
            return Pickle()
        elif format == ".json":
            return Json()
        elif format == ".toml":
            return Toml()
        return Yaml()