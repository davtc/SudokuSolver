from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

import cv2
import numpy as np

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
        with open('screenshot.png', 'wb') as f:
            f.write(image)
    else:
        # Increase the window size in case the Sudoku grid is too large to be captured in the screenshot
        driver.set_window_size(1000, 1000)
        driver.save_screenshot('screenshot.png')

    driver.close()

# Calculate the width/height of a rectangle/square from its corner coordinates
def getDimensions(corners):
    A, B, C, D = corners
    width = int(max(np.linalg.norm(A - B), np.linalg.norm(C - D)))
    height = int(max(np.linalg.norm(A - D), np.linalg.norm(B - C)))
    return width, height

# Function to transform the perspective of the image to a square(approximately) with corners ABCD which basically crops the Sudoku
def crop_sudoku_image(image, corners):
    width, height = getDimensions(corners)
    resize = int(width/2)
    width += resize
    height += resize
    input = np.float32(corners)
    output = np.float32([[0, 0],  [0, height], [width, height], [width, 0]])

    matrix = cv2.getPerspectiveTransform(input, output)
    cropped_image = cv2.warpPerspective(image, matrix, (width, height))

    return cropped_image

# Function to find the corners of the Sudoku grid.
def find_sudoku_corners():
    # Turn the image into grayscale
    image = cv2.imread('screenshot.png')
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Turn the image into a binary black/white image
    threshold_image = cv2.adaptiveThreshold(image_gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY_INV,21,2)
    # Find the corners of the Sudoku grid
    contours, _ = cv2.findContours(threshold_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)

    for contour in contours:
        length = cv2.arcLength(contour, True)
        corners = cv2.approxPolyDP(contour, 0.02 * length, True)
        # Return early if the contour is a square
        if len(corners) == 4:
            width, height = getDimensions(corners)
            if abs(float(height/width - 1)) <= 0.1:
                return threshold_image, corners
    return threshold_image, contour
# Function to process the Sudoku image so that it can be parsed into an OCR model and have the numbers be recognized
def process_sudoku_image():
    threshold_image, corners = find_sudoku_corners()
    cropped_image = crop_sudoku_image(threshold_image, corners)
    cv2.imshow('output', cropped_image)
    cv2.waitKey(5000)
    
def main():
    get_sudoku_image('https://sudoku.com.au/')
    process_sudoku_image()

if __name__ == '__main__':
    main()
    exit()
