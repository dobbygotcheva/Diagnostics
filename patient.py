#this is the parent class patient
from typing import List

class Patient:
    def __init__(self, age: int, kg: float, height: float):
        self.age = age
        self.kg = kg
        self.height = height

    def symptoms(file_name: str) -> List[str]:
        """
        Read the contents of a file and return a list of strings, one for each line.

        Args:
        file_name (str): The name of the file to read.

        Returns:
        List[str]: A list of strings, where each string represents a line in the file.
        """
        try:
            with open(file_name, "r") as f:
                return [line.strip() for line in f]
        except FileNotFoundError:
            raise FileNotFoundError

    def hospitalization(file_name: str)->None:
        pass

