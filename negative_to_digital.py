import cv2
import numpy as np

def invert_colors(image):
    """Invert the image's colors."""
    return 255 - image

def find_darkest_brightest_neutral_gray_pixels(image):
    """Find the darkest, brightest, and a neutral gray pixel in the image."""
    pixel_sums = np.sum(image, axis=2)
    darkest_index = np.argmin(pixel_sums)
    brightest_index = np.argmax(pixel_sums)
    
    h, w, _ = image.shape
    darkest_coords = np.unravel_index(darkest_index, (h, w))
    brightest_coords = np.unravel_index(brightest_index, (h, w))
    
    darkest_rgb = image[darkest_coords]
    brightest_rgb = image[brightest_coords]
    
    rgb_differences = np.max(image, axis=2) - np.min(image, axis=2)
    gray_indices = np.where((rgb_differences < 15) & (pixel_sums > 128 * 3) & (pixel_sums < 192 * 3))
    
    if gray_indices[0].size > 0:
        neutral_gray_rgb = image[gray_indices[0][0], gray_indices[1][0]]
    else:
        neutral_gray_rgb = np.array([128, 128, 128], dtype=np.uint8)
    
    return darkest_rgb, brightest_rgb, neutral_gray_rgb

def apply_curves_adjustment(image, darkest_rgb, brightest_rgb, neutral_gray_rgb):
    """Adjust the image based on the darkest, brightest, and a neutral gray points."""
    float_image = image.astype(np.float32)
    
    darkest_norm = darkest_rgb / 255.0
    brightest_norm = brightest_rgb / 255.0
    
    scale = 1 / (brightest_norm - darkest_norm)
    offset = -darkest_norm * scale
    
    adjusted_image = (float_image * scale) + (offset * 255)
    adjusted_image = np.clip(adjusted_image, 0, 255).astype(np.uint8)
    
    return adjusted_image

def process_image(image_path):
    """Load an image, invert its colors, and apply color balance adjustments."""
    image_bgr = cv2.imread(image_path)
    image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)
    
    inverted_image = invert_colors(image_rgb)
    
    darkest_rgb, brightest_rgb, neutral_gray_rgb = find_darkest_brightest_neutral_gray_pixels(inverted_image)
    
    adjusted_image = apply_curves_adjustment(inverted_image, darkest_rgb, brightest_rgb, neutral_gray_rgb)
    
    # Display the results
    # cv2.imshow('Original Image', image_bgr)
    # cv2.imshow('Inverted Image', cv2.cvtColor(inverted_image, cv2.COLOR_RGB2BGR))
    cv2.imshow('Adjusted Image', cv2.cvtColor(adjusted_image, cv2.COLOR_RGB2BGR))
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Example usage
# Replace 'path_to_your_negative_image.jpg' with the actual path to your negative image
process_image("path_to_your_negative_image.jpg")
