import logging
from typing import Any
from shadowstep.decorators.decorators import current_page
from shadowstep.element.element import Element
from shadowstep.page_base import PageBaseShadowstep


class PageLocation(PageBaseShadowstep):

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
        return "Location"

    @property
    def title(self) -> Element:
        return self.shadowstep.get_element({
        'content-desc': 'Location',
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
    def switch_bar(self) -> Element:
        return self.recycler.scroll_to_element({
            'resource-id': 'com.android.settings:id/switch_bar',
            'class': 'android.widget.LinearLayout'
        })

    @property
    def frame(self) -> Element:
        return self.recycler.scroll_to_element({
            'resource-id': 'com.android.settings:id/frame',
            'class': 'android.widget.LinearLayout'
        })

    @property
    def recent_access(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'Recent access',
            'resource-id': 'android:id/title',
            'class': 'android.widget.TextView'
        })

    @property
    def no_apps_recently_accessed_location(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'No apps recently accessed location',
            'resource-id': 'android:id/title',
            'class': 'android.widget.TextView'
        })

    @property
    def see_all(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'See all',
            'resource-id': 'android:id/title',
            'class': 'android.widget.TextView'
        })

    @property
    def location_services(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'Location services',
            'resource-id': 'android:id/title',
            'class': 'android.widget.TextView'
        })

    @property
    def apps_with_the_nearby_devices(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'Apps with the Nearby devices permission can determine the relative position of connected devices.',
            'resource-id': 'android:id/title',
            'class': 'android.widget.TextView'
        })

    @property
    def use_location(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'Use location',
            'resource-id': 'com.android.settings:id/switch_text',
            'class': 'android.widget.TextView'
        })

    @property
    def use_location_switch(self) -> Element:
        return self.use_location.get_cousin(
            {
            'resource-id': 'android:id/switch_widget',
            'class': 'android.widget.Switch'
        })

    @property
    def app_location_permissions(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'App location permissions',
            'resource-id': 'android:id/title',
            'class': 'android.widget.TextView'
        })

    @property
    def app_location_permissions_summary(self) -> Element:
        return self.app_location_permissions.get_sibling({
            'resource-id': 'android:id/summary'
        })

    @property
    def learn_more_about_location_settings(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'Learn more about Location Settings.',
            'resource-id': 'com.android.settings:id/settingslib_learn_more',
            'class': 'android.widget.TextView'
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
