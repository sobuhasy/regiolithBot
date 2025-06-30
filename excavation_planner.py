import numpy as np
import matplotlib.pyplot as plt

class ExcavationPlanner:
    def __init__(self, elevation_map, flat_mask, sample_data):
        """
        elevation_map: 2D numpy array representing the terrain elevation
        flat_mask: 2D boolean array indicating flat zones
        sample_data: List of RegiolithSample objects containing sample information, each with {
            "location": [x, y],

            "classification": str

        :param elevation_map:
        :param flat_mask:
        :param sample_data:
        """
        self.elevation_map = elevation_map
        self.flat_mask = flat_mask
        self.sample_data = sample_data
        self.priority_map = np.zeros_like(elevation_map)

    def classify_value_score(self, classification):
        """
        Assign numerical scores to sample classifications
        :param classification:
        :return:
        """
        scores = {
            "⚠️ Hazardous (toxic)": -10,
            "💧 Potentially Habitable - Water Detected": 10,
            "🏗️ Construction Material - High Silicate and Iron Content": 8,
            "🔬 Unknown - Further Analysis Required": 5
        }
        return scores.get(classification, 0)

    def compute_priority_map(self):
        """
        Compute priority map based on flat zones and sample classifications
        :return:
        """
        for sample in self.sample_data:
            x, y = sample["location"]
            classification = sample["classification"]
            score = self.classify_value_score(classification)

            # Convert physical coordinates to grid indices (assuming 1:1 mapping for simplicity)
            x_idx, y_idx = int(x), int(y)

            if (0 <= x_idx < self.flat_mask.shape[0]) and (0 <= y_idx < self.flat_mask.shape[1]):
                if self.flat_mask[x_idx, y_idx]:
                    self.priority_map[x_idx, y_idx] = score
                else:
                    self.priority_map[x_idx, y_idx] = score * 0.5  # Reduce score for non-flat zones

    def get_top_excavation_sites(self, n=5):
        """
        Return top N coordinates with highest priority scores
        :param n:
        :return:
        """

        flat_indices = np.dstack(np.unravel_index(np.argsort(self.priority_map.ravel())[::-1], self.priority_map.shape))[0]
        top_sites = []
        for y, x in flat_indices:
            if self.priority_map[x, y] > 0:
                top_sites.append((x, y, self.priority_map[x, y]))
            if len(top_sites) >= n:
                break
        return top_sites

    def display_priority_map(self):
        """
        Visualize the priority map
        :return:
        """
        plt.imshow(self.priority_map, cmap='hot', origin='lower')
        plt.title('Excavation Priority Map')
        plt.colorbar(label='Priority Score')
        plt.xlabel('X Coordinate')
        plt.ylabel('Y Coordinate')
        plt.show()

# Example usage:
if __name__ == "__main__":
    # Simulated data for testing
    elevation_map = np.random.rand(100, 100)  # Random elevation map
    flat_mask = elevation_map < 0.5  # Flat zones where elevation is below 0.5
    sample_data = [
        {"location": [10, 20], "classification": "💧 Potentially Habitable - Water Detected"},
        {"location": [30, 40], "classification": "⚠️ Hazardous (toxic)"},
        {"location": [50, 60], "classification": "🏗️ Construction Material - High Silicate and Iron Content"},
        {"location": [70, 80], "classification": "🔬 Unknown - Further Analysis Required"}
    ]

    planner = ExcavationPlanner(elevation_map, flat_mask, sample_data)
    planner.compute_priority_map()
    planner.display_priority_map()

    top_sites = planner.get_top_excavation_sites()
    print("Top Excavation Sites:")
    for site in top_sites:
        print(f"Location: {site[0]}, {site[1]} - Score: {site[2]}")
