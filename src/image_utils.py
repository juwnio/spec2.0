import cv2
import numpy as np

def split_screenshot_into_grids(image_path, grid_size=5):
    image = cv2.imread(image_path)

    height, width, _ = image.shape
    grid_height = height // grid_size
    grid_width = width // grid_size

    grid_tiles = []

    for row in range(grid_size):
        for col in range(grid_size):
            start_x = col * grid_width
            start_y = row * grid_height
            end_x = (col + 1) * grid_width
            end_y = (row + 1) * grid_height

            grid_tile = image[start_y:end_y, start_x:end_x]
            grid_tiles.append(grid_tile)

    return grid_tiles
