from discord.ext import tasks, commands
import discord
from typing import Optional
import pickledb


class XP(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.cooldowns = {}
        self.xp_db = pickledb.load("data\\xp.db", True)
        self.vault_db = pickledb.load("data\\vault.db", True)

    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.guild is None or msg.author.bot:
            return

        if self.get_cooldown(str(msg.author.id)) == 0:
            amt = self.xp_db.get(str(msg.author.id))
            if not amt:
                amt = 0

            self.xp_db.set(str(msg.author.id), amt + 1)
            self.set_cooldown(str(msg.author.id), 15)

    @tasks.loop(seconds=1.0)
    async def cooldown_loop(self):
        for cooldown in self.cooldowns.keys():
            self.cooldowns[cooldown] -= 1
            if self.cooldowns[cooldown] == 0:
                del self.cooldowns[cooldown]

    def get_cooldown(self, name: str) -> int:
        if name in self.cooldowns:
            return self.cooldowns[name]
        else:
            return 0

    def set_cooldown(self, name: str, amt: int):
        self.cooldowns[name] = amt

    async def get_xp(self, user) -> int:
        user = str(user)
        xp_amt = self.xp_db.get(user)
        if not xp_amt:
            return 0
        else:
            return xp_amt

    async def set_xp(self, user, amt):
        user = str(user)
        return self.xp_db.set(user, int(amt))

    async def get_vault(self, user) -> int:
        user = str(user)
        xp_amt = self.vault_db.get(user)
        if not xp_amt:
            return 0
        else:
            return xp_amt

    async def set_vault(self, user, amt):
        user = str(user)
        return self.vault_db.set(user, int(amt))

    @commands.command()
    async def xp(self, ctx, *, user: Optional[discord.Member]):
        """See your or the mentioned user's XP amount."""
        if user:
            user_id = user.id
        else:
            user_id = ctx.author.id

        xp_amt = self.xp_db.get(str(user_id))

        if not xp_amt:
            xp_amt = 0

        if user:
            await ctx.send(f"**{user.display_name}** has **{xp_amt}** XP points.")
        else:
            await ctx.send(f"You have **{xp_amt}** XP points.")

    @commands.command()
    async def vault(self, ctx):
        """See the balance of your vault"""
        vault_amt = self.vault_db.get(str(ctx.author.id))

        if not vault_amt:
            vault_amt = 0

        await ctx.send(f"You have **{vault_amt}** XP points in your vault.")

    @commands.command()
    async def deposit(self, ctx, *, amt: int):
        """Deposit XP points into your vault"""
        if amt <= 0:
            return await ctx.send("The amount can't be 0 or below!")

        xp_amt = self.xp_db.get(str(ctx.author.id))

        if not xp_amt:
            xp_amt = 0

        if amt > xp_amt:
            return await ctx.send("You don't have that many XP points!")

        vault_amt = self.vault_db.get(str(ctx.author.id))

        if not vault_amt:
            vault_amt = 0

        self.vault_db.set(str(ctx.author.id), vault_amt + amt)
        self.xp_db.set(str(ctx.author.id), xp_amt - amt)

        await ctx.send(f"Successfully deposited **{amt}** XP points into your vault.")

    @commands.command()
    async def withdraw(self, ctx, *, amt: int):
        """Withdraw XP points from your vault"""
        if amt <= 0:
            return await ctx.send("The amount can't be 0 or below!")

        vault_amt = self.vault_db.get(str(ctx.author.id))

        if not vault_amt:
            vault_amt = 0

        if amt > vault_amt:
            return await ctx.send("You don't have that many XP points in your vault!")

        xp_amt = self.xp_db.get(str(ctx.author.id))

        if not xp_amt:
            xp_amt = 0

        self.xp_db.set(str(ctx.author.id), xp_amt + amt)
        self.vault_db.set(str(ctx.author.id), vault_amt - amt)

        await ctx.send(f"Successfully withdrew **{amt}** XP points from your vault.")


def setup(bot):
    bot.add_cog(XP(bot))
