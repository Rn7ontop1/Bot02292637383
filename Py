import discord
from discord.ext import tasks, commands
import asyncio

# ضع هنا توكن البوت
TOKEN = "MTQ0NjYwNjU1MTcwMjgzMTMwNQ.Gg6CQ_.r3BC2JZ6o6RDlqtsJyl7v8rLfXvxyuroz5DmGM"

# ضع هنا ID الروم اللي تريد البوت يرسل فيه الرسائل
CHANNEL_ID = 1394385787323285574  # استبدل بالـID الخاص بالروم

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    send_message.start()  # تشغيل المهمة بعد دخول البوت

@tasks.loop(seconds=15)  # كل 15 ثانية
async def send_message():
    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        await channel.send("السلام عليكم ورحمة الله وبركاته")
    else:
        print("الروم غير موجود!")

bot.run(TOKEN)
