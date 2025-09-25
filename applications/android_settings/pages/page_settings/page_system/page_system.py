import logging
from typing import Any
from shadowstep.decorators.decorators import current_page
from shadowstep.element.element import Element
from shadowstep.page_base import PageBaseShadowstep


class PageSystem(PageBaseShadowstep):

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
        return "System"

    @property
    def title(self) -> Element:
        return self.shadowstep.get_element({
        'content-desc': 'System',
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
    def gestures(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'Gestures',
            'resource-id': 'android:id/title',
            'class': 'android.widget.TextView'
        })

    @property
    def backup(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'Backup',
            'resource-id': 'android:id/title',
            'class': 'android.widget.TextView'
        })

    @property
    def developer_options(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'Developer options',
            'resource-id': 'android:id/title',
            'class': 'android.widget.TextView'
        })

    @property
    def languages(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'Languages',
            'resource-id': 'android:id/title',
            'class': 'android.widget.TextView'
        })

    @property
    def languages_summary(self) -> Element:
        return self.languages.get_sibling({
            'resource-id': 'android:id/summary'
        })

    @property
    def keyboard(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'Keyboard',
            'resource-id': 'android:id/title',
            'class': 'android.widget.TextView'
        })

    @property
    def keyboard_summary(self) -> Element:
        return self.keyboard.get_sibling({
            'resource-id': 'android:id/summary'
        })

    @property
    def date_time(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'Date & time',
            'resource-id': 'android:id/title',
            'class': 'android.widget.TextView'
        })

    @property
    def date_time_summary(self) -> Element:
        return self.date_time.get_sibling({
            'resource-id': 'android:id/summary'
        })

    @property
    def multiple_users(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'Multiple users',
            'resource-id': 'android:id/title',
            'class': 'android.widget.TextView'
        })

    @property
    def multiple_users_summary(self) -> Element:
        return self.multiple_users.get_sibling({
            'resource-id': 'android:id/summary'
        })

    @property
    def reset_options(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'Reset options',
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
