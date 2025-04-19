Camera Calibration and Epipolar Geometry Using OpenCV
This project demonstrates the use of OpenCV for camera calibration and epipolar geometry estimation using real-world images. It is structured around two core tasks:

Estimating the intrinsic parameters of a camera using a checkerboard.

Computing the fundamental and essential matrices between two stereo images and visualizing epipolar lines.

📂 Folder Structure
csharp
Copy
Edit
camera-calibration-epipolar-geometry/
│
├── calib_images/               # 21 checkerboard images
├── fundamental_images/         # 2 stereo images of a book
│
├── calib.png                   # Sample checkerboard view
├── calib_res.png               # Overlay of reprojected corners
├── epipolar_lines_result.png   # Epipolar line visualization
│
├── calibration_code.py         # Camera calibration script
├── fundamental_matrix.py       # Fundamental matrix & epipolar geometry
│
├── main_report.tex             # LaTeX report (CVPR-style)
├── main_report.pdf             # Compiled report
├── README.md                   # This file
🧠 Project Summary
Camera Calibration
Printed checkerboard with 8×6 inner corners, square size: 25mm.

21 images captured using a mobile phone camera from various angles.

Intrinsic matrix (K) and distortion coefficients computed using OpenCV.

Mean reprojection error: 0.2574

Epipolar Geometry
2 images of a book captured from slightly different angles.

ORB feature detection and brute-force matching.

Fundamental matrix F estimated using RANSAC.

Essential matrix E computed as: E = K.T @ F @ K

Epipolar lines plotted to visualize feature correspondence.

🔧 Dependencies
Python 3.x

OpenCV

NumPy

Matplotlib

LaTeX (with minted, tcolorbox for code blocks)

🚀 How to Run
Calibration
Run the camera calibration script:

nginx
Copy
Edit
python calibration_code.py
Fundamental Matrix & Epipolar Lines
Run the stereo geometry script:

nginx
Copy
Edit
python fundamental_matrix.py
Generate Report
Compile the main_report.tex file using LaTeX (e.g., Overleaf or TeXStudio).

📈 Sample Results
Intrinsic Matrix (K):

lua
Copy
Edit
[[3137.18    0.00   2080.91]
 [   0.00 3142.22   1545.15]
 [   0.00    0.00      1.00]]
Distortion Coefficients:

csharp
Copy
Edit
[0.1966, -0.7646, -0.0014, 0.0001, 0.8190]
Epipolar Geometry Visualization: Epipolar lines correctly align with corresponding points across the two views. For example, the yellow line in image 1 passes through the letter I in "APPLIED", and the corresponding yellow dot in image 2 lies over the same feature — confirming correctness.

👤 Author
Chinmay Amrutkar
ASU ID: 1233273147
Email: chinmay.amrutkar@asu.edu

📚 References
OpenCV Camera Calibration Tutorial

OpenCV Epipolar Geometry Tutorial

Checkerboard Generator