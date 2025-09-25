import logging
from typing import Any
from shadowstep.decorators.decorators import current_page
from shadowstep.element.element import Element
from shadowstep.page_base import PageBaseShadowstep


class PageBattery(PageBaseShadowstep):

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
        return "Battery"

    @property
    def title(self) -> Element:
        return self.shadowstep.get_element({
        'content-desc': 'Battery',
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
    def num_100(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': '100 %',
            'resource-id': 'com.android.settings:id/usage_summary',
            'class': 'android.widget.TextView'
        })

    @property
    def progress(self) -> Element:
        return self.recycler.scroll_to_element({
            'resource-id': 'android:id/progress',
            'class': 'android.widget.ProgressBar'
        })

    @property
    def charged(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'Charged',
            'resource-id': 'com.android.settings:id/bottom_summary',
            'class': 'android.widget.TextView'
        })

    @property
    def remaining_battery_life_is_approximate(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'Remaining battery life is approximate and can change based on usage',
            'resource-id': 'android:id/title',
            'class': 'android.widget.TextView'
        })

    @property
    def battery_percentage(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'Battery percentage',
            'resource-id': 'android:id/title',
            'class': 'android.widget.TextView'
        })

    @property
    def battery_percentage_switch(self) -> Element:
        return self.battery_percentage.get_cousin(
            {
            'resource-id': 'android:id/switch_widget',
            'class': 'android.widget.Switch'
        })

    @property
    def battery_usage(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'Battery usage',
            'resource-id': 'android:id/title',
            'class': 'android.widget.TextView'
        })

    @property
    def battery_usage_summary(self) -> Element:
        return self.battery_usage.get_sibling({
            'resource-id': 'android:id/summary'
        })

    @property
    def battery_saver(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'Battery Saver',
            'resource-id': 'android:id/title',
            'class': 'android.widget.TextView'
        })

    @property
    def battery_saver_summary(self) -> Element:
        return self.battery_saver.get_sibling({
            'resource-id': 'android:id/summary'
        })

    @property
    def battery_percentage_summary(self) -> Element:
        return self.battery_percentage.get_sibling({
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
