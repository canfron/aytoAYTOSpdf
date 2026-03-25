#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Automated PDF downloader for the New Espacio Clientes portal.
Hard‑coded credentials – no prompts.
"""

import os
import sys
import time
import pathlib
from urllib.parse import urljoin

import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# --------------------------------------------------------------------------- #
# 1. CONFIGURATION – EDIT IF NECESSARY
# --------------------------------------------------------------------------- #

BASE_URL = "https://new-espacioclientes.berger-levrault.es/"

# ----> HARD‑CODED CREDENTIALS (replace with your own) <----
USERNAME = "mario@aranjuez.es"
PASSWORD = "Ozd=_X3).e05"
# --------------------------------------------------------------------------- #

SOFTWARE_PAGE_LINK_TEXT = "Software"   # text shown in the left‑hand menu
WAIT_TIMEOUT = 15                     # seconds – adjust if needed
DOWNLOAD_DIR = pathlib.Path.home() / "Downloads" / "BergerLevr"

# --------------------------------------------------------------------------- #
# 2. HELPER FUNCTIONS
# --------------------------------------------------------------------------- #

def init_driver() -> webdriver.Chrome:
    """Instantiate a Chrome WebDriver (headless optional)."""
    options = webdriver.ChromeOptions()
    # Uncomment to run headless
    # options.add_argument("--headless")
    options.add_argument("--window-size=1920x1080")
    options.add_argument("--disable-gpu")

    service = ChromeService()          # assumes chromedriver is on PATH
    driver = webdriver.Chrome(service=service, options=options)
    return driver


def wait_for_element(driver: webdriver.Chrome, by: By, value: str):
    """Wait until an element is present and visible."""
    return WebDriverWait(driver, WAIT_TIMEOUT).until(
        EC.visibility_of_element_located((by, value))
    )


def click_link_by_text(driver: webdriver.Chrome, link_text: str):
    """Click a link identified by its visible text."""
    link = wait_for_element(driver, By.LINK_TEXT, link_text)
    link.click()


def download_file(url: str, dest_path: pathlib.Path):
    """Download a file via requests and write it to disk."""
    print(f"  → Downloading {url}")
    r = requests.get(url, stream=True, timeout=WAIT_TIMEOUT)
    r.raise_for_status()
    with open(dest_path, "wb") as f:
        for chunk in r.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)


def ensure_dir(path: pathlib.Path):
    """Create directory if it doesn't exist."""
    path.mkdir(parents=True, exist_ok=True)

# --------------------------------------------------------------------------- #
# 3. MAIN LOGIC
# --------------------------------------------------------------------------- #

def main():
    driver = init_driver()
    wait = WebDriverWait(driver, WAIT_TIMEOUT)

    try:
        # --------------------------------------------------- #
        # a) Log in
        # --------------------------------------------------- #
        print("Navigating to login page...")
        driver.get(BASE_URL)
        username_field = wait_for_element(driver, By.ID, "username")
        password_field = wait_for_element(driver, By.ID, "password")

        username_field.clear()
        username_field.send_keys(USERNAME)

        password_field.clear()
        password_field.send_keys(PASSWORD)

        login_btn = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        login_btn.click()

        # --------------------------------------------------- #
        # b) Go to Software section
        # --------------------------------------------------- #
        print("Waiting for dashboard…")
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        time.sleep(2)

        print(f"Clicking on '{SOFTWARE_PAGE_LINK_TEXT}' menu item…")
        click_link_by_text(driver, SOFTWARE_PAGE_LINK_TEXT)

        # --------------------------------------------------- #
        # c) Grab all program links
        # --------------------------------------------------- #
        print("Collecting program list...")
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "ul.program-list")))
        program_elements = driver.find_elements(By.CSS_SELECTOR, "ul.program-list li a")

        program_links = [(elem.text.strip(), elem.get_attribute("href")) for elem in program_elements]
        print(f"Found {len(program_links)} programs.")

        # --------------------------------------------------- #
        # d) Process each program
        # --------------------------------------------------- #
        for prog_name, prog_url in program_links:
            print(f"\n=== Processing '{prog_name}' ===")
            driver.get(prog_url)
            time.sleep(2)

            base_prog_dir = DOWNLOAD_DIR / prog_name
            doc_dir = base_prog_dir / "Documentación"
            ver_dir = base_prog_dir / "Versiones"

            ensure_dir(doc_dir)
            ensure_dir(ver_dir)

            # 1️⃣ Documentación tab
            print(" - Switching to 'Documentación' tab")
            click_link_by_text(driver, "Documentación")
            time.sleep(1)

            pdf_links = driver.find_elements(By.CSS_SELECTOR, "a[href$='.pdf']")
            for link in pdf_links:
                href = link.get_attribute("href")
                filename = pathlib.Path(href).name
                dest_path = doc_dir / filename
                if dest_path.exists():
                    print(f"   • Skipping existing file: {filename}")
                else:
                    download_file(href, dest_path)

            # 2️⃣ Versiones tab
            print(" - Switching to 'Versiones' tab")
            click_link_by_text(driver, "Versiones")
            time.sleep(1)

            pdf_links = driver.find_elements(By.CSS_SELECTOR, "a[href$='.pdf']")
            for link in pdf_links:
                href = link.get_attribute("href")
                filename = pathlib.Path(href).name
                dest_path = ver_dir / filename
                if dest_path.exists():
                    print(f"   • Skipping existing file: {filename}")
                else:
                    download_file(href, dest_path)

        print("\n✅ All downloads finished.")
    except Exception as e:
        print(f"\n❌ ERROR: {e}", file=sys.stderr)
    finally:
        driver.quit()


# --------------------------------------------------------------------------- #
if __name__ == "__main__":
    main()
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Automated PDF downloader for the New Espacio Clientes portal.
Hard‑coded credentials – no prompts.
"""

import os
import sys
import time
import pathlib
from urllib.parse import urljoin

import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# --------------------------------------------------------------------------- #
# 1. CONFIGURATION – EDIT IF NECESSARY
# --------------------------------------------------------------------------- #

BASE_URL = "https://new-espacioclientes.berger-levrault.es/"

# ----> HARD‑CODED CREDENTIALS (replace with your own) <----
USERNAME = "mario@aranjuez.es"
PASSWORD = "Ozd=_X3).e05"
# --------------------------------------------------------------------------- #

SOFTWARE_PAGE_LINK_TEXT = "Software"   # text shown in the left‑hand menu
WAIT_TIMEOUT = 15                     # seconds – adjust if needed
DOWNLOAD_DIR = pathlib.Path.home() / "Downloads" / "BergerLevr"

# --------------------------------------------------------------------------- #
# 2. HELPER FUNCTIONS
# --------------------------------------------------------------------------- #

def init_driver() -> webdriver.Chrome:
    """Instantiate a Chrome WebDriver (headless optional)."""
    options = webdriver.ChromeOptions()
    # Uncomment to run headless
    # options.add_argument("--headless")
    options.add_argument("--window-size=1920x1080")
    options.add_argument("--disable-gpu")

    service = ChromeService()          # assumes chromedriver is on PATH
    driver = webdriver.Chrome(service=service, options=options)
    return driver


def wait_for_element(driver: webdriver.Chrome, by: By, value: str):
    """Wait until an element is present and visible."""
    return WebDriverWait(driver, WAIT_TIMEOUT).until(
        EC.visibility_of_element_located((by, value))
    )


def click_link_by_text(driver: webdriver.Chrome, link_text: str):
    """Click a link identified by its visible text."""
    link = wait_for_element(driver, By.LINK_TEXT, link_text)
    link.click()


def download_file(url: str, dest_path: pathlib.Path):
    """Download a file via requests and write it to disk."""
    print(f"  → Downloading {url}")
    r = requests.get(url, stream=True, timeout=WAIT_TIMEOUT)
    r.raise_for_status()
    with open(dest_path, "wb") as f:
        for chunk in r.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)


def ensure_dir(path: pathlib.Path):
    """Create directory if it doesn't exist."""
    path.mkdir(parents=True, exist_ok=True)

# --------------------------------------------------------------------------- #
# 3. MAIN LOGIC
# --------------------------------------------------------------------------- #

def main():
    driver = init_driver()
    wait = WebDriverWait(driver, WAIT_TIMEOUT)

    try:
        # --------------------------------------------------- #
        # a) Log in
        # --------------------------------------------------- #
        print("Navigating to login page...")
        driver.get(BASE_URL)
        username_field = wait_for_element(driver, By.ID, "username")
        password_field = wait_for_element(driver, By.ID, "password")

        username_field.clear()
        username_field.send_keys(USERNAME)

        password_field.clear()
        password_field.send_keys(PASSWORD)

        login_btn = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        login_btn.click()

        # --------------------------------------------------- #
        # b) Go to Software section
        # --------------------------------------------------- #
        print("Waiting for dashboard…")
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        time.sleep(2)

        print(f"Clicking on '{SOFTWARE_PAGE_LINK_TEXT}' menu item…")
        click_link_by_text(driver, SOFTWARE_PAGE_LINK_TEXT)

        # --------------------------------------------------- #
        # c) Grab all program links
        # --------------------------------------------------- #
        print("Collecting program list...")
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "ul.program-list")))
        program_elements = driver.find_elements(By.CSS_SELECTOR, "ul.program-list li a")

        program_links = [(elem.text.strip(), elem.get_attribute("href")) for elem in program_elements]
        print(f"Found {len(program_links)} programs.")

        # --------------------------------------------------- #
        # d) Process each program
        # --------------------------------------------------- #
        for prog_name, prog_url in program_links:
            print(f"\n=== Processing '{prog_name}' ===")
            driver.get(prog_url)
            time.sleep(2)

            base_prog_dir = DOWNLOAD_DIR / prog_name
            doc_dir = base_prog_dir / "Documentación"
            ver_dir = base_prog_dir / "Versiones"

            ensure_dir(doc_dir)
            ensure_dir(ver_dir)

            # 1️⃣ Documentación tab
            print(" - Switching to 'Documentación' tab")
            click_link_by_text(driver, "Documentación")
            time.sleep(1)

            pdf_links = driver.find_elements(By.CSS_SELECTOR, "a[href$='.pdf']")
            for link in pdf_links:
                href = link.get_attribute("href")
                filename = pathlib.Path(href).name
                dest_path = doc_dir / filename
                if dest_path.exists():
                    print(f"   • Skipping existing file: {filename}")
                else:
                    download_file(href, dest_path)

            # 2️⃣ Versiones tab
            print(" - Switching to 'Versiones' tab")
            click_link_by_text(driver, "Versiones")
            time.sleep(1)

            pdf_links = driver.find_elements(By.CSS_SELECTOR, "a[href$='.pdf']")
            for link in pdf_links:
                href = link.get_attribute("href")
                filename = pathlib.Path(href).name
                dest_path = ver_dir / filename
                if dest_path.exists():
                    print(f"   • Skipping existing file: {filename}")
                else:
                    download_file(href, dest_path)

        print("\n✅ All downloads finished.")
    except Exception as e:
        print(f"\n❌ ERROR: {e}", file=sys.stderr)
    finally:
        driver.quit()


# --------------------------------------------------------------------------- #
if __name__ == "__main__":
    main()
