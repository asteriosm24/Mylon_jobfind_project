import unittest
from Jobfind_Page.Jobfind_Page import JobfindPage

class JobFindTest(JobfindPage):
    # ------------ Variables ----------------------------------------
    INFORMATIKA = "Πληροφορική - Προγραμματιστές"
    CATEGORY = "QA Engineer"
    CATEGORY_RESULT = "Software Tester"

    # ------------ Main Test ----------------------------------------
    def test_1_do_actions(self):
        """
        Main test case to open the JobFind website, handle the GDPR pop-up,
        filters and validates the expected result.
        """
        # You need to pass the arguments (INFORMATIKA, CATEGORY, CATEGORY_RESULT) correctly
        self.test_navigate_with_filtering(self.INFORMATIKA, self.CATEGORY, self.CATEGORY_RESULT)

if __name__ == "__main__":
    unittest.main()  # This runs all the test methods in the file