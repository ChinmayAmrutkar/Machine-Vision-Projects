# Camera Calibration and Epipolar Geometry

Welcome to the **Camera Calibration and Epipolar Geometry** project! This repository showcases a hands-on implementation of foundational concepts in multi-view geometry using **OpenCV**, including:

- Camera intrinsic parameter calibration  
- Feature matching between two views  
- Fundamental and essential matrix estimation  
- Visualization of epipolar lines to validate stereo correspondence

---

## Project Structure

- **calib_images/** – Contains 21 images of an 8×6 checkerboard from different viewpoints  
- **fundamental_images/** – Two images of a book taken from different camera angles   
- **calibration_code.py** – Code to calibrate camera and compute intrinsic matrix  
- **fundamental_matrix.py** – Code to estimate fundamental and essential matrices  
- **Camera_Calibration_and_Epipolar_Geometry_Using_OpenCV.pdf** – Report with detailed explanation, results, and analysis  
- **README.md** – This file

---

## What This Project Covers

### Camera Calibration

- Uses a printed 8×6 checkerboard with 25mm square size  
- Estimates the intrinsic camera matrix (K) and distortion coefficients  
- Computes a reprojection error (~0.2574) to validate accuracy

### Epipolar Geometry

- Captures two images of a static object from different viewpoints  
- Uses ORB for keypoint detection and brute-force matcher  
- Estimates the fundamental matrix using RANSAC  
- Derives the essential matrix using the known intrinsic matrix  
- Visualizes epipolar lines to check stereo correspondences

---

## 🛠 Tools & Libraries

- OpenCV  
- NumPy  
- Python 3.x  
- Matplotlib (optional, for visualizations)

---

## How to Run

1. Run the calibration code:

    python calibration_code.py

2. Run the fundamental matrix and epipolar visualization code:

    python fundamental_matrix.py

---

## Results

**Estimated Intrinsic Matrix (K):**

    [[3137.18,    0.00, 2080.91],
     [   0.00, 3142.22, 1545.15],
     [   0.00,    0.00,    1.00]]

**Distortion Coefficients:**

    [0.1966, -0.7646, -0.0014, 0.0001, 0.8190]

**Epipolar Geometry Example:**
![epipolar_lines_result](https://github.com/user-attachments/assets/0f023eb2-6e5e-4223-8bed-ed7e5dd9fcba)

One of the epipolar lines in image 1 passes through the letter “I” in the word **APPLIED**, and its corresponding point (yellow dot) in image 2 lies on the same word — confirming correct stereo matching.

For more information and visual results, please refer to the [report.pdf](https://github.com/ChinmayAmrutkar/Machine-Vision-Projects/blob/main/camera-calibration-epipolar-geometry/Camera_Calibration_and_Epipolar_Geometry_Using_OpenCV.pdf) document provided in the repository.

---

## References

- https://docs.opencv.org/4.x/dc/dbb/tutorial_py_calibration.html  
- https://docs.opencv.org/3.4/da/de9/tutorial_py_epipolar_geometry.html  
- https://markhedleyjones.com/projects/calibration-checkerboard-collection  

---

<p align="center">
  <em>Exploring geometry in vision — one camera at a time!</em>
</p>
