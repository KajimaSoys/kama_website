from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

import time
import logging
from logging.handlers import RotatingFileHandler
import os

import urllib.request
from urllib.parse import urlparse

logging.basicConfig(level=logging.INFO, format='%(asctime)s|%(name)s|%(levelname)s| %(message)s')

logger = logging.getLogger(__name__)
logging.getLogger('selenium').setLevel(logging.WARNING)

handler = RotatingFileHandler("files_backup/parser.log", maxBytes=80000, backupCount=5)
logger.addHandler(handler)

options = webdriver.ChromeOptions()
# options.add_argument("--headless=new")
# options.add_argument("--no-sandbox")
# options.add_argument("--disable-dev-shm-usage")
# options.add_argument('--disk-cache-size=1')
options.add_argument('--user-agent=""Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5810.200 Safari/537.36""')
options.add_experimental_option('excludeSwitches', ['enable-logging'])


def main(target_url: str):
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    logger.info("Webdriver has been initialized")
    wait = WebDriverWait(driver, 3)

    driver.get(target_url)
    time.sleep(60)

    last_review_index = 0  # Переменная для хранения индекса последнего собранного отзыва

    reviews = driver.find_elements('css selector', 'div.style-snippet-E6g8Y')
    main_folder = 'files'

    for i, review in enumerate(reviews[last_review_index:], start=last_review_index):
        logger.info(f"Parsing review №{i}")

        try:
            review_folder = os.path.join(main_folder, f"review_{i}")
            if not os.path.exists(review_folder):
                os.mkdir(review_folder)

            try:
                image_element = review.find_element('css selector', 'img.desktop-zfo75o')
                image_src = image_element.get_attribute("src")
            except:
                image_src = ''

            if 'static' not in image_src:
                author_photo_folder = os.path.join(review_folder, "author_photo")
                if not os.path.exists(author_photo_folder):
                    os.mkdir(author_photo_folder)

                parsed_url = urlparse(image_src)
                image_name = os.path.basename(parsed_url.path)
                image_path = os.path.join(author_photo_folder, f"{image_name}.jpg")
                urllib.request.urlretrieve(image_src, image_path)

            review_text = review.find_element('css selector', 'span.desktop-rkrl0v').text
            with open(os.path.join(review_folder, "review.txt"), "w", encoding="utf-8") as f:
                f.write(review_text)

            review_author = review.find_element('css selector', 'span.desktop-fzlb6d').text
            with open(os.path.join(review_folder, "author_name.txt"), "w", encoding="utf-8") as f:
                f.write(review_author)

            image_wrappers = review.find_elements("css selector", "div.style-imageWrapper-SGJTU")
            if image_wrappers:
                review_photo_folder = os.path.join(review_folder, "review_photo")
                if not os.path.exists(review_photo_folder):
                    os.mkdir(review_photo_folder)

                img_idx = 1
                for image_wrapper in image_wrappers:
                    image_wrapper.click()
                    time.sleep(1)
                    image_element = driver.find_element("css selector", "img.styles-extended-gallery-img-_q67M")
                    image_src = image_element.get_attribute("src")
                    parsed_url = urlparse(image_src)
                    image_name = os.path.basename(parsed_url.path)
                    if not any(ext in image_name for ext in [".jpg", ".jpeg", ".webp"]):
                        image_name += ".jpg"
                    image_path = os.path.join(review_photo_folder, f"{img_idx}_{image_name}")
                    urllib.request.urlretrieve(image_src, image_path)

                    cross_button = driver.find_element("css selector", "div.styles-cross-jE1a2")
                    cross_button.click()

                    img_idx += 1

            last_review_index = i  # Обновляем индекс последнего успешно собранного отзыва
        except Exception as e:
            print(f"Ошибка при обработке отзыва {i}: {e}")

    time.sleep(300)


if __name__ == "__main__":
    target_url = 'https://www.avito.ru/user/b8baa491c8a12a8ca17da8f9b4179c32/profile?src=sharing'
    main(target_url)
