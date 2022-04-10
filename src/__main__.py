import argparse
import numpy as np
import cv2
import os

from src.utils import Parser
from src.core import Data, ColorDetector, ShapeDetector

if __name__ == "__main__":
    parser = Parser()

    image_data = Data(os.path.join("./data", parser.filename))
    
    color_detector = ColorDetector(image_data.image)
    image_color, red_result, blue_result, color_result = color_detector.find_color()

    shape_detector = ShapeDetector(red_result, blue_result, color_result)
    image_shape = shape_detector.find_shape()

    print(image_data.image.shape)
    print(image_shape.shape)

    final_result = cv2.bitwise_or(image_data.image, image_shape)

    # Show the output image
    cv2.imshow('Final Result', final_result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()