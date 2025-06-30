\# 🪐 RegolithBot: Autonomous Mars Excavation Simulator



\*\*RegolithBot\*\* is a modular Python-based system designed to simulate robotic excavation, terrain analysis, and regolith classification for future Mars colonies.



Currently under active development, it lays the foundation for AI-assisted construction, habitat planning, and in-situ resource utilization (ISRU) on the Martian surface.



---



\## ✅ Completed Modules



\### 1. `terrain\_mapping.py`

Simulates Martian terrain using LiDAR/stereo depth data (or synthetic input).  

Includes:

\- Elevation map generation

\- Slope analysis

\- Flat zone detection (for construction or excavation)

\- Terrain visualization

\- Export to 3D point cloud (Open3D compatible)



---



\### 2. `sample\_analysis.py`

Models in-situ chemical analysis of regolith samples using simulated spectrometry.  

Includes:

\- Composition breakdown (e.g. Fe₂O₃, SiO₂, H₂O, perchlorates, etc.)

\- Automated sample classification:

&nbsp; - 💧 Water Extraction Candidate

&nbsp; - 🏗️ Construction Grade

&nbsp; - 🟡 Mixed Utility

&nbsp; - ⚠️ Hazardous (toxic)

\- JSON report export



---



\### 3. `excavation\_planner.py`

Generates a priority map by combining terrain flatness and sample utility to guide where robots should dig.  

Includes:

\- Scoring system based on regolith classification

\- Terrain penalty for non-flat zones

\- Top excavation site selection

\- Heatmap visualization of excavation zones



---



\## 🚧 In Progress



\### 4. `main.py`

This orchestration script will:

\- Tie all modules together

\- Generate terrain and sample data

\- Run excavation planning

\- Control future robotic actions (via arm controller)



Estimated: \*\*WIP\*\*



---



\### 5. `arm\_control.py`

Simulates robotic arm behavior for:

\- Targeted movement using (mock) inverse kinematics

\- Digging operations

\- Gripper actions (grab/release)

\- Sample transport



Estimated: \*\*WIP\*\*



---



\## 📦 Project Goals



\- Provide an extensible, modular pipeline for Martian regolith research

\- Visualize terrain + excavation maps in Python

\- Train future AI-based excavation and planning agents

\- Enable hardware integration with ROS in later phases



---



\## 🛠️ Installation



```bash

git clone https://github.com/your-username/RegolithBot

cd RegolithBot

pip install -r requirements.txt

