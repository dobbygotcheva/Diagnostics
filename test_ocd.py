import unittest
from ocd import OCD


class TestOCD(unittest.TestCase):
    def setUp(self):
        self.patient = OCD(age=30, weight=70.5, height=1.75, name="John")

    def test_symptoms(self):
        file_name = "ocd_symptoms.txt"
        self.patient.symptoms(file_name)
        self.assertEqual(self.patient.diagnosis, "OCD")

    def test_symptoms_file_not_found(self):
        file_name = "non_existent_file.txt"
        with self.assertRaises(FileNotFoundError):
            self.patient.symptoms(file_name)

    def test_hospitalization(self):
        self.patient.hospitalization()
        self.assertEqual(self.patient.diagnosis, None)

    def test_hospitalization_requires(self):
        with open("ocd_symptoms.txt", "w") as f:
            f.write("fear of harming\nfear of disease\ncleaning\nchecking\n")
        self.patient.hospitalization()
        self.assertEqual(self.patient.diagnosis, "OCD")

    def test_hospitalization_requires_not_enough_symptoms(self):
        with open("ocd_symptoms.txt", "w") as f:
            f.write("fear of harming\nfear of disease\ncleaning\n")
        self.patient.hospitalization()
        self.assertEqual(self.patient.diagnosis, None)

    def tearDown(self):
        self.patient = None


if __name__ == "__main__":
    unittest.main()