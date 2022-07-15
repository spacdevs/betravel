def test_visitors_view_home_page_successfully(browser):
    browser.visit('/')

    assert browser.status_code == 200
    assert browser.is_text_present('Olá, Flask!')