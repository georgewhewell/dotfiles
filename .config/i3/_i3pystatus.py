# -*- coding: utf-8 -*-
from i3pystatus import Status

status = Status()

# Displays clock like this:
# Tue 30 Jul 11:59:46 PM KW31
#                          ^-- calendar week
status.register("clock",
    format="%a %-d %b %X",)

status.register("uptime")
# Shows the average load of the last minute and the last 5 minutes
# (the default value for format is used)
status.register("load")

# Shows your CPU temperature, if you have a Intel CPU
status.register("cpu_freq",
    format="{avgg} GHz",)
status.register("temp")

# The battery monitor has many formatting options, see README for details
status.register("cpu_usage_graph")

status.register("mem")
# This would look like this, when discharging (or charging)
# ↓14.22W 56.15% [77.81%] 2h:41m
# And like this if full:
# =14.22W 100.0% [91.21%]
#
# This would also display a desktop notification (via D-Bus) if the percentage
# goes below 5 percent while discharging. The block will also color RED.
# If you don't have a desktop notification demon yet, take a look at dunst:
#   http://www.knopwob.org/dunst/

# This would look like this:
# Discharging 6h:51m
status.register("network",
    interface = "br0",
    hints = {"markup": "pango"},
    format_up = "<span color=\"#00FF00\">{v4cidr}</span> {bytes_recv:6.1f}KiB {bytes_sent:5.1f}KiB",
    format_down = "",
    dynamic_color = True,
    start_color = "#00FF00",
    end_color = "#FF0000",
    color_down = "#FF0000",
)

# Note: requires both netifaces and basiciw (for essid and quality)
# status.register("network",
#     interface="br0",
#     format_up="{essid} {quality:03.0f}%",)

# Shows disk usage of /
# Format:
# 42/128G [86G]
status.register("disk",
    path="/",
    format="Local: {used}/{total}G [{avail}G]",)

status.register("disk",
    path="/mnt/Media",
    format="NAS: {used}/{total}G [{avail}G]",)

status.run()
