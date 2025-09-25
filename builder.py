from typing import Any

from shadowstep.page_object.page_object_recycler_explorer import PageObjectRecyclerExplorer
from shadowstep.shadowstep import Shadowstep

app = Shadowstep()
capabilities: dict[str, Any] = {
    "platformName": "android",
    "appium:automationName": "uiautomator2",
    "appium:UDID": '127.0.0.1:6555',
    "appium:noReset": True,
    "appium:autoGrantPermissions": True,
    "appium:newCommandTimeout": 900,
}
app.connect(capabilities=capabilities,
            server_ip='127.0.0.1',
            server_port=4723)

try:
    page_object_explorer = PageObjectRecyclerExplorer(app, translator=None)
    page_object_explorer.explore("pages")
except Exception as error:
    print(error)
finally:
    app.disconnect()
