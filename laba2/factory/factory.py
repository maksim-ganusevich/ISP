from pickle_serializer.pickle_serializer import Pickle

class Factory:
    def create_serializer(format):
        if format == ".pickle":
            return Pickle()