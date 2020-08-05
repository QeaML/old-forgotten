from discord.ext import tasks, commands
from random import randint, choice


class Minigames(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        self.gsr_games = {}
        self.gsr_diff = {
            "easy": (5, 10),
            "medium": (10, 25),
            "hard": (25, 75),
            "hardest": (75, 300),
        }

        self.scr_games = {}
        with open("data\\scramble_words.txt") as fh:
            self.scr_words = fh.read().split("\n")

        self.cnt_games = {}

        self.cooldown.start()

    def cog_unload(self):
        self.cooldown.cancel()

    @tasks.loop(seconds=1)
    async def cooldown(self):
        async def withdict(d):
            for u in d.keys():
                d[u][2] -= 1
                if d[u][2] == 0:
                    ch = self.bot.get_channel(d[u][3])
                    await ch.send(
                        "You took too long to guess! " f"The answer was {d[u][0]}."
                    )
                    del d[u]

        await withdict(self.gsr_games)
        await withdict(self.scr_games)

    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.author.bot or msg.guild is None:
            return
        prefix = await self.bot.get_prefix(msg)
        if True in [msg.content.startswith(p) for p in prefix]:
            return

        u = str(msg.author.id)
        # [answer, tries, cooldown, channel]
        if u in self.gsr_games.keys():
            if self.gsr_games[u][3] == msg.channel.id:
                self.gsr_games[u][1] += 1
                self.gsr_games[u][2] = 30
                v = self.gsr_games[u][0]
                t = self.gsr_games[u][1]

                try:
                    n = int(msg.content)
                except ValueError:
                    await msg.channel.send("That's not a valid number!")
                else:

                    if n > v:
                        await msg.channel.send("Too big!")
                    elif n < v:
                        await msg.channel.send("Too low!")
                    elif n == v:
                        r_n = 25 - (t * 5)
                        if r_n < 0:
                            r_n = 0

                        r = r_n + 5
                        if t <= 2:
                            r *= 1.5

                        r_d = 0

                        for diff in self.gsr_diff.keys():
                            d = self.gsr_diff[diff]
                            r_d += 1
                            if d[0] > v and d[1] < v:
                                break

                        r = int(r * r_d)

                        xp_cog = self.bot.get_cog("XP")
                        xp_amt = await xp_cog.get_xp(u)

                        await xp_cog.set_xp(u, xp_amt + r)

                        await msg.channel.send(
                            "You guessed it! " f"You got **{r}** XP for guessing."
                        )
                        del self.gsr_games[u]
        elif u in self.scr_games.keys():
            if self.scr_games[u][3] == msg.channel.id:
                self.scr_games[u][1] += 1
                self.scr_games[u][2] = 30
                v = self.scr_games[u][0]
                t = self.scr_games[u][1]

                if n != v:
                    await msg.channel.send("That's not it!")
                elif n == v:
                    r_n = 25 - (t * 5)
                    if r_n < 0:
                        r_n = 0
                    r = r_n + 5

                    if t <= 2:
                        r *= 1.5

                    r = int(r)

                    xp_cog = self.bot.get_cog("XP")
                    xp_amt = await xp_cog.get_xp(u)

                    await xp_cog.set_xp(u, xp_amt + r)

                    await msg.channel.send(
                        "You guessed it! " f"You got **{r}** XP for guessing."
                    )
                    del self.gsr_games[u]
        """elif u in self.cnt_games.keys():
            if self.cnt_games[u][3] == msg.channel.id:
                self.cnt_games[u][1] += 1
                self.cnt_games[u][2] = 30
                v = self.cnt_games[u][0]
                t = self.cnt_games[u][1]

                try:
                    n = int(msg.content)
                except ValueError:
                    if t >= v // 2:
                        await msg.channel.send(
                            "You messed up!"
                        )"""

    def gsr_randint(self, min: int, max: int) -> int:
        numbers = [randint(min, max) for x in range(0, 3)]
        numbers_even = [n for n in numbers if n % 2 == 0]
        numbers_even_3div = [n for n in numbers_even if n % 3 == 0]

        if len(numbers_even_3div) != 0:
            return choice(numbers_even_3div)
        elif len(numbers_even) != 0:
            return choice(numbers_even)
        else:
            return choice(numbers)

    @commands.command()
    async def guesser(self, ctx, *, difficulty: str):
        """Start a game of Guesser
        About Guesser:
        When a game is started, start guessing numbers between the bounds given when \
the game starts. You should also know that even numbers and numbers divisible \
by 3 are more common than those which aren't."""
        difficulty = difficulty.lower()

        if difficulty in self.gsr_diff.keys():
            diff = self.gsr_diff[difficulty]
        else:
            return await ctx.send(
                "That's not a valid difficulty! "
                "Choose one of: `easy`, `medium`, `hard`, `hardest`."
            )

        n = self.gsr_randint(*diff)
        t = 0
        cl = 30
        ch = ctx.channel.id
        u = str(ctx.author.id)

        self.gsr_games[u] = [n, t, cl, ch]

        await ctx.send(
            "You have started a game of Guesser! "
            f"Start guessing numbers from {diff[0]} to {diff[1] - 1}."
        )


def setup(bot):
    bot.add_cog(Minigames(bot))
