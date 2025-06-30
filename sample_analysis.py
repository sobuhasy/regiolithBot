import numpy as np
import random
import json

class RegiolithSample:
    def __init__(self, location, sample_id):
        self.location = location
        self.sample_id = sample_id
        self.composition = {}
        self.classification = None

    def simulate_spectrometry_data(self):
        """
        Simulate a chemical signature of Martian regolith
        Composition is in percentage of sample mass
        :return:
        """
        self.composition = {
            "Fe203": round(random.uniform(10, 25), 2),  # Iron Oxide
            "SiO2": round(random.uniform(30, 50), 2),   # Silicon Dioxide
            "H2O": round(random.uniform(0, 10), 2),      # Water content
            "MgSO4": round(random.uniform(0, 8), 2),   # Magnesium Sulfate
            "ClO4": round(random.uniform(0, 3), 2),    # Perchlorates
            "Organics": round(random.uniform(0, 1), 2)  # Organic compounds
        }

    def classify_sample(self):
        """
        Classify sample based on composition
        :return:
        """
        water = self.composition.get("H2O", 0)
        perchlorates = self.composition.get("ClO4", 0)
        silicates = self.composition.get("SiO2", 0)
        iron = self.composition.get("Fe203", 0)

        if perchlorates > 2:
            self.classification = "⚠️ Hazardous (toxic)"
        elif water > 5:
            self.classification = "💧 Potentially Habitable - Water Detected"
        elif silicates > 40 and iron > 15:
            self.classification = "🏗️ Construction Material - High Silicate and Iron Content"
        else:
            self.classification = "🔬 Unknown - Further Analysis Required"

    def generate_report(self, output_json=False):
            """
            Generate a report of the sample analysis
            :param output_json: If True, save report as JSON file
            :return:
            """
            print(f"--- Martian Regolith Sample Report [{self.sample_id}] ---")
            print(f"📍Location: {self.location}")
            print("🔬Composition(%):")
            for element, percentage in self.composition.items():
                print(f"  - {element}: {percentage}%")
            print(f"📊Classification: {self.classification}")

            if output_json:
                report = {
                    "location": self.location,
                    "sample_id": self.sample_id,
                    "composition": self.composition,
                    "classification": self.classification
                }
                with open(f"sample_report_{self.sample_id}.json", "w") as f:
                    json.dump(report, f, indent=4)
                print(f"Report saved as sample_report_{self.sample_id}.json")

if __name__ == "__main__":
    sample = RegiolithSample(location=(12.3, 7.8), sample_id="MARS-REG-017")
    sample.simulate_spectrometry_data()
    sample.classify_sample()
    sample.generate_report(output_json=True)


