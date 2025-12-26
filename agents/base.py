from abc import ABC, abstractmethod


class BaseAgent(ABC):
    def __init__(self, name: str, role: str):
        self.name = name
        self.role = role

    @abstractmethod
    def run(self, input_text: str):
        pass
