#this is the file that helps by diagnosis of patients with obsessive compulsive disorder
from patient import Patient
from typing import List

class OCD(Patient):
    def __init__(self, age: int, weight: float, height: float, name: str):
        """
        Initializes an instance of the OCD class.

        :param age: The age of the patient.
        :type age: int
        :param weight: The weight of the patient in kg.
        :type weight: float
        :param height: The height of the patient in meters.
        :type height: float
        :param name: The name of the patient.
        :type name: str
        """
        super().__init__(age, weight, height)
        self.name = name
        self.diagnosis = None  # Define the diagnosis attribute with a default value of None

    def symptoms(self, file_name: str) -> None:
        """
        Prints the OCD symptoms of the patient and sets the diagnosis if the patient has 5 or more symptoms.

        :param file_name: The name of the file containing the symptoms of the patient.
        :type file_name: str
        """
        try:
            with open(file_name) as f:
                symptoms = f.read().splitlines()

            num_symptoms = len(symptoms)
            print(f"{self.name} has {num_symptoms} OCD symptoms:")
            for symptom in symptoms:
                print(f"- {symptom}")

            if num_symptoms >= 5:
                self.diagnosis = "OCD"
        except FileNotFoundError:
            raise FileNotFoundError

    def hospitalization(self) -> None:
        """
        Determines whether the patient requires hospitalization based on their symptoms and prints the appropriate
        message.
        """

        try:
            with open("ocd_symptoms.txt") as f:
                symptoms = f.read().splitlines()
            if len(set(["fear of harming", "fear of disease", "need for symmetry", "cleaning", "checking", "counting",
                        "ordering and arranging", "repeating words in the head"]).intersection(set(symptoms))) >= 3:
                print(f"{self.name} has Obsessive Compulsive Disorder and requires hospitalization.")
            else:
                print(f"{self.name} does not require hospitalization.")
        except FileNotFoundError:
            raise FileNotFoundError

