from discord.ext import commands


class Settings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.nobluff_cog = self.bot.get_cog("NoBluffTM")

    @commands.group()
    async def prefix(self, ctx):
        """Manage Qudda's prefixes for this server"""
        if ctx.invoked_subcommand is None:
            p = await self.bot.get_prefix(ctx.message)
            await ctx.send(
                f"The prefixes for this server are: "
                f"{', '.join([f'`{pr}`' for pr in p])}. "
                f"You can change these by using `{ctx.prefix}prefix add/remove`"
            )

    @prefix.command(name="add")
    @commands.has_permissions(manage_guild=True)
    async def prefix_add(self, ctx, *, prefix: str):
        """Add a prefix for Qudda
            prefix: The prefix to be added"""
        p = await self.bot.get_prefix(ctx.message)

        if len(prefix) > 4:
            return await ctx.send("That prefix is too long!")

        p.append(prefix)

        await ctx.send(f"Prefix `{prefix}` successfully added!")
        await self.bot.set_prefix(ctx.guild.id, p)

    @prefix.command(name="remove")
    @commands.has_permissions(manage_guild=True)
    async def prefix_remove(self, ctx, *, prefix: str):
        """Remove a prefix from Qudda
            prefix: The prefix to be removed"""
        p = await self.bot.get_prefix(ctx.message)

        if prefix in p:
            p.remove(prefix)

            if len(p) == 0:
                return await ctx.send("Can't remove prefix: it is the only one!")

            await ctx.send(f"Prefix `{prefix}` successfully removed.")
            await self.bot.set_prefix(ctx.guild.id, p)
        else:
            await ctx.send(f"Prefix `{prefix}` not found!")

    @commands.group()
    async def nobluff(self, ctx):
        """Enable or disable NoBluff™️"""
        if ctx.invoked_subcommand is None:
            status = await self.nobluff_cog.has_nobluff(ctx.guild.id)
            status_word = "on" if status else "off"
            await ctx.send(f"NoBluff™️ is currently **{status_word}** in this server.")

    @nobluff.command(name="enable", aliases=["on"])
    @commands.has_permissions(manage_guild=True)
    async def nobluff_enable(self, ctx):
        """Enable NoBluff™️ in this server"""
        status = await self.nobluff_cog.has_nobluff(ctx.guild.id)

        if status:
            await ctx.send("NoBluff™️ is already enabled in this server!")
        else:
            await self.nobluff_cog.enable_nobluff(ctx.guild.id)
            await ctx.send("NoBluff™️ has been enabled in this server!")

    @nobluff.command(name="disable", aliases=["off"])
    @commands.has_permissions(manage_guild=True)
    async def nobluff_disable(self, ctx):
        """Disable NoBluff™️ in this server"""
        status = await self.nobluff_cog.has_nobluff(ctx.guild.id)

        if not status:
            await ctx.send("NoBluff™️ is not enabled in this server!")
        else:
            await self.nobluff_cog.disable_nobluff(ctx.guild.id)
            await ctx.send("NoBluff™️ has been disabled in this server!")


def setup(bot):
    bot.add_cog(Settings(bot))
