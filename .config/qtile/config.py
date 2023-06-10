from libqtile import bar, layout, widget, hook, extension
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from random import choices
from os import listdir
from pathlib import Path
from subprocess import call as sh_run
from subprocess import run

# static vars
HOME = str(Path.home())  # your home dir
WALL_PATH = HOME + "/wallpapers"  # wallpaper path
MODE = "mod4"
TERMINAL = "alacritty"


# functions
def random_wallpaper() -> str:
    return (
            "/home/devoid/wallpapers/"
            + choices(list(filter(lambda b: b.endswith(".jpg"), listdir(WALL_PATH))))[0]
    )


# hooks
@hook.subscribe.startup
def autostart():
    sh_run(HOME + "/.config/qtile/autostart.sh")


@hook.subscribe.startup_once
def cmd_at_start():
    run(['xscreensaver', '-nosplash'])


keys = [
    Key([MODE], "left", lazy.layout.left(), desc="Move focus to left"),
    Key([MODE], "right", lazy.layout.right(), desc="Move focus to right"),
    Key([MODE], "down", lazy.layout.down(), desc="Move focus down"),
    Key([MODE], "up", lazy.layout.up(), desc="Move focus up"),
    Key(
        [MODE, "shift"], "left", lazy.layout.shuffle_left(), desc="Move window to the left"
    ),
    Key(
        [MODE, "shift"],
        "right",
        lazy.layout.shuffle_right(),
        desc="Move window to the right",
    ),
    Key([MODE, "shift"], "down", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([MODE, "shift"], "up", lazy.layout.shuffle_up(), desc="Move window up"),
    Key([MODE, "control"], "left", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key(
        [MODE, "control"], "right", lazy.layout.grow_right(), desc="Grow window to the right"
    ),
    Key([MODE, "control"], "down", lazy.layout.grow_down(), desc="Grow window down"),
    Key([MODE, "control"], "up", lazy.layout.grow_up(), desc="Grow window up"),

    Key(
        [MODE, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([MODE], "t", lazy.spawn(TERMINAL), desc="Launch terminal"),
    Key([MODE], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([MODE], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([MODE, "shift"], "r", lazy.reload_config(), desc="Reload the config"),

    # Better Lock Screen
    Key([MODE, "shift"], "l", lazy.spawn("betterlockscreen -l")),
    Key([MODE, "shift"], "q", lazy.shutdown()),
    # Bar Keys
    Key([MODE], "h", lazy.hide_show_bar(), desc="Hides the bar"),

    # App Keys
    Key([MODE], "s", lazy.spawn("flameshot gui"), desc="Launch Flameshot"),

    # Dmenu
    Key([MODE], 'm', lazy.run_extension(extension.DmenuRun(
        dmenu_lines=4,
        dmenu_prompt="devoid@devoid ~>",
        background="#111111",
        dmenu_bottom=True,
        dmenu_ignorecase=True,
        selected_background="#555555",
        foreground="#777777",
        selected_foreground="#999999",
    ))),
]

groups = [
    Group("1", label="code", spawn="emacs", layout="max"),
    Group("2", label="firefox", spawn="firefox --new-instance", layout="max"),
    Group("3", label="console"),
    Group("4", label="social", spawn="discord"),
    Group("5", label="empty"),
]

for i in groups:
    keys.extend(
        [
            Key(
                [MODE],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            Key(
                [MODE, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            )
        ]
    )

layouts = [
    layout.Columns(
        border_focus_stack="#555555",
        # border_focus="",
        border_width=2,
        margin=4
    ),
    layout.Max(
        margin=4
    ),
]

widget_defaults = dict(
    font="sans",
    fontsize=12,
    padding=3,
    border_focus="#999999"
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Spacer(length=20),
                widget.Spacer(),
                widget.Clock(format=" %d/%m/%y %H:%M "),  # "%Y-%m-%d %a %I:%M %p"
                widget.Spacer(),
                widget.Systray(
                    background="#111111",
                    padding=5,
                    icon_size=18,
                ),
                widget.Spacer(length=20),
            ],
            20,
            background="#111111",
            border_color=["#FF0000", "", "", ""],
            border_width=[1, 0, 0, 0],
            margin=3,
            opacity=0.90,
        ),
        wallpaper=random_wallpaper(),
        wallpaper_mode="fill",
    ),
]

mouse = [
    Drag(
        [MODE],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [MODE], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
    Click([MODE], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False

floating_layout = layout.Floating(
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class='dialog'),  # Dialogs stuff
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)

auto_fullscreen = True

focus_on_window_activation = "smart"

reconfigure_screens = True

auto_minimize = True

wmname = "LG3D"
