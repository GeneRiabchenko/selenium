import unittest
from selenium import webdriver
from app_functions import save_button_click
from app_functions import find_all_comments
from app_functions import click_return_button
from app_functions import click_save_and_return
from app_functions import enter_number
from app_functions import choose_first_comment_duplicate
from Tests import ExpectedResults


class DuplicateButtonTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(executable_path='res\chromedriver.exe')
        self.browser.get('http://commentssprintone.azurewebsites.net')
        choose_first_comment_duplicate(self.browser)

    def tearDown(self):
        self.browser.close()

    def test_duplicate_without_number(self):
        # clear field number
        comment_number = self.browser.find_element_by_id('Number')
        comment_number.clear()

        # save comment
        save_button_click(self.browser)

        # return to the row of comments
        click_return_button(self.browser)

        # find created comment
        comments = find_all_comments(self.browser)
        self.assertIn(ExpectedResults.duplicate_button_without_number, comments)

    def test_duplicate_comment_save_with_number(self):
        number = ExpectedResults.duplicate_button_with_number[0]
        # enter number
        enter_number(self.browser, number)

        # save comment
        save_button_click(self.browser)

        # return to the row of comments
        click_return_button(self.browser)

        # find created comment
        comments = find_all_comments(self.browser)
        self.assertIn(ExpectedResults.duplicate_button_with_number, comments)

    def test_duplicate_comment_return_save_without_number(self):
        # clear field number
        comment_number = self.browser.find_element_by_id('Number')
        comment_number.clear()

        # save comment and return
        click_save_and_return(self.browser)

        # check that comment was created
        comments = find_all_comments(self.browser)
        self.assertIn(ExpectedResults.duplicate_button_without_number, comments)

    def test_duplicate_comment_return_save_with_number(self):
        # enter number
        number = ExpectedResults.duplicate_button_with_number[0]
        enter_number(self.browser, number)

        # save comment and return
        click_save_and_return(self.browser)

        # check that comment was created
        comments = find_all_comments(self.browser)
        self.assertIn(ExpectedResults.duplicate_button_with_number, comments)
