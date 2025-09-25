import logging
from typing import Any
from shadowstep.decorators.decorators import current_page
from shadowstep.element.element import Element
from shadowstep.page_base import PageBaseShadowstep


class PageWallpaper(PageBaseShadowstep):

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
        return "Wallpaper"

    @property
    def title(self) -> Element:
        return self.shadowstep.get_element({
        'content-desc': 'Choose wallpaper from',
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
    def gallery(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'Gallery',
            'resource-id': 'android:id/title',
            'class': 'android.widget.TextView'
        })

    @property
    def live_wallpapers(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'Live Wallpapers',
            'resource-id': 'android:id/title',
            'class': 'android.widget.TextView'
        })

    @property
    def wallpapers(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'Wallpapers',
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
