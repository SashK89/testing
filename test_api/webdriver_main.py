from autoriafolder.autoria import AutoRiaMainPage

def test_found_moto_section():
    page = AutoRiaMainPage()
    page.search_items_moto()
    assert page.show_items() > 0

#test_found_moto_section()