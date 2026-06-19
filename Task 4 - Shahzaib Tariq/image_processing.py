import os
import cv2

SUPPORTED_EXTENSIONS = {".jpg", ".jpeg", ".png", ".bmp"}


def load_image(image_path):
    """Load an image from disk and validate supported file types."""
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image file not found: {image_path}")

    _, ext = os.path.splitext(image_path)
    ext = ext.lower()
    if ext not in SUPPORTED_EXTENSIONS:
        raise ValueError(f"Unsupported image format: {ext}. Use JPG, PNG, BMP.")

    image = cv2.imread(image_path)
    if image is None:
        raise ValueError(f"Failed to load image: {image_path}")

    return image


def convert_to_grayscale(image):
    """Convert a color image to grayscale."""
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


def remove_noise(gray_image, kernel_size=(5, 5)):
    """Reduce noise using Gaussian blur."""
    return cv2.GaussianBlur(gray_image, kernel_size, 0)


def apply_threshold(gray_image, method="adaptive"):
    """Apply adaptive thresholding or basic binary thresholding."""
    if method == "adaptive":
        return cv2.adaptiveThreshold(
            gray_image,
            255,
            cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
            cv2.THRESH_BINARY,
            11,
            2,
        )

    _, thresholded = cv2.threshold(
        gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )
    return thresholded
