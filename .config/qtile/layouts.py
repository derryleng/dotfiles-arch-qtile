from libqtile import layout
from libqtile.config import Match

layout_defaults = {
    "border_focus": '#c4341a',
    "border_normal": '#202020',
    "border_on_single": False,
    "border_width": 2,
    "margin": 12
}

layouts = [
    # layout.Columns(**layout_defaults),
    layout.MonadTall(**layout_defaults),
    layout.MonadWide(**layout_defaults),
    layout.Max(),
    # layout.Matrix(**layout_defaults),
    # layout.Stack(num_stacks=3, **layout_defaults),
    # layout.Bsp(**layout_defaults),
    layout.RatioTile(**layout_defaults),
    # layout.Tile(**layout_defaults),
    # layout.TreeTab(),
    # layout.VerticalTile(**layout_defaults),
    layout.Zoomy(**layout_defaults),
]

floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry

        Match(wm_class="pavucontrol"),  # Volume controls
    ]
)
