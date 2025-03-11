from seleniumbase import BaseCase

class JobfindPage(BaseCase):
    # ----------- Paths -------------------------------------------
    def path_login_button(self):
        path = "//a[contains(.,'Είσοδος')]"
        return path  # Adjust based on actual site

    def path_email_input(self):
        path = "//input[@id='dxtxtEmail']"
        return path

    def path_password_input(self):
        path = "//input[@id='dxtxtPassword']"
        return path

    def path_submit_button(self):
        path = "//input[@type='submit']"
        return path

    def path_consent_button_xpath(self):
        return "//button[contains(.,'ΣΥΜΦΩΝΩ')]"

    def path_greece_xpath(self):
        return "//h4[contains(.,'Όλη η Ελλάδα')]"

    def path_informatica_list_choice(self, specialty):
        return f'//a[contains(.,"{specialty}")]'

    def path_specialty_category(self, category):
        return f"//a[contains(.,'{category}')]"

    def path_category_result(self, result):
        """Returns a flexible XPath for the expected text."""
        return f"//*[contains(normalize-space(), '{result}')]"

    # ----------- Clicks & Existence ---------------------------------------

    def existence(self, text):
        """Validates if a specific text is visible on the page."""
        text_xpath = f"//*[contains(normalize-space(), '{text}')]"

        # Wait for the element to appear before checking
        self.wait_for_element_visible(text_xpath, timeout=5)

        if self.is_element_visible(text_xpath):
            print(f"✅ The text '{text}' is visible on the page.")
            return True
        else:
            print(f"❌ The text '{text}' is NOT visible on the page.")
            return False

    def click_for_login_button(self):
        """ Click to open the login button"""
        self.click(self.path_login_button())
        print("✅ Πατήθηκε το κουμπί 'Είσοδος'.")

    def click_for_submit_button(self):
        """ Click the button submit"""
        self.click(self.path_submit_button())
        print("✅ Πατήθηκε το κουμπί 'Είσοδος/submit'.")

    def click_to_open_website(self):
        """Open the website"""
        self.open("https://www.jobfind.gr/")
        self.sleep(3)  # Wait for 3 seconds to see the page before closing
        self.maximize_window()

    def click_to_handle_gdpr_popup(self):
        """Handle the GDPR pop-up if it appears"""
        if self.is_element_visible(self.path_consent_button_xpath()):
            self.click(self.path_consent_button_xpath())
            print("✅ Clicked the GDPR pop-up to close it.")

    def click_greece_tab(self):
        """Click the 'Όλη η Ελλάδα' tab"""
        self.click(self.path_greece_xpath())
        print("✅ Clicked the 'Όλη η Ελλάδα' button.")

    def click_specialty_list_choice(self, specialty):
        """Clicks the specialty from the list"""
        self.click(self.path_informatica_list_choice(specialty=specialty))
        print(f"✅ Clicked the '{specialty}' specialty.")

    def click_specialty_category(self, category):
        """Clicks the category in the list after clicking the specialty."""
        self.click(self.path_specialty_category(category=category))
        print(f"✅ Clicked the '{category}' category.")

    # ----------- Send_Keys ----------------------------------------

    def send_keys_for_email(self, email):
        """ Send keys to email typetext """
        self.send_keys(self.path_email_input(), email)
        print(f"✅ Μπήκε το email: {email}")

    def send_keys_for_pass(self, password):
        """ Send keys to password typetext """
        self.send_keys(self.path_password_input(), password)
        print("✅ Μπήκε το password")

    # ----------- Validation ---------------------------------------

    def validation_category_result(self, result):
        """Validates the existence of the expected result"""
        return self.existence(result)

    # ----------- Functions -----------------------------------------

    def login(self, user):
        """
        Logs in a user by retrieving credentials and using send_keys.
        """
        email = user["email"]
        password = user["password"]
        # Press the button 'Είσοδος'
        self.click_for_login_button()
        self.wait(2)
        # Enter the credentials, 1st the e-mail and 2nd the password.
        self.send_keys_for_email(email)
        self.send_keys_for_pass(password)
        # Press the button 'Είσοδος'
        self.click_for_submit_button()
        print(f"✅ Είσοδος με το {email}")

    def test_navigate_with_filtering(self, specialty, category, result):
        """
        This function open the JobFind website, handle the GDPR pop-up,
        filters and validates the expected result.
        """
        self.click_to_open_website()
        self.click_to_handle_gdpr_popup()
        self.click_greece_tab()
        self.click_specialty_list_choice(specialty)
        self.click_specialty_category(category)
        self.wait(2)
        # Validate that the expected category result exists
        assert self.validation_category_result(result=result)
