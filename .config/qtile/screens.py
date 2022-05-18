import os
from libqtile import qtile, bar, widget
from libqtile.config import Screen

terminal = "alacritty"

widget_defaults = dict(
    font="sans",
    fontsize=20,
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
        widget.WindowName(),
        widget.Chord(
            chords_colors={
                "launch": ("#ff0000", "#ffffff"),
            },
            name_transform=lambda name: name.upper(),
        ),
        widget.Prompt(),
        widget.CheckUpdates(
            update_interval=1800,
            display_format="Updates: {updates}",
            colour_have_updates="aa0033",
            colour_no_updates="80ff33",
            mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(terminal + ' -e sudo pacman -Syu')},
        ),
        widget.Systray(),
        Sep,
        widget.ThermalSensor(
            threshold = 90,
            fmt = 'Temp: {}',
        ),
        Sep,
        widget.Memory(
            mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(terminal + ' -e htop')},
            fmt='Mem: {}',
        ),
        Sep,
        widget.KeyboardLayout(
            fmt='Keyboard: {}',
        ),
        Sep,
        widget.Net(
            interface = "enp2s1",
            format = 'Net: {down} ↓↑ {up}',
        ),
        Sep,
        widget.PulseVolume(
            mouse_callbacks={'Button3': lambda: qtile.cmd_spawn("pavucontrol")},
            update_interval=0,
            fmt='Vol: {}'
        ),
        Sep,
        widget.Clock(format="%a %d %B %H:%M"),
        Sep,
        widget.QuickExit(default_text="Logout", countdown_format="ETA {}"),
    ],
    size=32,
    opacity=0.75,
    margin=0,
    background="202020",
    border_width=[3, 10, 3, 10],
    border_color="202020"
)

screens = [
    Screen(bottom=bar1),
]
