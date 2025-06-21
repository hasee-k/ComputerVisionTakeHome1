# Image Processing Operations in Python

This project includes Python scripts for basic image processing tasks using OpenCV and NumPy.

## Features

1. **Reduce Intensity Levels**
   - Reduces grayscale or RGB image intensity levels (e.g., from 256 to 2, 4, 8, ...).

2. **Spatial Averaging (Blurring)**
   - Applies a simple average filter using kernel sizes like 3x3, 10x10, and 20x20.

3. **Image Rotation**
   - Rotates images by any angle (e.g., 45°, 90°) without cropping. Black borders are preserved.

4. **Block Averaging (Resolution Reduction)**
   - For each non-overlapping block (3x3, 5x5, etc.), replaces all pixels with the block average to simulate resolution reduction.

## Requirements

- Python 3.x
- OpenCV (`cv2`)
- NumPy

Install dependencies using:

```bash
pip install opencv-python numpy
