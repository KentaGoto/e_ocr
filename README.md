# e_ocr

This Python script performs OCR (Optical Character Recognition) on image files in a specified directory, using the easyOCR library.

## Getting Started

Prerequisites
Before running this script, you need to install the following Python libraries:

1. `easyocr` - For performing OCR.
2. `opencv-python` (cv2) - For handling image data.
3. `Pillow` (PIL) - For image file handling.

You can install these packages using pip:

```bash
pip install easyocr opencv-python pillow
```

## Usage

To run the script, navigate to the directory where the script is located and run:

```bash
python ocr_script.py
```

When prompted, input whether you want to use grayscale for image processing (yes/no). Then, input the directory path which contains the image files you want to process.

The script will walk through the specified directory, identify image files, and perform OCR on them. The recognized text is then written to a `.txt` file with the same name as the original image file.

## How It Works

The process_image function is the heart of this script. It takes an image file path and a boolean value for whether to use grayscale in processing.

The function does the following:

1. Reads the image file with OpenCV.
2. Depending on the use_grayscale argument, it converts the image to grayscale or RGB color space.
3. Initializes an easyOCR reader in Japanese and English.
4. Extracts text from the image using the easyOCR reader.
5. Writes the extracted text to a .txt file in the same directory as the original image.

## License

MIT

## Author

Kenta Goto