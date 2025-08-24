import time

from shadowstep.shadowstep import Shadowstep

from applications.android_settings.pages.page_apps.page_apps import PageApps
from applications.android_settings.pages.page_apps.page_default_apps.page_default_apps import PageDefaultApps
from applications.android_settings.pages.page_apps.page_default_apps.page_opening_links.page_opening_links import \
    PageOpeningLinks
from applications.android_settings.pages.page_connected_devices.page_connected_devices import PageConnectedDevices
from applications.android_settings.pages.page_network_internet.page_network_internet import PageNetworkInternet
from applications.android_settings.pages.page_settings.page_settings import PageSettings


class AndroidSettings:
    def __init__(self):
        self.shadowstep = Shadowstep()
        self._package = "com.android.settings"
        self._launchable_activity = "com.android.settings.Settings"
        
        #pages
        self.page_settings = PageSettings()
        self.page_network_internet = PageNetworkInternet()
        self.page_connected_devices = PageConnectedDevices()
        self.page_apps = PageApps()
        self.page_default_apps = PageDefaultApps()
        self.page_opening_links = PageOpeningLinks()

    def open(self):
        self.close()
        self.shadowstep.terminal.start_activity(
            package=self._package, activity=self._launchable_activity
        )
        time.sleep(1)

    def close(self):
        self.shadowstep.terminal.close_app(package=self._package)
        time.sleep(1)
        