# Project 4: Image or Text Recognition (Basic)

## Project Objective

This project demonstrates basic machine perception by performing Optical Character Recognition (OCR) on input images. The application loads an image, preprocesses it to improve readability, extracts text using Tesseract OCR, and saves the results.

## Features

- Load image files in `.jpg`, `.jpeg`, `.png`, and `.bmp` formats.
- Display the original image and the preprocessed image.
- Convert images to grayscale, apply noise reduction, and perform adaptive thresholding.
- Extract text using `pytesseract` with selectable page segmentation modes.
- Save OCR output to `output/output.txt` or individual `.txt` files.
- Save processed image files to the `output` folder.
- Batch processing for all supported images in a folder.
- Error handling for missing files, unsupported formats, empty OCR results, and missing Tesseract installation.

## Project Structure

```
Task 4 - Shahzaib Tariq/
│
├── main.py
├── ocr_engine.py
├── image_processing.py
├── requirements.txt
├── README.md
├── sample_images/
├── output/
└── screenshots/
```

## Libraries Used

- `opencv-python`
- `pytesseract`
- `numpy`
- `Pillow`

## Installation Steps

1. Install Python 3.x if not already installed.
2. Install the Tesseract OCR engine:
   - Windows: download from https://github.com/tesseract-ocr/tesseract/releases
   - macOS: `brew install tesseract`
   - Linux: `sudo apt-get install tesseract-ocr`
3. Install Python dependencies:

```bash
pip install -r requirements.txt
```

4. Confirm the Tesseract binary is on your system `PATH`.

## How OCR Works

1. The application loads the selected image using OpenCV.
2. It converts the image to grayscale to reduce color complexity.
3. It applies Gaussian blur to remove noise and smooth details.
4. Adaptive thresholding converts the image to a binary format for better OCR accuracy.
5. `pytesseract` reads the processed image and extracts text content.
6. The application returns the text and confidence score, then optionally saves the result.

## Running the Application

From the `Task 4 - Shahzaib Tariq` folder, run:

```bash
python main.py
```

Follow the menu prompts to:

- OCR a single image
- OCR all images in a folder
- Exit the application

## Sample Output

When OCR succeeds, the application prints the recognized text and the average confidence score. It also displays the original image and the processed image.

Example:

```
Loaded image: sample_images/document.png
Recognized text:
Hello World
Average confidence: 89.45%
Saved extracted text to: output/output.txt
Saved processed image to: output/document_processed.png
```

## Screenshots

Place screenshots of your running application and OCR results in the `screenshots/` folder. Include:

- Original image view
- Processed image view
- Sample OCR results saved in `output/`

## Notes

- Tesseract must be installed separately and accessible from the command line.
- If OCR finds no text, the application warns the user and still allows saving an empty result.
- Use the sample images folder to organize example input files.

## Conclusion

This project provides a complete OCR pipeline using Python, OpenCV, and Tesseract. It is structured for readability and reuse, with separate modules for image preprocessing and OCR processing.
