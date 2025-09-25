import logging
from typing import Any
from shadowstep.decorators.decorators import current_page
from shadowstep.element.element import Element
from shadowstep.page_base import PageBaseShadowstep


class PageStorage(PageBaseShadowstep):

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
        return "Storage"

    @property
    def title(self) -> Element:
        return self.shadowstep.get_element({
        'content-desc': 'Storage',
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
    def num_19_gb_used(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': '19 GB used',
            'resource-id': 'com.android.settings:id/usage_summary',
            'class': 'android.widget.TextView'
        })

    @property
    def num_32_gb_total(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': '32 GB total',
            'resource-id': 'com.android.settings:id/total_summary',
            'class': 'android.widget.TextView'
        })

    @property
    def progress(self) -> Element:
        return self.recycler.scroll_to_element({
            'resource-id': 'android:id/progress',
            'class': 'android.widget.ProgressBar'
        })

    @property
    def progress_1(self) -> Element:
        return self.recycler.scroll_to_element({
            'resource-id': 'android:id/progress',
            'class': 'android.widget.ProgressBar'
        })

    @property
    def storage_manager(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'Storage manager',
            'resource-id': 'android:id/title',
            'class': 'android.widget.TextView'
        })

    @property
    def storage_manager_switch(self) -> Element:
        return self.storage_manager.get_cousin(
            {
            'content-desc': 'Storage manager',
            'resource-id': 'com.android.settings:id/switchWidget',
            'class': 'android.widget.Switch'
        })

    @property
    def free_up_space(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'Free up space',
            'resource-id': 'android:id/title',
            'class': 'android.widget.TextView'
        })

    @property
    def free_up_space_summary(self) -> Element:
        return self.free_up_space.get_sibling({
            'resource-id': 'android:id/summary'
        })

    @property
    def system(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'System',
            'resource-id': 'android:id/title',
            'class': 'android.widget.TextView'
        })

    @property
    def system_summary(self) -> Element:
        return self.system.get_sibling({
            'resource-id': 'android:id/summary'
        })

    @property
    def apps(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'Apps',
            'resource-id': 'android:id/title',
            'class': 'android.widget.TextView'
        })

    @property
    def apps_summary(self) -> Element:
        return self.apps.get_sibling({
            'resource-id': 'android:id/summary'
        })

    @property
    def trash(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'Trash',
            'resource-id': 'android:id/title',
            'class': 'android.widget.TextView'
        })

    @property
    def trash_summary(self) -> Element:
        return self.trash.get_sibling({
            'resource-id': 'android:id/summary'
        })

    @property
    def documents_other(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'Documents & other',
            'resource-id': 'android:id/title',
            'class': 'android.widget.TextView'
        })

    @property
    def documents_other_summary(self) -> Element:
        return self.documents_other.get_sibling({
            'resource-id': 'android:id/summary'
        })

    @property
    def games(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'Games',
            'resource-id': 'android:id/title',
            'class': 'android.widget.TextView'
        })

    @property
    def games_summary(self) -> Element:
        return self.games.get_sibling({
            'resource-id': 'android:id/summary'
        })

    @property
    def audio(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'Audio',
            'resource-id': 'android:id/title',
            'class': 'android.widget.TextView'
        })

    @property
    def audio_summary(self) -> Element:
        return self.audio.get_sibling({
            'resource-id': 'android:id/summary'
        })

    @property
    def videos(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'Videos',
            'resource-id': 'android:id/title',
            'class': 'android.widget.TextView'
        })

    @property
    def videos_summary(self) -> Element:
        return self.videos.get_sibling({
            'resource-id': 'android:id/summary'
        })

    @property
    def system_summary_1(self) -> Element:
        return self.system.get_sibling({
            'resource-id': 'android:id/summary'
        })

    @property
    def images(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'Images',
            'resource-id': 'android:id/title',
            'class': 'android.widget.TextView'
        })

    @property
    def images_summary(self) -> Element:
        return self.images.get_sibling({
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
