# dotfiles

## Dotfiles repo setup
- Add to .zshrc: alias dotfiles='/usr/bin/git --git-dir=$HOME/.cfg/ --work-tree=$HOME'
- run: echo ".cfg" >> .gitignore
- clone this repo: git clone --bare https://github.com/bbrockbernd/dotfiles.git $HOME/.cfg
- dotfiles checkout -f

## Vmware setup
### Install
- Use ext4 file system
- pipewire

### Vmtools
- install vmtools: sudo pacman -S open-vm-tools
- install deps: sudo pacman -Su xf86-input-vmmouse xf86-video-vmware mesa gtk2 gtkmm
- add kernel modules (/etc/mkinitcpio.conf): MODULES=(vsock vmw_vsock_vmci_transport vmw_balloon vmw_vmci vmgfx)

