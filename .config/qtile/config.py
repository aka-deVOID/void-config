from libqtile import bar, layout, widget, extension, hook, qtile
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from pathlib import Path
from subprocess import run, call as sh_run

# PATHS
HOME = str(Path.home())  # home dir
WALL_PATH = HOME + "/wallpapers"  # wallpaper path
VERTICAL_WALLPAPER = WALL_PATH + "/vertical"
MODE = "mod4"  # win key
TERMINAL = "alacritty"

# Screen Style
SECOND_SCREEM_IS_VERTICAL = False

from utils import random_wallpaper, random_wallpaper_for_second_screen, set_to_vertical, set_to_horizonal

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

    # Bar Keys
    Key([MODE], "h", lazy.hide_show_bar(), desc="Hides the bar"),

    # App Keys
    Key([MODE], "s", lazy.spawn("flameshot gui"), desc="Launch Flameshot"),

    # Dmenu
    Key([MODE], 'm', lazy.run_extension(extension.DmenuRun(
        dmenu_lines=4,
        dmenu_prompt="~>",
        background="#111111",
        dmenu_bottom=True,
        dmenu_ignorecase=True,
        selected_background="#555555",
        foreground="#777777",
        selected_foreground="#999999",
    ))),

    # Second Screen
    Key([MODE, "control"], "v", lazy.spawn("xrandr --output HDMI-A-0 --mode 1920x1080 --rotate left --scale 1x1"),
        desc="rotate right screen to (to vertical)"),
    Key([MODE, "control"], "h", lazy.spawn("xrandr --output HDMI-A-0 --mode 1920x1080 --scale 1x1"),
        desc="rotate screen to normal (horizonal)"),
    # Key([MODE], "c", )
]

# WORKSPACES
groups = [
    Group("1", label="editor", layout="max"),
    Group("2", label="firefox", spawn="firefox", layout="max"),
    Group("3", label="any"),
    Group("4", label="social", spawn="discord"),
    Group("5", label="terminal"),
    Group("6", label="...", layout="columns")
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

# LAYOUTS

_float_rules = [
    Match(wm_class="confirmreset"),  # gitk
    Match(wm_class='dialog'),  # Dialogs stuff
    Match(wm_class="makebranch"),  # gitk
    Match(wm_class="maketag"),  # gitk
    Match(wm_class="error"),
    Match(wm_class="ssh-askpass"),  # ssh-askpass
    Match(title="branchdialog"),  # gitk
    Match(title="pinentry"),  # GPG key password entry
].extend(layout.Floating.default_float_rules)

layouts = [
    layout.Columns(
        border_width=2,
        border_focus="#999999",
        border_focus_stack="#999999",
        border_normal="#555555",
        border_normal_stack="#555555",
        border_on_single=False,
        margin_on_single=2,
        grow_amount=4,
        num_columns=3,
        margin=2
    ),
    layout.Max(
        border_width=2,
        border_focus="#999999",
        border_normal="#555555",
        margin=2
    ),
    layout.Floating(
        border_width=2,
        border_focus="#999999",
        border_normal="#555555",
        float_rules=_float_rules
    )
]

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Spacer(length=20),
                widget.CurrentLayout(background="#111111", ),
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
            size=20,
            background="#111111",
            # border_color=["#111111", "#555555", "#777777", "#999999"],  # Border Color
            border_width=[0, 0, 0, 0],
            margin=[2, 2, 0, 2],
            opacity=0.75,
        ),
        wallpaper=random_wallpaper(),
        wallpaper_mode="fill",
    ),
    Screen(
        top=bar.Bar(
            [
                widget.Spacer(length=20),
                widget.CurrentLayout(background="#111111", ),
                widget.Spacer(),
                widget.Clock(format=" %d/%m/%y %H:%M "),  # "%Y-%m-%d %a %I:%M %p"
                widget.Spacer(),
                widget.Spacer(length=20),
            ],
            size=20,
            background="#111111",
            # border_color=["#111111", "#555555", "#777777", "#999999"],  # Border Color
            border_width=[0, 0, 0, 0],
            margin=[2, 2, 0, 2],
            opacity=0.75,
        ),
        wallpaper=random_wallpaper_for_second_screen() if SECOND_SCREEM_IS_VERTICAL else random_wallpaper(),
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

auto_minimize = False
widget_defaults = {"font": "sans", "fontsize": 12}


# HOOKS
@hook.subscribe.startup
def _():
    qtile.cmd_hide_show_bar('all')  # hide bar at startup
    sh_run(HOME + "/.config/qtile/autostart.sh")  # start shell script to run apps at startup
    if len(qtile.screen) > 1:
        # first screen
        qtile.groups_map["1"].cmd_toscreen(0, toggle=True)
        qtile.groups_map["2"].cmd_toscreen(0, toggle=True)
        qtile.groups_map["3"].cmd_toscreen(0, toggle=True)
        # second screen
        qtile.groups_map["4"].cmd_toscreen(1, toggle=True)
        qtile.groups_map["5"].cmd_toscreen(1, toggle=True)
        qtile.groups_map["6"].cmd_toscreen(1, toggle=True)


@hook.subscribe.startup_once
def _():
    run(['xscreensaver', '-nosplash'])
