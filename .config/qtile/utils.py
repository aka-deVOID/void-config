from os import listdir
from random import choices
from libqtile.lazy import lazy

from config import WALL_PATH, VERTICAL_WALLPAPER, SECOND_SCREEM_IS_VERTICAL


def random_wallpaper() -> str:
    return (
            WALL_PATH + "/" + choices(list(filter(lambda b: b.endswith(".jpg"), listdir(WALL_PATH))))[0]
    )


def random_wallpaper_for_second_screen() -> str:
    return (
            VERTICAL_WALLPAPER + "/" + choices(list(filter(lambda b: b.endswith(".jpg"), listdir(VERTICAL_WALLPAPER))))[
        0]
    )


def set_to_vertical() -> None:
    # global SECOND_SCREEM_IS_VERTICAL
    # SECOND_SCREEM_IS_VERTICAL: bool = True
    lazy.spawn("xrandr --output HDMI-A-0 --mode 1920x1080 --rotate left --scale 1x1")


def set_to_horizonal() -> None:
    # global SECOND_SCREEM_IS_VERTICAL
    # SECOND_SCREEM_IS_VERTICAL: bool = False
    lazy.spawn("xrandr --output HDMI-A-0 --mode 1920x1080 --scale 1x1")
