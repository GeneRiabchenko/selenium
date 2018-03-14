def find_all_comments(browser):
        comments_list = list()
        footer = browser.find_element_by_class_name("webgrid-footer")
        links = footer.find_elements_by_tag_name("a")
        pages_links = set()
        for page in links:
            pages_links.add(page.get_attribute("href"))

        columns_list = browser.find_elements_by_class_name('webgrid-row-style')
        columns_list += browser.find_elements_by_class_name('webgrid-alternating-row')
        for column in columns_list:
            comment = list()
            comment_number = column.find_element_by_class_name('numbercolumn').text
            comment.append(comment_number)
            comment_text = column.find_element_by_class_name('textcolumn').text
            comment.append(comment_text)
            comment_inactive = column.find_element_by_class_name('inactivecolumn').text
            comment.append(comment_inactive)
            comment_category = column.find_element_by_class_name('categorycolumn').text
            comment.append(comment_category)
            comments_list.append(comment)

        for page in pages_links:
            browser.get(page)
            columns_list = browser.find_elements_by_class_name('webgrid-row-style')
            columns_list += browser.find_elements_by_class_name('webgrid-alternating-row')
            for column in columns_list:
                comment = list()
                comment_number = column.find_element_by_class_name('numbercolumn').text
                comment.append(comment_number)
                comment_text = column.find_element_by_class_name('textcolumn').text
                comment.append(comment_text)
                comment_inactive = column.find_element_by_class_name('inactivecolumn').text
                comment.append(comment_inactive)
                comment_category = column.find_element_by_class_name('categorycolumn').text
                comment.append(comment_category)
                comments_list.append(comment)
        return comments_list


def save_button_click(browser):
        button = browser.find_element_by_xpath('//*[@id="editor-navigation"]/input[1]')
        button.click()


def click_return_button(browser):
        return_button = browser.find_element_by_xpath('//*[@id="logindisplay"]/a')
        return_button.click()


def click_all_category(browser):
        category = browser.find_element_by_name('AllSelect')
        category.click()


def click_save_and_return(browser):
        save_button = browser.find_element_by_xpath('//*[@id="editor-navigation"]/input[2]')
        save_button.click()


def click_delete_button(browser):
    save_button = browser.find_element_by_xpath('//*[@id="command-navigation"]/input[3]')
    save_button.click()


def select_category(browser, category_number):
        category = browser.find_elements_by_id(
                'Categories')
        # find checkbox cat0
        category[category_number].click()


def comment_text_write(browser, comment_name):
        comment = browser.find_element_by_xpath('//*[@id="Text"]')
        comment.click()
        comment.send_keys(comment_name)


def enter_number(browser, number):
        comment_number = browser.find_element_by_id('Number')
        comment_number.clear()
        comment_number.send_keys(number)


def choose_first_comment(browser):
        comment_to_change = browser.find_element_by_xpath(
            '//*[@id="main"]/div/div[5]/form/table/tbody/tr[1]/td[1]/input[1]')
        comment_to_change.click()


def choose_first_comment_duplicate(browser):
        comment_to_change = browser.find_element_by_xpath(
            '//*[@id="main"]/div/div[5]/form/table/tbody/tr[1]/td[1]/input[1]')
        comment_to_change.click()
        edit_button = browser.find_element_by_xpath('//*[@id="command-navigation"]/input[1]')
        edit_button.click()


def choose_first_comment_edit(browser):
        comment_to_change = browser.find_element_by_xpath(
            '//*[@id="main"]/div/div[5]/form/table/tbody/tr[1]/td[1]/input[1]')
        comment_to_change.click()
        # click to edit button
        edit_button = browser.find_element_by_xpath('//*[@id="command-navigation"]/input[2]')
        edit_button.click()










