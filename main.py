import discord
from discord.ext import commands
from discord import app_commands

embedColor = 0x2d4bff
bot = commands.Bot(command_prefix = None, intents = discord.Intents.default())

class Slowmode(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    @app_commands.command(name = "slowmode_text", description = "Set the slowmode delay in a specific text channel for any amount of time")
    async def slowmode_text(self, interaction:discord.Interaction, text_channel:discord.TextChannel, seconds:int):
        if seconds < 0:
            embedf = discord.Embed(title = "A channel's slowmode delay cannot be negative", color = embedColor)
            embedf.set_footer(text = "Setback - Easily manage channels in you Discord server", icon_url = "https://th.bing.com/th?id=OIP.Ltkr1NZQvMBf26kRVcHx9AHaHa&w=250&h=250&c=8&rs=1&qlt=90&o=6&cb=13&dpr=1.5&pid=3.1&rm=2")
            await interaction.response.send_message(embed = embedf, ephemeral = True)
            return

        bot_member: discord.Member = interaction.guild.get_member(bot.application_id)
        perms = bot_member.guild_permissions.manage_channels

        user_member: discord.Member = interaction.user
        user_perms = user_member.guild_permissions.moderate_members

        if user_perms:
            if perms:
                await text_channel.edit(slowmode_delay = seconds)
                embed = discord.Embed(title = f"Slowmode delay set to {seconds} seconds for {text_channel.mention}", color = embedColor)
                embed.set_footer(text = "Setback - Easily manage channels in you Discord server", icon_url = "https://th.bing.com/th?id=OIP.Ltkr1NZQvMBf26kRVcHx9AHaHa&w=250&h=250&c=8&rs=1&qlt=90&o=6&cb=13&dpr=1.5&pid=3.1&rm=2")
                await interaction.response.send_message(embed = embed, ephemeral = True)
            else:
                embed = discord.Embed(title = f"You must enable the global **`Manage Channels`** permission for the bot to run this command", color = embedColor)
                embed.set_footer(text = "Setback - Easily manage channels in you Discord server", icon_url = "https://th.bing.com/th?id=OIP.Ltkr1NZQvMBf26kRVcHx9AHaHa&w=250&h=250&c=8&rs=1&qlt=90&o=6&cb=13&dpr=1.5&pid=3.1&rm=2")
                await interaction.response.send_message(embed = embed, ephemeral = True)
        else:
            embed = discord.Embed(title = f"You don't have permission to do that", color = embedColor)
            embed.set_footer(text = "Setback - Easily manage channels in you Discord server", icon_url = "https://th.bing.com/th?id=OIP.Ltkr1NZQvMBf26kRVcHx9AHaHa&w=250&h=250&c=8&rs=1&qlt=90&o=6&cb=13&dpr=1.5&pid=3.1&rm=2")
            await interaction.response.send_message(embed = embed, ephemeral = True)

    @app_commands.command(name = "slowmode_vc", description = "Set the slowmode delay in a specific voice channel for any amount of time")
    async def slowmode_vc(self, interaction:discord.Interaction, voice_channel:discord.VoiceChannel, seconds:int):
        if seconds < 0:
            embedf = discord.Embed(title = "A channel's slowmode delay cannot be negative", color = embedColor)
            embedf.set_footer(text = "Setback - Easily manage channels in you Discord server", icon_url = "https://th.bing.com/th?id=OIP.Ltkr1NZQvMBf26kRVcHx9AHaHa&w=250&h=250&c=8&rs=1&qlt=90&o=6&cb=13&dpr=1.5&pid=3.1&rm=2")
            await interaction.response.send_message(embed = embedf, ephemeral = True)
            return

        bot_member: discord.Member = interaction.guild.get_member(bot.application_id)
        perms = bot_member.guild_permissions.manage_channels

        user_member: discord.Member = interaction.user
        user_perms = user_member.guild_permissions.moderate_members

        if user_perms:
            if perms:
                await voice_channel.edit(slowmode_delay = seconds)
                embed = discord.Embed(title = f"Slowmode delay set to {seconds} seconds for {voice_channel.mention}", color = embedColor)
                embed.set_footer(text = "Setback - Easily manage channels in you Discord server", icon_url = "https://th.bing.com/th?id=OIP.Ltkr1NZQvMBf26kRVcHx9AHaHa&w=250&h=250&c=8&rs=1&qlt=90&o=6&cb=13&dpr=1.5&pid=3.1&rm=2")
                await interaction.response.send_message(embed = embed, ephemeral = True)
            else:
                embed = discord.Embed(title = f"You must enable the global **`Manage Channels`** permission for the bot to run this command", color = embedColor)
                embed.set_footer(text = "Setback - Easily manage channels in you Discord server", icon_url = "https://th.bing.com/th?id=OIP.Ltkr1NZQvMBf26kRVcHx9AHaHa&w=250&h=250&c=8&rs=1&qlt=90&o=6&cb=13&dpr=1.5&pid=3.1&rm=2")
                await interaction.response.send_message(embed = embed, ephemeral = True)
        else:
            embed = discord.Embed(title = f"You don't have permission to do that", color = embedColor)
            embed.set_footer(text = "Setback - Easily manage channels in you Discord server", icon_url = "https://th.bing.com/th?id=OIP.Ltkr1NZQvMBf26kRVcHx9AHaHa&w=250&h=250&c=8&rs=1&qlt=90&o=6&cb=13&dpr=1.5&pid=3.1&rm=2")
            await interaction.response.send_message(embed = embed, ephemeral = True)

    @app_commands.command(name = "slowmode_forum", description = "Set the slowmode delay in a specific forum channel for any amount of time")
    async def slowmode_forum(self, interaction:discord.Interaction, forum_channel:discord.ForumChannel, seconds:int):
        if seconds < 0:
            embedf = discord.Embed(title = "A channel's slowmode delay cannot be negative", color = embedColor)
            embedf.set_footer(text = "Setback - Easily manage channels in you Discord server", icon_url = "https://th.bing.com/th?id=OIP.Ltkr1NZQvMBf26kRVcHx9AHaHa&w=250&h=250&c=8&rs=1&qlt=90&o=6&cb=13&dpr=1.5&pid=3.1&rm=2")
            await interaction.response.send_message(embed = embedf, ephemeral = True)
            return
        
        bot_member: discord.Member = interaction.guild.get_member(bot.application_id)
        perms = bot_member.guild_permissions.manage_channels

        user_member: discord.Member = interaction.user
        user_perms = user_member.guild_permissions.moderate_members

        if user_perms:
            if perms:
                await forum_channel.edit(slowmode_delay = seconds)
                embed = discord.Embed(title = f"Slowmode delay set to {seconds} seconds for {forum_channel.mention}", color = embedColor)
                embed.set_footer(text = "Setback - Easily manage channels in you Discord server", icon_url = "https://th.bing.com/th?id=OIP.Ltkr1NZQvMBf26kRVcHx9AHaHa&w=250&h=250&c=8&rs=1&qlt=90&o=6&cb=13&dpr=1.5&pid=3.1&rm=2")
                await interaction.response.send_message(embed = embed, ephemeral = True)
            else:
                embed = discord.Embed(title = f"You must enable the global **`Manage Channels`** permission for the bot to run this command", color = embedColor)
                embed.set_footer(text = "Setback - Easily manage channels in you Discord server", icon_url = "https://th.bing.com/th?id=OIP.Ltkr1NZQvMBf26kRVcHx9AHaHa&w=250&h=250&c=8&rs=1&qlt=90&o=6&cb=13&dpr=1.5&pid=3.1&rm=2")
                await interaction.response.send_message(embed = embed, ephemeral = True)
        else:
            embed = discord.Embed(title = f"You don't have permission to do that", color = embedColor)
            embed.set_footer(text = "Setback - Easily manage channels in you Discord server", icon_url = "https://th.bing.com/th?id=OIP.Ltkr1NZQvMBf26kRVcHx9AHaHa&w=250&h=250&c=8&rs=1&qlt=90&o=6&cb=13&dpr=1.5&pid=3.1&rm=2")
            await interaction.response.send_message(embed = embed, ephemeral = True)

    @app_commands.command(name = "slowmode_stage", description = "Set the slowmode delay in a specific stage channel for any amount of time")
    async def slowmode_stage(self, interaction:discord.Interaction, stage_channel:discord.StageChannel, seconds:int):
        if seconds < 0:
            embedf = discord.Embed(title = "A channel's slowmode delay cannot be negative", color = embedColor)
            embedf.set_footer(text = "Setback - Easily manage channels in you Discord server", icon_url = "https://th.bing.com/th?id=OIP.Ltkr1NZQvMBf26kRVcHx9AHaHa&w=250&h=250&c=8&rs=1&qlt=90&o=6&cb=13&dpr=1.5&pid=3.1&rm=2")
            await interaction.response.send_message(embed = embedf, ephemeral = True)
            return
        
        bot_member: discord.Member = interaction.guild.get_member(bot.application_id)
        perms = bot_member.guild_permissions.manage_channels

        user_member: discord.Member = interaction.user
        user_perms = user_member.guild_permissions.moderate_members

        if user_perms:
            if perms:
                await stage_channel.edit(slowmode_delay = seconds)
                embed = discord.Embed(title = f"Slowmode delay set to {seconds} seconds for {stage_channel.mention}", color = embedColor)
                embed.set_footer(text = "Setback - Easily manage channels in you Discord server", icon_url = "https://th.bing.com/th?id=OIP.Ltkr1NZQvMBf26kRVcHx9AHaHa&w=250&h=250&c=8&rs=1&qlt=90&o=6&cb=13&dpr=1.5&pid=3.1&rm=2")
                await interaction.response.send_message(embed = embed, ephemeral = True)
            else:
                embed = discord.Embed(title = f"You must enable the global **`Manage Channels`** permission for the bot to run this command", color = embedColor)
                embed.set_footer(text = "Setback - Easily manage channels in you Discord server", icon_url = "https://th.bing.com/th?id=OIP.Ltkr1NZQvMBf26kRVcHx9AHaHa&w=250&h=250&c=8&rs=1&qlt=90&o=6&cb=13&dpr=1.5&pid=3.1&rm=2")
                await interaction.response.send_message(embed = embed, ephemeral = True)
        else:
            embed = discord.Embed(title = f"You don't have permission to do that", color = embedColor)
            embed.set_footer(text = "Setback - Easily manage channels in you Discord server", icon_url = "https://th.bing.com/th?id=OIP.Ltkr1NZQvMBf26kRVcHx9AHaHa&w=250&h=250&c=8&rs=1&qlt=90&o=6&cb=13&dpr=1.5&pid=3.1&rm=2")
            await interaction.response.send_message(embed = embed, ephemeral = True)

class Timeout(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    @app_commands.command(name = "timeout", description = "Timeout a user for any amount of time")
    async def timeout(self, interaction:discord.Interaction, user:discord.Member, seconds:int = 0, minutes:int = 0, hours:int = 0, days:int = 0, reason:str = ""):
        length = seconds + minutes * 60 + hours * 3600 + days * 86400
        if length < 1:
            embedf = discord.Embed(title = "A user cannot be timed out negative amount of time", color = embedColor)
            embedf.set_footer(text = "Setback - Easily manage channels in you Discord server", icon_url = "https://th.bing.com/th?id=OIP.Ltkr1NZQvMBf26kRVcHx9AHaHa&w=250&h=250&c=8&rs=1&qlt=90&o=6&cb=13&dpr=1.5&pid=3.1&rm=2")
            await interaction.response.send_message(embed = embedf, ephemeral = True)
            return
        
        import datetime
        time_delta = datetime.timedelta(seconds = length)

        bot_member: discord.Member = interaction.guild.get_member(bot.application_id)
        bot_perms = bot_member.guild_permissions.moderate_members

        user_member: discord.Member = interaction.user
        user_perms = user_member.guild_permissions.moderate_members

        if user_perms:
            if bot_perms:
                await user.timeout(time_delta, reason = reason)
                embed = discord.Embed(title = f"{user.display_name} has been timed out for {days} days, {hours} hours, {minutes} minutes, and {seconds} seconds", color = embedColor)
                embed.set_footer(text = "Setback - Easily manage channels in you Discord server", icon_url = "https://th.bing.com/th?id=OIP.Ltkr1NZQvMBf26kRVcHx9AHaHa&w=250&h=250&c=8&rs=1&qlt=90&o=6&cb=13&dpr=1.5&pid=3.1&rm=2")
                await interaction.response.send_message(embed = embed, ephemeral = True)
            else:
                embed = discord.Embed(title = f"You must enable the global **`Timeout Members`** permission for the bot to run this command", color = embedColor)
                embed.set_footer(text = "Setback - Easily manage channels in you Discord server", icon_url = "https://th.bing.com/th?id=OIP.Ltkr1NZQvMBf26kRVcHx9AHaHa&w=250&h=250&c=8&rs=1&qlt=90&o=6&cb=13&dpr=1.5&pid=3.1&rm=2")
                await interaction.response.send_message(embed = embed, ephemeral = True)
        else:
            embed = discord.Embed(title = f"You don't have permission to do that", color = embedColor)
            embed.set_footer(text = "Setback - Easily manage channels in you Discord server", icon_url = "https://th.bing.com/th?id=OIP.Ltkr1NZQvMBf26kRVcHx9AHaHa&w=250&h=250&c=8&rs=1&qlt=90&o=6&cb=13&dpr=1.5&pid=3.1&rm=2")
            await interaction.response.send_message(embed = embed, ephemeral = True)

@bot.event
async def on_ready():
    await bot.change_presence(status = discord.Status.online)
    await bot.add_cog(Slowmode(bot))
    await bot.add_cog(Timeout(bot))
    await bot.tree.sync()

bot.run("TOKEN")