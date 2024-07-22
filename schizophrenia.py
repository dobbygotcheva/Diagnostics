#this class is the one that helps by diagnosing schizophrenia
from patient import Patient
from typing import List
class Schizophrenia(Patient):
    """
    A class representing a patient diagnosed with schizophrenia.

    Inherits from the Patient class, and adds additional methods specific to the diagnosis of schizophrenia.
    """

    def __init__(self, age: int, weight: float, height: float, name: str):
        """
        Initializes a Schizophrenia object.

        Args:
            age (int): The age of the patient in years.
            weight (float): The weight of the patient in kilograms.
            height (float): The height of the patient in meters.
            name (str): The name of the patient as a string.
        """
        super().__init__(age, weight, height)
        self.name = name
        self.diagnosis = None
        self.num_positive_symptoms = 0
        self.num_negative_symptoms = 0

    def symptoms(self, file_name: str) -> None:
        """
        Determines the number of positive and negative symptoms of schizophrenia based on a file.

        Reads the contents of the file at the given file path, counts the number of positive and negative
        symptoms of schizophrenia, and sets the diagnosis attribute of the Schizophrenia object if the
        number of positive symptoms is greater than or equal to 2.

        Args:
            file_name (str): The name of the file to read.

        Returns:
            None.
        """
        try:
            with open(file_name) as f:
                symptoms = f.read().splitlines()

            self.num_positive_symptoms = 0
            self.num_negative_symptoms = 0

            for symptom in symptoms:
                if symptom in ["delusions", "hallucinations", "disorganized thinking", "abnormal motor behaviour"]:
                    self.num_positive_symptoms += 1
                elif symptom in ["lack of hygiene", "no eye contact", "lack of mimic", "depression",
                                 "changed sleep pattern", "nervousness", "social withdrawal"]:
                    self.num_negative_symptoms += 1

            if self.num_positive_symptoms >= 2:
                self.diagnosis = "Schizophrenia"
        except FileNotFoundError:
            raise FileNotFoundError

    def hospitalization(self, file_name: str) -> None:
        """
        Determines whether the patient requires hospitalization based on their symptoms.

        Reads a file containing common symptoms of schizophrenia, and determines whether the patient requires
        hospitalization based on whether they have hallucinations or are feeling suicidal.

        Returns:
            None. Prints a message indicating whether hospitalization is required.
        """
        try:
            with open(file_name) as f:
                symptoms = f.read().splitlines()
            if "hallucinations" in symptoms:
                print(f"Hospitalization for {self.name} for 4 months.")
            elif "suicidal" in symptoms:
                print(f"Hospitalization duration for {self.name}: until improvement.")
            else:
                print(f"{self.name} does not require hospitalization.")
        except FileNotFoundError:
            raise FileNotFoundError