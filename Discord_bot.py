import discord
import random
import asyncio

class Client(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')
    
    async def on_message(self, message):
        if message.author == self.user:
            return
        
        if message.content.startswith('$fortune'):
            while True:  # Loop for continuous readings
                await message.channel.send("Please enter your choice (past, present, future) to get a tarot card reading.")

                def check(m):
                    return m.author == message.author and m.channel == message.channel
                
                choice_msg=await self.wait_for('message',check=check)
                choice = choice_msg.content.lower()

                past_meanings = {
                    "The Fool": "You’ve had a time in your life when you took a leap of faith. It marked a fresh start.",
                    "The Magician": "You’ve harnessed your potential in powerful ways before—using your talents and skills to create something meaningful.",
                    "The High Priestess": "You may have relied on your intuition in the past, even when logic seemed to contradict it. There was wisdom you trusted within yourself.",
                    "The Empress": "You’ve experienced nurturing energy—perhaps through creativity, love, or even a maternal figure who provided support.",
                    "The Emperor": "You’ve built structure and stability in your life before, or you’ve been influenced by a figure of authority.",
                    "The Pope": "Tradition or formal education has played a significant role in shaping you. Perhaps you leaned on established systems or mentors.",
                    "The Lovers": "A powerful connection—romantic or otherwise—once shaped your path. Choices tied to your heart brought significant change.",
                    "The Chariot": "You overcame obstacles through sheer determination. Your willpower drove you forward when challenges arose.",
                    "Strength": "You’ve shown resilience in the face of adversity before, relying on inner strength and patience to overcome.",
                    "The Hermit": "There was a time when solitude or introspection allowed you to find clarity and wisdom.",
                    "Wheel of Fortune": "Life’s ups and downs have taught you that nothing is permanent. You’ve experienced both luck and challenge.",
                    "Justice": "Karmic or legal matters may have been resolved in the past, teaching you the importance of fairness.",
                    "The Hanged Man": "You’ve been through a time of suspension or delay, where patience brought new perspectives.",
                    "Death": "You’ve experienced endings before—transformations that cleared the way for growth.",
                    "Temperance": "You’ve found balance and harmony before, blending different aspects of your life successfully.",
                    "The Devil":  "You’ve found balance and harmony before, blending different aspects of your life successfully.",
                    "The Tower": "You’ve experienced sudden upheavals that forced you to rebuild and rethink.",
                    "The Star": "There was a moment when hope or inspiration lit your path, even in darkness.",
                    "The Moon": "You’ve navigated uncertainty and illusion before, trusting your intuition to guide you.",
                    "The Sun": "You’ve had moments of pure joy and clarity before—times when everything felt right.",
                    "Judgement": "You’ve had moments of pure joy and clarity before—times when everything felt right.",
                    "The World": "You’ve completed a significant chapter before, reaching a milestone of fulfillment."
                }

                    # Present meanings
                present_meanings = {
                    "The Fool": "You’re being called to embrace spontaneity. Take a risk, even if it feels uncertain.",
                    "The Magician": "Now is the time to channel your focus. You have the tools to achieve success if you take action.",
                    "The High Priestess": "A situation now requires stillness and introspection. Answers will come when you listen to your inner voice.",
                    "The Empress": "Abundance is flowing around you now. This is a time for growth, connection, and self-care.",
                    "The Emperor": "It’s time to take charge. Discipline and order will serve you well now.",
                    "The Pope": "Now, you may benefit from seeking guidance or aligning with a community that shares your values.",
                    "The Lovers": "A relationship or major decision is in focus. Align your actions with your values and desires.",
                    "The Chariot": "This is your moment to focus and take control. The path ahead requires balance and unwavering focus.",
                    "Strength": "You’re being reminded to approach challenges with compassion and courage. You’re stronger than you think.",
                    "The Hermit": "Step back from distractions now. You’re being called to reflect and seek truth within yourself.",
                    "The Wheel of Fortune": "You’re in the midst of change. Trust that the wheel is turning in your favor, even if it feels uncertain.",
                    "Justice": "Seek truth and accountability now. Decisions must align with honesty and integrity.",
                    "The Hanged Man": "Let go of control and embrace the pause. A shift in perspective will reveal the way forward.",
                    "Death": "An ending is unfolding now, but it’s paving the way for renewal. Embrace the change.",
                    "Temperance": "Moderation and patience are key right now. Find your center.",
                    "The Devil": "What binds you now? Recognize where you’re giving away your power.",
                    "The Tower": "Change is happening, and it may feel chaotic. Trust that destruction clears the way for growth.",
                    "The Star": "Renew your faith now. Healing and clarity are shining on you.",
                    "The Moon": "Things may not be as they seem now. Listen to your instincts and trust your dreams.",
                    "The Sun": "This is a time of success, positivity, and light. Bask in the warmth of this moment.",
                    "Judgement": "A moment of awakening is here. Embrace accountability and rise to your higher calling.",
                    "The World": "Completion is near. Celebrate your achievements and prepare for a new cycle."
                }

                    # Future meanings
                future_meanings = {
                    "The Fool": "Adventure awaits! A chance to begin anew will come your way.",
                    "The Magician": "Soon, you’ll be in a position to manifest your desires. Trust your abilities; the magic is within you.",
                    "The High Priestess": "Secrets or deeper truths will soon come to light. Trust your instincts as you navigate what’s ahead.",
                    "The Empress": "Soon, you’ll see the fruits of your labor. A fertile and prosperous period is on its way.",
                    "The Emperor": "Leadership opportunities or a chance to create lasting foundations are coming your way.",
                    "The Pope": "You’ll soon face a situation where tradition or conformity will influence your choices. Learn from those with experience.",
                    "The Lovers": "You’ll encounter an opportunity for love or harmony, but it will require making a deeply personal choice.",
                    "The Chariot": "Victory is on the horizon if you stay disciplined. Success will require determination, but it’s within reach.",
                    "Strength": "A situation will arise where inner strength, not force, will be your greatest ally.",
                    "The Hermit": "Soon, you’ll find yourself seeking guidance or answers. Embrace solitude when it comes.",
                    "The Wheel of Fortune": "A shift in fate is coming. Be open to new opportunities as the tides turn.",
                    "Justice": "A situation requiring fairness or balance is approaching. Justice will be served.",
                    "The Hanged Man": "You may soon face a situation that requires surrender or a fresh viewpoint.",
                    "Death": "Transformation is on its way. Letting go will allow you to welcome new beginnings.",
                    "Temperance": "Peace and equilibrium will come if you maintain balance through what’s ahead.",
                    "The Devil": "A temptation or test of will is on the horizon. Awareness will be your strength.",
                    "The Tower": "A shake-up will occur, but it will liberate you from stagnant foundations.",
                    "The Star": "A time of hope, peace, and renewal is on the way. Stay optimistic.",
                    "The Moon": "Mysteries and the unknown will come your way. Let intuition lead you through.",
                    "The Sun": "Happiness and achievement are on the horizon. A brighter day is coming.",
                    "Judgement": "A reckoning is ahead. You’ll soon face a decision that requires reflection and renewal.",
                    "The World": "A sense of wholeness and accomplishment awaits. The journey will come full circle."
                }

                # Card Images
                card_images = {
                    "The Fool": "https://imgur.com/MSvOYu9.jpg",
                    "The Magician": "https://imgur.com/Tg3pD2S.jpg",
                    "The High Priestess":"https://imgur.com/b5ePIxU.jpg",
                    "The Empress": "https://imgur.com/pxwXTsRg.jpg",
                    "The Emperor": "https://imgur.com/1S9ISkm.jpg",
                    "The Pope": "https://imgur.com/zwLZk01.jpg",
                    "The Lovers": "https://imgur.com/lfVJAUm.jpg",
                    "The Chariot": "https://imgur.com/Ai3iIi4.jpg",
                    "Strength": "https://imgur.com/ipwiSk5.jpg",
                    "The Hermit": "https://imgur.com/rMx8UdA.jpg",
                    "Wheel of Fortune": "https://imgur.com/6OwtZXO.jpg",
                    "Justice": "https://imgur.com/weWSUwo.jpg",
                    "The Hanged Man": "https://imgur.com/gqUmoBW.jpg",
                    "Death": "https://imgur.com/kZ7kM3X.jpg",
                    "Temperance": "https://imgur.com/nqkKUgg.jpg",
                    "The Devil": "https://imgur.com/Nywe2QC.jpg",
                    "The Tower": "https://imgur.com/hdv3zEP.jpg",
                    "The Star": "https://imgur.com/V2fjPyx.jpg",
                    "The Moon": "https://imgur.com/Vg24vvD.jpg",
                    "The Sun": "https://imgur.com/eDINHhJ.jpg",
                    "Judgement": "https://imgur.com/5Ezagjb.jpg",
                    "The World": "https://imgur.com/v470bUY.jpg"
                }

                if choice == "past":
                    card,meaning=random.choice(list(past_meanings.items()))
                    image=card_images.get(card)
                    await message.channel.send(f"Card: {card}\nMeaning: {meaning}\n{image}") 
                elif choice == "present":
                    card, meaning = random.choice(list(present_meanings.items()))
                    image=card_images.get(card)
                    await message.channel.send(f"Card: {card}\nMeaning: {meaning}\n{image}")

                elif choice == "future":
                    card, meaning = random.choice(list(future_meanings.items()))
                    image=card_images.get(card)
                    await message.channel.send(f"Card: {card}\nMeaning: {meaning}\n{image}")

                else:
                    await message.channel.send("Invalid choice. Please enter 'past', 'present', or 'future'.")
                    return
                
                await message.channel.send("Would you like to read another tarot card? (yes/y or no/o)")

                another_reading_msg = await self.wait_for('message', check=check)
                if another_reading_msg.content.lower() == "yes" or another_reading_msg.content.lower() == "y":
                    await message.channel.send("Please enter your choice (past, present, future) to get a tarot card reading.")
                else:
                    await message.channel.send("Thank you for using the Tarot bot. Goodbye!")
                    break

# Set up intents to allow reading messages
intents = discord.Intents.default()
intents.message_content = True

# Create the client and run the bot
client = Client(intents=intents)
client.run(#Put the TOKEN here)
