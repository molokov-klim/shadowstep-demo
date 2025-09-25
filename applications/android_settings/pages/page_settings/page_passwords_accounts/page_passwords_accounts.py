import logging
from typing import Any
from shadowstep.decorators.decorators import current_page
from shadowstep.element.element import Element
from shadowstep.page_base import PageBaseShadowstep


class PagePasswordsAccounts(PageBaseShadowstep):

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
        return "Passwords & accounts"

    @property
    def title(self) -> Element:
        return self.shadowstep.get_element({
        'content-desc': 'Passwords & accounts',
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
    def passwords_passkeys_and_data_services(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'Passwords, passkeys and data services',
            'resource-id': 'android:id/title',
            'class': 'android.widget.TextView'
        })

    @property
    def none(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'None',
            'resource-id': 'android:id/title',
            'class': 'android.widget.TextView'
        })

    @property
    def accounts_for_owner_1(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'Accounts for Owner',
            'resource-id': 'android:id/title',
            'class': 'android.widget.TextView'
        })

    @property
    def add_account(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'Add account',
            'resource-id': 'android:id/title',
            'class': 'android.widget.TextView'
        })

    @property
    def automatically_sync_app_data(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'Automatically sync app data',
            'resource-id': 'android:id/title',
            'class': 'android.widget.TextView'
        })

    @property
    def automatically_sync_app_data_switch(self) -> Element:
        return self.automatically_sync_app_data.get_cousin(
            {
            'resource-id': 'android:id/switch_widget',
            'class': 'android.widget.Switch'
        })

    @property
    def automatically_sync_app_data_summary(self) -> Element:
        return self.automatically_sync_app_data.get_sibling({
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
