# dotfiles

## Dotfiles repo setup
- Add to .zshrc: alias dotfiles='/usr/bin/git --git-dir=$HOME/.cfg/ --work-tree=$HOME'
- run: echo ".cfg" >> .gitignore
- clone this repo: git clone --bare https://github.com/bbrockbernd/dotfiles.git $HOME/.cfg
- dotfiles checkout -f

### Store git credentials
git config --global credential.helper /usr/lib/git-core/git-credential-libsecret

## Pacman install
### Install
- Use ext4 file system
- pulse audio
- lightdm
- qtile
- alacritty
- dunst
- feh
- fzf
- networkmanager
- oh-my-zsh-plugin-autosuggestions
- oh-my-zsh-plugin-syntax-highlighting
- p7zip
- rofi
- gnome-keyring
- variety
- xinput
- bluez
- bluez-utils
- p7zip
- brightnessctl

### Multiscreen
- arander
- linux-headers
- linux-lts-headers
- nvidia-dkms
- nvidia-utils
- xf86-video-intel
- optimus-manager

### To make the bar work:
- upower (python)
- dbus_next (python)
- iwlib (python)

### Vmtools
- install vmtools: sudo pacman -S open-vm-tools
- install deps: sudo pacman -Su xf86-input-vmmouse xf86-video-vmware mesa gtk2 gtkmm
- add kernel modules (/etc/mkinitcpio.conf): MODULES=(vsock vmw_vsock_vmci_transport vmw_balloon vmw_vmci vmgfx)

# TODO
## Qtile
- Fix groups to screens
- Detect screen connection
- Dual widget groupbox
- font size alacritty second screen
- optimus-manager to systray
