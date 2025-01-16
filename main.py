import time
import pyautogui
from PIL import Image
import random


def countdown(seconds):
    for i in range(seconds, 0, -1):
        print(f"Countdown: {i} seconds remaining...")
        time.sleep(1)


def press_right_arrow_and_take_screenshot(
    iterations: int, screenshot_region: tuple[int, int, int, int]
) -> list[str]:
    names = []
    for i in range(iterations):
        print(f"hello{i}")
        pyautogui.press("right")
        time.sleep(random.uniform(0.1, 0.5))
        screenshot = pyautogui.screenshot(region=screenshot_region)
        name = f"image{i}.png"
        screenshot.save(name)
        names.append(name)
    return names


def create_pdf_from_images(image_filenames: list[str], output_pdf: str):
    images = []
    for filename in image_filenames:
        image = Image.open(filename)
        images.append(image)
    images[0].save(output_pdf, save_all=True, append_images=images[1:])


countdown(5)
screenshot_region = (280, 0, 720, 1020)
names = press_right_arrow_and_take_screenshot(79 - 8, screenshot_region)
create_pdf_from_images(names, "result.pdf")

print("end")
