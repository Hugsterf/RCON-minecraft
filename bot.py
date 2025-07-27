from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message
from mcrcon import MCRcon
import asyncio
import logging

TOKEN = "YOUR_TOKEN"
RCON_IP = "RCON_IP"
RCON_PORT = #RCON_PORT
RCON_PASS = "RCON_PASS"
username = "PLAYER'S NAME"

bot = Bot(token=TOKEN)
dp = Dispatcher()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s"
)

def send_rcon(command: str):
    try:
        with MCRcon(RCON_IP, RCON_PASS, RCON_PORT) as mcr:
            mcr.command(command)
        return True
    except:
        return False

@dp.message(Command("zomb"))
async def spawn_zombie(message: Message):
    cmd = f"execute at {username} run summon zombie ~ ~ ~"
    
    if send_rcon(cmd):
        await message.answer("✅ 1 зомби заспавнен!")
    else:
        await message.answer("❌ Не удалось отправить команду на сервер")

@dp.message(Command("sword"))
async def give_sword(message: Message):
    cmd = f"give {username} minecraft:diamond_sword 1"
    
    if send_rcon(cmd):
        await message.answer("✅ Зомби заспавнен!")
    else:
        await message.answer("❌ Не удалось отправить команду на сервер")

@dp.message(Command("creeper"))
async def spawn_creeper(message: Message):
    cmd = f"execute at {username} run summon minecraft:creeper ~ ~ ~"

    if send_rcon(cmd):
        await message.answer("✅ Крипер заспавнен!")
    else:
        await message.answer("❌ Не удалось отправить команду на сервер")

@dp.message(Command("dragon"))
async def spawn_dragon(message: Message):
    cmd = f"execute at {username} run summon minecraft:ender_dragon ~ ~ ~"

    if send_rcon(cmd):
        await message.answer("✅ Ender Dragon заспавнен!") 
    else:
        await message.answer("❌ Не удалось отправить команду на сервер")

@dp.message(Command("ghast"))
async def spawn_ghast(message: Message):
    cmd = f"execute at {username} run summon minecraft:ghast ~ ~ ~"

    if send_rcon(cmd):
        await message.answer("✅ Гаст заспавнен!")
    else:
        await message.answer("❌ Не удалось отправить команду на сервер")

@dp.message(Command("wither"))
async def spawn_wither(message: Message):
    cmd = f"execute at {username} run summon minecraft:wither ~ ~ ~"

    if send_rcon(cmd):
        await message.answer("✅ Визер заспавнен!") 
    else:
        await message.answer("❌ Не удалось отправить команду на сервер")

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())