from Jobfind_Page.Jobfind_Page import JobfindPage
from Jobfind_Page.Jobfind_users import user1


class JobFindTest(JobfindPage):
    # ------------ Variables -------------------------------------
    STELARAS = user1()

    def test_2_login(self):
        """Test login with user credentials"""
        self.click_to_open_website()
        self.click_to_handle_gdpr_popup()
        # Login with the expected credentials of the created user.
        self.login(self.STELARAS)

if __name__ == "__main__":
    from seleniumbase import SB

    with SB() as sb:
        sb.open("https://www.jobfind.gr/")
        sb.sleep(3)  # Allows you to see the opened page
        test = JobFindTest()
        test.login(user1())