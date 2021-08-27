from abc import ABC, abstractmethod
from typing import Dict, List


class Importer(ABC):
    @abstractmethod
    def import_data(self, path: str) -> List[Dict]:
        raise NotImplementedError("you should not be raising this")
