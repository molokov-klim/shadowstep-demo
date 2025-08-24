import logging
from typing import Any
from shadowstep.decorators.decorators import current_page
from shadowstep.element.element import Element
from shadowstep.page_base import PageBaseShadowstep


class PageApps(PageBaseShadowstep):

    def __init__(self) -> None:
        super().__init__()
        self.logger = logging.getLogger(__name__)

    def __repr__(self) -> str:
        return f"{self.name} ({self.__class__.__name__})"

    @property
    def edges(self) -> dict[str, Any]:
        return {"PageSettings": self.to_settings,
                "PageDefaultApps": self.to_default_apps}
    
    def to_default_apps(self):
        self.default_apps.tap()
        return self.shadowstep.get_page("PageDefaultApps") 

    def to_settings(self):
        self.shadowstep.terminal.press_back()
        return self.shadowstep.get_page("PageSettings")

    @property
    def name(self) -> str:
        return "Apps"

    @property
    def title(self) -> Element:
        return self.shadowstep.get_element({
        'content-desc': 'Apps',
        'resource-id': 'com.android.settings:id/collapsing_toolbar',
        'class': 'android.widget.FrameLayout'
    })

    @property
    def navigate_up(self) -> Element:
        return self.recycler.scroll_to_element({
            'content-desc': 'Navigate up',
            'class': 'android.widget.ImageButton'
        })

    @property
    def recently_opened_apps(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'Recently opened apps',
            'resource-id': 'android:id/title',
            'class': 'android.widget.TextView'
        })

    @property
    def see_all_18_apps(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'See all 18 apps',
            'resource-id': 'android:id/title',
            'class': 'android.widget.TextView'
        })

    @property
    def general(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'General',
            'resource-id': 'android:id/title',
            'class': 'android.widget.TextView'
        })

    @property
    def search(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'Search',
            'resource-id': 'android:id/title',
            'class': 'android.widget.TextView'
        })

    @property
    def search_summary(self) -> Element:
        return self.search.get_sibling({
            'resource-id': 'android:id/summary'
        })

    @property
    def phone(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'Phone',
            'resource-id': 'android:id/title',
            'class': 'android.widget.TextView'
        })

    @property
    def phone_summary(self) -> Element:
        return self.phone.get_sibling({
            'resource-id': 'android:id/summary'
        })

    @property
    def appium_settings(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'Appium Settings',
            'resource-id': 'android:id/title',
            'class': 'android.widget.TextView'
        })

    @property
    def appium_settings_summary(self) -> Element:
        return self.appium_settings.get_sibling({
            'resource-id': 'android:id/summary'
        })

    @property
    def gallery(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'Gallery',
            'resource-id': 'android:id/title',
            'class': 'android.widget.TextView'
        })

    @property
    def gallery_summary(self) -> Element:
        return self.gallery.get_sibling({
            'resource-id': 'android:id/summary'
        })

    @property
    def phone_summary_1(self) -> Element:
        return self.phone.get_sibling({
            'resource-id': 'android:id/summary'
        })

    @property
    def default_apps(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'Default apps',
            'resource-id': 'android:id/title',
            'class': 'android.widget.TextView'
        })

    @property
    def default_apps_summary(self) -> Element:
        return self.default_apps.get_sibling({
            'resource-id': 'android:id/summary'
        })

    @property
    def unused_apps(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'Unused apps',
            'resource-id': 'android:id/title',
            'class': 'android.widget.TextView'
        })

    @property
    def unused_apps_summary(self) -> Element:
        return self.unused_apps.get_sibling({
            'resource-id': 'android:id/summary'
        })

    @property
    def special_app_access(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'Special app access',
            'resource-id': 'android:id/title',
            'class': 'android.widget.TextView'
        })

    @property
    def special_app_access_summary(self) -> Element:
        return self.special_app_access.get_sibling({
            'resource-id': 'android:id/summary'
        })

    @property
    def recycler(self) -> Element:
        return self.shadowstep.get_element({
            'resource-id': 'com.android.settings:id/content_parent',
            'class': 'android.widget.ScrollView'
        })

    @current_page()
    def is_current_page(self) -> bool:
        try:
            return self.title.is_visible()
        except Exception as error:
            self.logger.error(error)
            return False
