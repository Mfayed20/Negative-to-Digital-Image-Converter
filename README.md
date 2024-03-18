# Negative to Digital Image Converter

This Python script is designed to convert negative images into positive ones. It uses the OpenCV and NumPy libraries to perform image processing tasks.

## How it Works

The script contains several functions that work together to process the image:

1. `invert_colors(image)`: This function inverts the colors of the image. It subtracts the color values of the image from 255, effectively creating a negative of the image.

2. `find_darkest_brightest_neutral_gray_pixels(image)`: This function finds the darkest, brightest, and a neutral gray pixel in the image. These values are used later to adjust the color balance of the image.

3. `apply_curves_adjustment(image, darkest_rgb, brightest_rgb, neutral_gray_rgb)`: This function adjusts the color balance of the image based on the darkest, brightest, and a neutral gray points found earlier.

4. `process_image(image_path)`: This is the main function that brings everything together. It loads an image, inverts its colors, finds the darkest, brightest, and a neutral gray pixels, applies color balance adjustments, and finally displays the adjusted image.

## Usage

To use this script, simply call the `process_image(image_path)` function with the path to your negative image as the argument.
