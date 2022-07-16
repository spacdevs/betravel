def test_visitors_view_home_page_successfully(browser):
    browser.visit("/")

    assert browser.status_code == 200
    assert browser.is_text_present("Viagens")
    assert browser.is_text_present("&COPY; Todos os direitos reservados. Be Travel 2022")

def test_visitors_view_menu(browser):
    browser.visit("/")

    assert browser.is_text_present("Be Travel")
    assert browser.is_text_present("Nova Postagem")
    assert browser.is_text_present("Nova Categoria")
    assert browser.is_text_present("Entrar")
    assert browser.is_text_present("Olá, Marcus Pereira")
    assert browser.is_text_present("Sair")