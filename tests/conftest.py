from typing import Any

import pytest

from applications.android_settings.android_settings import AndroidSettings

capabilities: dict[str, Any] = {
    "platformName": "android",
    "appium:automationName": "uiautomator2",
    "appium:UDID": "192.168.30.101:5555",
    "appium:noReset": True,
    "appium:autoGrantPermissions": True,
    "appium:newCommandTimeout": 900,
}


@pytest.fixture
def android_app():
    app = AndroidSettings()
    app.shadowstep.connect(capabilities=capabilities)
    yield app
    app.shadowstep.disconnect()

