#!/bin/sh
vmtoolsd -n vmusr &
variety &
picom &
xinput set-prop 14 349 1 & # tappin enabled
xinput set-prop 14 322 1 & # natural scrolling
xinput set-prop 14 362 1 & # middle emulation
xbindkeys &
