from discord.ext import commands


class Reactions(commands.Cog):
    '''Idk what to write'''

    def __init__(self,bot):
        self.bot = bot

    # bot.events -> commands.Cog.listener
    @commands.Cog.listener()
    async def on_reaction_add(self,reaction,user):
        print(reaction.emoji)
        if reaction.emoji == '👍':
            role = user.guild.get_role(1005525459473268866)
            await user.add_roles(role)
        elif reaction.emoji =='💩':
            role = user.guild.get_role(1005525659377991761)
        await user.add_roles(role)

def setup(bot):
    bot.add_cog(Reactions(bot))