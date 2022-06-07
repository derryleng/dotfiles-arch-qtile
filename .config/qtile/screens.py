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

# Defined Widgets
Sep = widget.Sep(padding=24, linewidth=1, size_percent=100)

# Bar Widgets
bar1_widgets = [
    widget.CurrentLayoutIcon(padding=0, scale=0.8),
    widget.CurrentLayout(fmt = ' {}'),
    Sep,
    widget.GroupBox(highlight_method='block'),
    Sep,
    widget.WindowName(),
    # widget.WindowTabs(),
    # widget.Chord(
    #     chords_colors={
    #         "launch": ("#ff0000", "#ffffff"),
    #     },
    #     name_transform=lambda name: name.upper(),
    # ),
    # widget.Prompt(),
    # widget.CheckUpdates(
    #     update_interval=3600,
    #     display_format="Updates: {updates}",
    #     colour_have_updates="aa0033",
    #     colour_no_updates="80ff33",
    #     mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(terminal + ' -e sudo pacman -Syu')},
    # ),
    Sep,
    widget.Image(
        filename="~/.config/qtile/icons/network-wired-solid-white.png",
        margin_y=6,
    ),
    widget.Net(
        format = ' {} ↓↑ {}'.format("{down}", "{up}"),
    ),
    Sep,
    # widget.Image(
    #     filename="~/.config/qtile/icons/temperature-2-128.png",
    # ),
    # widget.ThermalSensor(
    #     threshold = 90,
    #     fmt = ' {}',
    # ),
    # Sep,
    widget.Image(
        filename="~/.config/qtile/icons/memory-solid-white.png",
        margin_y=5,
    ),
    widget.Memory(
        mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(terminal + ' -e htop')},
        fmt=' {}',
    ),
    Sep,
    widget.Image(
        filename="~/.config/qtile/icons/keyboard-2-128.png",
        margin_y=2,
    ),
    widget.KeyboardLayout(
        configured_keyboards=['uk'],
        fmt=' {}',
    ),
    Sep,
    widget.Image(
        filename="~/.config/qtile/icons/volume-up-4-128.png",
        margin_y=5,
    ),
    widget.PulseVolume(
        mouse_callbacks={'Button3': lambda: qtile.cmd_spawn("pavucontrol")},
        update_interval=0,
        fmt=' {}',
    ),
    Sep,
    # widget.Systray(
    #     background="ffffff",
    # ),
    # Sep,
    widget.Clock(format="%a %d %B %H:%M"),
    # Sep,
    # widget.QuickExit(default_text="Logout", countdown_format="ETA {}"),
]

# Bars
bar1 = bar.Bar(
    bar1_widgets,
    size=33,
    opacity=1,
    margin=0,
    border_width=[3, 10, 3, 10],
    #border_color="222222",
    #background="222222",
    border_color="000000",
    background="000000",
)

screens = [
    Screen(bottom=bar1),
]
