import os
from libqtile import qtile, bar, widget
from libqtile.config import Screen

terminal = "alacritty"

widget_defaults = dict(
    font="sans",
    fontsize=22,
    padding=3,
)
extension_defaults = widget_defaults.copy()

# Widgets
Sep = widget.Sep(padding=24, linewidth=1, size_percent=100)

# Bars
bar1 = bar.Bar(
    [
        widget.CurrentLayoutIcon(padding=0, scale=0.8),
        # widget.CurrentLayout(),
        Sep,
        widget.GroupBox(),
        Sep,
        #widget.WindowName(),
        widget.WindowTabs(),
        widget.Chord(
            chords_colors={
                "launch": ("#ff0000", "#ffffff"),
            },
            name_transform=lambda name: name.upper(),
        ),
        #widget.Prompt(),
        widget.CheckUpdates(
            update_interval=3600,
            display_format="Updates: {updates}",
            colour_have_updates="aa0033",
            colour_no_updates="80ff33",
            mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(terminal + ' -e sudo pacman -Syu')},
        ),
        Sep,
        widget.Image(
            filename="~/.config/qtile/icons/network-wired-solid-white.png",
            margin_y=4,
        ),
        widget.Net(
            format = '{} ↓↑{}'.format("{down}", "{up}"),
        ),
        Sep,
        widget.Image(
            filename="~/.config/qtile/icons/temperature-2-128.png",
        ),
        widget.ThermalSensor(
            threshold = 90,
            fmt = ' {}',
        ),
        Sep,
        widget.Image(
            filename="~/.config/qtile/icons/memory-solid-white.png",
            margin_y=2,
        ),
        widget.Memory(
            mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(terminal + ' -e htop')},
            fmt=' {}',
        ),
        Sep,
        widget.Image(
            filename="~/.config/qtile/icons/keyboard-2-128.png",
        ),
        widget.KeyboardLayout(
            configured_keyboards=['uk'],
            fmt=' {}',
        ),
        Sep,
        widget.Image(
            filename="~/.config/qtile/icons/volume-up-4-128.png",
            margin_y=2,
        ),
        widget.PulseVolume(
            mouse_callbacks={'Button3': lambda: qtile.cmd_spawn("pavucontrol")},
            update_interval=0,
            fmt=' {}'
        ),
        Sep,
        widget.Systray(
            background="ffffff",
        ),
        Sep,
        widget.Clock(format="%a %d %B %H:%M"),
        #Sep,
        #widget.QuickExit(default_text="Logout", countdown_format="ETA {}"),
    ],
    size=32,
    opacity=0.75,
    margin=0,
    background="202020",
    border_width=[3, 10, 3, 10],
    border_color="202020",
)

screens = [
    Screen(top=bar1),
]
