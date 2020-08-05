import discord
import logMe as logger
from random import randint

client = discord.Client()
commandSymbol = "dude,"
a = 0

@client.event
async def on_ready():
	logger.info('logged in as '+str(client.user.name))

@client.event
async def on_message(message):
	a = 0
	mssg = str(message.content).split(' ')
	if message.author == client.user:
		return
	else:
		if mssg[0] == commandSymbol+"hello":
		await message.channel.send('you too <@'+str(message.author.id)+'> i guess')
		logger.info('executed hello')
	if mssg[0] == commandSymbol+"credits":
		await message.channel.send("Annoying Bot created by QeaML, using discord.py.")
		logger.info('executed credits')
	if mssg[0] == commandSymbol+"spam":
		logger.info('executed credits')
		while a < 10:
			await message.channel.send("ok")
			a = int(a) + 1
	if not commandSymbol in mssg[0] and message.author.bot != True:
		logger.info(str(message.author.name)+' said '+str(message.content))
		randomNumber = randint(0,32)
		logger.info('rolled '+str(randomNumber))
		if randomNumber == 0:
			await message.channel.send("perhaps")
			logger.info("replied perhaps")
		if randomNumber == 1:
			await message.channel.send("yes")
			logger.info("replied yes")
		if randomNumber == 2:
			await message.channel.send("no")
			logger.info("replied no")
		if randomNumber == 3:
			await message.channel.send("maaaybe ;)")
			logger.info("replied maaaybe ;)")
		if randomNumber == 4:
			await message.channel.send("bitch why you askin'")
			logger.info("replied bitch why you askin'")
		if randomNumber == 5:
			await message.channel.send("go suck a dick")
			logger.info("replied go suck a dick")
		if randomNumber == 6:
			await message.channel.send("i ain't answering that")
			logger.info("replied i ain't answering that")
		if randomNumber == 7:
			await message.channel.send("fuck you too")
			logger.info("replied fuck you too")
		if randomNumber == 8:
			await message.channel.send("yesn't")
			logger.info("replied yesn't")

client.run('aaa')


