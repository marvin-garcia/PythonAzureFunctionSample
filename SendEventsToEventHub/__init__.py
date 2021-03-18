import json
import logging
from random import randint
from datetime import datetime

import azure.functions as func

RANDOM_PHRASES = [
    "Alcohol! Because no great story started with someone eating a salad.",
    "I don't need a hair stylist, my pillow gives me a new hairstyle every morning.",
    "Don't worry if plan A fails, there are 25 more letters in the alphabet.",
    "If I'm not back in five minutes, just wait longer...",
    "A bank is a place that will lend you money, if you can prove that you don’t need it.",
    "A balanced diet means a cupcake in each hand.",
    "Doing nothing is hard, you never know when you're done.",
    "If you’re not supposed to eat at night, why is there a light bulb in the refrigerator?",
    "Don’t drink while driving – you might spill the beer.",
    "I think the worst time to have a heart attack is during a game of charades.",
    "I refuse to answer that question on the grounds that I don't know the answer.",
    "Alcohol doesn't solve any problem, but neither does milk.",
    "Funny saying about drinking alcohol",
    "My wallet is like an onion. When I open it, it makes me cry...",
    "Doesn’t expecting the unexpected make the unexpected expected?",
    "I'm not clumsy, The floor just hates me, the table and chairs are bullies and the walls get in my way.",
    "Life is short, smile while you still have teeth.",
    "The only reason I'm fat is because a tiny body couldn't store all this personality.",
    "I'm jealous of my parents, I'll never have a kid as cool as them.",
    "I'm not lazy, I'm just very relaxed.",
    "Always remember you're unique, just like everyone else.",
    "You're born free, then you're taxed to death.",
    "The best part of going to work is coming back home at the end of the day.",
    "A cookie a day keeps the sadness away. An entire jar of cookies a day brings it back.",
    "A successful man is one who makes more money than his wife can spend. A successful woman is one who can find such a man.",
    "I asked God for a bike, but I know God doesn’t work that way. So I stole a bike and asked for forgiveness.",
    "Do not argue with an idiot. He will drag you down to his level and beat you with experience.",
    "If you think nobody cares if you’re alive, try missing a couple of bank payments.",
    "Money can’t buy happiness, but it sure makes misery easier to live with.",
    "If you do a job too well, you’ll get stuck with it.",
    "Quantity is what you count, quality is what you count on.",
    "The road to success is always under construction.",
    "When you're right, no one remembers. When you're wrong, no one forgets.",
    "If you can't see the bright side of life, polish the dull side.",
    "If you can’t live without me, why aren’t you dead yet?",
    "Don't tell me the sky is the limit when there are footprints on the moon.",
    "I don’t suffer from insanity, I enjoy every minute of it.",
    "I get enough exercise pushing my luck.",
    "Funny saying about excercising",
    "Sometimes I wake up grumpy; other times I let her sleep.",
    "God created the world, everything else is made in China.",
    "Birthdays are good for you. Statistics show that people who have the most live the longest.",
    "When life gives you melons, you might be dyslexic.",
    "Children in the back seat cause accidents, accidents in the back seat cause children!",
    "I’d like to help you out today. Which way did you come in?",
    "You never truly understand something until you can explain it to your grandmother.",
    "Experience is a wonderful thing. It enables you to recognise a mistake when you make it again.",
    "You can't have everything, where would you put it?",
    "Don't you wish they made a clap on clap off device for some peoples mouths?",
    "If your parents never had children, chances are you won't either.",
]

def main(mytimer: func.TimerRequest) -> str:
    
    message_count = randint(1, 10)
    messages = []
    for i in range(message_count):
        message = {
            "timestamp": str(datetime.utcnow()),
            "message": RANDOM_PHRASES[randint(0, len(RANDOM_PHRASES) - 1)],
            "messageNumber": i + 1,
            "totalMessages": message_count,
        }
        messages.append(message)

    logging.info('Sending %s messages to hub', message_count)
    return json.dumps(messages)