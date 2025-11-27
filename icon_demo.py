"""
Demo showing different behavior of window icon when using toga.App vs. an empty subclass.

Not intended to be run directly. Run `python -m working` or `python -m broken` instead.
"""

from typing import Any
import toga

class IconWorking(toga.App):
    pass

def build(app: toga.App, **kwargs: dict[str, Any]):
    box = toga.Box()

    pointer = toga.Label('\u2191 Look at the window icon \u2196')
    pointer.style.margin = 5 # type: ignore
    box.add(pointer)

    return box


def main(broken: bool):
    if broken:
        appclass = toga.App
    else:
        appclass = IconWorking


    app = appclass(
        'Icon Demo',
        'azurstarshine.icon_demo',
        startup=build,
    )

    print(app.app_name)
    print(app.icon.path)

    app.main_loop()
