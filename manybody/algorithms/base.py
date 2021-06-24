from abc import ABC, abstractmethod

class Algorithm(ABC):
    tasks = []
    name = None

    def train(self, *args, **kwargs):
        raise NotImplementedError

    def infer(self, *args, **kwargs):
        raise NotImplementedError
