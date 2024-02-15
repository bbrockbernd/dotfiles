#!/bin/sh
vmtoolsd -n vmusr &
variety &
picom &
xinput set-prop "SYNA307B:00 06CB:CD46 Touchpad" "libinput Tapping Enabled" 1 & # tappin enabled
xinput set-prop "SYNA307B:00 06CB:CD46 Touchpad" "libinput Natural Scrolling Enabled" 1 & # natural scrolling
xinput set-prop "SYNA307B:00 06CB:CD46 Touchpad" "libinput Middle Emulation Enabled" 1 & # middle emulation
xbindkeys &
optimus-manager-qt &
udiskie &
