import os

import cv2
import pytesseract
from pytesseract import Output


def get_tesseract_version():
    """Return the installed Tesseract version or raise an informative error."""
    try:
        return pytesseract.get_tesseract_version()
    except Exception as exc:
        raise EnvironmentError(
            "Tesseract OCR engine not found. Install Tesseract and ensure it is on your PATH."
        ) from exc


def extract_text(image, psm=3, oem=3, lang="eng", draw_boxes=False):
    """Run OCR on the image and optionally return an image with bounding boxes."""
    if image is None:
        raise ValueError("No image supplied for OCR extraction.")

    config = f"--oem {oem} --psm {psm}"
    data = pytesseract.image_to_data(
        image,
        output_type=Output.DICT,
        config=config,
        lang=lang,
    )

    lines = {}
    confidences = []

    for i, word in enumerate(data.get("text", [])):
        cleaned = word.strip()
        if not cleaned:
            continue

        line_num = data.get("line_num", [0])[i]
        lines.setdefault(line_num, []).append(cleaned)

        conf_value = data.get("conf", ["-1"])[i]
        try:
            conf_float = float(conf_value)
            if conf_float >= 0:
                confidences.append(conf_float)
        except ValueError:
            continue

    extracted_text = "\n".join(
        " ".join(words) for _, words in sorted(lines.items())
    ).strip()

    average_confidence = (
        sum(confidences) / len(confidences) if confidences else 0.0
    )

    boxed_image = None
    if draw_boxes:
        boxed_image = image.copy()
        n_boxes = len(data.get("level", []))
        for i in range(n_boxes):
            if data["text"][i].strip():
                x = int(data["left"][i])
                y = int(data["top"][i])
                w = int(data["width"][i])
                h = int(data["height"][i])
                cv2_color = (0, 255, 0)
                cv2.rectangle(boxed_image, (x, y), (x + w, y + h), cv2_color, 2)

    return extracted_text, average_confidence, boxed_image


def save_text(text, output_path):
    """Save extracted OCR text to a file."""
    directory = os.path.dirname(output_path)
    if directory and not os.path.exists(directory):
        os.makedirs(directory, exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as file:
        file.write(text or "")

    return output_path
