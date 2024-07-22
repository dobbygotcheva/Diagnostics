import unittest
from schizophrenia import Schizophrenia


class TestSchizophrenia(unittest.TestCase):
    def setUp(self):
        self.patient = Schizophrenia(age=25, weight=70.0, height=1.75, name="John Doe")

    def test_symptoms(self):
        self.patient.symptoms("schizophrenia_symptoms.txt")
        self.assertEqual(self.patient.num_positive_symptoms, 2)
        self.assertEqual(self.patient.num_negative_symptoms, 2)
        self.assertEqual(self.patient.diagnosis, "Schizophrenia")

        with self.assertRaises(FileNotFoundError):
            self.patient.symptoms("nonexistent_file.txt")

    def test_hospitalization(self):
        with self.assertRaises(FileNotFoundError):
            self.patient.hospitalization("nonexistent_file.txt")


if __name__ == '__main__':
    unittest.main()