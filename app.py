import cv2
import os

def detect_human_in_image(image_path):
    # Load the pre-trained Haar Cascade classifier for detecting people
    cascade_path = cv2.data.haarcascades + 'haarcascade_fullbody.xml'
    human_cascade = cv2.CascadeClassifier(cascade_path)

    # Read the image
    img = cv2.imread(image_path)
    if img is None:
        print(f"Error: Couldn't open image {image_path}")
        return False

    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect humans in the image
    humans = human_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    if len(humans) > 0:
        return True  # Human detected
    return False  # No human detected

def delete_images_with_humans(directory):
    # Loop through the images in the specified directory
    for filename in os.listdir(directory):
        image_path = os.path.join(directory, filename)

        # Only process image files (you can add more types if needed)
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            if detect_human_in_image(image_path):
                os.remove(image_path)
                print(f"Deleted image: {filename}")
            else:
                print(f"Image {filename} does not contain a human.")

# Set the directory containing your images
image_directory = 'images'

# Run the function to delete images with humans
delete_images_with_humans(image_directory)