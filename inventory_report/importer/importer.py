from abc import ABC, abstractmethod
from typing import Dict, List


class Importer(ABC):
    @staticmethod
    @abstractmethod
    def import_data(path: str) -> List[Dict]:
        raise NotImplementedError("you should not be raising this")
