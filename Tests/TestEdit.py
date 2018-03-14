import unittest
from selenium import webdriver
from app_functions import save_button_click
from app_functions import find_all_comments
from app_functions import click_return_button
from app_functions import click_save_and_return
from app_functions import choose_first_comment_edit
from app_functions import comment_text_write
from Tests import ExpectedResults


class EditTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(executable_path='res\chromedriver.exe')
        self.browser.get('http://commentssprintone.azurewebsites.net')
        choose_first_comment_edit(self.browser)

    def tearDown(self):
        self.browser.close()

    def test_edit_save_without_number(self):
        comment_name = ExpectedResults.edit_button_without_number[1]
        # enter comment's name
        comment_text_write(self.browser, comment_name)

        # save comment and return
        click_save_and_return(self.browser)

        # find created comment
        comments = find_all_comments(self.browser)
        self.assertIn(ExpectedResults.edit_button_without_number, comments)

    def test_edit_comment_save_with_number(self):
        comment_name = ExpectedResults.edit_button_with_number[1]
        number = ExpectedResults.edit_button_with_number[0]
        # enter comment's name
        comment_text_write(self.browser, comment_name)
        # enter number
        comment_number = self.browser.find_element_by_id('Number')
        comment_number.send_keys(number)

        # save comment
        save_button_click(self.browser)

        # return to the row of comments
        click_return_button(self.browser)

        # find created comment
        comments = find_all_comments(self.browser)
        self.assertIn(ExpectedResults.edit_button_with_number, comments)

    def test_edit_comment_return_save_without_number(self):
        comment_name = ExpectedResults.edit_button_without_number[1]
        # enter comment's name
        comment_text_write(self.browser, comment_name)

        # save comment and return
        click_save_and_return(self.browser)

        # check that comment was created
        comments = find_all_comments(self.browser)
        self.assertIn(ExpectedResults.edit_button_without_number, comments)

    def test_edit_comment_return_save_with_number(self):
        comment_name = ExpectedResults.edit_button_with_number[1]
        number = ExpectedResults.edit_button_with_number[0]
        # enter comment's name
        comment_text_write(self.browser, comment_name)
        # enter number
        comment_number = self.browser.find_element_by_id('Number')
        comment_number.send_keys(number)

        # save comment and return
        click_save_and_return(self.browser)

        # check that comment was created
        comments = find_all_comments(self.browser)
        self.assertIn(ExpectedResults.edit_button_with_number, comments)
