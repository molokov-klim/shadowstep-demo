from applications.android_settings.android_settings import AndroidSettings


def test_debug(android_app: AndroidSettings):
    app = android_app
    app.open()
    app.shadowstep.navigator.navigate(from_page=app.page_settings,
                                      to_page=app.page_opening_links)
    assert app.page_opening_links.is_current_page()

    assert app.page_opening_links.instant_apps_switch.checked == 'true'
    
    assert app.page_opening_links.instant_apps_summary.text == 'Open links in apps,djhkfjhkfdjhjkdn even if they’re not installed'
