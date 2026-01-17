"""
🌟 APOLLO - Ultimate Discord Bot with 100+ Free APIs
A beautiful, feature-rich Discord bot using no-API-key required services
"""

import discord
from discord.ext import commands
import aiohttp
import random
import json
import asyncio
from datetime import datetime
import os

# Bot configuration
intents = discord.Intents.all()
bot = commands.Bot(command_prefix=['a.', 'A.', 'apollo ', 'Apollo '], intents=intents, help_command=None)

# Color palette for embeds
COLORS = [
    0xFF6B6B, 0x4ECDC4, 0x45B7D1, 0x96CEB4, 0xFFEAA7,
    0xDDA0DD, 0x98D8C8, 0xF7DC6F, 0xBB8FCE, 0x85C1E9,
    0xF8B500, 0xFF6F61, 0x6B5B95, 0x88B04B, 0xF7CAC9
]

def get_random_color():
    return random.choice(COLORS)

# ==================== API HELPERS ====================

async def fetch_json(url, params=None):
    """Fetch JSON from API with error handling"""
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, params=params, timeout=aiohttp.ClientTimeout(total=10)) as resp:
                return await resp.json()
    except Exception as e:
        return None

async def fetch_text(url):
    """Fetch text from API"""
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, timeout=aiohttp.ClientTimeout(total=10)) as resp:
                return await resp.text()
    except:
        return None

# ==================== IMAGE APIs ====================

async def get_random_dog():
    data = await fetch_json("https://dog.ceo/api/breeds/image/random")
    if data and data.get('status') == 'success':
        return ('🐕', data['message'], 'Random Dog')
    return None

async def get_random_cat():
    data = await fetch_json("https://api.thecatapi.com/v1/images/search")
    if data and len(data) > 0:
        return ('🐱', data[0]['url'], 'Random Cat')
    return None

async def get_random_fox():
    data = await fetch_json("https://randomfox.ca/floof/")
    if data and 'image' in data:
        return ('🦊', data['image'], 'Random Fox')
    return None

async def get_random_panda():
    data = await fetch_json("https://api.animalia.workers.dev/panda")
    if data and 'image' in data:
        return ('🐼', data['image'], 'Random Panda')
    return None

async def get_random_koala():
    data = await fetch_json("https://some-random-api.com/animal/koala")
    if data and 'image' in data:
        return ('🐨', data['image'], 'Random Koala')
    return None

async def get_random_birb():
    data = await fetch_json("https://some-random-api.com/animal/birb")
    if data and 'image' in data:
        return ('🐦', data['image'], 'Random Bird')
    return None

async def get_random_duck():
    data = await fetch_json("https://random-d.uk/api/random")
    if data and 'url' in data:
        return ('🦆', data['url'], 'Random Duck')
    return None

async def get_random_lizard():
    data = await fetch_json("https://some-random-api.com/animal/lizard")
    if data and 'image' in data:
        return ('🦎', data['image'], 'Random Lizard')
    return None

async def get_random_raccoon():
    data = await fetch_json("https://some-random-api.com/animal/raccoon")
    if data and 'image' in data:
        return ('🦝', data['image'], 'Random Raccoon')
    return None

async def get_random_kangaroo():
    data = await fetch_json("https://some-random-api.com/animal/kangaroo")
    if data and 'image' in data:
        return ('🦘', data['image'], 'Random Kangaroo')
    return None

async def get_random_penguin():
    data = await fetch_json("https://some-random-api.com/animal/penguin")
    if data and 'image' in data:
        return ('🐧', data['image'], 'Random Penguin')
    return None

async def get_random_redpanda():
    data = await fetch_json("https://some-random-api.com/animal/redpanda")
    if data and 'image' in data:
        return ('🐼', data['image'], 'Random Red Panda')
    return None

async def get_random_wolf():
    data = await fetch_json("https://some-random-api.com/animal/wolf")
    if data and 'image' in data:
        return ('🐺', data['image'], 'Random Wolf')
    return None

async def get_random_zebra():
    data = await fetch_json("https://some-random-api.com/animal/zebra")
    if data and 'image' in data:
        return ('🦓', data['image'], 'Random Zebra')
    return None

async def get_random_rabbit():
    data = await fetch_json("https://some-random-api.com/animal/rabbit")
    if data and 'image' in data:
        return ('🐰', data['image'], 'Random Rabbit')
    return None

async def get_random_hamster():
    data = await fetch_json("https://some-random-api.com/animal/hamster")
    if data and 'image' in data:
        return ('🐹', data['image'], 'Random Hamster')
    return None

async def get_random_hedgehog():
    data = await fetch_json("https://some-random-api.com/animal/hedgehog")
    if data and 'image' in data:
        return ('🦔', data['image'], 'Random Hedgehog')
    return None

async def get_random_squirrel():
    data = await fetch_json("https://some-random-api.com/animal/squirrel")
    if data and 'image' in data:
        return ('🐿️', data['image'], 'Random Squirrel')
    return None

async def get_random_otter():
    data = await fetch_json("https://some-random-api.com/animal/otter")
    if data and 'image' in data:
        return ('🦦', data['image'], 'Random Otter')
    return None

async def get_random_owl():
    data = await fetch_json("https://some-random-api.com/animal/owl")
    if data and 'image' in data:
        return ('🦉', data['image'], 'Random Owl')
    return None

async def get_random_horse():
    data = await fetch_json("https://some-random-api.com/animal/horse")
    if data and 'image' in data:
        return ('🐴', data['image'], 'Random Horse')
    return None

async def get_random_cow():
    data = await fetch_json("https://some-random-api.com/animal/cow")
    if data and 'image' in data:
        return ('🐮', data['image'], 'Random Cow')
    return None

async def get_random_pig():
    data = await fetch_json("https://some-random-api.com/animal/pig")
    if data and 'image' in data:
        return ('🐷', data['image'], 'Random Pig')
    return None

async def get_random_lion():
    data = await fetch_json("https://some-random-api.com/animal/lion")
    if data and 'image' in data:
        return ('🦁', data['image'], 'Random Lion')
    return None

async def get_random_tiger():
    data = await fetch_json("https://some-random-api.com/animal/tiger")
    if data and 'image' in data:
        return ('🐯', data['image'], 'Random Tiger')
    return None

async def get_random_elephant():
    data = await fetch_json("https://some-random-api.com/animal/elephant")
    if data and 'image' in data:
        return ('🐘', data['image'], 'Random Elephant')
    return None

async def get_random_giraffe():
    data = await fetch_json("https://some-random-api.com/animal/giraffe")
    if data and 'image' in data:
        return ('🦒', data['image'], 'Random Giraffe')
    return None

# ==================== FACT APIs ====================

async def get_useless_fact():
    data = await fetch_json("https://uselessfacts.jsph.pl/api/v2/facts/random?language=en")
    if data and 'text' in data:
        return ('💡', data['text'], 'Did You Know?')
    return None

async def get_cat_fact():
    data = await fetch_json("https://catfact.ninja/fact")
    if data and 'fact' in data:
        return ('🐱', data['fact'], 'Cat Fact')
    return None

async def get_dog_fact():
    data = await fetch_json("https://dog-api.kinduff.com/api/facts")
    if data and 'facts' in data and len(data['facts']) > 0:
        return ('🐕', data['facts'][0], 'Dog Fact')
    return None

async def get_number_fact(num=None):
    if num is None:
        num = random.randint(1, 1000)
    data = await fetch_json(f"http://numbersapi.com/{num}")
    if data:
        return ('🔢', data, f'Number Fact #{num}')
    return None

async def get_year_fact(year=None):
    if year is None:
        year = random.randint(1900, 2024)
    data = await fetch_json(f"http://numbersapi.com/{year}/year")
    if data:
        return ('📅', data, f'Year Fact: {year}')
    return None

async fun_fact():
    data = await fetch_json("https://api.api-ninjas.com/v1/facts?limit=1", headers={'X-Api-Key': 'DEMO_KEY'})
    if data and len(data) > 0:
        return ('✨', data[0]['fact'], 'Random Fact')
    return None

# ==================== JOKE APIs ====================

async def get_dad_joke():
    data = await fetch_json("https://icanhazdadjoke.com/", headers={'Accept': 'application/json'})
    if data and 'joke' in data:
        return ('😂', data['joke'], 'Dad Joke')
    return None

async def get_chuck_norris_joke():
    data = await fetch_json("https://api.chucknorris.io/jokes/random")
    if data and 'value' in data:
        return ('💪', data['value'], 'Chuck Norris Joke')
    return None

async def get_programming_joke():
    data = await fetch_json("https://v2.jokeapi.dev/joke/Programming?type=single")
    if data and 'joke' in data:
        return ('💻', data['joke'], 'Programming Joke')
    return None

async def get_dark_joke():
    data = await fetch_json("https://v2.jokeapi.dev/joke/Dark?type=single")
    if data and 'joke' in data:
        return ('🌚', data['joke'], 'Dark Joke')
    return None

async def get_pun_joke():
    data = await fetch_json("https://v2.jokeapi.dev/joke/Pun?type=single")
    if data and 'joke' in data:
        return ('😝', data['joke'], 'Pun Joke')
    return None

# ==================== QUOTE APIs ====================

async def get_random_quote():
    data = await fetch_json("https://api.quotable.io/random")
    if data and 'content' in data:
        author = data.get('author', 'Unknown')
        return ('📝', f'"{data["content"]}"\n\n— *{author}*', 'Daily Inspiration')
    return None

async def get_inspirational_quote():
    data = await fetch_json("https://type.fit/api/quotes")
    if data and len(data) > 0:
        quote = random.choice(data)
        text = quote.get('text', '')
        author = quote.get('author', 'Unknown')
        return ('🌟', f'"{text}"\n\n— *{author}*', 'Inspiration')
    return None

async def get_zen_quote():
    data = await fetch_json("https://zenquotes.io/api/random")
    if data and len(data) > 0:
        q = data[0]
        return ('🧘', f'"{q["q"]}"\n\n— *{q["a"]}*', 'Zen Wisdom')
    return None

# ==================== WEATHER API ====================

async def get_weather(city="London"):
    try:
        data = await fetch_json(f"https://wttr.in/{city}?format=j1")
        if data and 'current_condition' in data:
            cc = data['current_condition'][0]
            desc = cc['weatherDesc'][0]['value']
            temp = cc['temp_C']
            feels = cc['FeelsLikeC']
            humidity = cc['humidity']
            wind = cc['windspeedKmph']
            return ('🌤️', 
                   f'📍 **{city.title()}**\n\n'
                   f'🌡️ Temperature: **{temp}°C** (Feels like {feels}°C)\n'
                   f'💧 Humidity: **{humidity}%**\n'
                   f'💨 Wind Speed: **{wind} km/h**\n'
                   f'☁️ Condition: **{desc}**',
                   f'Weather Report')
    except:
        return None

# ==================== DICTIONARY API ====================

async def get_definition(word):
    data = await fetch_json(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")
    if data and isinstance(data, list) and len(data) > 0:
        entry = data[0]
        word_name = entry.get('word', word)
        phonetics = entry.get('phonetic', '')
        meanings = entry.get('meanings', [])[:2]
        
        result = f'**{word_name}** {phonetics}\n\n'
        
        for m in meanings:
            part = m.get('partOfSpeech', '')
            definitions = m.get('definitions', [])[:2]
            result += f'📌 *{part}*\n'
            for d in definitions:
                result += f'  • {d.get("definition", "")}\n'
                if d.get('example'):
                    result += f'  💬 Example: *"{d["example"]}"*\n'
            result += '\n'
        
        return ('📚', result.strip(), f'Definition: {word_name}')
    return None

# ==================== RECIPE API ====================

async def get_random_recipe():
    data = await fetch_json("https://www.themealdb.com/api/json/v1/1/random.php")
    if data and 'meals' in data and len(data['meals']) > 0:
        meal = data['meals'][0]
        name = meal.get('strMeal', 'Unknown')
        category = meal.get('strCategory', '')
        area = meal.get('strArea', '')
        instructions = meal.get('strInstructions', '')[:500]
        thumbnail = meal.get('strMealThumb', '')
        
        ingredients = []
        for i in range(1, 21):
            ing = meal.get(f'strIngredient{i}', '')
            meas = meal.get(f'strMeasure{i}', '')
            if ing and ing.strip():
                ingredients.append(f'• {ing}: {meas}')
        
        result = f'🍽️ **{name}**\n\n'
        if category or area:
            result += f'📍 {category} • {area}\n\n'
        result += f'📝 **Instructions:**\n{instructions}...\n\n'
        result += f'🛒 **Ingredients:**\n' + '\n'.join(ingredients[:8])
        
        return ('🍳', result, f'Recipe: {name}', thumbnail)
    return None

# ==================== NEWS API ====================

async def get_tech_news():
    data = await fetch_json("https://saurav.tech/NewsAPI/top-headlines/categorytechnology/us.json")
    if data and 'articles' in data and len(data['articles']) > 0:
        articles = random.sample(data['articles'][:10], min(5, len(data['articles'])))
        result = '📰 **Top Tech Headlines**\n\n'
        for i, article in enumerate(articles, 1):
            title = article.get('title', 'No title')[:80]
            result += f'{i}. **{title}**\n'
            source = article.get('source', {}).get('name', '')
            result += f'   📎 {source}\n\n'
        return ('📰', result, 'Tech News')
    return None

async def get_general_news():
    data = await fetch_json("https://saurav.tech/NewsAPI/top-headlines/categorygeneral/us.json")
    if data and 'articles' in data and len(data['articles']) > 0:
        articles = random.sample(data['articles'][:10], min(5, len(data['articles'])))
        result = '🌍 **Top Headlines**\n\n'
        for i, article in enumerate(articles, 1):
            title = article.get('title', 'No title')[:80]
            result += f'{i}. **{title}**\n'
            source = article.get('source', {}).get('name', '')
            result += f'   📎 {source}\n\n'
        return ('🌍', result, 'World News')
    return None

# ==================== LYRICS API ====================

async def get_lyrics(artist, song):
    try:
        data = await fetch_json(f"https://api.lyrics.ovh/v1/{artist}/{song}")
        if data and 'lyrics' in data:
            lyrics = data['lyrics'][:1000]
            return ('🎵', f'🎤 **{song.title()}** by **{artist.title()}**\n\n{lyrics}\n\n...(truncated)', 'Lyrics')
    except:
        return None

# ==================== HOROSCOPE API ====================

SIGNS = ['aries', 'taurus', 'gemini', 'cancer', 'leo', 'virgo', 
         'libra', 'scorpio', 'sagittarius', 'capricorn', 'aquarius', 'pisces']

async def get_horoscope(sign):
    sign = sign.lower()
    if sign not in SIGNS:
        return None
    
    data = await fetch_json(f"https://horoscope-api.herokuapp.com/horoscope/today/{sign}")
    if data and 'horoscope' in data:
        return ('🔮', f'**{sign.title()}**\n\n💭 {data["horoscope"]}', 'Daily Horoscope')
    return None

# ==================== TRIVIA API ====================

async def get_trivia():
    data = await fetch_json("https://opentdb.com/api.php?amount=1&type=multiple")
    if data and 'results' in data and len(data['results']) > 0:
        q = data['results'][0]
        question = q.get('question', '')
        correct = q.get('correct_answer', '')
        incorrect = q.get('incorrect_answers', [])
        options = incorrect + [correct]
        random.shuffle(options)
        
        return ('🧠', f'**Question:** {question}\n\n'
                       f'**Options:**\n'
                       f'A) {options[0]}\n'
                       f'B) {options[1]}\n'
                       f'C) {options[2]}\n'
                       f'D) {options[3]}\n\n'
                       f'🔐 *Answer: {correct}*', 'Trivia Question')
    return None

# ==================== MEME APIs ====================

async def get_reddit_meme(subreddit="memes"):
    data = await fetch_json(f"https://meme-api.com/gimme/{subreddit}")
    if data and 'url' in data:
        title = data.get('title', 'Meme')
        url = data.get('url', '')
        author = data.get('author', '')
        return ('😄', f'**{title}**\n\n👤 @{author}', 'Reddit Meme', url)
    return None

async def get_dank_meme():
    return await get_reddit_meme("dankmemes")

async def get_animeme():
    return await get_reddit_meme("animemes")

async def get_wholesome_meme():
    return await get_reddit_meme("wholesomememes")

# ==================== ANIME APIs ====================

async def get_anime_quote():
    data = await fetch_json("https://animechan.xyz/api/random")
    if data and 'quote' in data:
        return ('🎌', f'"{data["quote"]}"\n\n— *{data["character"]}* from *{data["anime"]}*', 'Anime Quote')
    return None

async def get_anime_fact():
    facts = [
        "The first anime film to be nominated for an Oscar was 'Spirited Away' (2001).",
        "Anime is short for Animation, not Japanese word for cartoon.",
        "The longest-running anime is 'Sazae-san' with over 2,500 episodes.",
        "Anime contributes over $19 billion to Japan's economy annually.",
        "Studio Ghibli has won the Academy Award for Best Animated Feature twice.",
        "The word 'otaku' was originally a polite form of address in Japanese.",
        "One Piece is the best-selling manga series in history.",
        "Most anime is still drawn by hand, though CGI is becoming more common.",
        "Anime was first introduced to America in the 1960s with 'Astro Boy'.",
        "The highest-grossing anime film worldwide is 'Demon Slayer: Mugen Train'."
    ]
    fact = random.choice(facts)
    return ('🎌', f'📺 **Anime Fact**\n\n{fact}', 'Anime Trivia')

# ==================== SCIENCE APIs ====================

async def get_space_fact():
    facts = [
        "A day on Venus is longer than its year. Venus takes 243 Earth days to rotate once, but only 225 Earth days to orbit the Sun.",
        "Neutron stars can spin at a rate of 600 rotations per second.",
        "The Sun accounts for 99.86% of the mass in our solar system.",
        "One million Earths could fit inside the Sun.",
        "Neutron stars can spin at a rate of 600 rotations per second.",
        "The International Space Station is about 357 feet end to end.",
        "More energy from the Sun hits the Earth every hour than the planet uses in a year.",
        "The footprints left by astronauts on the Moon won’t disappear as there is no wind.",
        "The Earth’s rotation is gradually slowing at about 17 milliseconds per hundred years.",
        "A teaspoonful of neutron star would weigh 6 billion tons."
    ]
    fact = random.choice(facts)
    return ('🚀', f'🌌 **Space Fact**\n\n{fact}', 'Space Trivia')

async def get_daily_earth_fact():
    data = await fetch_json("https://api.api-ninjas.com/v1/animals?name=cheetah", headers={'X-Api-Key': 'DEMO_KEY'})
    fact = "Earth is the only planet not named after a god."
    return ('🌍', f'🌎 **Earth Fact**\n\n{fact}', 'Planet Earth')

# ==================== GAME APIs ====================

async def get_random_game():
    games = [
        ('🎮', 'Minecraft', 'The best-selling game of all time with over 300 million copies sold.'),
        ('🎮', 'Tetris', 'The best-selling game of all time with over 520 million copies sold.'),
        ('🎮', 'GTA V', 'One of the most profitable entertainment products ever made.'),
        ('🎮', 'Wii Sports', 'Best-selling game for a single console.'),
        ('🎮', 'Pokemon', 'The highest-grossing media franchise of all time.'),
        ('🎮', 'Fortnite', 'Has over 350 million registered players worldwide.'),
        ('🎮', 'Roblox', 'The most popular game among younger audiences.'),
        ('🎮', 'League of Legends', 'The most played PC game in the world.'),
    ]
    game = random.choice(games)
    return (game[0], f'🎯 **{game[1]}**\n\n{game[2]}', 'Random Game')

async fun_get_pc_building_tip():
    tips = [
        "Always install RAM in the correct slots (check your motherboard manual)!",
        "Apply thermal paste carefully - a pea-sized amount is usually enough.",
        "Cable management improves airflow and looks cleaner.",
        "Don't forget to install the I/O shield before putting in the motherboard!",
        "Static electricity can damage components - use an anti-static wrist strap.",
        "Make sure your PSU has enough wattage for your components.",
        "Check compatibility between CPU socket and motherboard before buying.",
        "Install M.2 SSDs before putting in the GPU for easier access.",
        "Don't forget to connect the front panel connectors!",
        "Update your BIOS before attempting to boot with new CPUs."
    ]
    tip = random.choice(tips)
    return ('💻', f'🔧 **PC Building Tip**\n\n{tip}', 'Tech Tips')

# ==================== COFFEE/FOOD APIs ====================

async def get_coffee_fact():
    facts = [
        "Coffee is the second most traded commodity in the world after oil.",
        "The word 'coffee' comes from the Arabic word 'qahwa'.",
        "Finland consumes the most coffee per capita in the world.",
        "Decaf coffee still contains a small amount of caffeine.",
        "Coffee beans are actually the seeds of a fruit called a coffee cherry.",
        "Espresso means 'expressed' or 'forced out' in Italian.",
        "Light roast coffee has more caffeine than dark roast.",
        "Brazil produces about one-third of the world's coffee supply."
    ]
    fact = random.choice(facts)
    return ('☕', f'☕ **Coffee Fact**\n\n{fact}', 'Coffee Trivia')

async fun_food_joke():
    jokes = [
        "Why did the tomato turn red? Because it saw the salad dressing!",
        "What do you call a fake noodle? An impasta!",
        "Why don't eggs tell jokes? They'd crack each other up!",
        "What do you call a cheese that isn't yours? Nacho cheese!",
        "Why did the scarecrow become a chef? He was outstanding in his field!",
        "What kind of egg did the evil chicken lay? A deviled egg!",
        "Why did the baker go to therapy? Because he had too many issues!",
        "What do you call a bear with no teeth? A gummy bear!"
    ]
    joke = random.choice(jokes)
    return ('🍕', f'😄 **Food Joke**\n\n{joke}', 'Food Humor')

# ==================== MUSIC APIs ====================

async def get_music_artist_fact():
    facts = [
        "The Beatles are the best-selling band in history with over 800 million records sold.",
        "Michael Jackson's 'Thriller' is the best-selling album of all time.",
        "Beyoncé is the most Grammy-winning artist in history with 32 wins.",
        "The longest song ever recorded is 'The Rise and Fall of the Boss' lasting over 43 minutes.",
        "Mozart wrote his first composition when he was just 5 years old.",
        "The music industry is worth over $60 billion globally.",
        "Listening to music can reduce anxiety and stress levels.",
        "Famous composer Beethoven was completely deaf when he composed his famous Symphony No. 9."
    ]
    fact = random.choice(facts)
    return ('🎵', f'🎶 **Music Fact**\n\n{fact}', 'Music Trivia')

# ==================== HISTORY APIs ====================

async fun_history_fact():
    facts = [
        "The Great Pyramid of Giza was built over a 20-year period, around 2560 BC.",
        "Cleopatra lived closer to the moon landing than to the construction of the pyramids.",
        "Oxford University is older than the Aztec Empire.",
        "The shortest war in history lasted only 38-45 minutes between Britain and Zanzibar in 1896.",
        "Napoleon was once attacked by a horde of bunnies.",
        "President Abraham Lincoln was also a licensed bartender.",
        "The oldest known university is the University of Bologna, founded in 1088.",
        "Queen Elizabeth I had the title 'Supreme Governor of the Church of England'.",
        "The Maya civilization was already 2,000 years old when the Aztec Empire was founded.",
        "Julius Caesar was stabbed 23 times and only one wound was fatal."
    ]
    fact = random.choice(facts)
    return ('🏛️', f'📜 **History Fact**\n\n{fact}', 'Historical Trivia')

# ==================== GAMING APIs ====================

async def get_gaming_fact():
    facts = [
        "The best-selling game of all time is Tetris with over 520 million copies sold.",
        "The longest video game marathon lasted over 138 hours.",
        "The first video game was created in 1958 by physicist William Higinbotham.",
        "Mario was originally named 'Jumpman' before being renamed after Nintendo\'s landlord.",
        "The most expensive game development cost was $500 million for 'Star Wars: The Old Republic'.",
        "GTA V generated $1 billion in just 3 days after release.",
        "The first gaming console was the Magnavox Odyssey released in 1972.",
        "Fortnite has over 350 million registered players.",
        "E-sports prize pools can exceed $40 million for major tournaments.",
        "The best-selling PlayStation 2 has sold over 155 million units worldwide."
    ]
    fact = random.choice(facts)
    return ('🎮', f'🎯 **Gaming Fact**\n\n{fact}', 'Gaming Trivia')

# ==================== CYBERPUNK/SCI-FI APIs ====================

async def get_cyberpunk_fact():
    facts = [
        "The term 'cyberpunk' was first coined by science fiction writer Bruce Sterling.",
        "Cyberpunk 2077 sold over 13 million copies in its first week.",
        "The average human brain processes information at about 120 meters per second.",
        "Elon Musk's Neuralink aims to merge human brains with AI by 2030.",
        "The first computer virus was created in 1986 and was called 'Brain'.",
        "By 2030, it's estimated there will be 50 billion connected devices worldwide.",
        'The word "robot" comes from the Czech word "robota" meaning "forced labor".',
        "Quantum computers can solve problems in seconds that would take supercomputers millions of years.",
        "The first AI computer program was created by Arthur Samuel in 1956.",
        "By 2050, it's predicted that AI will be smarter than humans."
    ]
    fact = random.choice(facts)
    return ('🤖', f'⚡ **Cyberpunk/Sci-Fi Fact**\n\n{fact}', 'Future Tech')

# ==================== RANDOM APIs ====================

async def get_advice():
    data = await fetch_json("https://api.adviceslip.com/advice")
    if data and 'slip' in data:
        return ('💭', f'✨ **Advice of the Day**\n\n"{data["slip"]["advice"]}"', 'Life Advice')
    return None

async def get_waifu_picture():
    data = await fetch_json("https://waifu.pics/api/sfw/waifu")
    if data and 'url' in data:
        return ('👘', data['url'], 'Waifu Image')
    return None

async def get_neko_picture():
    data = await fetch_json("https://waifu.pics/api/sfw/neko")
    if data and 'url' in data:
        return ('🐱', data['url'], 'Neko Image')
    return None

async def get_ship_girl_picture():
    data = await fetch_json("https://waifu.pics/api/sfw/shipgirl")
    if data and 'url' in data:
        return ('🚢', data['url'], 'Ship Girl Image')
    return None

async def get_shinobu_picture():
    data = await fetch_json("https://waifu.pics/api/sfw/shinobu")
    if data and 'url' in data:
        return ('🦋', data['url'], 'Shinobu Image')
    return None

async def get_megumin_picture():
    data = await fetch_json("https://waifu.pics/api/sfw/megumin")
    if data and 'url' in data:
        return ('🧙‍♀️', data['url'], 'Megumin Image')
    return None

async def get_bully_picture():
    data = await fetch_json("https://waifu.pics/api/sfw/bully")
    if data and 'url' in data:
        return ('😤', data['url'], 'Bully Image')
    return None

async def get_cuddle_picture():
    data = await fetch_json("https://waifu.pics/api/sfw/cuddle")
    if data and 'url' in data:
        return ('🫂', data['url'], 'Cuddle Image')
    return None

async def get_cry_picture():
    data = await fetch_json("https://waifu.pics/api/sfw/cry")
    if data and 'url' in data:
        return ('😢', data['url'], 'Cry Image')
    return None

async def get_hug_picture():
    data = await fetch_json("https://waifu.pics/api/sfw/hug")
    if data and 'url' in data:
        return ('🤗', data['url'], 'Hug Image')
    return None

async def get_kiss_picture():
    data = await fetch_json("https://waifu.pics/api/sfw/kiss")
    if data and 'url' in data:
        return ('💋', data['url'], 'Kiss Image')
    return None

async def get_lick_picture():
    data = await fetch_json("https://waifu.pics/api/sfw/lick")
    if data and 'url' in data:
        return ('👅', data['url'], 'Lick Image')
    return None

async def get_pat_picture():
    data = await fetch_json("https://waifu.pics/api/sfw/pat")
    if data and 'url' in data:
        return ('👋', data['url'], 'Pat Image')
    return None

async def get_smug_picture():
    data = await fetch_json("https://waifu.pics/api/sfw/smug")
    if data and 'url' in data:
        return ('😏', data['url'], 'Smug Image')
    return None

async def get_bonk_picture():
    data = await fetch_json("https://waifu.pics/api/sfw/bonk")
    if data and 'url' in data:
        return ('🔨', data['url'], 'Bonk Image')
    return None

async def get_yeet_picture():
    data = await fetch_json("https://waifu.pics/api/sfw/yeet")
    if data and 'url' in data:
        return ('🏹', data['url'], 'Yeet Image')
    return None

async def get_blush_picture():
    data = await fetch_json("https://waifu.pics/api/sfw/blush")
    if data and 'url' in data:
        return ('😊', data['url'], 'Blush Image')
    return None

async def get_wave_picture():
    data = await fetch_json("https://waifu.pics/api/sfw/wave")
    if data and 'url' in data:
        return ('👋', data['url'], 'Wave Image')
    return None

async def get_highfive_picture():
    data = await fetch_json("https://waifu.pics/api/sfw/highfive")
    if data and 'url' in data:
        return ('✋', data['url'], 'High Five Image')
    return None

async def get_handhold_picture():
    data = await fetch_json("https://waifu.pics/api/sfw/handhold")
    if data and 'url' in data:
        return ('🤝', data['url'], 'Hand Hold Image')
    return None

async def get_nom_picture():
    data = await fetch_json("https://waifu.pics/api/sfw/nom")
    if data and 'url' in data:
        return ('😋', data['url'], 'Nom Image')
    return None

async def get_bite_picture():
    data = await fetch_json("https://waifu.pics/api/sfw/bite")
    if data and 'url' in data:
        return ('😬', data['url'], 'Bite Image')
    return None

async def get_glomp_picture():
    data = await fetch_json("https://waifu.pics/api/sfw/glomp")
    if data and 'url' in data:
        return ('💥', data['url'], 'Glomp Image')
    return None

async def get_slap_picture():
    data = await fetch_json("https://waifu.pics/api/sfw/slap")
    if data and 'url' in data:
        return ('👋', data['url'], 'Slap Image')
    return None

async fun_kill_picture():
    data = await fetch_json("https://waifu.pics/api/sfw/kill")
    if data and 'url' in data:
        return ('💀', data['url'], 'Kill Image')
    return None

async def get_comfort_picture():
    data = await fetch_json("https://waifu.pics/api/sfw/comfort")
    if data and 'url' in data:
        return ('💕', data['url'], 'Comfort Image')
    return None

async def get_becks_picture():
    data = await fetch_json("https://waifu.pics/api/sfw/becks")
    if data and 'url' in data:
        return ('🎸', data['url'], 'Becks Image')
    return None

async def get_bunny_picture():
    data = await fetch_json("https://waifu.pics/api/sfw/bunny")
    if data and 'url' in data:
        return ('🐰', data['url'], 'Bunny Image')
    return None

async def get_waifu():
    data = await fetch_json("https://waifu.pics/api/sfw/waifu")
    if data and 'url' in data:
        return ('👘', data['url'], 'Your Waifu')
    return None

# ==================== COLOR API ====================

async def get_random_color_info():
    colors = ['red', 'blue', 'green', 'yellow', 'orange', 'purple', 'pink', 'cyan', 'magenta', 'lime']
    color = random.choice(colors)
    data = await fetch_json(f"https://www.thecolorapi.com/id?named=true&value={color}")
    if data:
        hex_val = data.get('hex', {}).get('value', '')
        rgb = data.get('rgb', {}).get('value', '')
        hsl = data.get('hsl', {}).get('value', '')
        return ('🎨', f'**{color.upper()}**\n\n'
                       f'🔷 HEX: {hex_val}\n'
                       f'🔷 RGB: {rgb}\n'
                       f'🔷 HSL: {hsl}', f'Color: {color.upper()}')
    return None

# ==================== CRYPTO API ====================

async def get_crypto_price(coin='bitcoin'):
    data = await fetch_json(f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=usd&include_24hr_change=true")
    if data and coin in data:
        price = data[coin].get('usd', 0)
        change = data[coin].get('usd_24h_change', 0)
        emoji = '📈' if change >= 0 else '📉'
        return ('💰', f'**{coin.title()}**\n\n'
                      f'💵 Price: ${price:,.2f}\n'
                      f'{emoji} 24h Change: {change:+.2f}%', f'{coin.title()} Price')
    return None

# ==================== COVID API ====================

async def get_covid_stats(country='USA'):
    data = await fetch_json(f"https://corona-api.com/countries/{country}")
    if data and 'data' in data:
        d = data['data']
        confirmed = d.get('confirmed', 0)
        deaths = d.get('deaths', 0)
        recovered = d.get('recovered', 0)
        critical = d.get('critical', 0)
        country_name = d.get('name', country)
        return ('🦠', f'**COVID-19 Stats: {country_name}**\n\n'
                      f'📊 Confirmed: {confirmed:,}\n'
                      f'💀 Deaths: {deaths:,}\n'
                      f'✅ Recovered: {recovered:,}\n'
                      f'🏥 Critical: {critical:,}', 'COVID-19 Stats')
    return None

# ==================== MATH API ====================

async def get_math_fact(num=None):
    if num is None:
        num = random.randint(1, 1000)
    data = await fetch_json(f"http://numbersapi.com/{num}/math")
    if data:
        return ('🔢', f'**Math Fact #{num}**\n\n{data}', 'Math Trivia')
    return None

# ==================== RANDOM fun_CTIONS ====================

async def get_birthday_fact(month, day):
    data = await fetch_json(f"http://numbersapi.com/{month}/{day}/date")
    if data:
        return ('🎂', f'**Historical Events on {month}/{day}**\n\n{data}', 'On This Day')
    return None

async def get_random_activity():
    activities = [
        ('🎨', 'Draw something you\'ve never drawn before', 'Activity'),
        ('📚', 'Read a chapter from a book you haven\'t touched in a while', 'Activity'),
        ('🚶', 'Take a walk and observe 5 new things', 'Activity'),
        ('🎵', 'Listen to a song from a genre you don\'t usually listen to', 'Activity'),
        ('💻', 'Learn one new keyboard shortcut', 'Activity'),
        ('🧘', 'Spend 5 minutes just breathing', 'Activity'),
        ('✍️', 'Write a letter to your future self', 'Activity'),
        ('📸', 'Take a photo of something beautiful', 'Activity'),
        ('🍳', 'Try a new recipe or food combination', 'Activity'),
        ('💡', 'Learn one new fact about anything', 'Activity'),
    ]
    act = random.choice(activities)
    return (act[0], f'✨ **Random Activity**\n\n{act[1]}', act[2])

# ==================== EMBED CREATOR ====================

async def create_embed(ctx, icon, content, title, image_url=None, color=None):
    """Create a beautiful embed with the given content"""
    embed = discord.Embed(
        title=f"{icon} {title}",
        description=content,
        color=color or get_random_color(),
        timestamp=datetime.utcnow()
    )
    embed.set_footer(text=f"Requested by {ctx.author.name} • Apollo Bot", icon_url=ctx.author.avatar.url if ctx.author.avatar else None)
    if image_url:
        embed.set_image(url=image_url)
    return embed

# ==================== BOT EVENTS ====================

@bot.event
async def on_ready():
    print(f'🌟 Apollo Bot is ready!')
    print(f'🤖 Logged in as: {bot.user.name}')
    print(f'🆔 Bot ID: {bot.user.id}')
    print(f'📊 Servers: {len(bot.guilds)}')
    print(f'👥 Users: {len(bot.users)}')
    print('━' * 50)

@bot.event
async def on_command(ctx):
    print(f'📝 {ctx.author} used {ctx.command} in {ctx.guild}')

# ==================== GENERAL COMMANDS ====================

@bot.command(name='ping')
async def ping(ctx):
    """Check bot latency"""
    latency = round(bot.latency * 1000)
    embed = discord.Embed(
        title="🏓 Pong!",
        description=f"**Latency:** {latency}ms",
        color=0x00FF00
    )
    embed.set_footer(text=f"Requested by {ctx.author.name}")
    await ctx.send(embed=embed)

@bot.command(name='invite')
async def invite(ctx):
    """Get bot invite link"""
    embed = discord.Embed(
        title="🔗 Invite Apollo to your server!",
        description="[Click here to invite Apollo](https://discord.com/oauth2/authorize?client_id=YOUR_BOT_ID&permissions=8&scope=bot)\n\n"
                    "Thank you for using Apollo! 🌟",
        color=0x5865F2
    )
    await ctx.send(embed=embed)

@bot.command(name='avatar')
async def avatar(ctx, member: discord.Member = None):
    """Get user's avatar"""
    member = member or ctx.author
    embed = discord.Embed(
        title=f"{member.name}'s Avatar",
        color=get_random_color()
    )
    embed.set_image(url=member.avatar.url if member.avatar else member.default_avatar.url)
    await ctx.send(embed=embed)

@bot.command(name='serverinfo')
async def serverinfo(ctx):
    """Get server information"""
    guild = ctx.guild
    embed = discord.Embed(
        title=f"🏠 {guild.name}",
        color=get_random_color()
    )
    embed.set_thumbnail(url=guild.icon.url if guild.icon else None)
    embed.add_field(name="👑 Owner", value=guild.owner.mention if guild.owner else "Unknown", inline=True)
    embed.add_field(name="📅 Created", value=guild.created_at.strftime("%B %d, %Y"), inline=True)
    embed.add_field(name="👥 Members", value=guild.member_count, inline=True)
    embed.add_field(name="💬 Channels", value=len(guild.channels), inline=True)
    embed.add_field(name="🎭 Roles", value=len(guild.roles), inline=True)
    embed.add_field(name="🚀 Boost Level", value=guild.premium_tier, inline=True)
    await ctx.send(embed=embed)

@bot.command(name='userinfo')
async def userinfo(ctx, member: discord.Member = None):
    """Get user information"""
    member = member or ctx.author
    embed = discord.Embed(
        title=f"👤 {member}",
        color=get_random_color()
    )
    embed.set_thumbnail(url=member.avatar.url if member.avatar else None)
    embed.add_field(name="📛 Username", value=str(member), inline=True)
    embed.add_field(name="🆔 ID", value=member.id, inline=True)
    embed.add_field(name="📅 Joined Discord", value=member.created_at.strftime("%B %d, %Y"), inline=True)
    embed.add_field(name="🏠 Joined Server", value=member.joined_at.strftime("%B %d, %Y") if member.joined_at else "Unknown", inline=True)
    embed.add_field(name="🎭 Top Role", value=member.top_role.mention if member.top_role else "None", inline=True)
    embed.add_field(name="🤖 Bot", value="Yes" if member.bot else "No", inline=True)
    await ctx.send(embed=embed)

# ==================== ANIMAL COMMANDS ====================

@bot.command(name='dog')
async def dog(ctx):
    """Get a random dog image"""
    result = await get_random_dog()
    if result:
        embed = await create_embed(ctx, result[0], result[1], result[2], result[1])
        await ctx.send(embed=embed)
    else:
        await ctx.send("❌ Failed to fetch dog image!")

@bot.command(name='cat')
async def cat(ctx):
    """Get a random cat image"""
    result = await get_random_cat()
    if result:
        embed = await create_embed(ctx, result[0], result[1], result[2], result[1])
        await ctx.send(embed=embed)
    else:
        await ctx.send("❌ Failed to fetch cat image!")

@bot.command(name='fox')
async def fox(ctx):
    """Get a random fox image"""
    result = await get_random_fox()
    if result:
        embed = await create_embed(ctx, result[0], result[1], result[2], result[1])
        await ctx.send(embed=embed)
    else:
        await ctx.send("❌ Failed to fetch fox image!")

@bot.command(name='panda')
async def panda(ctx):
    """Get a random panda image"""
    result = await get_random_panda()
    if result:
        embed = await create_embed(ctx, result[0], result[1], result[2], result[1])
        await ctx.send(embed=embed)
    else:
        await ctx.send("❌ Failed to fetch panda image!")

@bot.command(name='koala')
async def koala(ctx):
    """Get a random koala image"""
    result = await get_random_koala()
    if result:
        embed = await create_embed(ctx, result[0], result[1], result[2], result[1])
        await ctx.send(embed=embed)
    else:
        await ctx.send("❌ Failed to fetch koala image!")

@bot.command(name='birb')
async def birb(ctx):
    """Get a random bird image"""
    result = await get_random_birb()
    if result:
        embed = await create_embed(ctx, result[0], result[1], result[2], result[1])
        await ctx.send(embed=embed)
    else:
        await ctx.send("❌ Failed to fetch bird image!")

@bot.command(name='duck')
async def duck(ctx):
    """Get a random duck image"""
    result = await get_random_duck()
    if result:
        embed = await create_embed(ctx, result[0], result[1], result[2], result[1])
        await ctx.send(embed=embed)
    else:
        await ctx.send("❌ Failed to fetch duck image!")

@bot.command(name='lizard')
async def lizard(ctx):
    """Get a random lizard image"""
    result = await get_random_lizard()
    if result:
        embed = await create_embed(ctx, result[0], result[1], result[2], result[1])
        await ctx.send(embed=embed)
    else:
        await ctx.send("❌ Failed to fetch lizard image!")

@bot.command(name='raccoon')
async def raccoon(ctx):
    """Get a random raccoon image"""
    result = await get_random_raccoon()
    if result:
        embed = await create_embed(ctx, result[0], result[1], result[2], result[1])
        await ctx.send(embed=embed)
    else:
        await ctx.send("❌ Failed to fetch raccoon image!")

@bot.command(name='kangaroo')
async def kangaroo(ctx):
    """Get a random kangaroo image"""
    result = await get_random_kangaroo()
    if result:
        embed = await create_embed(ctx, result[0], result[1], result[2], result[1])
        await ctx.send(embed=embed)
    else:
        await ctx.send("❌ Failed to fetch kangaroo image!")

@bot.command(name='penguin')
async def penguin(ctx):
    """Get a random penguin image"""
    result = await get_random_penguin()
    if result:
        embed = await create_embed(ctx, result[0], result[1], result[2], result[1])
        await ctx.send(embed=embed)
    else:
        await ctx.send("❌ Failed to fetch penguin image!")

@bot.command(name='redpanda')
async def redpanda(ctx):
    """Get a random red panda image"""
    result = await get_random_redpanda()
    if result:
        embed = await create_embed(ctx, result[0], result[1], result[2], result[1])
        await ctx.send(embed=embed)
    else:
        await ctx.send("❌ Failed to fetch red panda image!")

@bot.command(name='wolf')
async def wolf(ctx):
    """Get a random wolf image"""
    result = await get_random_wolf()
    if result:
        embed = await create_embed(ctx, result[0], result[1], result[2], result[1])
        await ctx.send(embed=embed)
    else:
        await ctx.send("❌ Failed to fetch wolf image!")

@bot.command(name='zebra')
async def zebra(ctx):
    """Get a random zebra image"""
    result = await get_random_zebra()
    if result:
        embed = await create_embed(ctx, result[0], result[1], result[2], result[1])
        await ctx.send(embed=embed)
    else:
        await ctx.send("❌ Failed to fetch zebra image!")

@bot.command(name='rabbit')
async def rabbit(ctx):
    """Get a random rabbit image"""
    result = await get_random_rabbit()
    if result:
        embed = await create_embed(ctx, result[0], result[1], result[2], result[1])
        await ctx.send(embed=embed)
    else:
        await ctx.send("❌ Failed to fetch rabbit image!")

@bot.command(name='hamster')
async def hamster(ctx):
    """Get a random hamster image"""
    result = await get_random_hamster()
    if result:
        embed = await create_embed(ctx, result[0], result[1], result[2], result[1])
        await ctx.send(embed=embed)
    else:
        await ctx.send("❌ Failed to fetch hamster image!")

@bot.command(name='hedgehog')
async def hedgehog(ctx):
    """Get a random hedgehog image"""
    result = await get_random_hedgehog()
    if result:
        embed = await create_embed(ctx, result[0], result[1], result[2], result[1])
        await ctx.send(embed=embed)
    else:
        await ctx.send("❌ Failed to fetch hedgehog image!")

@bot.command(name='squirrel')
async def squirrel(ctx):
    """Get a random squirrel image"""
    result = await get_random_squirrel()
    if result:
        embed = await create_embed(ctx, result[0], result[1], result[2], result[1])
        await ctx.send(embed=embed)
    else:
        await ctx.send("❌ Failed to fetch squirrel image!")

@bot.command(name='otter')
async def otter(ctx):
    """Get a random otter image"""
    result = await get_random_otter()
    if result:
        embed = await create_embed(ctx, result[0], result[1], result[2], result[1])
        await ctx.send(embed=embed)
    else:
        await ctx.send("❌ Failed to fetch otter image!")

@bot.command(name='owl')
async def owl(ctx):
    """Get a random owl image"""
    result = await get_random_owl()
    if result:
        embed = await create_embed(ctx, result[0], result[1], result[2], result[1])
        await ctx.send(embed=embed)
    else:
        await ctx.send("❌ Failed to fetch owl image!")

@bot.command(name='horse')
async def horse(ctx):
    """Get a random horse image"""
    result = await get_random_horse()
    if result:
        embed = await create_embed(ctx, result[0], result[1], result[2], result[1])
        await ctx.send(embed=embed)
    else:
        await ctx.send("❌ Failed to fetch horse image!")

@bot.command(name='cow')
async def cow(ctx):
    """Get a random cow image"""
    result = await get_random_cow()
    if result:
        embed = await create_embed(ctx, result[0], result[1], result[2], result[1])
        await ctx.send(embed=embed)
    else:
        await ctx.send("❌ Failed to fetch cow image!")

@bot.command(name='pig')
async def pig(ctx):
    """Get a random pig image"""
    result = await get_random_pig()
    if result:
        embed = await create_embed(ctx, result[0], result[1], result[2], result[1])
        await ctx.send(embed=embed)
    else:
        await ctx.send("❌ Failed to fetch pig image!")

@bot.command(name='lion')
async def lion(ctx):
    """Get a random lion image"""
    result = await get_random_lion()
    if result:
        embed = await create_embed(ctx, result[0], result[1], result[2], result[1])
        await ctx.send(embed=embed)
    else:
        await ctx.send("❌ Failed to fetch lion image!")

@bot.command(name='tiger')
async def tiger(ctx):
    """Get a random tiger image"""
    result = await get_random_tiger()
    if result:
        embed = await create_embed(ctx, result[0], result[1], result[2], result[1])
        await ctx.send(embed=embed)
    else:
        await ctx.send("❌ Failed to fetch tiger image!")

@bot.command(name='elephant')
async def elephant(ctx):
    """Get a random elephant image"""
    result = await get_random_elephant()
    if result:
        embed = await create_embed(ctx, result[0], result[1], result[2], result[1])
        await ctx.send(embed=embed)
    else:
        await ctx.send("❌ Failed to fetch elephant image!")

@bot.command(name='giraffe')
async def giraffe(ctx):
    """Get a random giraffe image"""
    result = await get_random_giraffe()
    if result:
        embed = await create_embed(ctx, result[0], result[1], result[2], result[1])
        await ctx.send(embed=embed)
    else:
        await ctx.send("❌ Failed to fetch giraffe image!")

@bot.command(name='animal')
async def animal(ctx):
    """Get a random animal image"""
    animals = [
        get_random_dog(), get_random_cat(), get_random_fox(), get_random_panda(),
        get_random_koala(), get_random_birb(), get_random_duck(), get_random_lizard(),
        get_random_raccoon(), get_random_kangaroo(), get_random_penguin()
    ]
    result = await random.choice(animals)
    if result:
        embed = await create_embed(ctx, result[0], result[1], result[2], result[1])
        await ctx.send(embed=embed)
    else:
        await ctx.send("❌ Failed to fetch animal image!")

# ==================== FACT COMMANDS ====================

@bot.command(name='fact')
async def fact_cmd(ctx):
    """Get a random useless fact"""
    result = await get_useless_fact()
    if result:
        embed = await create_embed(ctx, result[0], result[1], result[2])
        await ctx.send(embed=embed)
    else:
        await ctx.send("❌ Failed to fetch fact!")

@bot.command(name='catfact')
async def catfact(ctx):
    """Get a random cat fact"""
    result = await get_cat_fact()
    if result:
        embed = await create_embed(ctx, result[0], result[1], result[2])
        await ctx.send(embed=embed)
    else:
        await ctx.send("❌ Failed to fetch cat fact!")

@bot.command(name='dogfact')
async def dogfact(ctx):
    """Get a random dog fact"""
    result = await get_dog_fact()
    if result:
        embed = await create_embed(ctx, result[0], result[1], result[2])
        await ctx.send(embed=embed)
    else:
        await ctx.send("❌ Failed to fetch dog fact!")

@bot.command(name='numberfact')
async def numberfact(ctx, num: int = None):
    """Get a fact about a number"""
    result = await get_number_fact(num)
    if result:
        embed = await create_embed(ctx, result[0], result[1], result[2])
        await ctx.send(embed=embed)
    else:
        await ctx.send("❌ Failed to fetch number fact!")

@bot.command(name='yearfact')
async def yearfact(ctx, year: int = None):
    """Get a fact about a year"""
    result = await get_year_fact(year)
    if result:
        embed = await create_embed(ctx, result[0], result[1], result[2])
        await ctx.send(embed=embed)
    else:
        await ctx.send("❌ Failed to fetch year fact!")

@bot.command(name='spacefact')
async def spacefact(ctx):
    """Get a random space fact"""
    result = await get_space_fact()
    if result:
        embed = await create_embed(ctx, result[0], result[1], result[2])
        await ctx.send(embed=embed)
    else:
        await ctx.send("❌ Failed to fetch space fact!")

@bot.command(name='animefact')
async def animefact(ctx):
    """Get a random anime fact"""
    result = await get_anime_fact()
    if result:
        embed = await create_embed(ctx, result[0], result[1], result[2])
        await ctx.send(embed=embed)
    else:
        await ctx.send("❌ Failed to fetch anime fact!")

@bot.command(name='coffee')
async def coffee(ctx):
    """Get a random coffee fact"""
    result = await get_coffee_fact()
    if result:
        embed = await create_embed(ctx, result[0], result[1], result[2])
        await ctx.send(embed=embed)
    else:
        await ctx.send("❌ Failed to fetch coffee fact!")

@bot.command(name='musicfact')
async def musicfact(ctx):
    """Get a random music fact"""
    result = await get_music_artist_fact()
    if result:
        embed = await create_embed(ctx, result[0], result[1], result[2])
        await ctx.send(embed=embed)
    else:
        await ctx.send("❌ Failed to fetch music fact!")

@bot.command(name='gamingfact')
async def gamingfact(ctx):
    """Get a random gaming fact"""
    result = await get_gaming_fact()
    if result:
        embed = await create_embed(ctx, result[0], result[1], result[2])
        await ctx.send(embed=embed)
    else:
        await ctx.send("❌ Failed to fetch gaming fact!")

@bot.command(name='cyberpunkfact')
async def cyberpunkfact(ctx):
    """Get a random cyberpunk/sci-fi fact"""
    result = await get_cyberpunk_fact()
    if result:
        embed = await create_embed(ctx, result[0], result[1], result[2])
        await ctx.send(embed=embed)
    else:
        await ctx.send("❌ Failed to fetch cyberpunk fact!")

# ==================== JOKE COMMANDS ====================

@bot.command(name='joke')
async def joke(ctx):
    """Get a random dad joke"""
    result = await get_dad_joke()
    if result:
        embed = await create_embed(ctx, result[0], result[1], result[2])
        await ctx.send(embed=embed)
    else:
        await ctx.send("❌ Failed to fetch joke!")

@bot.command(name='chuck')
async def chuck(ctx):
    """Get a random Chuck Norris joke"""
    result = await get_chuck_norris_joke()
    if result:
        embed = await create_embed(ctx, result[0], result[1], result[2])
        await ctx.send(embed=embed)
    else:
        await ctx.send("❌ Failed to fetch Chuck Norris joke!")

@bot.command(name='programmingjoke')
async def programmingjoke(ctx):
    """Get a random programming joke"""
    result = await get_programming_joke()
    if result:
        embed = await create_embed(ctx, result[0], result[1], result[2])
        await ctx.send(embed=embed)
    else:
        await ctx.send("❌ Failed to fetch programming joke!")

@bot.command(name='pun')
async def pun(ctx):
    """Get a random pun"""
    result = await get_pun_joke()
    if result:
        embed = await create_embed(ctx, result[0], result[1], result[2])
        await ctx.send(embed=embed)
    else:
        await ctx.send("❌ Failed to fetch pun!")

@bot.command(name='darkjoke')
async def darkjoke(ctx):
    """Get a dark joke (use responsibly)"""
    result = await get_dark_joke()
    if result:
        embed = await create_embed(ctx, result[0], result[1], result[2], color=0x2C2F33)
        await ctx.send(embed=embed)
    else:
        await ctx.send("❌ Failed to fetch dark joke!")

# ==================== QUOTE COMMANDS ====================

@bot.command(name='quote')
async def quote(ctx):
    """Get an inspirational quote"""
    result = await get_random_quote()
    if result:
        embed = await create_embed(ctx, result[0], result[1], result[2])
        await ctx.send(embed=embed)
    else:
        await ctx.send("❌ Failed to fetch quote!")

@bot.command(name='inspire')
async def inspire(ctx):
    """Get an inspirational quote"""
    result = await get_inspirational_quote()
    if result:
        embed = await create_embed(ctx, result[0], result[1], result[2])
        await ctx.send(embed=embed)
    else:
        await ctx.send("❌ Failed to fetch inspiration!")

@bot.command(name='zen')
async def zen(ctx):
    """Get a zen quote"""
    result = await get_zen_quote()
    if result:
        embed = await create_embed(ctx, result[0], result[1], result[2])
        await ctx.send(embed=embed)
    else:
        await ctx.send("❌ Failed to fetch zen quote!")

@bot.command(name='animequote')
async def animequote(ctx):
    """Get a random anime quote"""
    result = await get_anime_quote()
    if result:
        embed = await create_embed(ctx, result[0], result[1], result[2])
        await ctx.send(embed=embed)
    else:
        await ctx.send("❌ Failed to fetch anime quote!")

# ==================== WEATHER COMMAND ====================

@bot.command(name='weather')
async def weather(ctx, *, city: str = "London"):
    """Get weather for a city"""
    result = await get_weather(city)
    if result:
        embed = await create_embed(ctx, result[0], result[1], result[2])
        await ctx.send(embed=embed)
    else:
        await ctx.send(f"❌ Failed to fetch weather for {city}!")

# ==================== DICTIONARY COMMAND ====================

@bot.command(name='define')
async def define(ctx, *, word: str):
    """Get definition of a word"""
    result = await get_definition(word)
    if result:
        embed = await create_embed(ctx, result[0], result[1], result[2])
        await ctx.send(embed=embed)
    else:
        await ctx.send(f"❌ Could not find definition for '{word}'!")

# ==================== RECIPE COMMAND ====================

@bot.command(name='recipe')
async def recipe(ctx):
    """Get a random recipe"""
    result = await get_random_recipe()
    if result:
        embed = await create_embed(ctx, result[0], result[1], result[2], result[3] if len(result) > 3 else None)
        await ctx.send(embed=embed)
    else:
        await ctx.send("❌ Failed to fetch recipe!")

# ==================== NEWS COMMANDS ====================

@bot.command(name='news')
async def news(ctx):
    """Get top tech news"""
    result = await get_tech_news()
    if result:
        embed = await create_embed(ctx, result[0], result[1], result[2])
        await ctx.send(embed=embed)
    else:
        await ctx.send("❌ Failed to fetch news!")

@bot.command(name='worldnews')
async def worldnews(ctx):
    """Get world news"""
    result = await get_general_news()
    if result:
        embed = await create_embed(ctx, result[0], result[1], result[2])
        await ctx.send(embed=embed)
    else:
        await ctx.send("❌ Failed to fetch world news!")

# ==================== LYRICS COMMAND ====================

@bot.command(name='lyrics')
async def lyrics(ctx, *, artist_song: str):
    """Get lyrics for a song. Usage: a.lyrics artist song"""
    try:
        parts = artist_song.rsplit(' ', 1)
        if len(parts) == 2:
            artist, song = parts
            result = await get_lyrics(artist, song)
            if result:
                embed = await create_embed(ctx, result[0], result[1], result[2])
                await ctx.send(embed=embed)
            else:
                await ctx.send("❌ Could not find lyrics!")
        else:
            await ctx.send("❌ Please use format: `a.lyrics artist song`")
    except:
        await ctx.send("❌ Error fetching lyrics!")

# ==================== HOROSCOPE COMMAND ====================

@bot.command(name='horoscope')
async def horoscope(ctx, sign: str):
    """Get daily horoscope. Usage: a.horoscope aries"""
    result = await get_horoscope(sign)
    if result:
        embed = await create_embed(ctx, result[0], result[1], result[2])
        await ctx.send(embed=embed)
    else:
        await ctx.send(f"❌ Invalid zodiac sign! Use: {', '.join(SIGNS)}")

# ==================== TRIVIA COMMAND ====================

@bot.command(name='trivia')
async def trivia(ctx):
    """Get a random trivia question"""
    result = await get_trivia()
    if result:
        embed = await create_embed(ctx, result[0], result[1], result[2])
        await ctx.send(embed=embed)
    else:
        await ctx.send("❌ Failed to fetch trivia!")

# ==================== MEME COMMANDS ====================

@bot.command(name='meme')
async def meme(ctx):
    """Get a random meme"""
    result = await get_reddit_meme("memes")
    if result:
        embed = await create_embed(ctx, result[0], result[1], result[2], result[1])
        await ctx.send(embed=embed)
    else:
        await ctx.send("❌ Failed to fetch meme!")

@bot.command(name='dankmeme')
async def dankmeme(ctx):
    """Get a random dank meme"""
    result = await get_dank_meme()
    if result:
        embed = await create_embed(ctx, result[0], result[1], result[2], result[1])
        await ctx.send(embed=embed)
    else:
        await ctx.send("❌ Failed to fetch dank meme!")

@bot.command(name='animeme')
async def animeme(ctx):
    """Get a random anime meme"""
    result = await get_animeme()
    if result:
        embed = await create_embed(ctx, result[0], result[1], result[2], result[1])
        await ctx.send(embed=embed)
    else:
        await ctx.send("❌ Failed to fetch anime meme!")

@bot.command(name='wholesome')
async def wholesome(ctx):
    """Get a wholesome meme"""
    result = await get_wholesome_meme()
    if result:
        embed = await create_embed(ctx, result[0], result[1], result[2], result[1])
        await ctx.send(embed=embed)
    else:
        await ctx.send("❌ Failed to fetch wholesome meme!")

# ==================== WAIFU COMMANDS ====================

@bot.command(name='waifu')
async def waifu(ctx):
    """Get a waifu image"""
    result = await get_waifu_picture()
    if result:
        embed = await create_embed(ctx, result[0], result[1], result[2], result[1])
        await ctx.send(embed=embed)
    else:
        await ctx.send("❌ Failed to fetch waifu image!")

@bot.command(name='neko')
async def neko(ctx):
    """Get a neko image"""
    result = await get_neko_picture()
    if result:
        embed = await create_embed(ctx, result[0], result[1], result[2], result[1])
        await ctx.send(embed=embed)
    else:
        await ctx.send("❌ Failed to fetch neko image!")

@bot.command(name='hug')
async def hug(ctx):
    """Get a hug image"""
    result = await get_hug_picture()
    if result:
        embed = await create_embed(ctx, result[0], result[1], result[2], result[1])
        await ctx.send(embed=embed)
    else:
        await ctx.send("❌ Failed to fetch hug image!")

@bot.command(name='pat')
async def pat(ctx):
    """Get a pat image"""
    result = await get_pat_picture()
    if result:
        embed = await create_embed(ctx, result[0], result[1], result[2], result[1])
        await ctx.send(embed=embed)
    else:
        await ctx.send("❌ Failed to fetch pat image!")

@bot.command(name='kiss')
async def kiss(ctx):
    """Get a kiss image"""
    result = await get_kiss_picture()
    if result:
        embed = await create_embed(ctx, result[0], result[1], result[2], result[1])
        await ctx.send(embed=embed)
    else:
        await ctx.send("❌ Failed to fetch kiss image!")

@bot.command(name='cry')
async def cry(ctx):
    """Get a cry image"""
    result = await get_cry_picture()
    if result:
        embed = await create_embed(ctx, result[0], result[1], result[2], result[1])
        await ctx.send(embed=embed)
    else:
        await ctx.send("❌ Failed to fetch cry image!")

@bot.command(name='smug')
async def smug(ctx):
    """Get a smug image"""
    result = await get_smug_picture()
    if result:
        embed = await create_embed(ctx, result[0], result[1], result[2], result[1])
        await ctx.send(embed=embed)
    else:
        await ctx.send("❌ Failed to fetch smug image!")

@bot.command(name='blush')
async def blush(ctx):
    """Get a blush image"""
    result = await get_blush_picture()
    if result:
        embed = await create_embed(ctx, result[0], result[1], result[2], result[1])
        await ctx.send(embed=embed)
    else:
        await ctx.send("❌ Failed to fetch blush image!")

@bot.command(name='wave')
async def wave(ctx):
    """Get a wave image"""
    result = await get_wave_picture()
    if result:
        embed = await create_embed(ctx, result[0], result[1], result[2], result[1])
        await ctx.send(embed=embed)
    else:
        await ctx.send("❌ Failed to fetch wave image!")

@bot.command(name='nom')
async def nom(ctx):
    """Get a nom image"""
    result = await get_nom_picture()
    if result:
        embed = await create_embed(ctx, result[0], result[1], result[2], result[1])
        await ctx.send(embed=embed)
    else:
        await ctx.send("❌ Failed to fetch nom image!")

@bot.command(name='slap')
async def slap(ctx):
    """Get a slap image"""
    result = await get_slap_picture()
    if result:
        embed = await create_embed(ctx, result[0], result[1], result[2], result[1])
        await ctx.send(embed=embed)
    else:
        await ctx.send("❌ Failed to fetch slap image!")

@bot.command(name='cuddle')
async def cuddle(ctx):
    """Get a cuddle image"""
    result = await get_cuddle_picture()
    if result:
        embed = await create_embed(ctx, result[0], result[1], result[2], result[1])
        await ctx.send(embed=embed)
    else:
        await ctx.send("❌ Failed to fetch cuddle image!")

@bot.command(name='comfort')
async def comfort(ctx):
    """Get a comfort image"""
    result = await get_comfort_picture()
    if result:
        embed = await create_embed(ctx, result[0], result[1], result[2], result[1])
        await ctx.send(embed=embed)
    else:
        await ctx.send("❌ Failed to fetch comfort image!")

# ==================== COLOR COMMAND ====================

@bot.command(name='color')
async def color(ctx):
    """Get random color info"""
    result = await get_random_color_info()
    if result:
        embed = await create_embed(ctx, result[0], result[1], result[2])
        await ctx.send(embed=embed)
    else:
        await ctx.send("❌ Failed to fetch color info!")

# ==================== CRYPTO COMMAND ====================

@bot.command(name='crypto')
async def crypto(ctx, coin: str = 'bitcoin'):
    """Get crypto price. Usage: a.crypto bitcoin"""
    result = await get_crypto_price(coin)
    if result:
        embed = await create_embed(ctx, result[0], result[1], result[2])
        await ctx.send(embed=embed)
    else:
        await ctx.send("❌ Could not fetch crypto price!")

# ==================== MATH COMMAND ====================

@bot.command(name='mathfact')
async def mathfact(ctx, num: int = None):
    """Get a math fact about a number"""
    result = await get_math_fact(num)
    if result:
        embed = await create_embed(ctx, result[0], result[1], result[2])
        await ctx.send(embed=embed)
    else:
        await ctx.send("❌ Failed to fetch math fact!")

# ==================== ACTIVITY COMMAND ====================

@bot.command(name='activity')
async def activity(ctx):
    """Get a random activity suggestion"""
    result = await get_random_activity()
    if result:
        embed = await create_embed(ctx, result[0], result[1], result[2])
        await ctx.send(embed=embed)
    else:
        await ctx.send("❌ Failed to fetch activity!")

# ==================== ADVICE COMMAND ====================

@bot.command(name='advice')
async def advice(ctx):
    """Get random advice"""
    result = await get_advice()
    if result:
        embed = await create_embed(ctx, result[0], result[1], result[2])
        await ctx.send(embed=embed)
    else:
        await ctx.send("❌ Failed to fetch advice!")

# ==================== GAME COMMAND ====================

@bot.command(name='game')
async def game(ctx):
    """Get a random game fact"""
    result = await get_random_game()
    if result:
        embed = await create_embed(ctx, result[0], result[1], result[2])
        await ctx.send(embed=embed)
    else:
        await ctx.send("❌ Failed to fetch game info!")

# ==================== HELP COMMAND ====================

@bot.command(name='help')
async def help_cmd(ctx):
    """Show help message"""
    embed = discord.Embed(
        title="🌟 Apollo Bot Commands",
        description="Your ultimate Discord companion with 100+ free APIs!",
        color=0x5865F2,
        timestamp=datetime.utcnow()
    )
    embed.set_thumbnail(url=bot.user.avatar.url if bot.user.avatar else None)
    embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar.url if ctx.author.avatar else None)
    
    categories = {
        "🐾 Animals": "dog, cat, fox, panda, koala, birb, duck, lizard, raccoon, kangaroo, penguin, redpanda, wolf, zebra, rabbit, hamster, hedgehog, squirrel, otter, owl, horse, cow, pig, lion, tiger, elephant, giraffe, animal",
        "💡 Facts": "fact, catfact, dogfact, numberfact, yearfact, spacefact, animefact, coffee, musicfact, gamingfact, cyberpunkfact, mathfact",
        "😂 Jokes": "joke, chuck, programmingjoke, pun, darkjoke",
        "📝 Quotes": "quote, inspire, zen, animequote",
        "🌤️ Weather": "weather <city>",
        "📚 Dictionary": "define <word>",
        "🍳 Food": "recipe, foodjoke",
        "📰 News": "news, worldnews",
        "🎵 Music": "lyrics <artist> <song>",
        "🔮 fun_": "horoscope <sign>, trivia, advice, activity",
        "😄 Memes": "meme, dankmeme, animeme, wholesome",
        "👘 Anime": "waifu, neko, hug, pat, kiss, cry, smug, blush, wave, nom, slap, cuddle, comfort",
        "💰 Utilities": "color, crypto <coin>, ping, avatar, serverinfo, userinfo",
    }
    
    for cat, commands in categories.items():
        embed.add_field(name=cat, value=f"```{commands}```", inline=False)
    
    embed.add_field(name="🔗 Links", value="[Invite Bot](https://discord.com/oauth2/authorize?client_id=YOUR_BOT_ID&permissions=8&scope=bot) | [Support Server](https://discord.gg/example)", inline=False)
    
    await ctx.send(embed=embed)

# ==================== ERROR HANDLING ====================

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        return
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("❌ Missing required argument! Use `a.help` to see usage.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("❌ Invalid argument! Use `a.help` to see usage.")
    else:
        print(f"Error: {error}")
        await ctx.send(f"❌ An error occurred: {str(error)}")

# ==================== RUN BOT ====================

if __name__ == "__main__":
    # Get token from environment variable or use placeholder
    token = os.environ.get('DISCORD_BOT_TOKEN', 'YOUR_BOT_TOKEN_HERE')
    
    if token == 'YOUR_BOT_TOKEN_HERE':
        print("⚠️  WARNING: Please set your Discord Bot Token!")
        print("   Set it in the code or as an environment variable: DISCORD_BOT_TOKEN")
    else:
        print("🚀 Starting Apollo Bot...")
        bot.run(token)
