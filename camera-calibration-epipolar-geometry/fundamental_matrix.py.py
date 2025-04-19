import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load images
img1 = cv2.imread('fundamental_images/1.jpg', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('fundamental_images/2.jpg', cv2.IMREAD_GRAYSCALE)

# Initialize ORB detector
orb = cv2.ORB_create(nfeatures=2000)

# Find keypoints and descriptors
kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)

# Match features using Brute-Force matcher
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
matches = bf.match(des1, des2)
matches = sorted(matches, key=lambda x: x.distance)

# Extract matched points
pts1 = np.float32([kp1[m.queryIdx].pt for m in matches]).reshape(-1, 1, 2)
pts2 = np.float32([kp2[m.trainIdx].pt for m in matches]).reshape(-1, 1, 2)

# Compute fundamental matrix with RANSAC
F, mask = cv2.findFundamentalMat(pts1, pts2, cv2.FM_RANSAC)

# Select inlier points
pts1 = pts1[mask.ravel() == 1]
pts2 = pts2[mask.ravel() == 1]

print("Fundamental Matrix (F):\n", F)

# Function to draw epipolar lines
def draw_epilines(img1, img2, lines, pts1, pts2):
    r, c = img1.shape
    img1_color = cv2.cvtColor(img1, cv2.COLOR_GRAY2BGR)
    img2_color = cv2.cvtColor(img2, cv2.COLOR_GRAY2BGR)
    for r, pt1, pt2 in zip(lines, pts1, pts2):
        color = tuple(np.random.randint(0, 255, 3).tolist())
        x0, y0 = map(int, [0, -r[2]/r[1]])
        x1, y1 = map(int, [c, -(r[2]+r[0]*c)/r[1]])
        img1_color = cv2.line(img1_color, (x0, y0), (x1, y1), color, 1)
        img1_color = cv2.circle(img1_color, tuple(pt1[0].astype(int)), 5, color, -1)
        img2_color = cv2.circle(img2_color, tuple(pt2[0].astype(int)), 5, color, -1)
    return img1_color, img2_color

# Compute epilines in img1 for pts in img2
lines1 = cv2.computeCorrespondEpilines(pts2.reshape(-1,1,2), 2, F)
lines1 = lines1.reshape(-1, 3)
img1_with_lines, img2_with_points = draw_epilines(img1, img2, lines1, pts1, pts2)

# Show and save visualization
plt.figure(figsize=(14,6))
plt.subplot(121), plt.imshow(img1_with_lines), plt.title("Epilines on Image 1")
plt.subplot(122), plt.imshow(img2_with_points), plt.title("Points on Image 2")
plt.tight_layout()
plt.savefig("epipolar_lines_result.jpg")
plt.show()

# Use your intrinsic matrix K (from earlier calibration)
K = np.array([[3137.18, 0, 2080.91],
              [0, 3142.22, 1545.15],
              [0, 0, 1]])

# Compute essential matrix: E = K^T * F * K
E = K.T @ F @ K
print("\nEssential Matrix (E):\n", E)

# Compute epipoles (right nullspace of F and left nullspace of F)
_, _, Vt = np.linalg.svd(F)
e1 = Vt[-1]
e1 = e1 / e1[2]

U, _, _ = np.linalg.svd(F)
e2 = U[:, -1]
e2 = e2 / e2[2]

print("\nEpipole in Image 1 (Right nullspace):", e1)
print("Epipole in Image 2 (Left nullspace):", e2)
