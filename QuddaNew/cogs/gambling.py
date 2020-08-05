from discord.ext import commands
import discord
import random


class Gambling(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def gamble(self, ctx, *, amt: int):
        """Gamble a certain amount of your XP."""
        em = discord.Embed()
        xp = self.bot.get_cog("XP")
        bal = await xp.get_xp(ctx.author.id)

        if amt > bal:
            return await ctx.send("You don't have that many XP points!")

        playerroll = random.randint(0, 101)
        botroll = random.randint(0, 86)
        multiplier = random.randint(50, 201) / 100
        total = int(amt * multiplier)
        em.add_field(name="You", value=playerroll)
        em.add_field(name="Qudaa", value=botroll)
        em.set_footer(text=f"Multiplier: {multiplier}x")

        if playerroll > botroll:
            em.color = 0x00FF00
            em.add_field(
                name="You win!",
                value="Your number was higher than mine. " f"You win {total} XP.",
                inline=False,
            )
            await xp.set_xp(ctx.author.id, bal + total)
        elif playerroll == botroll:
            em.color = 0xFFFF00
            em.add_field(
                name="It's a tie!",
                value="Our numbers were the same. "
                "You don't win anything, but you didn't lose either.",
                inline=False,
            )
        elif playerroll < botroll:
            em.color = 0xFF0000
            em.add_field(
                name="You lose!",
                value="Your number was lower than mine. " f"You lose {total} XP.",
                inline=False,
            )
            await xp.set_xp(ctx.author.id, bal - total)

        await ctx.send(embed=em)


def setup(bot):
    bot.add_cog(Gambling(bot))
