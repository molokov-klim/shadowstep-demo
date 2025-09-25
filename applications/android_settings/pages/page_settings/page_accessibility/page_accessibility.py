import logging
from typing import Any
from shadowstep.decorators.decorators import current_page
from shadowstep.element.element import Element
from shadowstep.page_base import PageBaseShadowstep


class PageAccessibility(PageBaseShadowstep):

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
        return "Accessibility"

    @property
    def title(self) -> Element:
        return self.shadowstep.get_element({
        'content-desc': 'Accessibility',
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
    def display(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'Display',
            'resource-id': 'android:id/title',
            'class': 'android.widget.TextView'
        })

    @property
    def display_size_and_text(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'Display size and text',
            'resource-id': 'android:id/title',
            'class': 'android.widget.TextView'
        })

    @property
    def color_and_motion(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'Color and motion',
            'resource-id': 'android:id/title',
            'class': 'android.widget.TextView'
        })

    @property
    def interaction_controls(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'Interaction controls',
            'resource-id': 'android:id/title',
            'class': 'android.widget.TextView'
        })

    @property
    def timing_controls(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'Timing controls',
            'resource-id': 'android:id/title',
            'class': 'android.widget.TextView'
        })

    @property
    def system_controls(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'System controls',
            'resource-id': 'android:id/title',
            'class': 'android.widget.TextView'
        })

    @property
    def magnification(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'Magnification',
            'resource-id': 'android:id/title',
            'class': 'android.widget.TextView'
        })

    @property
    def magnification_summary(self) -> Element:
        return self.magnification.get_sibling({
            'resource-id': 'android:id/summary'
        })

    @property
    def accessibility_menu(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'Accessibility Menu',
            'resource-id': 'android:id/title',
            'class': 'android.widget.TextView'
        })

    @property
    def accessibility_menu_summary(self) -> Element:
        return self.accessibility_menu.get_sibling({
            'resource-id': 'android:id/summary'
        })

    @property
    def captions(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'Captions',
            'resource-id': 'android:id/title',
            'class': 'android.widget.TextView'
        })

    @property
    def audio(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'Audio',
            'resource-id': 'android:id/title',
            'class': 'android.widget.TextView'
        })

    @property
    def audio_description(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'Audio description',
            'resource-id': 'android:id/title',
            'class': 'android.widget.TextView'
        })

    @property
    def audio_description_switch(self) -> Element:
        return self.audio_description.get_cousin(
            {
            'resource-id': 'android:id/switch_widget',
            'class': 'android.widget.Switch'
        })

    @property
    def caption_preferences(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'Caption preferences',
            'resource-id': 'android:id/title',
            'class': 'android.widget.TextView'
        })

    @property
    def caption_preferences_summary(self) -> Element:
        return self.caption_preferences.get_sibling({
            'resource-id': 'android:id/summary'
        })

    @property
    def audio_description_summary(self) -> Element:
        return self.audio_description.get_sibling({
            'resource-id': 'android:id/summary'
        })

    @property
    def audio_adjustment(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'Audio adjustment',
            'resource-id': 'android:id/title',
            'class': 'android.widget.TextView'
        })

    @property
    def flash_notifications(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'Flash notifications',
            'resource-id': 'android:id/title',
            'class': 'android.widget.TextView'
        })

    @property
    def flash_notifications_summary(self) -> Element:
        return self.flash_notifications.get_sibling({
            'resource-id': 'android:id/summary'
        })

    @property
    def hearing_devices(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'Hearing devices',
            'resource-id': 'android:id/title',
            'class': 'android.widget.TextView'
        })

    @property
    def hearing_devices_summary(self) -> Element:
        return self.hearing_devices.get_sibling({
            'resource-id': 'android:id/summary'
        })

    @property
    def general(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'General',
            'resource-id': 'android:id/title',
            'class': 'android.widget.TextView'
        })

    @property
    def accessibility_shortcuts(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'Accessibility shortcuts',
            'resource-id': 'android:id/title',
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
