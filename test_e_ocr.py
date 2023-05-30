import unittest
import os
import tempfile
import shutil
from PIL import Image
from e_ocr import process_image


class TestOCR(unittest.TestCase):
    
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    def test_process_image(self):
        # Create an image file for testing (here an empty image is created as an example).
        img_path = os.path.join(self.test_dir, 'test.png')
        img = Image.new('RGB', (60, 30), color = (73, 109, 137))
        img.save(img_path)

        # Process images for testing.
        process_image(img_path, use_grayscale=False)

        # Verify that the text file exists after processing.
        txt_file_path = os.path.splitext(img_path)[0] + '.txt'
        self.assertTrue(os.path.exists(txt_file_path))

        # Verify that the file is empty (because the image contains no text).
        with open(txt_file_path, 'r', encoding='utf-8') as f:
            self.assertEqual(f.read(), '')

if __name__ == '__main__':
    unittest.main()
