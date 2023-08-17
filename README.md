# ArtBlendTool

This script allows you to overlay images from two different folders while removing the white background from the overlay images. The resulting overlay images are saved in a specified results folder. It's a versatile tool that helps you create unique compositions by combining images.

## Prerequisites

Before using this script, ensure you have the following libraries installed:

- `numpy`: For numerical operations on arrays.
- `PIL` (Python Imaging Library): For image processing and manipulation.
- `os`: For file and directory operations.

You can install these libraries using the following command:

```sh
pip install numpy pillow

```

# Setup
1. Set the `WHITE_THRESHOLD` variable in the script to adjust the threshold for identifying the white background. This threshold determines which pixels are considered white.

2. Define the paths for the `layer1_folder`, `layer2_folder`, and `results_folder`. These paths should point to the folders where your input images are stored and where you want the output images to be saved.

# Functions
`remove_white_background(image_array)`
This function takes an image array as input and removes the white background from it. It uses the `WHITE_THRESHOLD` value to determine which pixels are considered white. The function modifies the alpha channel of the image array to make the white pixels transparent.

`overlay_images(base_array, overlay_array, output_path)`
This function overlays two image arrays: `base_array` and `overlay_array`, and saves the resulting image in the specified `output_path`. The function resizes the overlay image to match the dimensions of the base image. It then calls the `remove_white_background` function to remove the white background from the overlay image. The function creates a mask based on the alpha channel of the overlay image and uses it to combine the two images. The resulting image is saved in PNG format.

`load_image(image_path)`
This function takes an image file path as input, opens the image using the PIL library, converts it to RGBA mode, and returns the image array as a NumPy array.

# Running the Script
1. Set up the script as mentioned in the "Setup" section.

2. Run the script in a Python environment using the following command:

```sh
python ArtBlendTool.py
```
 
The script iterates over each image in the `layer1` folder and loads it as the base image. It then iterates over each image in the `layer2` folder, overlays it with the base image, and saves the resulting overlay image in the `results` folder with a unique filename.

Any errors encountered during image loading will be printed to the console.

# Important Notes
* Ensure that the layer folders only contain image files with the extensions `.png`, `.jpg`, or `.jpeg`.
* The script saves the overlay images in PNG format to preserve transparency.
* Feel free to modify and customize the script to suit your specific requirements.

# License
This script is provided under the MIT License. You can find more details in the `LICENSE` file.

