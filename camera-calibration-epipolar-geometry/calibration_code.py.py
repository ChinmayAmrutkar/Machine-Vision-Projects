import cv2
import numpy as np
import glob

# Define the dimensions of checkerboard
checkerboard_size = (8, 6)  # 8 corners wide, 6 corners tall
square_size = 25  # mm, optional for real-world scaling

# Define real world coordinates for points in checkerboard plane
objp = np.zeros((checkerboard_size[0] * checkerboard_size[1], 3), np.float32)
objp[:, :2] = np.mgrid[0:checkerboard_size[0], 0:checkerboard_size[1]].T.reshape(-1, 2)
objp *= square_size  # scale if physical measurement is known

# Arrays to store object points and image points
objpoints = []  # 3D points
imgpoints = []  # 2D points

# Read all images from folder
images = glob.glob('calib_images/*.jpg')

for fname in images:
    img = cv2.imread(fname)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Find the checkerboard corners
    ret, corners = cv2.findChessboardCorners(gray, checkerboard_size, None)

    if ret:
        objpoints.append(objp)
        corners2 = cv2.cornerSubPix(
            gray, corners, (11, 11), (-1, -1),
            (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
        )
        imgpoints.append(corners2)

        # Optional: Show corners on image
        cv2.drawChessboardCorners(img, checkerboard_size, corners2, ret)
        cv2.imshow('Corners', img)
        cv2.waitKey(100)

cv2.destroyAllWindows()

# Calibrate the camera
ret, K, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)

print("✅ Camera Intrinsic Matrix (K):\n", K)
print("\n🔍 Distortion Coefficients:\n", dist)

# Compute reprojection error
total_error = 0
for i in range(len(objpoints)):
    imgpoints2, _ = cv2.projectPoints(objpoints[i], rvecs[i], tvecs[i], K, dist)
    error = cv2.norm(imgpoints[i], imgpoints2, cv2.NORM_L2) / len(imgpoints2)
    total_error += error

print("\n📐 Mean Reprojection Error: {:.4f}".format(total_error / len(objpoints)))

np.savez("calib_results.npz", K=K, dist=dist, rvecs=rvecs, tvecs=tvecs)
