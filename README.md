# final-staff
git repo for final project of CIS1051 Spring 2024

    import discord

    class Client(discord.Client): #This is how a bot runs
        async def on_ready(self): #This will be called whenever the bot turns on
            print(f'Logged on as {self.user}!')
        
        async def on_message(delf,message):
            if message.author == client.user:
                return
            
            if message.content.startswith("$hello"):
                await message.channel.send("Hello!")
    
    
    intents = discord.Intents.default()
    intents.message_content = True
    
    client = Client(intents=intents)
    client.run('(bottoken')
