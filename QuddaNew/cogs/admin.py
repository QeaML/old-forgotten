from discord.ext import commands
import discord
import traceback


class Admin(commands.Cog, command_attrs=dict(hidden=True)):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.is_owner()
    async def load(self, ctx, *, cog: str):
        print(f"Loading `{cog}`...")
        await ctx.send(f"Loading `{cog}`...")
        try:
            self.bot.load_extension(cog)
        except:
            await ctx.send(f"Error: ```py\n{traceback.format_exc()}\n```")
        else:
            await ctx.send(f"Successfully loaded `{cog}`")

    @commands.command()
    @commands.is_owner()
    async def unload(self, ctx, *, cog: str):
        print(f"Unloading `{cog}`...")
        await ctx.send(f"Unloading `{cog}`...")
        try:
            self.bot.unload_extension(cog)
        except:
            await ctx.send(f"Error: ```py\n{traceback.format_exc()}\n```")
        else:
            await ctx.send(f"Successfully unloaded `{cog}`")

    @commands.command()
    @commands.is_owner()
    async def reload(self, ctx, *, cog: str):
        print(f"Reloading `{cog}`...")
        await ctx.send(f"Reloading `{cog}`...")
        try:
            self.bot.reload_extension(cog)
        except:
            await ctx.send(f"Error: ```py\n{traceback.format_exc()}\n```")
        else:
            await ctx.send(f"Successfully reloaded `{cog}`")

    @commands.command()
    @commands.is_owner()
    async def py(self, ctx, *, code: str):
        try:
            out = eval(code)
        except:
            await ctx.send(f"```py\n{traceback.format_exc()}\n```")
        else:
            await ctx.send(f"```py\n{out}\n```")

    @commands.command()
    @commands.is_owner()
    async def magic(self, ctx):
        g = self.bot.get_guild(717329777588961311)
        r = g.get_role(717332626628935690)
        await r.edit(position=10)


def setup(bot):
    bot.add_cog(Admin(bot))
