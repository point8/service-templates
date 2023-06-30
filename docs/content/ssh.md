# SSH

You will connect to your new server using SSH. You can already add an entry to your `~/.ssh/config`:

```
Host *.point8.cloud
    Hostname your_subdomain.point8.cloud
    User your_username
    Port 22122
    IdentityFile ~/.ssh/your_point8_ssh_key
    ForwardX11 yes
    ForwardAgent yes
```
