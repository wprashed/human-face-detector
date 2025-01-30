# Human Detection & Image Deletion Script

This Python script scans a directory for images and automatically deletes those that contain human figures. It uses OpenCV's **Haar Cascade Classifier** to detect humans in images.

## Features
- Detects human presence in images using a pre-trained model.
- Deletes images that contain humans.
- Supports common image formats (`.jpg`, `.jpeg`, `.png`).
- Fast and efficient processing using OpenCV.

## Requirements
Ensure you have Python installed and install the required dependencies using:

```bash
pip install opencv-python
```

## Usage
1. Clone this repository or download the script.
2. Place all your images inside a folder.
3. Modify the script to set the correct `image_directory` path.

```python
image_directory = 'path_to_your_images'
```

4. Run the script:

```bash
python detect_and_delete.py
```

## How It Works
1. The script loads a **Haar Cascade Classifier** (`haarcascade_fullbody.xml`) to detect human figures.
2. It converts each image to grayscale and scans for human-like shapes.
3. If a human is detected, the image is **deleted** from the directory.

## Example Output
```
Image1.jpg does not contain a human.
Deleted image: Image2.jpg
Image3.png does not contain a human.
```

## Notes
- If you want to detect faces instead of full-body figures, replace:
  ```python
  cascade_path = cv2.data.haarcascades + 'haarcascade_fullbody.xml'
  ```
  with:
  ```python
  cascade_path = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
  ```

- The script is optimized for general human detection, but for higher accuracy, consider using deep learning models like YOLO, SSD, or Faster R-CNN.

## License
This project is open-source and available under the MIT License.
