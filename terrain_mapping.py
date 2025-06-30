import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter
import open3d as o3d

class TerrainMapper:
    def __init__(self, resolution=0.05, area_size=(10, 10)):
        self.resolution = resolution # meters per grid cell
        self.width, self.height = area_size
        self.grid_size = int(self.width / resolution), int(self.height / resolution)
        self.elevation_map = np.zeros(self.grid_size)

    def simulate_depth_data(self):
        """
        Simulate stereo/LIDAR point cloud data for Martian terrain
        Replace this with real sensor input in production.
        :return:
        """

        x = np.linspace(0, self.width, self.grid_size[0])
        y = np.linspace(0, self.height, self.grid_size[1])
        X, Y = np.meshgrid(x, y)

        # Simulate a simple terrain using sine hills + random noise
        Z = 0.5 * np.sin(0.5 * X) * np.cos(0.5 * Y) + 0.1 * np.random.randn(*X.shape)
        self.elevation_map = gaussian_filter(Z, sigma=2)
        return self.elevation_map

    def compute_slope(self):
        """
        Calculate slope from elevation map
        :return:
        """
        dzdx = np.gradient(self.elevation_map, self.resolution, axis=1)
        dzdy = np.gradient(self.elevation_map, self.resolution, axis=0)
        slope = np.sqrt(dzdx**2 + dzdy**2)
        return slope

    def detect_flat_zones(self, threshold=0.05):
        """
        Detect flat areas suitable for excavation
        :param threshold:
        :return:
        """
        slope = self.compute_slope()
        flat_mask = slope < threshold
        return flat_mask

    def visualize_map(self, show_flat_zones=True):
        """
        Display terrain and mark flat zones
        :param show_flat_zones:
        :return:
        """

        fig, ax = plt.subplots()
        ax.imshow(self.elevation_map, cmap='terrain', origin='lower')
        ax.set_title('Martian Terrain Elevation Map')

        if show_flat_zones:
            flat_mask = self.detect_flat_zones()
            ax.contour(flat_mask, colors='blue', linewidths=0.5)
            ax.set_title('Terrain with Flat Excavation Zones(blue)')

        plt.xlabel("X Axis")
        plt.ylabel("Y Axis")
        plt.show()

    def export_point_cloud(self, filename="terrain.pcd"):
        """
        Export terrain as a point cloud for use with 3D visualizers (Open3D, RViz)
        :param filename: Output file name
        :return:
        """

        x_coords, y_coords = np.meshgrid(
            np.arange(self.grid_size[0]) * self.resolution,
            np.arange(self.grid_size[1]) * self.resolution
        )
        z_coords = self.elevation_map

        points = np.vstack((
            x_coords.flatten(),
            y_coords.flatten(),
            z_coords.flatten()
        )).T

        pcd = o3d.geometry.PointCloud()
        pcd.points = o3d.utility.Vector3dVector(points)
        o3d.io.write_point_cloud(filename, pcd)
        print(f"Point cloud saved to: {filename}")

if __name__ == "__main__":
    mapper = TerrainMapper()
    mapper.simulate_depth_data()
    mapper.visualize_map()
    mapper.export_point_cloud("martian_terrain.pcd")
