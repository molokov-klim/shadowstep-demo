import logging
from typing import Any
from shadowstep.decorators.decorators import current_page
from shadowstep.element.element import Element
from shadowstep.page_base import PageBaseShadowstep


class PageSettings(PageBaseShadowstep):

    def __init__(self) -> None:
        super().__init__()
        self.logger = logging.getLogger(__name__)

    def __repr__(self) -> str:
        return f"{self.name} ({self.__class__.__name__})"

    @property
    def edges(self) -> dict[str, Any]:
        return {"PageNetworkInternet": self.to_network_internet,
                "PageConnectedDevices": self.to_connected_devices,
                "PageApps": self.to_apps}

    def to_network_internet(self):
        self.network_internet.tap()
        return self.shadowstep.get_page("PageNetworkInternet")

    def to_connected_devices(self):
        self.connected_devices.tap()
        return self.shadowstep.get_page("PageConnectedDevices")

    def to_apps(self):
        self.apps.tap()
        return self.shadowstep.get_page("PageApps")

    @property
    def name(self) -> str:
        return "Settings"

    @property
    def title(self) -> Element:
        return self.shadowstep.get_element({
        'text': 'Settings',
        'resource-id': 'com.android.settings:id/homepage_title',
        'class': 'android.widget.TextView'
    })

    @property
    def app_bar_container(self) -> Element:
        return self.recycler.scroll_to_element({
            'resource-id': 'com.android.settings:id/app_bar_container',
            'class': 'android.widget.LinearLayout'
        })

    @property
    def homepage_app_bar_regular_phone_view(self) -> Element:
        return self.recycler.scroll_to_element({
            'resource-id': 'com.android.settings:id/homepage_app_bar_regular_phone_view',
            'class': 'android.widget.LinearLayout'
        })

    @property
    def search_bar(self) -> Element:
        return self.recycler.scroll_to_element({
            'resource-id': 'com.android.settings:id/search_bar',
            'class': 'androidx.cardview.widget.CardView'
        })

    @property
    def search_action_bar(self) -> Element:
        return self.recycler.scroll_to_element({
            'resource-id': 'com.android.settings:id/search_action_bar',
            'class': 'android.view.ViewGroup'
        })

    @property
    def search_settings(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'Search settings',
            'resource-id': 'com.android.settings:id/search_action_bar_title',
            'class': 'android.widget.TextView'
        })

    @property
    def main_content_scrollable_container(self) -> Element:
        return self.recycler.scroll_to_element({
            'resource-id': 'com.android.settings:id/main_content_scrollable_container',
            'class': 'android.widget.ScrollView'
        })

    @property
    def homepage_container(self) -> Element:
        return self.recycler.scroll_to_element({
            'resource-id': 'com.android.settings:id/homepage_container',
            'class': 'android.widget.LinearLayout'
        })

    @property
    def text_frame(self) -> Element:
        return self.recycler.scroll_to_element({
            'resource-id': 'com.android.settings:id/text_frame',
            'class': 'android.widget.RelativeLayout'
        })

    @property
    def network_internet(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'Network & internet',
            'resource-id': 'android:id/title',
            'class': 'android.widget.TextView'
        })

    @property
    def network_internet_summary(self) -> Element:
        return self.network_internet.get_sibling({
            'resource-id': 'android:id/summary'
        })

    @property
    def connected_devices(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'Connected devices',
            'resource-id': 'android:id/title',
            'class': 'android.widget.TextView'
        })

    @property
    def connected_devices_summary(self) -> Element:
        return self.connected_devices.get_sibling({
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
    def notifications(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'Notifications',
            'resource-id': 'android:id/title',
            'class': 'android.widget.TextView'
        })

    @property
    def notifications_summary(self) -> Element:
        return self.notifications.get_sibling({
            'resource-id': 'android:id/summary'
        })

    @property
    def battery(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'Battery',
            'resource-id': 'android:id/title',
            'class': 'android.widget.TextView'
        })

    @property
    def battery_summary(self) -> Element:
        return self.battery.get_sibling({
            'resource-id': 'android:id/summary'
        })

    @property
    def settings_homepage_container(self) -> Element:
        return self.shadowstep.get_element({
            'resource-id': 'com.android.settings:id/settings_homepage_container',
            'class': 'android.widget.ScrollView'
        })

    @property
    def storage(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'Storage',
            'resource-id': 'android:id/title',
            'class': 'android.widget.TextView'
        })

    @property
    def storage_summary(self) -> Element:
        return self.storage.get_sibling({
            'resource-id': 'android:id/summary'
        })

    @property
    def sound_vibration(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'Sound & vibration',
            'resource-id': 'android:id/title',
            'class': 'android.widget.TextView'
        })

    @property
    def sound_vibration_summary(self) -> Element:
        return self.sound_vibration.get_sibling({
            'resource-id': 'android:id/summary'
        })

    @property
    def display(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'Display',
            'resource-id': 'android:id/title',
            'class': 'android.widget.TextView'
        })

    @property
    def display_summary(self) -> Element:
        return self.display.get_sibling({
            'resource-id': 'android:id/summary'
        })

    @property
    def security(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'Security',
            'resource-id': 'android:id/title',
            'class': 'android.widget.TextView'
        })

    @property
    def wallpaper(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'Wallpaper',
            'resource-id': 'android:id/title',
            'class': 'android.widget.TextView'
        })

    @property
    def wallpaper_summary(self) -> Element:
        return self.wallpaper.get_sibling({
            'resource-id': 'android:id/summary'
        })

    @property
    def accessibility(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'Accessibility',
            'resource-id': 'android:id/title',
            'class': 'android.widget.TextView'
        })

    @property
    def accessibility_summary(self) -> Element:
        return self.accessibility.get_sibling({
            'resource-id': 'android:id/summary'
        })

    @property
    def safety_emergency(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'Safety & emergency',
            'resource-id': 'android:id/title',
            'class': 'android.widget.TextView'
        })

    @property
    def security_summary(self) -> Element:
        return self.security.get_sibling({
            'resource-id': 'android:id/summary'
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
    def location(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'Location',
            'resource-id': 'android:id/title',
            'class': 'android.widget.TextView'
        })

    @property
    def location_summary(self) -> Element:
        return self.location.get_sibling({
            'resource-id': 'android:id/summary'
        })

    @property
    def security_summary_1(self) -> Element:
        return self.security.get_sibling({
            'resource-id': 'android:id/summary'
        })

    @property
    def safety_emergency_summary(self) -> Element:
        return self.safety_emergency.get_sibling({
            'resource-id': 'android:id/summary'
        })

    @property
    def passwords_accounts(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'Passwords & accounts',
            'resource-id': 'android:id/title',
            'class': 'android.widget.TextView'
        })

    @property
    def passwords_accounts_summary(self) -> Element:
        return self.passwords_accounts.get_sibling({
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
    def about_phone(self) -> Element:
        return self.recycler.scroll_to_element({
            'text': 'About phone',
            'resource-id': 'android:id/title',
            'class': 'android.widget.TextView'
        })

    @property
    def about_phone_summary(self) -> Element:
        return self.about_phone.get_sibling({
            'resource-id': 'android:id/summary'
        })

    @property
    def recycler(self) -> Element:
        return self.shadowstep.get_element({
            'resource-id': 'com.android.settings:id/settings_homepage_container',
            'class': 'android.widget.ScrollView'
        })

    @current_page()
    def is_current_page(self) -> bool:
        try:
            return self.title.is_visible()
        except Exception as error:
            self.logger.error(error)
            return False

