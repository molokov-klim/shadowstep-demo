from typing import Any

from shadowstep.page_object.page_object_generator import PageObjectGenerator
from shadowstep.page_object.page_object_parser import PageObjectParser
from shadowstep.page_object.page_object_recycler_explorer import PageObjectRecyclerExplorer
from shadowstep.shadowstep import Shadowstep

app = Shadowstep()

capabilities: dict[str, Any] = {
    "platformName": "android",
    "appium:automationName": "uiautomator2",
    "appium:UDID": '192.168.30.101:5555',
    "appium:noReset": True,
    "appium:autoGrantPermissions": True,
    "appium:newCommandTimeout": 900,
}

app.connect(capabilities=capabilities,
            server_ip='127.0.0.1',
            server_port=4723)

try:

    generator = PageObjectGenerator()
    recycler_explorer = PageObjectRecyclerExplorer(app)



except Exception as error:
    print("STOP STOP STOP STOP STOP STOP STOP STOP STOP STOP STOP STOP STOP ")
    print(error)
finally:
    try:
        app.disconnect()
    except Exception as e:
        if 'NoSuchSessionException' in str(e):
            print("Disconnected.")
        else:
            raise
