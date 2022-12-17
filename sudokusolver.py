# Use a txt file to input the puzzle.

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

# Take a screenshot of sudoku puzzle from domain https://sudoku.com/
def getSudokuImage():
    driver = webdriver.Chrome()
    driver.get('https://sudoku.com/')

    close_tips = driver.find_elements(By.CLASS_NAME, 'game-tip')

    for tip in close_tips:
        if tip.is_displayed():
            WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(tip)).click()

    image = driver.find_element(By.ID, 'game').screenshot_as_png

    with open('screenshot.png', 'wb') as file:
        file.write(image)

    driver.close()
