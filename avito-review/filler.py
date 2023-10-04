from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from dotenv import load_dotenv
import time

load_dotenv()

USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")

driver = webdriver.Chrome()

def main():
    driver.get("https://kamamebel.com/admin")
    # time.sleep(5)
    # username_field = driver.find_element(By.NAME, "username")
    # username_field.send_keys(USERNAME)
    # password_field = driver.find_element(By.NAME, "password")
    # password_field.send_keys(PASSWORD)
    # password_field.send_keys(Keys.RETURN)
    time.sleep(10)

    driver.get("https://kamamebel.com/admin/service/review/")
    time.sleep(3)

    add_review_button = driver.find_element(By.CSS_SELECTOR, "ul.object-tools li a.addlink")
    add_review_button.click()
    time.sleep(3)

    for i in range(0, 55):
        review_folder = os.path.join("files", f"review_{i}")

        # Author name
        with open(os.path.join(review_folder, "author_name.txt"), "r", encoding="utf-8") as f:
            author_name = f.read().strip()
        author_field = driver.find_element(By.ID, "id_author")
        author_field.send_keys(author_name)

        # Review text
        editor_frame = driver.find_element(By.CSS_SELECTOR, 'iframe.cke_wysiwyg_frame')
        driver.switch_to.frame(editor_frame)
        body = driver.find_element(By.TAG_NAME, "body")
        body.clear()
        with open(os.path.join(review_folder, "review.txt"), "r", encoding="utf-8") as f:
            review = f.read().strip()
        driver.execute_script("arguments[0].innerText = arguments[1];", body, review)
        driver.switch_to.default_content()

        # Author photo
        author_photo_folder = os.path.join(review_folder, "author_photo")
        if os.path.exists(author_photo_folder):
            author_photo_file = os.listdir(author_photo_folder)[0]  # Возьмем первое фото

            absolute_path_to_photo = os.path.abspath(
                os.path.join(author_photo_folder, author_photo_file)
            )

            author_photo_field = driver.find_element(By.ID, "id_author_photo")
            author_photo_field.send_keys(
                absolute_path_to_photo
            )

        # Review photos
        review_photo_folder = os.path.join(review_folder, "review_photo")
        if os.path.exists(review_photo_folder):
            review_photo_files = os.listdir(review_photo_folder)
            photo_idx = 0
            for review_photo_file in review_photo_files:
                absolute_path_to_photo = os.path.abspath(
                    os.path.join(review_photo_folder, review_photo_file)
                )

                review_photo_field = driver.find_element(By.ID, f"id_photos-{photo_idx}-photo")
                review_photo_field.send_keys(
                    absolute_path_to_photo
                )
                add_photo_button = driver.find_element(By.CSS_SELECTOR, "tr.add-row a")
                add_photo_button.click()
                photo_idx += 1

        save_and_continue_button = driver.find_element(By.NAME, "_addanother")
        save_and_continue_button.click()
        time.sleep(5)


if __name__ == '__main__':
    main()
