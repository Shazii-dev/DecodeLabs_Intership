import os
import sys

import cv2

from image_processing import (
    apply_threshold,
    convert_to_grayscale,
    load_image,
    remove_noise,
)
from ocr_engine import (  # noqa: E402
    extract_text,
    get_tesseract_version,
    save_text,
)


def ensure_output_directory(path="output"):
    if not os.path.exists(path):
        os.makedirs(path, exist_ok=True)
    return path


def show_image(title, image):
    try:
        cv2.imshow(title, image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    except Exception as error:
        print(f"Unable to display image '{title}': {error}")


def save_processed_image(image, original_path, output_dir="output"):
    base_name = os.path.splitext(os.path.basename(original_path))[0]
    target_path = os.path.join(output_dir, f"{base_name}_processed.png")
    cv2.imwrite(target_path, image)
    return target_path


def prompt_psm_mode():
    print("Available OCR page segmentation modes (PSM):")
    print("0 = Orientation and script detection (OSD) only")
    print("1 = Automatic page segmentation with OSD")
    print("3 = Fully automatic page segmentation")
    print("6 = Assume a single uniform block of text")
    print("11 = Sparse text. Find as much text as possible")

    choice = input("Enter PSM mode [default 3]: ").strip()
    if choice.isdigit():
        return int(choice)
    return 3


def process_single_image(image_path, output_dir="output"):
    try:
        image = load_image(image_path)
        print(f"Loaded image: {image_path}")
        show_image("Original Image", image)

        gray = convert_to_grayscale(image)
        denoised = remove_noise(gray)
        processed = apply_threshold(denoised)

        show_image("Processed Image", processed)

        psm = prompt_psm_mode()
        text, confidence, boxed_image = extract_text(processed, psm=psm, draw_boxes=True)

        if boxed_image is not None:
            show_image("Text Detection", boxed_image)

        if not text:
            print("Warning: OCR did not find any text in the image.")
        else:
            print("\nRecognized text:\n")
            print(text)
            print(f"\nAverage confidence: {confidence:.2f}%")

        ensure_output_directory(output_dir)

        if input("Save extracted text to output.txt? (y/N): ").strip().lower() == "y":
            text_path = os.path.join(output_dir, "output.txt")
            save_text(text or "", text_path)
            print(f"Saved extracted text to: {text_path}")

        if input("Save processed image? (y/N): ").strip().lower() == "y":
            saved_path = save_processed_image(processed, image_path, output_dir)
            print(f"Saved processed image to: {saved_path}")

    except Exception as error:
        print(f"Error: {error}")


def process_image_folder(folder_path, output_dir="output"):
    if not os.path.isdir(folder_path):
        print(f"Folder not found: {folder_path}")
        return

    image_files = [
        os.path.join(folder_path, f)
        for f in sorted(os.listdir(folder_path))
        if os.path.splitext(f.lower())[1] in {".jpg", ".jpeg", ".png", ".bmp"}
    ]

    if not image_files:
        print("No supported image files found in the folder.")
        return

    ensure_output_directory(output_dir)
    for path in image_files:
        print(f"\nProcessing: {path}")
        try:
            image = load_image(path)
            gray = convert_to_grayscale(image)
            denoised = remove_noise(gray)
            processed = apply_threshold(denoised)
            text, confidence, _ = extract_text(processed, psm=3, draw_boxes=False)

            base_name = os.path.splitext(os.path.basename(path))[0]
            save_text(text or "", os.path.join(output_dir, f"{base_name}.txt"))
            save_processed_image(processed, path, output_dir)
            print(f"Saved OCR output and image for {base_name}")
            print(f"Confidence: {confidence:.2f}%")
        except Exception as error:
            print(f"Failed to process {path}: {error}")


def main():
    print("Artificial Intelligence Project 4: Image/Text Recognition")

    try:
        tesseract_version = get_tesseract_version()
        print(f"Detected Tesseract version: {tesseract_version}")
    except Exception as error:
        print(f"Warning: {error}")
        print("The application will still run, but OCR will fail until Tesseract is installed.")

    while True:
        print("\nMenu:")
        print("1. OCR single image")
        print("2. OCR all images in a folder")
        print("3. Exit")

        choice = input("Choose an option: ").strip()
        if choice == "1":
            image_path = input("Enter the path to an image file: ").strip()
            process_single_image(image_path)
        elif choice == "2":
            folder_path = input("Enter the folder path containing images: ").strip()
            process_image_folder(folder_path)
        elif choice == "3":
            print("Exiting application.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
