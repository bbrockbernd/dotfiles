#!/bin/sh
vmtoolsd -n vmusr &
variety &
picom &
xinput set-prop 14 "libinput Tapping Enabled" 1 & # tappin enabled
xinput set-prop 14 "libinput Natural Scrolling Enabled" 1 & # natural scrolling
xinput set-prop 14 "libinput Middle Emulation Enabled" 1 & # middle emulation
xbindkeys &
