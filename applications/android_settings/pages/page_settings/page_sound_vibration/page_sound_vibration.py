import logging
from typing import Any
from shadowstep.decorators.decorators import current_page
from shadowstep.element.element import Element
from shadowstep.page_base import PageBaseShadowstep


class PageSoundVibration(PageBaseShadowstep):

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
        return "Sound & vibration"

    @property
    def title(self) -> Element:
        return self.shadowstep.get_element({
        'content-desc': 'Sound & vibration',
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
    def media_volume(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'Media volume',
            'content-desc': 'Media volume',
            'resource-id': 'android:id/title',
            'class': 'android.widget.TextView'
        })

    @property
    def media_volume_1(self) -> Element:
        return self.recycler.scroll_to_element({
            'content-desc': 'Media volume',
            'resource-id': 'android:id/seekbar',
            'class': 'android.widget.SeekBar'
        })

    @property
    def call_volume(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'Call volume',
            'resource-id': 'android:id/title',
            'class': 'android.widget.TextView'
        })

    @property
    def call_volume_1(self) -> Element:
        return self.recycler.scroll_to_element({
            'content-desc': 'Call volume',
            'resource-id': 'android:id/seekbar',
            'class': 'android.widget.SeekBar'
        })

    @property
    def ring_volume(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'Ring volume',
            'content-desc': 'Ring volume',
            'resource-id': 'android:id/title',
            'class': 'android.widget.TextView'
        })

    @property
    def ring_volume_1(self) -> Element:
        return self.recycler.scroll_to_element({
            'content-desc': 'Ring volume',
            'resource-id': 'android:id/seekbar',
            'class': 'android.widget.SeekBar'
        })

    @property
    def notification_volume(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'Notification volume',
            'content-desc': 'Notification volume',
            'resource-id': 'android:id/title',
            'class': 'android.widget.TextView'
        })

    @property
    def notification_volume_1(self) -> Element:
        return self.recycler.scroll_to_element({
            'content-desc': 'Notification volume',
            'resource-id': 'android:id/seekbar',
            'class': 'android.widget.SeekBar'
        })

    @property
    def alarm_volume(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'Alarm volume',
            'resource-id': 'android:id/title',
            'class': 'android.widget.TextView'
        })

    @property
    def alarm_volume_1(self) -> Element:
        return self.recycler.scroll_to_element({
            'content-desc': 'Alarm volume',
            'resource-id': 'android:id/seekbar',
            'class': 'android.widget.SeekBar'
        })

    @property
    def do_not_disturb(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'Do Not Disturb',
            'resource-id': 'android:id/title',
            'class': 'android.widget.TextView'
        })

    @property
    def shortcut_to_prevent_ringing(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'Shortcut to prevent ringing',
            'resource-id': 'android:id/title',
            'class': 'android.widget.TextView'
        })

    @property
    def shortcut_to_prevent_ringing_switch(self) -> Element:
        return self.shortcut_to_prevent_ringing.get_cousin(
            {
            'content-desc': 'Shortcut to prevent ringing',
            'resource-id': 'com.android.settings:id/switchWidget',
            'class': 'android.widget.Switch'
        })

    @property
    def do_not_disturb_summary(self) -> Element:
        return self.do_not_disturb.get_sibling({
            'resource-id': 'android:id/summary'
        })

    @property
    def phone_ringtone(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'Phone ringtone',
            'resource-id': 'android:id/title',
            'class': 'android.widget.TextView'
        })

    @property
    def phone_ringtone_summary(self) -> Element:
        return self.phone_ringtone.get_sibling({
            'resource-id': 'android:id/summary'
        })

    @property
    def media(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'Media',
            'resource-id': 'android:id/title',
            'class': 'android.widget.TextView'
        })

    @property
    def media_summary(self) -> Element:
        return self.media.get_sibling({
            'resource-id': 'android:id/summary'
        })

    @property
    def shortcut_to_prevent_ringing_summary(self) -> Element:
        return self.shortcut_to_prevent_ringing.get_sibling({
            'resource-id': 'android:id/summary'
        })

    @property
    def dial_pad_tones(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'Dial pad tones',
            'resource-id': 'android:id/title',
            'class': 'android.widget.TextView'
        })

    @property
    def dial_pad_tones_switch(self) -> Element:
        return self.dial_pad_tones.get_cousin(
            {
            'resource-id': 'android:id/switch_widget',
            'class': 'android.widget.Switch'
        })

    @property
    def default_notification_sound(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'Default notification sound',
            'resource-id': 'android:id/title',
            'class': 'android.widget.TextView'
        })

    @property
    def default_notification_sound_summary(self) -> Element:
        return self.default_notification_sound.get_sibling({
            'resource-id': 'android:id/summary'
        })

    @property
    def default_alarm_sound(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'Default alarm sound',
            'resource-id': 'android:id/title',
            'class': 'android.widget.TextView'
        })

    @property
    def default_alarm_sound_summary(self) -> Element:
        return self.default_alarm_sound.get_sibling({
            'resource-id': 'android:id/summary'
        })

    @property
    def screen_locking_sound(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'Screen locking sound',
            'resource-id': 'android:id/title',
            'class': 'android.widget.TextView'
        })

    @property
    def screen_locking_sound_switch(self) -> Element:
        return self.screen_locking_sound.get_cousin(
            {
            'resource-id': 'android:id/switch_widget',
            'class': 'android.widget.Switch'
        })

    @property
    def charging_sounds_and_vibration(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'Charging sounds and vibration',
            'resource-id': 'android:id/title',
            'class': 'android.widget.TextView'
        })

    @property
    def charging_sounds_and_vibration_switch(self) -> Element:
        return self.charging_sounds_and_vibration.get_cousin(
            {
            'resource-id': 'android:id/switch_widget',
            'class': 'android.widget.Switch'
        })

    @property
    def tap_click_sounds(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'Tap & click sounds',
            'resource-id': 'android:id/title',
            'class': 'android.widget.TextView'
        })

    @property
    def tap_click_sounds_switch(self) -> Element:
        return self.tap_click_sounds.get_cousin(
            {
            'resource-id': 'android:id/switch_widget',
            'class': 'android.widget.Switch'
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
