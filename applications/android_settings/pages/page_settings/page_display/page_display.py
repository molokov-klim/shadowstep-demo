import logging
from typing import Any
from shadowstep.decorators.decorators import current_page
from shadowstep.element.element import Element
from shadowstep.page_base import PageBaseShadowstep


class PageDisplay(PageBaseShadowstep):

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
        return "Display"

    @property
    def title(self) -> Element:
        return self.shadowstep.get_element({
        'content-desc': 'Display',
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
    def brightness(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'Brightness',
            'resource-id': 'android:id/title',
            'class': 'android.widget.TextView'
        })

    @property
    def lock_display(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'Lock display',
            'resource-id': 'android:id/title',
            'class': 'android.widget.TextView'
        })

    @property
    def appearance(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'Appearance',
            'resource-id': 'android:id/title',
            'class': 'android.widget.TextView'
        })

    @property
    def dark_theme(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'Dark theme',
            'resource-id': 'android:id/title',
            'class': 'android.widget.TextView'
        })

    @property
    def dark_theme_switch(self) -> Element:
        return self.dark_theme.get_cousin(
            {
            'content-desc': 'Dark theme',
            'resource-id': 'com.android.settings:id/switchWidget',
            'class': 'android.widget.Switch'
        })

    @property
    def brightness_level(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'Brightness level',
            'resource-id': 'android:id/title',
            'class': 'android.widget.TextView'
        })

    @property
    def brightness_level_summary(self) -> Element:
        return self.brightness_level.get_sibling({
            'resource-id': 'android:id/summary'
        })

    @property
    def lock_screen(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'Lock screen',
            'resource-id': 'android:id/title',
            'class': 'android.widget.TextView'
        })

    @property
    def lock_screen_summary(self) -> Element:
        return self.lock_screen.get_sibling({
            'resource-id': 'android:id/summary'
        })

    @property
    def screen_timeout(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'Screen timeout',
            'resource-id': 'android:id/title',
            'class': 'android.widget.TextView'
        })

    @property
    def screen_timeout_summary(self) -> Element:
        return self.screen_timeout.get_sibling({
            'resource-id': 'android:id/summary'
        })

    @property
    def dark_theme_summary(self) -> Element:
        return self.dark_theme.get_sibling({
            'resource-id': 'android:id/summary'
        })

    @property
    def display_size_and_text(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'Display size and text',
            'resource-id': 'android:id/title',
            'class': 'android.widget.TextView'
        })

    @property
    def color(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'Color',
            'resource-id': 'android:id/title',
            'class': 'android.widget.TextView'
        })

    @property
    def colors(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'Colors',
            'resource-id': 'android:id/title',
            'class': 'android.widget.TextView'
        })

    @property
    def other_display_controls(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'Other display controls',
            'resource-id': 'android:id/title',
            'class': 'android.widget.TextView'
        })

    @property
    def auto_rotate_screen(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'Auto-rotate screen',
            'resource-id': 'android:id/title',
            'class': 'android.widget.TextView'
        })

    @property
    def auto_rotate_screen_switch(self) -> Element:
        return self.auto_rotate_screen.get_cousin(
            {
            'resource-id': 'android:id/switch_widget',
            'class': 'android.widget.Switch'
        })

    @property
    def screen_saver(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'Screen saver',
            'resource-id': 'android:id/title',
            'class': 'android.widget.TextView'
        })

    @property
    def screen_saver_summary(self) -> Element:
        return self.screen_saver.get_sibling({
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
