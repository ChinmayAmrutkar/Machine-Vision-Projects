# Messing Around with OpenCV and Images

## Overview
This repository is dedicated to exploring fundamental image processing techniques using the OpenCV framework. Through hands-on experiments, this project demonstrates key operations such as image display, color correction, cropping (zooming), resizing (downsampling and upsampling), and error analysis. Whether you’re new to machine vision or seeking practical insights into digital image manipulation, this guide provides clear explanations and code examples to help you get started.

## Project Structure

### 1. Image Display and Color Correction
**Objective:**  
Learn how to load and display an image, and understand why color correction is necessary when using OpenCV.

**What’s Happening:**  
- **Loading the Image:** The image is loaded using `cv2.imread`, which by default reads the image in BGR format.  
- **Displaying the Image:** The image is initially displayed using Matplotlib’s `plt.imshow`, which shows the colors incorrectly (inverted) due to the BGR format.  
- **Color Correction:** The `cv2.cvtColor` function is used to convert the image from BGR to RGB, ensuring that the colors are displayed as intended.

**Code**
```python
import cv2
import matplotlib.pyplot as plt

# Load an image captured near Hole in the Rock, Phoenix, Arizona
img = cv2.imread('A1_I1.jpg')

# Display the original BGR image (colors will appear inverted)
plt.imshow(img)
plt.title("BGR Image")
plt.show()

# Convert from BGR to RGB for correct color representation
image_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(image_rgb)
plt.title("RGB Image")
plt.show()
```

 **Observation:** <br>
The initial display shows inverted colors because OpenCV uses BGR by default. After conversion, the image reveals its true colors, highlighting a scenic view with a reflective water body, desert plants, and palm trees.

---

### 2. Zooming into an Image (Cropping)
**Objective:**
Focus on a specific region of the image by cropping to analyze details.

**What's Happening**
- A specific area around the top of two palm trees is selected by defining cropping coordinates.
- Cropping provides a closer look at textures, colors, and details that may become pixelated when zoomed in.

**Code**
```python
# Define cropping coordinates (x, y, width, height)
x, y, w, h = 560, 460, 70, 70
cropped_image = image_rgb[y:y+h, x:x+w]

# Display the zoomed-in (cropped) image
plt.imshow(cropped_image)
plt.title("Zoomed-In Image")
plt.show()
```

**Observation:** <br>
The cropped section highlights a detailed view of the palm trees. When images are zoomed beyond their native resolution, individual pixels become more apparent, leading to a grainy appearance.

---

### 3. Image Resizing (Downsampling)
**Objective:**  
Reduce the resolution of an image to understand the effects of downsampling.

**What’s Happening:**  
- A second image is loaded for the purpose of sampling.  
- The image is downsampled by reducing its width and height by a factor of 10 using `cv2.resize`. This process reduces the number of pixels, thereby decreasing the image resolution.

**Code**
```python
# Load another image for downsampling
img2 = cv2.imread('A1_I2.jpg')
image_rgb2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

# Downsample the image by a factor of 10 in both dimensions
downsampled = cv2.resize(image_rgb2, None, fx=0.1, fy=0.1)

# Display the downsampled image
plt.imshow(downsampled)
plt.title("Downsampled Image")
plt.show()
```

 **Observation:** <br>
The downsampled image retains the overall content but with lower detail due to the reduced resolution.

---
### 4. Image Resizing (Upsampling)
**Objective:**  
Restore the downsampled image back to its original resolution using two different interpolation methods.

**What’s Happening:**  
- **Nearest Neighbor Interpolation:** This method upscales the image by simply replicating the nearest pixel values, which can result in a blocky or pixelated appearance.
- **Bicubic Interpolation:** This method calculates new pixel values using a weighted average of surrounding pixels, producing a smoother image.

**Code**
```python
# Upsample using Nearest Neighbor interpolation
nearest_neighbor_image = cv2.resize(downsampled, None, fx=10, fy=10, interpolation=cv2.INTER_NEAREST)

# Upsample using Bicubic interpolation
bicubic_image = cv2.resize(downsampled, None, fx=10, fy=10, interpolation=cv2.INTER_CUBIC)

# Display both upsampled images side by side
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.imshow(nearest_neighbor_image)
plt.title("Nearest Neighbor Upsampling")

plt.subplot(1, 2, 2)
plt.imshow(bicubic_image)
plt.title("Bicubic Upsampling")

plt.show()
```

 **Observation:** <br>
- **Nearest Neighbor:** The image appears blocky and pixelated.
- **Bicubic:** The image is smoother and more visually appealing.
- **Use Cases:**
    - *Nearest Neighbor* is ideal for applications requiring a retro or pixelated effect (e.g., retro video games).
    - *Bicubic* is preferred for high-quality image applications like photo editing and printing.

---
### 5. Absolute Difference and Error Analysis
**Objective:**  
Quantify the error introduced during the upsampling process by comparing the upsampled images with the original high-resolution image.

**What’s Happening:**  
- The `cv2.absdiff` function calculates the absolute difference between the original image and each upsampled image.
- The pixel differences are summed up to provide a numerical measure of the error.

**Code**
```python
import numpy as np

# Calculate absolute differences between the ground truth and the upsampled images
difference_nearest = cv2.absdiff(image_rgb2, nearest_neighbor_image)
difference_bicubic = cv2.absdiff(image_rgb2, bicubic_image)

# Sum the pixel differences to quantify error
sum_difference_nearest = np.sum(difference_nearest)
sum_difference_bicubic = np.sum(difference_bicubic)

print("Nearest Neighbor Error:", sum_difference_nearest)
print("Bicubic Error:", sum_difference_bicubic)
```

 **Observation:** <br>
- The error for the Nearest Neighbor method was 3,446,690.
- The error for the Bicubic method was 3,137,288.
- The lower error in the Bicubic method indicates it preserves image details better, making it the preferred method when image quality is a priority.

---

## References:
- For detailed methodologies and data, refer to the full [documentation](https://github.com/ChinmayAmrutkar/Machine-Vision-Projects/blob/main/Messing_around_with_OpenCV_and_images/Messing_around_with_OpenCV_and_Images.pdf)

---

## Conclusion:
This project provides an introductory yet comprehensive exploration of image processing with OpenCV. By systematically displaying images, correcting colors, zooming in on specific details, resizing images, and performing error analysis, you gain a foundational understanding of digital image manipulation. This knowledge serves as a stepping stone for further exploration into advanced topics in computer vision and machine learning.
