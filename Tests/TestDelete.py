import unittest
from selenium import webdriver
from app_functions import find_all_comments
from app_functions import click_delete_button
from app_functions import choose_first_comment


class DeleteTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(executable_path='res\chromedriver.exe')
        self.browser.get('http://commentssprintone.azurewebsites.net')

    def tearDown(self):
        self.browser.close()

    def test_delete_one_comment(self):
        expected_result = ['', 'Comment Text 0', '', 'Cat0']

        # chose comment to delete
        choose_first_comment(self.browser)

        # press delete button
        click_delete_button(self.browser)

        # apply delete
        yes_button = self.browser.find_element_by_xpath('/html/body/div[2]/div[3]/div/button[1]')
        yes_button.click()

        # find created comment
        comments = find_all_comments(self.browser)
        self.assertNotIn(expected_result, comments)


