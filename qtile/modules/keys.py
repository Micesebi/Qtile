from libqtile.lazy import lazy
from libqtile.config import Key

mod = "mod4"
terminal = "xfce4-terminal"

keys = [
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod],
        "space",
        lazy.layout.next(),
        desc="Move window focus to other window"),

    Key([mod], "d", lazy.spawn("Hex")),
    Key([mod], "w", lazy.spawn("librewolf")),
    Key([mod], "f", lazy.spawn("thunar")),
    Key([mod], "s", lazy.spawn("spotify")),
    Key([mod], "t", lazy.spawn("teams")),
    Key([mod], "g", lazy.spawn("steam")),
    Key([mod], "o", lazy.spawn("openttd-jgrpp")),   
    Key([mod, "shift"], "d", lazy.spawn("discord")),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"],
        "h",
        lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"],
        "l",
        lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"],
        "j",
        lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"],
        "h",
        lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"],
        "l",
        lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"],
        "j",
        lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "shift", "control"], "h", lazy.layout.swap_column_left()),
    Key([mod, "shift", "control"], "l", lazy.layout.swap_column_right()),
    Key([mod, "shift"], "space", lazy.layout.flip()),
    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod, "shift"],
        "s",
        lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"),
    Key([], "XF86AudioRaiseVolume",lazy.spawn("amixer set Master 5%+")),
    Key([], "XF86AudioLowerVolume",lazy.spawn("amixer set Master 5%-")),
    Key([], "XF86AudioMute",lazy.spawn("amixer set Master toggle")),
    Key([], "XF86AudioPlay",lazy.spawn("playerctl play-pause")),
    Key([], "XF86AudioNext",lazy.spawn("playerctl next")),
    Key([], "XF86AudioPrev",lazy.spawn("playerctl previous")),
]
