import discord, os, random, time, colorama, json, sys
from discord.ext import commands
from colorama import Fore
from sys import platform

__version__ = 1.0

with open('config/alucard.json') as f:
    config = json.load(f)

TOKEN = config.get('Alucard-TOKEN')
PREFIX = config.get('Alucard-PREFIX')

alucard = commands.Bot(command_prefix=PREFIX)

alucardBanner = f"""


            
             █████╗ ██╗     ██╗   ██╗ ██████╗ █████╗ ██████╗ ██████╗ 
            ██╔══██╗██║     ██║   ██║██╔════╝██╔══██╗██╔══██╗██╔══██╗
            ███████║██║     ██║   ██║██║     ███████║██████╔╝██║  ██║
            ██╔══██║██║     ██║   ██║██║     ██╔══██║██╔══██╗██║  ██║
            ██║  ██║███████╗╚██████╔╝╚██████╗██║  ██║██║  ██║██████╔╝
            ╚═╝  ╚═╝╚══════╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ 
            
                                Version: {__version__}
══════════════════════════════════════════════════════════════════════════════════
                                                                     


"""

alucardOrginal = f"""



             ▄▄▄       ██▓     █    ██  ▄████▄   ▄▄▄       ██▀███  ▓█████▄ 
            ▒████▄    ▓██▒     ██  ▓██▒▒██▀ ▀█  ▒████▄    ▓██ ▒ ██▒▒██▀ ██▌
            ▒██  ▀█▄  ▒██░    ▓██  ▒██░▒▓█    ▄ ▒██  ▀█▄  ▓██ ░▄█ ▒░██   █▌
            ░██▄▄▄▄██ ▒██░    ▓▓█  ░██░▒▓▓▄ ▄██▒░██▄▄▄▄██ ▒██▀▀█▄  ░▓█▄   ▌
             ▓█   ▓██▒░██████▒▒▒█████▓ ▒ ▓███▀ ░ ▓█   ▓██▒░██▓ ▒██▒░▒████▓ 
             ▒▒   ▓▒█░░ ▒░▓  ░░▒▓▒ ▒ ▒ ░ ░▒ ▒  ░ ▒▒   ▓▒█░░ ▒▓ ░▒▓░ ▒▒▓  ▒ 
              ▒   ▒▒ ░░ ░ ▒  ░░░▒░ ░ ░   ░  ▒     ▒   ▒▒ ░  ░▒ ░ ▒░ ░ ▒  ▒ 
              ░   ▒     ░ ░    ░░░ ░ ░ ░          ░   ▒     ░░   ░  ░ ░  ░ 
                  ░  ░    ░  ░   ░     ░ ░            ░  ░   ░        ░    
                                       ░                            ░      

                                Version: {__version__}
══════════════════════════════════════════════════════════════════════════════════

"""
#Orginal Banner Unused

colorama.init()
def init():
    if config.get('Alucard-TOKEN') == "":
        print(
            f"[{Fore.WHITE}Alucard Selfbot{Fore.RESET}] / {Fore.LIGHTYELLOW_EX}[Error] {Fore.WHITE}|{Fore.RESET} {Fore.RED}Login Unseccessful (Improper Token){Fore.RESET}")
    try:
        alucard.run(TOKEN, bot=False)
    except discord.errors.LoginFailure as e:
        print(
            f"[{Fore.WHITE}Alucard Selfbot{Fore.RESET}] / {Fore.LIGHTYELLOW_EX}[Error] {Fore.WHITE}|{Fore.RESET} {Fore.RED}Login Unseccessful (Improper Token){Fore.RESET}")
        time.sleep(20)

@alucard.event
async def on_ready():
    os.system("cls")
    os.system("mode con lines=29 cols=82")
    os.system(f"title [ Alucard / User: {alucard.user.name}] ")
    print(alucardBanner)






if __name__ == "__main__":
    init()