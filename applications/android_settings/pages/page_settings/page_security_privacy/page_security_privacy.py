import logging
from typing import Any
from shadowstep.decorators.decorators import current_page
from shadowstep.element.element import Element
from shadowstep.page_base import PageBaseShadowstep


class PageSecurityPrivacy(PageBaseShadowstep):

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
        return "Security & privacy"

    @property
    def title(self) -> Element:
        return self.shadowstep.get_element({
        'content-desc': 'Security & privacy',
        'resource-id': 'com.android.permissioncontroller:id/collapsing_toolbar',
        'class': 'android.widget.FrameLayout'
    })

    @property
    def app_bar(self) -> Element:
        return self.recycler.scroll_to_element({
            'resource-id': 'com.android.permissioncontroller:id/app_bar',
            'class': 'android.widget.LinearLayout'
        })

    @property
    def action_bar(self) -> Element:
        return self.recycler.scroll_to_element({
            'resource-id': 'com.android.permissioncontroller:id/action_bar',
            'class': 'android.view.ViewGroup'
        })

    @property
    def navigate_up(self) -> Element:
        return self.recycler.scroll_to_element({
            'content-desc': 'Navigate up',
            'class': 'android.widget.ImageButton'
        })

    @property
    def content_frame(self) -> Element:
        return self.recycler.scroll_to_element({
            'resource-id': 'com.android.permissioncontroller:id/content_frame',
            'class': 'android.widget.FrameLayout'
        })

    @property
    def fragment_container(self) -> Element:
        return self.recycler.scroll_to_element({
            'resource-id': 'com.android.permissioncontroller:id/fragment_container',
            'class': 'android.widget.FrameLayout'
        })

    @property
    def security_and_privacy_status_device(self) -> Element:
        return self.recycler.scroll_to_element({
            'content-desc': 'Security and privacy status. Device may be at risk. See alert',
            'resource-id': 'com.android.permissioncontroller:id/status_title_and_summary',
            'class': 'android.widget.LinearLayout'
        })

    @property
    def device_may_be_at_risk(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'Device may be at risk',
            'resource-id': 'com.android.permissioncontroller:id/status_title',
            'class': 'android.widget.TextView'
        })

    @property
    def see_alert(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'See alert',
            'resource-id': 'com.android.permissioncontroller:id/status_summary',
            'class': 'android.widget.TextView'
        })

    @property
    def device_unlock(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'Device unlock',
            'content-desc': 'Alert. Device unlock',
            'resource-id': 'com.android.permissioncontroller:id/issue_card_attribution_title',
            'class': 'android.widget.TextView'
        })

    @property
    def dismiss(self) -> Element:
        return self.recycler.scroll_to_element({
            'content-desc': 'Dismiss',
            'resource-id': 'com.android.permissioncontroller:id/issue_card_dismiss_btn',
            'class': 'android.widget.ImageButton'
        })

    @property
    def set_a_screen_lock(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'Set a screen lock',
            'resource-id': 'com.android.permissioncontroller:id/issue_card_title',
            'class': 'android.widget.TextView'
        })

    @property
    def for_added_security_set_a(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'For added security, set a PIN, pattern, or password for this device.',
            'resource-id': 'com.android.permissioncontroller:id/issue_card_summary',
            'class': 'android.widget.TextView'
        })

    @property
    def issue_card_action_button_list(self) -> Element:
        return self.recycler.scroll_to_element({
            'resource-id': 'com.android.permissioncontroller:id/issue_card_action_button_list',
            'class': 'android.widget.LinearLayout'
        })

    @property
    def set_screen_lock(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'Set screen lock',
            'class': 'android.widget.Button'
        })

    @property
    def settings(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'Settings',
            'resource-id': 'android:id/title',
            'class': 'android.widget.TextView'
        })

    @property
    def device_unlock_1(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'Device unlock',
            'resource-id': 'android:id/title',
            'class': 'android.widget.TextView'
        })

    @property
    def device_unlock_1_summary(self) -> Element:
        return self.device_unlock_1.get_sibling({
            'resource-id': 'android:id/summary'
        })

    @property
    def other_settings(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'Other settings',
            'resource-id': 'android:id/title',
            'class': 'android.widget.TextView'
        })

    @property
    def privacy(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'Privacy',
            'resource-id': 'android:id/title',
            'class': 'android.widget.TextView'
        })

    @property
    def privacy_summary(self) -> Element:
        return self.privacy.get_sibling({
            'resource-id': 'android:id/summary'
        })

    @property
    def more_security_privacy(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'More security & privacy',
            'resource-id': 'android:id/title',
            'class': 'android.widget.TextView'
        })

    @property
    def more_security_privacy_summary(self) -> Element:
        return self.more_security_privacy.get_sibling({
            'resource-id': 'android:id/summary'
        })

    @property
    def recycler(self) -> Element:
        return self.shadowstep.get_element({
            'resource-id': 'com.android.permissioncontroller:id/content_parent',
            'class': 'android.widget.ScrollView'
        })

    @current_page()
    def is_current_page(self) -> bool:
        try:
            return self.title.is_visible()
        except Exception as error:
            self.logger.error(error)
            return False
