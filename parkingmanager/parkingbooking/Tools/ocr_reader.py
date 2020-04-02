try:
    from PIL import Image,ImageFilter
except ImportError:
    import Image
import pytesseract
import io

class OcrReader(object):

    def __init__(self):
        pass

    def get_text_from_image(self, image_path):
        """ Get text from an image"""
        print("OCR Pocess")
        img = Image.open(image_path)
        text_image = pytesseract.image_to_string(img, lang='eng')
        print(text_image)
        return text_image

        """
        img2 = img.filter(ImageFilter.BLUR)
        pixels = img2.load()
        width, height = img2.size
        x_ = []
        y_ = []
        for x in range(width):
            for y in range(height):
                if pixels[x, y] == (255, 255, 255):
                    x_.append(x)
                    y_.append(y)

        img = img.crop((min(x_), min(y_), max(x_), max(y_)))
        text = pytesseract.image_to_string(img, lang='eng',
                                           config='-c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
        print(text)
        print(pytesseract.image_to_string(image))
        
        """


