import logging
from typing import Any
from shadowstep.decorators.decorators import current_page
from shadowstep.element.element import Element
from shadowstep.page_base import PageBaseShadowstep


class PageOpeningLinks(PageBaseShadowstep):

    def __init__(self) -> None:
        super().__init__()
        self.logger = logging.getLogger(__name__)

    def __repr__(self) -> str:
        return f"{self.name} ({self.__class__.__name__})"

    @property
    def edges(self) -> dict[str, Any]:
        return {"PageDefaultApps": self.to_default_apps}
    
    def to_default_apps(self):
        self.shadowstep.terminal.press_back()
        return self.shadowstep.get_page("PageDefaultApps")

    @property
    def name(self) -> str:
        return "Opening links"

    @property
    def title(self) -> Element:
        return self.shadowstep.get_element({
        'content-desc': 'Opening links',
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
    def installed_apps(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'Installed apps',
            'resource-id': 'android:id/title',
            'class': 'android.widget.TextView'
        })

    @property
    def instant_apps(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'Instant apps',
            'resource-id': 'android:id/title',
            'class': 'android.widget.TextView'
        })

    @property
    def instant_apps_switch(self) -> Element:
        return self.instant_apps.get_cousin(
            {
            'resource-id': 'android:id/switch_widget',
            'class': 'android.widget.Switch'
        })

    @property
    def instant_apps_summary(self) -> Element:
        return self.instant_apps.get_sibling({
            'resource-id': 'android:id/summary'
        })

    @property
    def android_open_source_music_player(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'Android Open Source Music Player',
            'resource-id': 'android:id/title',
            'class': 'android.widget.TextView'
        })

    @property
    def android_open_source_music_player_summary(self) -> Element:
        return self.android_open_source_music_player.get_sibling({
            'resource-id': 'android:id/summary'
        })

    @property
    def calendar(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'Calendar',
            'resource-id': 'android:id/title',
            'class': 'android.widget.TextView'
        })

    @property
    def calendar_summary(self) -> Element:
        return self.calendar.get_sibling({
            'resource-id': 'android:id/summary'
        })

    @property
    def carrierdefaultapp(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'CarrierDefaultApp',
            'resource-id': 'android:id/title',
            'class': 'android.widget.TextView'
        })

    @property
    def carrierdefaultapp_summary(self) -> Element:
        return self.carrierdefaultapp.get_sibling({
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
    def webview_shell(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'WebView Shell',
            'resource-id': 'android:id/title',
            'class': 'android.widget.TextView'
        })

    @property
    def webview_shell_summary(self) -> Element:
        return self.webview_shell.get_sibling({
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
