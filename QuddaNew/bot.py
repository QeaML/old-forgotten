from discord.ext import commands
import discord
import json
import traceback
import pickledb


initial_extensions = (
    "cogs.xp",
    "cogs.errors",
    "cogs.admin",
    "cogs.minigames",
    "cogs.nobluff",
    "cogs.settings",
)


class Qudaa(commands.Bot):
    def __init__(self):
        config = {}
        with open("config.json") as f:
            config = json.loads(f.read())

        super(Qudaa, self).__init__(
            command_prefix=self.get_prefix,
            case_insensitive=True,
            description="Qudda v0.3.2",
        )

        self.config = config
        self.prefixdb = pickledb.load("data\\prefix.db", True)

        for extension in initial_extensions:
            try:
                self.load_extension(extension)
            except:
                print(f"Error while loading extension: {extension}")
                traceback.print_exc()
            else:
                print(f"Successfully loaded extension: {extension}")

    async def on_connect(self):
        await self.change_presence(status=discord.Status.idle)
        print("Connected!")

    async def on_ready(self):
        await self.change_presence(
            activity=discord.Game(name=f"q?help")
        )
        print(f"Ready! Logged in as {self.user}.")

    async def on_disconnect(self):
        print("Disconnected :(")

    async def get_prefix(self, msg) -> list:
        in_db = self.prefixdb.get(str(msg.guild.id))
        if in_db:
            return in_db
        return ["q?"]

    async def set_prefix(self, guild_id, prefixes):
        self.prefixdb.set(str(guild_id), prefixes)

    def go(self):
        self.run(self.config["token"])
