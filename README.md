Demo video link: https://youtu.be/8Zq33hNhAoY

#something about the experience/n
Michelle: We struggled with learning how to use discord bots and connect the code to it using the token of it. There was also a problem where the module wasn't updated to the latest version so we had to do that before anything else. Even following the videos was confusing because some videos would just tell you to put in a code without telling you why

Mai: The difficulty I faced was the images link. Initially, I tried to make the bot pull out from my computer's gallery but the output I kept getting was None. So I fixed it by using the URL links of the images I posted online but that also didn't work. I then look up on youtube and other resources and found out my links were missing .jpg. After I added it to the link, the images work perfectly! 

May: What I enjoyed most while working on this bot was seeing it slowly take shape, aligning more and more with the vision I had in mind as I updated it in the background. While it's still different from reading tarot cards in person, there are areas to refine, like expanding the meanings of each card. It has evolved into an interactive chatbot that users can use to engage.

In the process, I struggled with balancing simplicity and immersion, rethinking the structure to feel more intuitive, and debugging technical issues like duplicate prompts and input handling. Despite these challenges, the process has been rewarding, and I'm proud of how far the bot has come now.

# final-staff
git repo for final project of CIS1051 Spring 2024

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
                 
                    await message.channel.send("Welcome to the Tarot bot! What's your name?")
                    def check_name(m):
                        return m.author == message.author and m.channel == message.channel
    
                    name_msg = await self.wait_for('message', check=check_name)
                    user_name = name_msg.content.strip()
    
                    await message.channel.send(f"Nice to meet you, {user_name}! Let's start your tarot reading.")
                    
                    while True:
                        await message.channel.send(
                        f"{user_name}, before choosing a card, close your eyes and think deeply about your question. "
                        f"When you are ready, press the sacred 'Enter' key or wait for the countdown."
                    )
                        def check_ready(m):
                            return m.author == message.author and m.channel == message.channel
    
                        try:
                            ready_msg = await self.wait_for('message', timeout=5, check=check_ready)
                        except asyncio.TimeoutError:
                            await message.channel.send("The sacred countdown begins!")
                            for i in range(3, 0, -1):
                                await message.channel.send(f"...{i}")
                                await asyncio.sleep(1)
                            await message.channel.send("It’s time to reveal your card!")
                        else:
                            await message.channel.send("Thank you! Let's reveal your card.")
    
    
                        
    
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
                            "The Devil":  "You may have been trapped by unhealthy patterns, addictions, or attachments before.",
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
                            "The Empress": "https://imgur.com/pxwXTsR.jpg",
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
    
                        love_meanings ={
                            "The Fool": "Be open to new relationships, but avoid being reckless.",
                            "The Magician": "Trustworthy connections may form. Show your true self.",
                            "The High Priestess": "Be patient and observant; don’t rush into commitments.",
                            "The Empress": "Strong, nurturing relationships will flourish.",
                            "The Emperor": "Build stable relationships based on mutual respect.",
                            "The Pope": "Seek advice or wisdom in your relationships.",
                            "The Lovers": "Romantic relationships are strengthened or tested by decisions.",
                            "The Chariot": "Progress in love requires determination and compromise.",
                            "Strength": "Show compassion and patience in relationships.",
                            "The Hermit": "Temporary isolation can help clarify what you truly need in love.",
                            "Wheel of Fortune": "A sudden change in your romantic life may occur.",
                            "Justice": "Be honest and fair in your relationships.",
                            "The Hanged Man": "Patience is needed to navigate relationship struggles.",
                            "Death": "Old patterns in relationships may end, making way for growth.",
                            "Temperance": "Mutual understanding will strengthen relationships.",
                            "The Devil": "Avoid toxic relationships or unhealthy patterns.",
                            "The Tower": "A breakup or major shift in a relationship is possible.",
                            "The Star": "Romantic connections are renewed with positivity.",
                            "The Moon": "Emotions in relationships may feel confusing. Seek clarity.",
                            "The Sun": "Happiness and harmony define your relationships.",
                            "Judgement": "A time for reflection and making life-changing decisions.",
                            "The World": "Relationships reach a satisfying and harmonious state."
                        }
    
                        health_meanings ={
                            "The Fool": "Take care of yourself and avoid unnecessary risks.",
                            "The Magician": "Maintain balance to ensure continued well-being.",
                            "The High Priestess": "Inner calm will improve your mental and physical health.",
                            "The Empress": "Focus on self-care and emotional well-being.",
                            "The Emperor": "Focus on physical strength and endurance.",
                            "The Pope": "Balance your physical and spiritual well-being.",
                            "The Lovers": "Emotional health is key to overall well-being.",
                            "The Chariot": "Physical health improves through discipline and action.",
                            "Strength": "Physical and mental resilience will bring recovery and growth.",
                            "The Hermit": "Rest and solitude will rejuvenate your health.",
                            "Wheel of Fortune": "Your health may fluctuate, but positive changes are possible.",
                            "Justice": "Balance in life improves your overall health.",
                            "The Hanged Man": "Focus on mental clarity and letting go of stress.",
                            "Death": "A fresh approach can significantly improve health.",
                            "Temperance": "Focus on balance in diet, exercise, and rest.",
                            "The Devil": "Break free from harmful habits affecting your well-being.",
                            "The Tower": "Sudden issues may arise; focus on resilience.",
                            "The Star": "Healing and recovery are on the way.",
                            "The Moon": "Pay attention to emotional well-being.",
                            "The Sun": "Your health is radiant and improving.",
                            "Judgement": "Evaluate habits for long-term health improvements.",
                            "The World": "Physical and mental well-being are at their peak."
                        }
    
                        wealth_meanings ={
    
                            "The Fool": "New opportunities may arise, but manage risks wisely.",
                            "The Magician": "Positive changes are on the horizon. Seize opportunities.",
                            "The High Priestess": "Avoid impulsive spending and think carefully about investments.",
                            "The Empress": "Opportunities for growth and financial stability are present.",
                            "The Emperor": "Hard work and organization will lead to financial security.",
                            "The Pope": "Traditional approaches will yield the best results.",
                            "The Lovers": "Partnerships may lead to financial growth or challenges.",
                            "The Chariot": "Success in financial ventures comes through persistence.",
                            "Strength": "Financial stability comes through calm and steady decisions.",
                            "The Hermit": "Reflect on past decisions to guide future financial planning.",
                            "Wheel of Fortune": "Unexpected financial gains or losses could arise.",
                            "Justice": "Make financial decisions with careful consideration of consequences.",
                            "The Hanged Man": "Delays may occur, but a change in strategy could lead to success.",
                            "Death": "Ending unproductive habits can lead to financial success.",
                            "Temperance": "Financial stability comes through careful planning.",
                            "The Devil": "Beware of overindulgence or financial traps.",
                            "The Tower": "Financial instability may require quick adaptation.",
                            "The Star": "Optimism and creativity will improve financial prospects.",
                            "The Moon": "Avoid risky financial decisions during unclear times.",
                            "The Sun": "Financial success comes through confidence and optimism.",
                            "Judgement": "Reflect on past financial choices to guide future success.",
                            "The World": "Financial goals are achieved with success."
    
                        }
    
                        overall_meanings = {
                            "The Fool": "A time for new beginnings and adventures. Embrace the unknown.",
                            "The Magician": "You have the power to manifest your goals. Focus and determination are key.",
                            "The High Priestess": "Trust your intuition and allow things to unfold naturally.",
                            "The Empress": "A period of abundance and growth. Nurture your goals.",
                            "The Emperor": "Structure and discipline will bring success. Lead with confidence.",
                            "The Pope": "Tradition and guidance play an important role now. Follow established paths.",
                            "The Lovers": "A time of deep connections and important choices.",
                            "The Chariot": "Victory is within reach, but stay focused and disciplined.",
                            "Strength": "Inner strength and courage will overcome obstacles.",
                            "The Hermit": "Time for introspection and self-discovery. Seek your inner truth.",
                            "Wheel of Fortune": "Life is changing; embrace the ups and downs.",
                            "Justice": "Fairness and accountability are key. Decisions will have long-term effects.",
                            "The Hanged Man": "Let go of control and view challenges from a new perspective.",
                            "Death": "Transformation and new beginnings await. Let go of the past.",
                            "Temperance": "Balance and moderation will bring harmony.",
                            "The Devil": "Be aware of temptations and unhealthy attachments.",
                            "The Tower": "Sudden change may feel chaotic but leads to growth.",
                            "The Star": "Hope and inspiration guide you forward.",
                            "The Moon": "Uncertainty and illusions may cloud judgment. Trust your intuition.",
                            "The Sun": "Joy and success shine in your life. Embrace positivity.",
                            "Judgement": "A time for reflection and making life-changing decisions.",
                            "The World": "Fulfillment and completion of a major life cycle."
                        }
    
                        angel_guidance = {
                            "The Fool": "Trust in divine timing and take a leap of faith.",
                            "The Magician": "You have all the tools you need; believe in your abilities.",
                            "The High Priestess": "Listen to your inner wisdom for clarity and peace.",
                            "The Empress": "Open your heart to love and creativity.",
                            "The Emperor": "Take charge and assert your authority with kindness.",
                            "The Pope": "Seek spiritual guidance to stay grounded and aligned.",
                            "The Lovers": "Follow your heart and make choices with love.",
                            "The Chariot": "You are in control; steer your path with confidence.",
                            "Strength": "Trust your inner power and act with gentle strength.",
                            "The Hermit": "Take a step back and find answers within.",
                            "Wheel of Fortune": "Embrace change and trust the universe's plan.",
                            "Justice": "Stay true to your values and act with integrity.",
                            "The Hanged Man": "Release expectations and surrender to divine flow.",
                            "Death": "Embrace transformation and trust the rebirth process.",
                            "Temperance": "Find harmony through patience and inner peace.",
                            "The Devil": "Release what no longer serves your highest good.",
                            "The Tower": "Embrace change and trust in the rebuilding process.",
                            "The Star": "Shine your light and stay hopeful for the future.",
                            "The Moon": "Trust your intuition and embrace the unknown.",
                            "The Sun": "Bask in the warmth of joy and abundance.",
                            "Judgement": "Listen to your higher calling and make aligned choices.",
                            "The World": "Celebrate your journey and embrace the rewards."
                        }
                        card = random.choice(list(past_meanings.keys()))
                        past = past_meanings[card]
                        present = present_meanings[card]
                        future = future_meanings[card]
                        image = card_images.get(card)
    
                        await message.channel.send(
                        f"{user_name}, here are your three cards:\n\n"
                        f"**Card:** {card}\n"
                        f"**Past Meaning:** {past}\n"
                        f"**Present Meaning:** {present}\n"
                        f"**Future Meaning:** {future}\n"
                        f"{image}"
                    )
    
                        await message.channel.send(
                            "Would you like to draw another card for guidance on a specific area of your life? "
                            "(Love, Health, Wealth) Type 'no' to exit."
                    )
                        def check(m):
                            return m.author == message.author and m.channel == message.channel
                    
                        choice_msg=await self.wait_for('message',check=check)
                        choice = choice_msg.content.lower()
    
        # Define the function to get the meaning of a card      
                        if choice == "love":
                            card, meaning = random.choice(list(love_meanings.items()))
                            image = card_images.get(card)
                            await message.channel.send(f"{user_name}, your Love card is:\n\nCard: {card}\nMeaning: {meaning}\n{image}")
    
                        elif choice == "health":
                            card, meaning = random.choice(list(health_meanings.items()))
                            image = card_images.get(card)
                            await message.channel.send(f"{user_name}, your Health card is:\n\nCard: {card}\nMeaning: {meaning}\n{image}")
                        elif choice == "wealth":
                            card, meaning = random.choice(list(wealth_meanings.items()))
                            image = card_images.get(card)
                            await message.channel.send(f"{user_name}, your Wealth card is:\n\nCard: {card}\nMeaning: {meaning}\n{image}")
                        elif choice == "no" or choice == "n":
                            await message.channel.send(f"Thank you for using the Tarot bot, {user_name}! Goodbye!")
                            break
                        else:
                            await message.channel.send("Invalid choice. Please type Love, Health, Wealth, or No to exit.")
                            continue
    
                            
                            
                        await message.channel.send("Would you like to read another tarot card? (yes/y or no/n)")
    
                        another_reading_msg = await self.wait_for('message', check=check)
                            
                        if another_reading_msg.content.lower() not in ["yes", "y"]:
                            await message.channel.send(f"Thank you for using the Tarot bot, {user_name}! Goodbye!")
                            break
    
    
    intents = discord.Intents.default()
    intents.message_content = True
    
    
    client = Client(intents=intents)
    client.run("bottoken")


   
**Assets used**: 
https://www.youtube.com/watch?v=SPTfmiYiuok&ab_channel=freeCodeCamp.org
https://www.youtube.com/watch?v=82xCT7fC60k
https://labyrinthos.co/
https://www.californiapsychics.com/blog/?s=Card+Meaning
https://www.youtube.com/watch?v=sLbMNZQHNms&list=PLOEbl4-1QPZZzG9UHV07oDzcjlSLqsNvR
