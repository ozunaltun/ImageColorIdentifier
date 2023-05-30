# Dominant Color Extractor

This Python script calculates the most dominant color in image files. It uses the OpenCV, numpy, pandas and joblib libraries to process the images. The script resizes the images for performance optimization, reshapes them, and then calculates the most dominant color. The results are saved to a CSV file.

## Requirements

This script requires Python 3.7 or later, along with the following Python libraries:

- numpy
- opencv-python
- pandas
- Pillow
- joblib

You can install the required packages using pip:

pip install -r requirements.txt

## Usage

To use this script, simply run it in a directory with the images you want to process:

python main.py


By default, the script will process all files in the current directory with the extensions .png, .jpg, and .jpeg. It will write a CSV file (`color_codes.csv`) with the filename and the most dominant color (in hex format) for each image.


