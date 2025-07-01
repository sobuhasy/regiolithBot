from terrain_mapping import TerrainMapper
from sample_analysis import RegiolithSample
from excavation_planner import ExcavationPlanner
from arm_control import ArmController
import random

def generate_sample_data(flat_mask, num_samples=10):
    """
    Generate random sample locations and simulate their analyisis.
    :param flat_mask:
    :param num_samples:
    :return:
    """
    height, width = flat_mask.shape
    samples = []
    for i in range(num_samples):
        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)

        sample = RegolithSample(location=(x, y), sample_id=f"MARS-REG-{i:03d}")
        sample.simulate_spectometry_data()
        sample.classify_sample()
        sample.generate_report(output_json=False)

        samples.append({
            "location": (x, y),
            "classification": sample.classification
        })

    return samples

if __name__ == "__main__":
    print("🪐 Initializing RegolithBot System...")

    # Step 1: Terrain Mapping
    mapper = TerrainMapper()
    elevation_map = mapper.simulate_depth_data()
    flat_mask = mapper.detect_flat_zones()
    mapper.visualize_map()
    mapper.export_point_cloud()

    # Step 2: Simulate Samples
    sample_data = generate_sample_data(flat_mask, num_samples=10)

    # Step 3: Plan Excavation
    planner = ExcavationPlanner(elevation_map, flat_mask, sample_data)
    planner.compute_priority_map()
    planner.display_priority_map()
    top_sites = planner.get_top_excavation_sites()

    # Step 4: Excavation Arm Execution
    arm = ArmController()
    for i, (coords, score) in enumerate(top_sites):
        print(f"\n🔧 Executing excavation for site {i+1} at coordinates {coords} with score {score:.2f}")
        x, y = coords
        arm.move_to(x / 20, y / 20, 0.0) # Normalize to meters
        arm.dig(depth=0.3)
        arm.place_sample(bin_coords=(0.0, 0.5, 0.0))

    print("\n✅ Excavation complete! All samples collected and analyzed.")
