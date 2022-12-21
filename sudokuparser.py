from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

import cv2
import numpy as np

import easyocr

GRID_LENGTH = 9
CELL_LENGTH = 100
WINDOW_LENGTH = 1000
WHITE = 255
BLACK = 0

# Use the url website with a Sudoku puzzle as the input
# Take a screenshot of sudoku puzzle from domain https://sudoku.com/
def get_sudoku_image(url):
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(options=options)
    driver.get(url)

    if 'https://sudoku.com/' in url or 'https://www.sudoku.com/' in url:
        # The Sudoku puzzles from the domain 'https://www.sudoku.com/' are blocked by a game tip message element so the following code removes the element from blocking the grid.
        tips = driver.find_elements(By.CLASS_NAME, 'game-tip')
        for tip in tips:
            driver.execute_script("""var element = arguments[0];
                                 element.parentNode.removeChild(element);
                                 """, tip)
        image = driver.find_element(By.CLASS_NAME, 'game').screenshot_as_png
        with open('images/screenshot.png', 'wb') as f:
            f.write(image)
    else:
        # Increase the window size in case the Sudoku grid is too large to be captured in the screenshot
        driver.set_window_size(WINDOW_LENGTH, WINDOW_LENGTH)
        driver.save_screenshot('images/screenshot.png')

    driver.close()

# Calculate the width/height of a rectangle/square from its corner coordinates
def getDimensions(corners):
    A, B, C, D = corners
    width = int(max(np.linalg.norm(A - B), np.linalg.norm(C - D)))
    height = int(max(np.linalg.norm(A - D), np.linalg.norm(B - C)))
    return width, height

# Function to transform the perspective of the image to a square(approximately) with corners ABCD which basically crops the Sudoku
def crop_sudoku_image(image, corners):
    width = GRID_LENGTH * CELL_LENGTH
    height = GRID_LENGTH * CELL_LENGTH
    input = np.float32(corners)
    output = np.float32([[0, 0],  [0, height], [width, height], [width, 0]])

    matrix = cv2.getPerspectiveTransform(input, output)
    crop_image = cv2.warpPerspective(image, matrix, (width, height))

    return crop_image

# Function to find the corners of the Sudoku grid.
def find_sudoku_corners(image):
    # Turn the image into grayscale
    image = cv2.imread(image)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Turn the image into a binary black/white image
    threshold_image = cv2.adaptiveThreshold(gray_image, WHITE, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 21, 3)
    # Find the corners of the Sudoku grid
    contours, _ = cv2.findContours(threshold_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)

    for contour in contours:
        length = cv2.arcLength(contour, True)
        corners = cv2.approxPolyDP(contour, 0.02 * length, True)
        # Return early if the contour is a square
        if len(corners) == 4:
            width, height = getDimensions(corners)
            # Set a threshold for the width/height ratio to make sure the contour is approximately a square
            if abs(float(height/width - 1)) <= 0.1:
                return threshold_image, corners
    return threshold_image, contour

# Function to split the Sudoku image into seperate cells and join the images of the pre-filled cells in a row. 
def split_sudoku(image):
    prefill_locations = []
    first_digit = False
    prefill_image = None
    for i in range(0, GRID_LENGTH * CELL_LENGTH, CELL_LENGTH):
        for j in range(0, GRID_LENGTH * CELL_LENGTH, CELL_LENGTH):
            row = i//CELL_LENGTH
            col = j//CELL_LENGTH
            # Cut out the border areas of each cell so we have an image without the border noise.
            cell = image[i+15:i+84, j+15:j+84]
            # Get the images and locations of the prefilled digits by first checking the white to black pixel ratio.
            white_pixels = np.sum(cell == WHITE)
            black_pixels = np.sum(cell == BLACK)
            bw_ratio = float (white_pixels/black_pixels)
            # Set a threshold of 0.0005 white pixels to black pixels
            if bw_ratio > 0.0005:
                prefill_locations.append((row, col))
                if not first_digit:
                    prefill_image = cell
                    first_digit = True
                else:
                    # Join the images of the prefilled cells in a row
                    prefill_image = cv2.hconcat([prefill_image, cell])
    cv2.imwrite('images/digits.png', prefill_image)

    return prefill_locations, prefill_image

# Function to use OCR to read the prefill image and return a Sudoku in array form.
def parse_sudoku(reader, prefill_locations, prefill_image):
    result = reader.readtext(prefill_image, allowlist='0123456789', detail=0)
    result = [int(n) for n in ''.join(result)]
    sudoku = np.zeros((9, 9))
    for loc, digit in zip(prefill_locations, result):
        sudoku[loc[0], loc[1]] = digit
    return sudoku
    

# Function to process the Sudoku image so that it can be parsed into an OCR model and have the digits be recognized and input into an array.
def process_sudoku_image():
    threshold_image, corners = find_sudoku_corners('images/screenshot.png')
    crop_image = crop_sudoku_image(threshold_image, corners)
    cv2.imwrite('images/processed.png', crop_image)
    prefill_locations, prefill_image = split_sudoku(crop_image)
    reader = easyocr.Reader(['en'])
    sudoku = parse_sudoku(reader, prefill_locations, prefill_image)
    return sudoku

# Main function for testing
def get_sudoku():
    # get_sudoku_image('https://websudoku.com/')
    sudoku = process_sudoku_image()
    return sudoku

if __name__ == '__main__':
    get_sudoku()
