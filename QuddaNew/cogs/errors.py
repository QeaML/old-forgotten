from discord.ext import commands
import traceback


class ErrorHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, err):
        exc = err.__class__

        # print(err)
        # print(err.with_traceback)
        # print(dir(err))

        if exc == commands.MissingRequiredArgument:
            return await ctx.send("Not enough parameters!")

        if exc == commands.BadArgument:
            return await ctx.send("One or more parameters are invalid!")

        if exc == commands.CheckFailure:
            return await ctx.send("You can't use this command!")

        if exc == commands.CommandNotFound:
            return

        await ctx.send(f"Error!\n```py\n{exc}: {err.__cause__}\n```")


def setup(bot):
    bot.add_cog(ErrorHandler(bot))
