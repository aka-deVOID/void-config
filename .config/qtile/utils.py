from os import listdir
from random import choices

from config import WALL_PATH


def random_wallpaper() -> str:
    return (
            WALL_PATH + "/" + choices(list(filter(lambda b: b.endswith(".jpg"), listdir(WALL_PATH))))[0]
    )
