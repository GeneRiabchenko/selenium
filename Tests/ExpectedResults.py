all_categories = 'Cat0; Cat1; Cat2; Cat3; Cat4; Cat5'
comment_text = 'comment1'

# expected results for tests
new_button_without_number = ['', comment_text, '', all_categories]
new_button_with_number = ['32', comment_text, '', all_categories]
new_button_length_50 = ['', '12345678901234567890123456789012345678901234567890', '', all_categories]
new_button_number_999 = ['999', comment_text, '', all_categories]

duplicate_button_with_number = ['53', 'Copy of Comment Text 0', '', 'Cat0']
duplicate_button_without_number = ['', 'Copy of Comment Text 0', '', 'Cat0']

edit_button_with_number = ['32', comment_text, '', 'Cat0']
edit_button_without_number = ['', comment_text, '', 'Cat0']

symbols = ['.', '!', '@', '#', '$', '%', '{', '}', '[', ']', '&',
           '?', '=', '+', '-', '/', ':', ';', ',', '(', ')']

error_massage_not_alphanumeric = 'The Comment Text field should contain alphanumeric characters only'
