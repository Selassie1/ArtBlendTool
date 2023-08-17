import numpy as np
from PIL import Image
import os

WHITE_THRESHOLD = 200  # Adjust this threshold as needed

def remove_white_background(image_array):
    alpha_channel = image_array[..., 3]
    white_mask = np.all(image_array[..., :3] > WHITE_THRESHOLD, axis=-1)
    alpha_channel[white_mask] = 0
    image_array[..., 3] = alpha_channel
    return image_array

def overlay_images(base_array, overlay_array, output_path):
    overlay_image = Image.fromarray(overlay_array)
    overlay_image = overlay_image.resize(base_array.shape[:2][::-1], Image.LANCZOS)

    overlay_array_no_bg = remove_white_background(np.array(overlay_image))

    mask = overlay_array_no_bg[..., 3] > 0
    output_array = np.where(mask[..., np.newaxis], overlay_array_no_bg, base_array)

    generated_image = Image.fromarray(output_array.astype(np.uint8))

    # Convert RGBA to RGB mode before saving as PNG
    if generated_image.mode == 'RGBA':
        generated_image = generated_image.convert('RGB')

    # Check if the output file already exists and add suffix if necessary
    output_file_path = output_path + ".png"
    counter = 1
    while os.path.exists(output_file_path):
        output_file_path = output_path + f"_{counter}.png"
        counter += 1

    generated_image.save(output_file_path, format="PNG")  # Save as PNG


# Load an image and convert it to a NumPy array
def load_image(image_path):
    image = Image.open(image_path).convert('RGBA')
    image_array = np.array(image)
    return image_array

if __name__ == "__main__":
    layer1_folder = r"C:\path\to\layer1\folder"
    layer2_folder = r"C:\path\to\layer2\folder"
    results_folder = r"C:\path\to\results\folder"

    # Check if the results folder exists, create it if necessary
    if not os.path.exists(results_folder):
        os.makedirs(results_folder)

    # Get the list of image files in the layer1 and layer2 folders
    layer1_images = [f for f in os.listdir(layer1_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    layer2_images = [f for f in os.listdir(layer2_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

    for layer1_image in layer1_images:
        layer1_path = os.path.join(layer1_folder, layer1_image)
        try:
            layer1_array = load_image(layer1_path)
        except Exception as e:
            print(f"Error loading {layer1_image}: {e}")
            continue

        for layer2_image in layer2_images:
            layer2_path = os.path.join(layer2_folder, layer2_image)
            try:
                layer2_array = load_image(layer2_path)
            except Exception as e:
                print(f"Error loading {layer2_image}: {e}")
                continue

            output_name = f"result_{layer1_image}_{layer2_image}"
            output_path = os.path.join(results_folder, output_name)

            overlay_images(layer1_array, layer2_array, output_path)
