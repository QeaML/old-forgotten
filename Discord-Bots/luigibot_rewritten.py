import discord
from random import randint

bot = discord.Client()

prefix = "l?"

@bot.event
async def on_connect():
	print(f"Connected. Logged in as {bot.user}")

@bot.event
async def on_ready():
	await bot.change_presence(activity=discord.Game(name=prefix+"help"))
	print("Ready")

@bot.event
async def on_message(message):
	if not message.author.bot and (message.guild is not None and message.content.startswith(prefix)):
		arg = message.content.split(" ")[1:]
		cmd = message.content.lower().split(" ")[0][len(prefix):]
		if cmd == "hi":
			await message.channel.send("Hello, my name is Labut.")
		elif cmd == "blah":
			await message.channel.send("blah *blah* **blah** ***blah***")
		elif cmd == "macandcheese":
			await message.channel.send(f"Here, have some Mac and Cheese. *gives mac and cheese to <@{message.author.id}>*")
		elif cmd == "fastfood":
			await message.channel.send(f"Here, have some Fastfood. *gives hamburger and fries to <@{message.author.id}>*")
		elif cmd == "randomnumber":
			await message.channel.send(str(randint(0, 1000)))
		elif cmd == "help":
			await message.channel.send("**Labut help**\nl?help - shows this\nl?hi - says hello to you\nl?blah - does the blah blah blah thing\nl?macandcheese - gives you mac and cheese\nl?fastfood - gives you fastfood\nl?kill <victim> - kill the specified victim\nl?succ - ***s u c c***\nl?dicklength - shows the length of your dick\nl?credits - credits")
		elif cmd == "kill":
			try:
				victim = arg[0]
				await message.channel.send(f"**Loud screams of {victim}**")
			except:
				await message.channel.send("You need to specify what do you want to kill!")
		elif cmd == "succ":
			dicks = randint(0, 25)
			await message.channel.send(f"You have succ'd {dicks} dicks.")
		elif cmd == "dicklength":
			length = randint(-10, 20)
			await message.channel.send(f"Your dick is {length}cm long.")
		elif cmd == "credits":
			await message.channel.send("Original creator: <@490169798244958208>\nRewritten by: <@396699211946655745>")
				
bot.run("token")
