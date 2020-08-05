import pickledb
from discord.ext import commands


class NoBluffTM(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.nobluff_db = pickledb.load(r"data\nobluff.db", True)

    async def enable_nobluff(self, guild_id: int):
        self.nobluff_db.set(str(guild_id), True)

    async def disable_nobluff(self, guild_id: int):
        self.nobluff_db.set(str(guild_id), False)

    async def has_nobluff(self, guild_id: int):
        return self.nobluff_db.get(str(guild_id))

    @commands.Cog.listener()
    async def on_message_delete(self, msg):
        if msg.guild is None:
            return
        if self.nobluff_db.get(str(msg.guild.id)):
            if msg.author.id == self.bot.user.id and msg.content.startswith(
                "*NoBluff™️*"
            ):
                await msg.channel.send(msg.content)
            else:
                await msg.channel.send(
                    f"*NoBluff™️* <@{msg.author.id}>'s message was deleted.\n"
                    f'"{msg.content}"'
                )

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        if before.guild is None:
            return
        if self.nobluff_db.get(str(before.guild.id)):
            if before.author.id == self.bot.user.id:
                return
            else:
                await before.channel.send(
                    f"*NoBluff™️* <@{before.author.id}> edited their message.\n"
                    f"Before: {before.content}\n"
                    f"After: {after.content}"
                )


def setup(bot):
    bot.add_cog(NoBluffTM(bot))
