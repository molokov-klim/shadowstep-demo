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
        return {}

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
    def all_apps(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'All apps',
            'resource-id': 'android:id/title',
            'class': 'android.widget.TextView'
        })

    @property
    def all_apps_summary(self) -> Element:
        return self.all_apps.get_sibling({
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
    def app_battery_usage(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'App battery usage',
            'resource-id': 'android:id/title',
            'class': 'android.widget.TextView'
        })

    @property
    def app_battery_usage_summary(self) -> Element:
        return self.app_battery_usage.get_sibling({
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
