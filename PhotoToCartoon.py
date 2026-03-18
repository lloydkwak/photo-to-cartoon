import cv2
import numpy as np

def style_sketch(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    inv_gray = cv2.bitwise_not(gray)
    blur = cv2.GaussianBlur(inv_gray, (21, 21), 0)
    sketch_gray = cv2.divide(gray, cv2.bitwise_not(blur), scale=256.0)
    sketch_color = cv2.cvtColor(sketch_gray, cv2.COLOR_GRAY2BGR)
    
    return sketch_color


def style_watercolor(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    s = cv2.add(s, 40)
    hsv_boost = cv2.merge((h, s, v))
    color_boost = cv2.cvtColor(hsv_boost, cv2.COLOR_HSV2BGR)

    result = color_boost
    for _ in range(3):
        result = cv2.bilateralFilter(result, d=9, sigmaColor=75, sigmaSpace=75)
        
    return result

def main():
    image_path = 'input_image.jpg'
    img = cv2.imread(image_path)
    
    if img is None:
        print("Cannot read the image.")
        return
    
    max_width = 800
    if img.shape[1] > max_width:
        ratio = max_width / img.shape[1]
        img = cv2.resize(img, (int(img.shape[1] * ratio), int(img.shape[0] * ratio)))

    styles = [
        {"name": "Sketch", "func": style_sketch},
        {"name": "Soft Watercolor", "func": style_watercolor}
    ]
    
    style_idx = 0

    while True:
        current_style = styles[style_idx]
        processed_img = current_style["func"](img)

        merge = np.hstack((img, processed_img))

        cv2.imshow('Cartoon Rendering', merge)

        key = cv2.waitKey(0)
        
        if key == 27:
            break
        elif key == 9:
            style_idx = (style_idx + 1) % len(styles)

    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()