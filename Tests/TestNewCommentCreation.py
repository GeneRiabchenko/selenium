import unittest
from selenium import webdriver
from app_functions import save_button_click
from app_functions import find_all_comments
from app_functions import click_return_button
from app_functions import click_all_category
from app_functions import click_save_and_return
from app_functions import comment_text_write
from Tests import ExpectedResults


class NewButtonTests(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(executable_path='res\chromedriver.exe')
        self.browser.get('http://commentssprintone.azurewebsites.net')
        button = self.browser.find_element_by_id("newbutton")
        button.click()

    def tearDown(self):
        self.browser.close()

    def test_new_comment_save_without_number(self):
        comment_name = ExpectedResults.new_button_without_number[1]
        # enter comment's name
        comment_text_write(self.browser, comment_name)

        # chose all category
        click_all_category(self.browser)

        # save comment
        save_button_click(self.browser)

        # return to the row of comments
        click_return_button(self.browser)

        # find created comment
        comments = find_all_comments(self.browser)
        self.assertIn(ExpectedResults.new_button_without_number, comments)

    def test_new_comment_save_with_number(self):
        comment_name = ExpectedResults.new_button_with_number[1]
        number = ExpectedResults.new_button_with_number[0]

        # enter comment's name
        comment_text_write(self.browser, comment_name)

        # enter number
        comment_number = self.browser.find_element_by_id('Number')
        comment_number.send_keys(number)

        # chose all category
        click_all_category(self.browser)

        # save comment
        save_button_click(self.browser)

        # return to the table of comments
        click_return_button(self.browser)

        # find created comment
        comments = find_all_comments(self.browser)
        self.assertIn(ExpectedResults.new_button_with_number, comments)

    def test_new_comment_return_save_without_number(self):
        comment_name = ExpectedResults.new_button_without_number[1]
        # enter comment's name
        comment_text_write(self.browser, comment_name)

        # chose all category
        click_all_category(self.browser)

        # save comment and return
        click_save_and_return(self.browser)

        # check that comment was created
        comments = find_all_comments(self.browser)
        self.assertIn(ExpectedResults.new_button_without_number, comments)

    def test_new_comment_return_save_with_number(self):
        comment_name = ExpectedResults.new_button_with_number[1]
        number = ExpectedResults.new_button_with_number[0]
        # enter comment's name
        comment_text_write(self.browser, comment_name)
        # enter number
        comment_number = self.browser.find_element_by_id('Number')
        comment_number.send_keys(number)

        # chose all category
        click_all_category(self.browser)

        # save comment and return
        click_save_and_return(self.browser)

        # check that comment was created
        comments = find_all_comments(self.browser)
        self.assertIn(ExpectedResults.new_button_with_number, comments)

    def test_new_comment_length_50_text(self):
        comment_name = ExpectedResults.new_button_length_50[1]
        # enter comment's name
        comment_text_write(self.browser, comment_name)

        # chose all category
        click_all_category(self.browser)

        # save comment and return
        click_save_and_return(self.browser)

        # check that comment was created
        comments = find_all_comments(self.browser)
        self.assertIn(ExpectedResults.new_button_length_50, comments)

    def test_new_comment_number_999(self):
        comment_name = ExpectedResults.new_button_number_999[1]
        number = ExpectedResults.new_button_number_999[0]
        # enter comment's name
        comment_text_write(self.browser, comment_name)
        # enter number
        comment_number = self.browser.find_element_by_id('Number')
        comment_number.send_keys(number)

        # chose all category
        click_all_category(self.browser)

        # save comment and return
        click_save_and_return(self.browser)

        # check that comment was created
        comments = find_all_comments(self.browser)
        self.assertIn(ExpectedResults.new_button_number_999, comments)

    def test_new_comment_text_symbol(self):
        amount_pass_test = 0
        for symbol in ExpectedResults.symbols:
            # chose all category
            click_all_category(self.browser)

            # enter comment's name
            comment_name = symbol
            comment_text_write(self.browser, comment_name)

            # click button save
            save_button_click(self.browser)

            # check error massage displayed
            try:
                self.browser.find_element_by_id('errorfield').is_displayed()
                actual_result = self.browser.find_element_by_id('errorfield').text
            except:
                actual_result = None

            expected_massage = ExpectedResults.error_massage_not_alphanumeric
            if actual_result == expected_massage:
                amount_pass_test += 1
            else:
                print('Test fell on symbol ' + symbol)
            # clear comment text field
            self.browser.find_element_by_id('Text').clear()
        # check that all error massage were displayed
        self.assertEqual(amount_pass_test, len(ExpectedResults.symbols))


if __name__ == '__main__':
    unittest.main()
