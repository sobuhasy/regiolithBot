import time
import numpy as np

class ArmController:
    def __init__(self, arm_name="RegolithArm-01"):
        self.arm_name = arm_name
        self.joint_angles = [0.0] * 5 # 5 DOF example
        self.gripper_open = True
        self.status = "IDLE"

    def move_to(self, x, y, z):
        """
        Move the arm's end-effector to target coordinates using inverse kinematics
        For now, we simulate it with dummy values.
        :param x:
        :param y:
        :param z:
        :return:
        """
        self.status = "MOVING"
        print(f"🦾Moving {self.arm_name} to position (x={x}, y={y}, z={z})...")
        time.sleep(1.5)
        print(f"✅ Position reached. Joint angles: {self.joint_angles}")
        self.status = "IDLE"

    def inverse_kinematics(self, x, y, z):
        """
        Dummy inverse kinematics function. Replace with real IK solver later
        :param x:
        :param y:
        :param z:
        :return:
        """

        return [
            np.arctan2(y, x),                     # Base rotation
            np.clip(z / 10.0, -1, 1),             # Shoulder elevation
            np.clip((x+y)/ 20.0, -1, 1),          # Elbow flexion
            0.5,                                  # Wrist rotation
            0.0                                   # Gripper position (0.0 = closed, 1.0 = open)
        ]

    def dig(self, depth=0.3):
        """
        Perform a basic dig operation
        :param depth:
        :return:
        """
        print("🔽 Starting excavation sequence...")
        self.move_to(0.5, 0.0, 0.0)    # Move above target
        self.move_to(0.5, 0.0, -depth) # Move down to dig
        self.close_gripper()
        time.sleep(1)
        self.move_to(0.5, 0.0, 0.2)     # Lift soil
        print("✅ Soil collected.")

    def place_sample(self, bin_coords=(0.0, 0.5, 0.0)):
        """
        Move arm to sample container and release.
        :param bin_coords:
        :return:
        """
        print("📦 Transporting sample to bin...")
        self.move_to(*bin_coords)
        self.open_gripper()
        time.sleep(1)
        self.move_to(0.0, 0.0, 0.2)
        print("✅ Sample delivered.")

    def open_gripper(self):
        if not self.gripper_open:
            print("🖐️ Opening gripper...")
            self.gripper_open = True
            time.sleep(0.5)
        else:
            print("️️️🖐️ Gripper already open.")

    def close_gripper(self):
        if self.gripper_open:
            print("🤏 Closing gripper...")
            self.gripper_open = False
            time.sleep(0.5)
        else:
            print("🤏 Gripper already closed.")

    def emergency_stop(self):
        print("🚨 Emergency stop activated!")
        self.status = "EMERGENCY_STOP"
        # Stop all motor commands here

    def get_status(self):
        return {
            "arm": self.arm_name,
            "status": self.status,
            "joint_angles": self.joint_angles,
            "gripper_opem": self.gripper_open
        }

# Example usage
if __name__ == "__main__":
    arm = ArmController()
    arm.dig(depth=0.4)
    arm.place_sample(bin_coords=(0.0, 0.6, 0.0))
    print("📋 Final Status: ", arm.get_status())
