# cartoon_renderer

A simple image processing tool to convert photos into cartoon and sketch styles using OpenCV.

## Features

* **Multiple Rendering Styles:** Apply  distinct styles (Sketch, Soft Watercolor).
* **Side-by-Side Preview:** View the original image and the processed image simultaneously.
* **Interactive UI:** Switch between rendering styles in real-time using keyboard inputs.
* **Pure Image Processing:** Implemented strictly with Computer Vision techniques without the use of any AI models.

## How to Use

| Key | Action |
| --- | --- |
| **TAB** | Switch rendering style (Sketch -> HW Cartoon -> Soft Watercolor) |
| **ESC** | Exit Program |

## Preview & Output

### Good Examples (Where the styles work well)
![good example](https://github.com/lloydkwak/photo-to-cartoon/blob/main/Sketch_good_example.jpg?raw=true)
![good example](https://github.com/lloydkwak/photo-to-cartoon/blob/main/SoftWaterColor_good_example.jpg?raw=true)

### Bad Examples (Where the styles fail)
![bad example](https://github.com/lloydkwak/photo-to-cartoon/blob/main/Sketch_bad_example.jpg?raw=true)
![bad example](https://github.com/lloydkwak/photo-to-cartoon/blob/main/SoftWaterColor_bad_example.jpg?raw=true)

---

## Limitations (Failure Cases)

**1. Sketch Style**
* **When it fails:** Images with flat lighting, low contrast, or minimal color difference between the subject and the background.
* **Why it fails:** This method extracts strokes based on the intensity difference between the original and blurred images. Without sufficient contrast or clear boundaries, it fails to detect edges, leaving a washed-out, mostly blank canvas.

**2. Soft Watercolor Style**
* **When it fails:** Images requiring fine structural details, such as close-up portraits or small text.
* **Why it fails:** The bilateral filter smooths images while preserving strong edges[cite: 1018, 1019]. However, applying it iteratively flattens internal textures too aggressively. This blends away essential details like facial features, making subjects look unnatural or plastic-like.
