# final-staff
git repo for final project of CIS1051 Spring 2024

    import discord

    class Client(discord.Client): 
        async def on_ready(self): 
            print(f'Logged on as {self.user}!')
        
        async def on_message(delf,message):
            if message.author == client.user:
                return
            
            if message.content.startswith("$hello"):
                await message.channel.send("Hello!")
    
    
    intents = discord.Intents.default()
    intents.message_content = True
    
    client = Client(intents=intents)
    client.run('(bottoken**')

**Assets used**: 
https://www.youtube.com/watch?v=SPTfmiYiuok&ab_channel=freeCodeCamp.org
https://www.youtube.com/watch?v=82xCT7fC60k
https://labyrinthos.co/
https://www.californiapsychics.com/blog/?s=Card+Meaning
