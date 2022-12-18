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
        driver.save_screenshot('screenshot.png')

    driver.close()

# Function to transform the perspective of the image to a square(approximately) with corners ABCD which basically crops the Sudoku
def crop_sudoku_image(image, corners):
    A, B, C, D = corners[0:4]
    maxWidth = int(max(np.linalg.norm(A - B), np.linalg.norm(C - D)))
    maxHeight = int(max(np.linalg.norm(A - D), np.linalg.norm(B - C)))
    resize = int(maxWidth/2)
    width = maxWidth + resize
    height = maxHeight + resize
    input = np.float32([A, B, C, D])
    output = np.float32([[0, 0],  [0, height], [width, height], [width, 0]])

    matrix = cv2.getPerspectiveTransform(input, output)
    cropped = cv2.warpPerspective(image, matrix, (width, height))

    return cropped

# Function to find the corners of the Sudoku grid.
def find_sudoku_corners():
    # Turn the image into grayscale
    image = cv2.imread('screenshot.png')
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Turn the image into a binary black/white image
    threshold = cv2.adaptiveThreshold(image_gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY_INV,21,2)
    # Find the corners of the Sudoku grid
    corners, _ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    corners = sorted(corners, key=cv2.contourArea, reverse=True)

    for corner in corners:
        length = cv2.arcLength(corner, True)
        approx_corners = cv2.approxPolyDP(corner, 0.02 * length, True)
        if len(approx_corners) == 4:
            A, B, C, D = approx_corners[0:4]
            maxWidth = max(np.linalg.norm(A - B), np.linalg.norm(C - D))
            maxHeight = max(np.linalg.norm(A - D), np.linalg.norm(B - C))
            if abs(maxHeight//maxWidth - 1) <= 0.05:
                break
    return threshold, approx_corners

# Function to process the Sudoku image so that it can be parsed into an OCR model and have the numbers be recognized
def process_sudoku_image():
    threshold, corners = find_sudoku_corners()
    cropped = crop_sudoku_image(threshold, corners)
    cv2.imshow('output', cropped)
    cv2.waitKey(5000)
    
def main():
    get_sudoku_image('https://www.sudoku.com/')
    process_sudoku_image()

if __name__ == '__main__':
    main()
    exit()
