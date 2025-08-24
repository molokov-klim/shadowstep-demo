import logging
from typing import Any
from shadowstep.decorators.decorators import current_page
from shadowstep.element.element import Element
from shadowstep.page_base import PageBaseShadowstep


class PageDefaultApps(PageBaseShadowstep):

    def __init__(self) -> None:
        super().__init__()
        self.logger = logging.getLogger(__name__)

    def __repr__(self) -> str:
        return f"{self.name} ({self.__class__.__name__})"

    @property
    def edges(self) -> dict[str, Any]:
        return {"PageApps": self.to_apps,
                "PageOpeningLinks": self.to_opening_links}
    
    def to_opening_links(self):
        self.opening_links.tap()
        self.title.wait_for_not(timeout=10)
        return self.shadowstep.get_page("PageOpeningLinks")

    def to_apps(self):
        self.shadowstep.terminal.press_back()
        return self.shadowstep.get_page("PageApps")

    @property
    def name(self) -> str:
        return "Default apps"

    @property
    def title(self) -> Element:
        return self.shadowstep.get_element({
        'content-desc': 'Default apps',
        'resource-id': 'com.android.permissioncontroller:id/collapsing_toolbar',
        'class': 'android.widget.FrameLayout'
    })

    @property
    def app_bar(self) -> Element:
        return self.recycler.scroll_to_element({
            'resource-id': 'com.android.permissioncontroller:id/app_bar',
            'class': 'android.widget.LinearLayout'
        })

    @property
    def action_bar(self) -> Element:
        return self.recycler.scroll_to_element({
            'resource-id': 'com.android.permissioncontroller:id/action_bar',
            'class': 'android.view.ViewGroup'
        })

    @property
    def navigate_up(self) -> Element:
        return self.recycler.scroll_to_element({
            'content-desc': 'Navigate up',
            'class': 'android.widget.ImageButton'
        })

    @property
    def content_frame(self) -> Element:
        return self.recycler.scroll_to_element({
            'resource-id': 'com.android.permissioncontroller:id/content_frame',
            'class': 'android.widget.FrameLayout'
        })

    @property
    def preference_fragment_container(self) -> Element:
        return self.recycler.scroll_to_element({
            'resource-id': 'com.android.permissioncontroller:id/preference_fragment_container',
            'class': 'android.widget.FrameLayout'
        })

    @property
    def settings(self) -> Element:
        return self.recycler.scroll_to_element({
            'content-desc': 'Settings',
            'resource-id': 'com.android.permissioncontroller:id/settings_button',
            'class': 'android.widget.ImageButton'
        })

    @property
    def opening_links(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'Opening links',
            'resource-id': 'android:id/title',
            'class': 'android.widget.TextView'
        })

    @property
    def browser_app(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'Browser app',
            'resource-id': 'android:id/title',
            'class': 'android.widget.TextView'
        })

    @property
    def browser_app_summary(self) -> Element:
        return self.browser_app.get_sibling({
            'resource-id': 'android:id/summary'
        })

    @property
    def home_app(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'Home app',
            'resource-id': 'android:id/title',
            'class': 'android.widget.TextView'
        })

    @property
    def home_app_summary(self) -> Element:
        return self.home_app.get_sibling({
            'resource-id': 'android:id/summary'
        })

    @property
    def phone_app(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'Phone app',
            'resource-id': 'android:id/title',
            'class': 'android.widget.TextView'
        })

    @property
    def phone_app_summary(self) -> Element:
        return self.phone_app.get_sibling({
            'resource-id': 'android:id/summary'
        })

    @property
    def sms_app(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'SMS app',
            'resource-id': 'android:id/title',
            'class': 'android.widget.TextView'
        })

    @property
    def sms_app_summary(self) -> Element:
        return self.sms_app.get_sibling({
            'resource-id': 'android:id/summary'
        })

    @property
    def recycler(self) -> Element:
        return self.shadowstep.get_element({
            'resource-id': 'com.android.permissioncontroller:id/content_parent',
            'class': 'android.widget.ScrollView'
        })

    @current_page()
    def is_current_page(self) -> bool:
        try:
            return self.title.is_visible()
        except Exception as error:
            self.logger.error(error)
            return False
