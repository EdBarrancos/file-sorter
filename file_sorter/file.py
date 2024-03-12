import os
import re

class File:
    def __init__(
            self,
            name: str,
            path: str,
            depth: int,
            file_type: str):
        self.name = name
        self.full_path = path
        self.depth = depth
        self.file_type = file_type
    
    def __str__(self) -> str:
        return f"{self.name} - {self.depth}"
    
    def __repr__(self) -> str:
        return self.__str__()

    def full_name(self) -> str:
        return self.name + '.' + self.file_type
    
    def is_duplicate(self) -> bool:
        if len(self.name) < 3:
            return False
        return re.search("\([1-9]+[0-9]*\)$", self.name) is not None
    
    def delete(self) -> None:
        os.remove(self.full_path)

    def build_file(
            root: str,
            name : str,
            depth: str):
        return File(
            name.split('.')[0], 
            os.path.join(root, name), 
            depth,
            name.split('.')[-1])