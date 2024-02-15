# _______  _______  ______  _______  __        
# |       ||   _   ||   __ \|     __||  |.-----.
# |   -  _||       ||      <|__     ||  ||  _  |
# |_______||___|___||___|__||_______||__||   __|
#                                       |__|   
# SpectrumOS - Embrace the Chromatic Symphony!
# By: gibranlp <thisdoesnotwork@gibranlp.dev>
# MIT licence
# from functions import *
# Theme 
## Decorations
from libqtile import widget
import json
import os
import random
import socket
import subprocess
from os.path import expanduser
from pathlib import Path
import requests
from libqtile import bar, hook, layout, qtile, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from qtile_extras import widget
from qtile_extras.popup.toolkit import (PopupImage, PopupRelativeLayout, PopupText, PopupWidget)
from qtile_extras.widget.decorations import (BorderDecoration, PowerLineDecoration, RectDecoration)

bar_position = "top"

powerline = {
    "decorations": [RectDecoration(use_widget_background=True, radius=0, filled=True),
                    PowerLineDecoration(path="forward_slash")],
}

## Screens


color = [
    "#36393B", # grayish backgr 1
    "#A5D8FF", # blueish
    "#F0C808", # geel backgr 2
    "#DB504A",
    "#26A96C",
    "#46569E",
    "#8290cf"
]

main_font = "JetBrainsMonoNL Nerd Font"  # Font in use for the entire system
awesome_font = "Font Awesome 6 Pro"  # Font for the icons
font_size = 17
groups_font = font_size
hide_unused_groups = True

layout_margin = 10
single_layout_margin = 5
layout_border_width = 4
single_border_width = 4
font_size = 15
bar_size = 25
widget_width = 150
max_ratio = 0.85
ratio = 0.70
bar_margin = [5, 8, 0, 8]
prompt = " ".format(os.environ["USER"], socket.gethostname())
terminal = "alacritty"  # Terminal in use
w_appkey = "b9fc42de9568ac3bca3509bc9d608cf9"
w_cityid = "2747891"

transparent=color[0] + "00"

def get_net_dev():
    get_dev = "echo $(ip route get 8.8.8.8 | awk -- '{printf $5}')"
    ps = subprocess.Popen(get_dev, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output = ps.communicate()[0].decode('ascii').strip()
    return (output)


wifi = get_net_dev()

# Set Ethernet or Wi-Fi icon according
if wifi.startswith('e'):
    wifi_icon = ' '
else:
    wifi_icon = ' '

def get_private_ip():
    ip = socket.gethostbyname(socket.gethostname())
    return ip

private_ip = get_private_ip()

def get_public_ip():
    try:
        raw = requests.get('https://api.duckduckgo.com/?q=ip&format=json')
        answer = raw.json()["Answer"].split()[4]
    except Exception:
        return "0.0.0.0"
    else:
        return answer

public_ip = get_public_ip()

# def network_widget(qtile):
#     options = [' Wlan Manager','  Bandwith Monitor (CLI)', ' Network Manager (CLI)']
#     index, key = rofi_network.select(" " + private_ip + " -" + "  " + public_ip, options)
#     if key == -1:
#         rofi_network.close()
#     else:
#         if index == 0:
#             qtile.spawn(home + '/.local/bin/wifi2')
#         elif index==1:
#             qtile.spawn(terminal + ' -e bmon')
#         else:
#             qtile.spawn(terminal + ' -e nmtui')

def secondary_pallete(colors, differentiator):
    updated_colors = []
    for color in colors:
        # Remove the '#' symbol
        color = color.lstrip('#')
        # Convert hexadecimal colors to integers
        color_int = int(color, 16)
        differentiator_int = int(differentiator, 16)
        # Perform addition
        result_int = color_int + differentiator_int
        # Ensure the result is within the valid range of 0-FFFFFF
        result_int = min(result_int, 0xFFFFFF)
        result_int = max(result_int, 0)
        # Convert the result back to hexadecimal
        result_hex = '#' + hex(result_int)[2:].zfill(6).upper()

        updated_colors.append(result_hex)

    return updated_colors

differentiator = '222222'
secondary_color = secondary_pallete(color, differentiator)


def init_widgets_list():
    widgets_list = [
        widget.GroupBox(
            background=color[0],
            fontsize=groups_font,
            font=awesome_font,
            disable_drag=True,
            hide_unused=hide_unused_groups,
            padding_x=3,
            borderwidth=0,
            active=color[1],  # Program opened in that group
            inactive=color[6],  # Empty Group
            rounded=False,
            highlight_method="text",
            this_current_screen_border=color[2],
            center_aligned=True,
            other_curren_screen_border=color[2],
            block_highlight_text_color=color[2],
            urgent_border="fc0000",
            **powerline
        ),
        widget.CurrentLayoutIcon(
            use_mask=True,
            foreground=color[0],
            scale=0.9,
            background=color[1],
            **powerline,
        ),
        widget.TextBox(
            font=awesome_font,
            background=color[0],
            foreground=color[1],
            text="",
            **powerline,
        ),
        widget.CPU(
            background=color[0],
            foreground=color[1],
            format='{load_percent}',
            **powerline,
        ),
        widget.TextBox(
            font=awesome_font,
            background=color[1],
            foreground=color[0],
            text="",
            **powerline,
        ),
        widget.Memory(
            background=color[1],
            foreground=color[0],
            format='{MemUsed:.0f}{mm}',
            measure_mem='G',
            **powerline,
        ),
        widget.TextBox(
            background=color[0],
            foreground=color[1],
            text="",
            **powerline,
        ),
        widget.WindowName(
            background=color[0],
            foreground=color[1],
            width=widget_width,
            format='{name}',
            scroll=True,
            scroll_delay=2,
            scroll_repeat=True,
            scroll_step=1,
            **powerline,
        ),
        widget.Prompt(
            background=color[1],
            prompt=prompt,
            foreground=color[0],
            cursor_color=color[0],
            visual_bell_color=[0],
            visual_bell_time=0.2,
            **powerline,
        ),
        widget.Spacer(
            length=bar.STRETCH,
            background=color[0],
            **powerline,
        ),
        widget.Systray(
            background=color[0],
            foreground=color[1],
            **powerline,
        ),
        # widget.TextBox(
        #     background=color[3],
        #     text="",
        #     foreground=color[0],
        #     **powerline,
        # ),
        # # widget.Mpris2(
        # #     background=color[0],
        # #     mouse_callbacks={'Button1': lambda: qtile.spawn(terminal + " -e cava")},
        # #     objname=None,
        # #     foreground=color[3],
        # #     width=widget_width,
        # #     format='{xesam:artist}  {xesam:title}',
        # #     paused_text='  ',
        # #     scroll=True,
        # #     scroll_repeat=True,
        # #     scroll_delay=0.1,
        # #     **powerline,
        # # ),
        # widget.TextBox(
        #     background=color[3],
        #     text="",
        #     foreground=color[0],
        #     mouse_callbacks={'Button1': lambda: qtile.spawn(terminal + " -e cava")},
        #     **powerline,
        # ),
        # widget.Pomodoro(
        #     background=color[1],
        #     foreground=color[0],
        #     color_active=color[0],
        #     color_break=color[0],
        #     color_inactive=color[0],
        #     length_long_break=30,
        #     length_pomodori=45,
        #     length_short_break=15,
        #     notification_on=True,
        #     num_pomodori=3,
        #     prefix_active=' ',
        #     prefix_inactive='',
        #     prefix_break=' ',
        #     prefix_long_break=' ',
        #     prefix_paused=' ',
        #     **powerline,
        # )
        widget.TextBox(
            background=color[1],
            foreground=color[0],
            text="",
            # mouse_callbacks={'Button1': lambda: qtile.function(session_widget)},
            ),
        widget.Backlight(
                background=color[1],
                foreground=color[0],
                backlight_name='intel_backlight',
                brightness_file='brightness',
                max_brightness_file='max_brightness',
                **powerline,
                ),
        widget.TextBox( 
            background=color[0],
            text="",
            foreground=color[1],
            mouse_callbacks={'Button1': lambda: qtile.spawn('pavucontrol'), 'Button4': lambda: qtile.spawn(
                "amixer -q set Master 5%+ && dunstify -a Volume ' '$(pamixer --get-volume-human) -h int:value:$(pamixer --get-volume)",
                shell=True), 'Button5': lambda: qtile.spawn(
                "amixer -q set Master 5%- && dunstify -a Volume ' '$(pamixer --get-volume-human) -h int:value:$(pamixer --get-volume)",
                shell=True)},
            **powerline,
        ),
        widget.PulseVolume(
            background=color[0],
            foreground=color[1],
            **powerline,
                ),
        widget.Clock(
            foreground=color[0],
            format="%a %d %H:%M",
            update_interval=1,
            background=color[1],
            # mouse_callbacks={'Button1': lambda: qtile.function(calendar_notification),
            #                  'Button4': lambda: qtile.function(calendar_notification_prev),
            #                  'Button5': lambda: qtile.function(calendar_notification_next)},
            **powerline,
        ),
        ## Network
        widget.WidgetBox(
            background=color[0],
            text_closed=wifi_icon,
            text_open='',
            foreground=color[2],
            **powerline,
            widgets=[
                widget.TextBox(
                    background=color[0],
                    text='',
                    foreground=color[1],
                    # mouse_callbacks={'Button1': lambda: qtile.function(network_widget)},
                    **powerline,
                ),
                widget.TextBox(
                    background=color[1],
                    text=private_ip,
                    foreground=color[0],
                    # mouse_callbacks={'Button1': lambda: qtile.function(network_widget)},
                    **powerline,
                ),
                widget.TextBox(
                    background=color[0],
                    text='',
                    foreground=color[1],
                    # mouse_callbacks={'Button1': lambda: qtile.function(network_widget)},
                    **powerline,
                ),
                widget.TextBox(
                    background=color[1],
                    text=public_ip,
                    foreground=color[0],
                    # mouse_callbacks={'Button1': lambda: qtile.function(network_widget)},
                    **powerline,
                ),
                # widget.TextBox(
                #     background=color[0],
                #     text=wifi_icon,
                #     foreground=color[3],
                #     # mouse_callbacks={'Button1': lambda: qtile.function(network_widget)},
                #     **powerline,
                # ),
            ]
        ),
        widget.Wlan(
            interface=wifi,
            format='{essid}',
            disconnected_message='',
            foreground=color[1],
            width=widget_width,
            scroll=True,
            scroll_repeat=True,
            scroll_interval=0.1,
            scroll_step=1,
            update_interval=1,
            # mouse_callbacks={'Button1': lambda: qtile.function(network_widget)},
            background=color[0],
        ),
        widget.Wlan(
            background=color[0],
            interface=wifi,
            format='{percent:2.0%}',
            disconnected_message='',
            foreground=color[1],
            # mouse_callbacks={'Button1': lambda: qtile.function(network_widget)},
            **powerline,
        ),
        # widget.TextBox(
        #   background=color[2],
        #   text="",
        #   foreground=color[0],
        #   **powerline,
        # ),
        # widget.KeyboardLayout(
        #   background=color[2],
        #   configured_keyboards=['us intl', 'latam'],
        #   foreground=color[0],
        #   **powerline,
        # ),
        # widget.ALSAWidget(
        #     background=color[1],
        #     device='Master',
        #     bar_colour_high=color[0],
        #     bar_colour_loud=color[0],
        #     bar_colour_normal=color[0],
        #     bar_colour_mute=color[0],
        #     hide_interval=5,
        #     update_interval=0.1,
        #     bar_width=80,
        #     mode='bar',
        #     foreground=color[5],
        #     text_format=' ',
        #     **powerline,
        # ),
        widget.OpenWeather(
            background=color[1],
            app_key=w_appkey,
            cityid=w_cityid,
            weather_symbols={
                "Unknown": "",
                "01d": "",
                "01n": "",
                "02d": "",
                "02n": "",
                "03d": "",
                "03n": "",
                "04d": "",
                "04n": "",
                "09d": "⛆",
                "09n": "⛆",
                "10d": "",
                "10n": "",
                "11d": "🌩",
                "11n": "🌩",
                "13d": "❄",
                "13n": "❄",
                "50d": "",
                "50n": "",
            },
            format='{icon}',
            foreground=color[0],
            metric=True,
            update_interval=600,
            **powerline,
        ),
        widget.OpenWeather(
            background=color[1],
            app_key=w_appkey,
            cityid=w_cityid,
            foreground=color[0],
            format='{temp}°{units_temperature}',
            metric=True,
            update_interval=600,
            **powerline,
        ),
        widget.UPowerWidget(
            border_charge_colour=color[3],
            border_colour=secondary_color[0],
            border_critical_colour='#cc0000',
            fill_critical='#cc0000',
            fill_low='#FF5511',
            fill_normal=color[3],
            foreground=color[3],
            background=color[0],
            percentage_critical=0.2,
            percentage_low=0.4,
            text_charging=' ({percentage:.0f}%) {ttf} to ',
            text_discharging=' ({percentage:.0f}%) {tte} Left',
            **powerline,
        ),
        ## Lock, Logout, Poweroff
        widget.TextBox(
            background=color[1],
            foreground=color[0],
            text=" ",
            # mouse_callbacks={'Button1': lambda: qtile.function(session_widget)},
        )]
    return widgets_list


# def screen1_widgets():
#     widgets_screen1 = init_widgets_list()
#     return widgets_screen1


# def init_screens_bottom():
#     return [Screen(bottom=bar.Bar(widgets=screen1_widgets(), size=bar_size, background=transparent, margin=bar_margin))]

widgets_list = init_widgets_list()
# def init_screens_top():
#     return [Screen(top=bar.Bar(widgets=screen1_widgets(), size=bar_size, background=transparent, margin=bar_margin))]

def get_bar(margin=bar_margin, widgets=widgets_list):
    return bar.Bar(widgets=widgets, size=bar_size, background=color[0], margin=margin, border_width=[0, 0, 0, 0])

# if bar_position == "top":
#     screens = init_screens_top()
# else:
#     screens = init_screens_bottom()

# widgets_screen1 = screen1_widgets()
