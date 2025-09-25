import logging
from typing import Any
from shadowstep.decorators.decorators import current_page
from shadowstep.element.element import Element
from shadowstep.page_base import PageBaseShadowstep


class PageNotifications(PageBaseShadowstep):

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
        return "Notifications"

    @property
    def title(self) -> Element:
        return self.shadowstep.get_element({
        'content-desc': 'Notifications',
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
    def manage(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'Manage',
            'resource-id': 'android:id/title',
            'class': 'android.widget.TextView'
        })

    @property
    def conversation(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'Conversation',
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
    def app_notifications(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'App notifications',
            'resource-id': 'android:id/title',
            'class': 'android.widget.TextView'
        })

    @property
    def app_notifications_summary(self) -> Element:
        return self.app_notifications.get_sibling({
            'resource-id': 'android:id/summary'
        })

    @property
    def notification_history(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'Notification history',
            'resource-id': 'android:id/title',
            'class': 'android.widget.TextView'
        })

    @property
    def notification_history_summary(self) -> Element:
        return self.notification_history.get_sibling({
            'resource-id': 'android:id/summary'
        })

    @property
    def conversations(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'Conversations',
            'resource-id': 'android:id/title',
            'class': 'android.widget.TextView'
        })

    @property
    def conversations_summary(self) -> Element:
        return self.conversations.get_sibling({
            'resource-id': 'android:id/summary'
        })

    @property
    def bubbles(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'Bubbles',
            'resource-id': 'android:id/title',
            'class': 'android.widget.TextView'
        })

    @property
    def bubbles_summary(self) -> Element:
        return self.bubbles.get_sibling({
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
    def device_app_notifications(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'Device & app notifications',
            'resource-id': 'android:id/title',
            'class': 'android.widget.TextView'
        })

    @property
    def device_app_notifications_summary(self) -> Element:
        return self.device_app_notifications.get_sibling({
            'resource-id': 'android:id/summary'
        })

    @property
    def notifications_on_lock_screen(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'Notifications on lock screen',
            'resource-id': 'android:id/title',
            'class': 'android.widget.TextView'
        })

    @property
    def notifications_on_lock_screen_summary(self) -> Element:
        return self.notifications_on_lock_screen.get_sibling({
            'resource-id': 'android:id/summary'
        })

    @property
    def do_not_disturb(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'Do Not Disturb',
            'resource-id': 'android:id/title',
            'class': 'android.widget.TextView'
        })

    @property
    def do_not_disturb_summary(self) -> Element:
        return self.do_not_disturb.get_sibling({
            'resource-id': 'android:id/summary'
        })

    @property
    def wireless_emergency_alerts(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'Wireless emergency alerts',
            'resource-id': 'android:id/title',
            'class': 'android.widget.TextView'
        })

    @property
    def hide_silent_notifications_in_status(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'Hide silent notifications in status bar',
            'resource-id': 'android:id/title',
            'class': 'android.widget.TextView'
        })

    @property
    def hide_silent_notifications_in_status_switch(self) -> Element:
        return self.hide_silent_notifications_in_status.get_cousin(
            {
            'resource-id': 'android:id/switch_widget',
            'class': 'android.widget.Switch'
        })

    @property
    def allow_notification_snoozing(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'Allow notification snoozing',
            'resource-id': 'android:id/title',
            'class': 'android.widget.TextView'
        })

    @property
    def allow_notification_snoozing_switch(self) -> Element:
        return self.allow_notification_snoozing.get_cousin(
            {
            'resource-id': 'android:id/switch_widget',
            'class': 'android.widget.Switch'
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
    def notification_dot_on_app_icon(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'Notification dot on app icon',
            'resource-id': 'android:id/title',
            'class': 'android.widget.TextView'
        })

    @property
    def notification_dot_on_app_icon_switch(self) -> Element:
        return self.notification_dot_on_app_icon.get_cousin(
            {
            'resource-id': 'android:id/switch_widget',
            'class': 'android.widget.Switch'
        })

    @property
    def enhanced_notifications(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'Enhanced notifications',
            'resource-id': 'android:id/title',
            'class': 'android.widget.TextView'
        })

    @property
    def enhanced_notifications_switch(self) -> Element:
        return self.enhanced_notifications.get_cousin(
            {
            'content-desc': 'Enhanced notifications',
            'resource-id': 'com.android.settings:id/switchWidget',
            'class': 'android.widget.Switch'
        })

    @property
    def enhanced_notifications_summary(self) -> Element:
        return self.enhanced_notifications.get_sibling({
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
