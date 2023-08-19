# dotfiles

## Vmware setup
### Install
- Use ext4 file system
- pipewire

### Vmtools
- install vmtools: sudo pacman -S open-vm-tools
- install deps: sudo pacman -Su xf86-input-vmmouse xf86-video-vmware mesa gtk2 gtkmm
- add kernel modules (/etc/mkinitcpio.conf): MODULES=(vsock vmw_vsock_vmci_transport vmw_balloon vmw_vmci vmgfx)

