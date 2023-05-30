import cv2
import numpy as np
import pandas as pd
import os
import glob
from joblib import Parallel, delayed
from PIL import Image
import io

def calculate_most_common_color(image_path):
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Reduce the image size for performance optimization
    image = cv2.resize(image, (50, 50), interpolation=cv2.INTER_AREA)

    reshaped_image = image.reshape(-1, 3)

    colors, count = np.unique(reshaped_image, axis=0, return_counts=True)
    most_common_color = colors[count.argmax()]

    return most_common_color

def rgb_to_hex(rgb):
    return '#{:02x}{:02x}{:02x}'.format(int(rgb[0]), int(rgb[1]), int(rgb[2]))

def process_image(image_path):
    most_common_color = calculate_most_common_color(image_path)
    hex_color = rgb_to_hex(most_common_color)
    return {'File Name': image_path, 'Hex Color': hex_color}

output_csv = 'color_codes.csv'
extensions = ['png', 'jpg', 'jpeg']
image_paths = [file for ext in extensions for file in glob.glob(f'*.{ext}')]

# Use parallel processing to handle multiple images at the same time
results = Parallel(n_jobs=-1)(delayed(process_image)(image_path) for image_path in image_paths)

df = pd.DataFrame(results, columns=['File Name', 'Hex Color'])
df.to_csv(output_csv, index=False)
