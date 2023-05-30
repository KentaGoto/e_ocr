import easyocr
import cv2
from PIL import Image
import os


def all_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            yield os.path.join(root, file)

def is_image_file(file_path):
    try:
        Image.open(file_path)
    except IOError:
        return False
    return True

def process_image(file_path, use_grayscale):
    img = cv2.imread(file_path)

    # If use_grayscale is True, convert from OpenCV BGR to grayscale.
    # If False, convert to OpenCV RGB.
    if use_grayscale:
        img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    else:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    reader = easyocr.Reader(['ja', 'en']) # Languages used.
    results = reader.readtext(img)

    extracted_texts = []
    for (bbox, text, prob) in results:
        extracted_texts.append(text)

    txt_file_path = os.path.splitext(file_path)[0] + '.txt'

    with open(txt_file_path, 'w', encoding='utf-8') as f:
        for text in extracted_texts:
            f.write(text + '\n')


if __name__ == '__main__':
    use_grayscale = input("Use grayscale? (yes/no): ").lower() == 'yes'
    root_dir = input("Dir: ").strip('\"')

    for i in all_files(root_dir):
        if is_image_file(i):
            process_image(i, use_grayscale)