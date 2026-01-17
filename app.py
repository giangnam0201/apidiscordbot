import streamlit as st
import threading
import os
import asyncio
import sys
import time
# --- 1. THE "ULTIMATE" GLOBAL LOCK ---
# We check if our custom 'bot_lock' exists in the system modules.
# This prevents the bot from starting twice, even if the page is refreshed.
if "bot_lock" not in sys.modules:
    sys.modules["bot_lock"] = True
    FIRST_RUN = True
else:
    FIRST_RUN = False

# --- 2. STREAMLIT UI ---
st.set_page_config(page_title="Bot Server", page_icon="🚀")
st.title("Service Status: Online ✅")
st.write("The bot is running in the background.")

# BRIDGE: Injects Streamlit Secrets into the environment
for key, value in st.secrets.items():
    os.environ[key] = str(value)

# --- 3. YOUR CODE ---
RAW_CODE = """
import os
import asyncio
import aiohttp
import discord
import random
from discord.ext import commands
from dotenv import load_dotenv

# --- CONFIG ---
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)
bot.remove_command('help')

# --- THE MEGA API MAP (100+ UNIQUE SITES) ---
# Format: "cmd": {"url": "...", "path": "JSON.Path", "type": "text|image|plain", "site": "Provider"}
APIS = {
    # ANIMALS (Unique Sites)
    "cat": {"url": "https://aws.random.cat/meow", "path": "file", "type": "image", "site": "random.cat"},
    "dog": {"url": "https://dog.ceo/api/breeds/image/random", "path": "message", "type": "image", "site": "dog.ceo"},
    "fox": {"url": "https://randomfox.ca/floof/", "path": "image", "type": "image", "site": "randomfox.ca"},
    "duck": {"url": "https://random-d.uk/api/v2/random", "path": "url", "type": "image", "site": "random-d.uk"},
    "shibe": {"url": "https://shibe.online/api/shibes?count=1", "path": "0", "type": "image", "site": "shibe.online"},
    "panda": {"url": "https://some-random-api.com/img/panda", "path": "link", "type": "image", "site": "some-random-api"},
    "axolotl": {"url": "https://axoltlapi.herokuapp.com/", "path": "url", "type": "image", "site": "axoltlapi"},
    "catfact": {"url": "https://catfact.ninja/fact", "path": "fact", "type": "text", "site": "catfact.ninja"},
    "dogfact": {"url": "https://dog-api.kinduff.com/api/facts", "path": "facts.0", "type": "text", "site": "dog-api"},
    "meow": {"url": "https://meowfacts.herokuapp.com/", "path": "data.0", "type": "text", "site": "meowfacts"},

    # FUN & JOKES (Unique Sites)
    "joke": {"url": "https://v2.jokeapi.dev/joke/Any?type=single", "path": "joke", "type": "text", "site": "jokeapi.dev"},
    "dadjoke": {"url": "https://icanhazdadjoke.com/", "path": None, "type": "json_text", "site": "icanhazdadjoke.com"},
    "kanye": {"url": "https://api.kanye.rest/", "path": "quote", "type": "text", "site": "kanye.rest"},
    "chuck": {"url": "https://api.chucknorris.io/jokes/random", "path": "value", "type": "text", "site": "chucknorris.io"},
    "trump": {"url": "https://api.whatdoestrumpthink.com/api/v1/quotes/random", "path": "message", "type": "text", "site": "whatdoestrumpthink.com"},
    "advice": {"url": "https://api.adviceslip.com/advice", "path": "slip.advice", "type": "text", "site": "adviceslip.com"},
    "affirm": {"url": "https://www.affirmations.dev/", "path": "affirmation", "type": "text", "site": "affirmations.dev"},
    "insult": {"url": "https://evilinsult.com/generate_insult.php?lang=en&type=json", "path": "insult", "type": "text", "site": "evilinsult.com"},
    "geek": {"url": "https://geek-jokes.sameerkumar.website/api?format=json", "path": "joke", "type": "text", "site": "geek-jokes"},
    "boring": {"url": "https://bored.api.lewagon.com/api/activity", "path": "activity", "type": "text", "site": "lewagon.com"},

    # DATA & UTILITY (Unique Sites)
    "ip": {"url": "https://api.ipify.org?format=json", "path": "ip", "type": "text", "site": "ipify.org"},
    "ipinfo": {"url": "http://ip-api.com/json/", "path": "query", "type": "text", "site": "ip-api.com"},
    "uuid": {"url": "https://www.uuidtools.com/api/generate/v1", "path": "0", "type": "text", "site": "uuidtools.com"},
    "gender": {"url": "https://api.genderize.io/?name=alex", "path": "gender", "type": "text", "site": "genderize.io"},
    "age": {"url": "https://api.agify.io/?name=alex", "path": "age", "type": "text", "site": "agify.io"},
    "nation": {"url": "https://api.nationalize.io/?name=nathaniel", "path": "country.0.country_id", "type": "text", "site": "nationalize.io"},
    "excuse": {"url": "https://excuser-three.vercel.app/v1/excuse", "path": "0.excuse", "type": "text", "site": "excuser-three"},
    "tech": {"url": "https://techy-api.vercel.app/api/json", "path": "message", "type": "text", "site": "techy-api"},
    "corp": {"url": "https://corporatebs-generator.sameerkumar.website/", "path": "phrase", "type": "text", "site": "corp-bs"},
    "wiki": {"url": "https://en.wikipedia.org/api/rest_v1/page/random/summary", "path": "extract", "type": "text", "site": "wikipedia.org"},

    # NUMBERS & FACTS (Unique Sites)
    "fact": {"url": "https://uselessfacts.jsph.pl/random.json?language=en", "path": "text", "type": "text", "site": "uselessfacts"},
    "number": {"url": "http://numbersapi.com/random/trivia", "path": None, "type": "plain", "site": "numbersapi.com"},
    "iss": {"url": "http://api.open-notify.org/iss-now.json", "path": "iss_position", "type": "text", "site": "open-notify.org"},
    "space": {"url": "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY", "path": "url", "type": "image", "site": "nasa.gov"},
    "spacex": {"url": "https://api.spacexdata.com/v4/launches/latest", "path": "name", "type": "text", "site": "spacexdata.com"},
    "bitcoin": {"url": "https://api.coindesk.com/v1/bpi/currentprice.json", "path": "bpi.USD.rate", "type": "text", "site": "coindesk.com"},
    "crypto": {"url": "https://api.coincap.io/v2/assets/bitcoin", "path": "data.priceUsd", "type": "text", "site": "coincap.io"},
    "eth": {"url": "https://api.binance.com/api/v3/ticker/price?symbol=ETHUSDT", "path": "price", "type": "text", "site": "binance.com"},
    "exchange": {"url": "https://open.er-api.com/v6/latest/USD", "path": "rates.EUR", "type": "text", "site": "er-api.com"},
    "weather": {"url": "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current_weather=true", "path": "current_weather.temperature", "type": "text", "site": "open-meteo.com"},

    # POP CULTURE (Unique Sites)
    "poke": {"url": "https://pokeapi.co/api/v2/pokemon/1", "path": "sprites.front_default", "type": "image", "site": "pokeapi.co"},
    "ghibli": {"url": "https://ghibliapi.vercel.app/films", "path": "0.title", "type": "text", "site": "ghibliapi"},
    "breakingbad": {"url": "https://api.breakingbadquotes.xyz/v1/quotes", "path": "0.quote", "type": "text", "site": "breakingbadquotes"},
    "swapi": {"url": "https://swapi.dev/api/people/1/", "path": "name", "type": "text", "site": "swapi.dev"},
    "marvel": {"url": "https://whenisthenextmcufilm.com/api", "path": "title", "type": "text", "site": "whenisthenextmcu"},
    "disney": {"url": "https://api.disneyapi.dev/character", "path": "data.0.name", "type": "text", "site": "disneyapi"},
    "rick": {"url": "https://rickandmortyapi.com/api/character/1", "path": "name", "type": "text", "site": "rickandmortyapi"},
    "simpsons": {"url": "https://thesimpsonsquoteapi.glitch.me/quotes", "path": "0.quote", "type": "text", "site": "glitch.me"},
    "futurama": {"url": "https://futuramaapi.herokuapp.com/api/quotes", "path": "0.quote", "type": "text", "site": "futuramaapi"},
    "potter": {"url": "https://api.potterdb.com/v1/characters", "path": "data.0.attributes.name", "type": "text", "site": "potterdb.com"},

    # ANIME (Unique Sites)
    "waifu": {"url": "https://api.waifu.pics/sfw/waifu", "path": "url", "type": "image", "site": "waifu.pics"},
    "neko": {"url": "https://nekos.best/api/v2/neko", "path": "results.0.url", "type": "image", "site": "nekos.best"},
    "animequote": {"url": "https://animechan.xyz/api/random", "path": "quote", "type": "text", "site": "animechan.xyz"},
    "catboy": {"url": "https://api.catboys.com/img", "path": "url", "type": "image", "site": "catboys.com"},
    "nekoslife": {"url": "https://nekos.life/api/v2/img/neko", "path": "url", "type": "image", "site": "nekos.life"},
    "jikan": {"url": "https://api.jikan.moe/v4/random/anime", "path": "data.title", "type": "text", "site": "jikan.moe"},
    "anifact": {"url": "https://anime-facts-rest-api.herokuapp.com/api/v1", "path": "data.0.fact", "type": "text", "site": "anime-facts"},

    # FOOD & DRINK (Unique Sites)
    "coffee": {"url": "https://coffee.alexflipnote.dev/random.json", "path": "file", "type": "image", "site": "alexflipnote.dev"},
    "foodish": {"url": "https://foodish-api.com/api/", "path": "image", "type": "image", "site": "foodish-api.com"},
    "brewery": {"url": "https://api.openbrewerydb.org/breweries/random", "path": "0.name", "type": "text", "site": "openbrewerydb.org"},
    "cocktail": {"url": "https://www.thecocktaildb.com/api/json/v1/1/random.php", "path": "drinks.0.strDrink", "type": "text", "site": "thecocktaildb.com"},
    "meal": {"url": "https://www.themealdb.com/api/json/v1/1/random.php", "path": "meals.0.strMeal", "type": "text", "site": "themealdb.com"},
    "wine": {"url": "https://api.sampleapis.com/wines/reds", "path": "0.wine", "type": "text", "site": "sampleapis.com"},

    # GENERATORS (Unique Sites)
    "robo": {"url": "https://robohash.org/asdf", "path": None, "type": "direct_image", "site": "robohash.org"},
    "avatar": {"url": "https://api.dicebear.com/7.x/avataaars/svg?seed=Lucky", "path": None, "type": "direct_image", "site": "dicebear.com"},
    "picsum": {"url": "https://picsum.photos/400/300", "path": None, "type": "direct_image", "site": "picsum.photos"},
    "qr": {"url": "https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=Hello", "path": None, "type": "direct_image", "site": "qrserver.com"},
    "yesno": {"url": "https://yesno.wtf/api", "path": "image", "type": "image", "site": "yesno.wtf"},
    "user": {"url": "https://randomuser.me/api/", "path": "results.0.email", "type": "text", "site": "randomuser.me"},
    "pravatar": {"url": "https://i.pravatar.cc/300", "path": None, "type": "direct_image", "site": "pravatar.cc"},
    "bear": {"url": "https://placebear.com/400/300", "path": None, "type": "direct_image", "site": "placebear.com"},
    "murray": {"url": "https://www.fillmurray.com/400/300", "path": None, "type": "direct_image", "site": "fillmurray.com"},

    # MISC & TECH (Unique Sites)
    "httpcat": {"url": "https://http.cat/200", "path": None, "type": "direct_image", "site": "http.cat"},
    "httpdog": {"url": "https://http.dog/200.jpg", "path": None, "type": "direct_image", "site": "http.dog"},
    "emoji": {"url": "https://emojihub.yurace.pro/api/random", "path": "unicode.0", "type": "text", "site": "emojihub"},
    "color": {"url": "https://x-colors.yurace.pro/api/random", "path": "hex", "type": "text", "site": "x-colors.yurace"},
    "bible": {"url": "https://bible-api.com/john 3:16", "path": "text", "type": "text", "site": "bible-api.com"},
    "quran": {"url": "https://api.alquran.cloud/v1/ayah/random", "path": "data.text", "type": "text", "site": "alquran.cloud"},
    "word": {"url": "https://api.dictionaryapi.dev/api/v2/entries/en/hello", "path": "0.meanings.0.definitions.0.definition", "type": "text", "site": "dictionaryapi.dev"},
    "poem": {"url": "https://poetrydb.org/random/1", "path": "0.lines.0", "type": "text", "site": "poetrydb.org"},
    "binary": {"url": "https://networkcalc.com/api/binary/10101010", "path": "converted", "type": "text", "site": "networkcalc.com"},
    "deck": {"url": "https://deckofcardsapi.com/api/deck/new/draw/?count=1", "path": "cards.0.image", "type": "image", "site": "deckofcardsapi.com"},
    "tv": {"url": "https://api.tvmaze.com/search/shows?q=girls", "path": "0.show.name", "type": "text", "site": "tvmaze.com"},
    "pray": {"url": "http://api.aladhan.com/v1/timingsByCity?city=London&country=UK&method=2", "path": "data.timings.Fajr", "type": "text", "site": "aladhan.com"},
    "country": {"url": "https://restcountries.com/v3.1/all", "path": "0.name.common", "type": "text", "site": "restcountries.com"},
    "nobel": {"url": "https://api.nobelprize.org/2.1/laureates?limit=1", "path": "laureates.0.knownName.en", "type": "text", "site": "nobelprize.org"},
    "github": {"url": "https://api.github.com/users/github", "path": "bio", "type": "text", "site": "github.com"},
    "art": {"url": "https://api.artic.edu/api/v1/artworks/search?q=cats", "path": "data.0.title", "type": "text", "site": "artic.edu"},
    "met": {"url": "https://collectionapi.metmuseum.org/public/collection/v1/objects/1", "path": "title", "type": "text", "site": "metmuseum.org"},
    "forbes": {"url": "https://forbes400.herokuapp.com/api/forbes400?limit=1", "path": "0.uri", "type": "text", "site": "forbes400"},
    "magic": {"url": "https://eightballapi.com/api", "path": "reading", "type": "text", "site": "eightballapi.com"},
    "status": {"url": "https://www.githubstatus.com/api/v2/status.json", "path": "status.description", "type": "text", "site": "githubstatus.com"},
    "amiibo": {"url": "https://www.amiiboapi.com/api/amiibo/", "path": "amiibo.0.name", "type": "text", "site": "amiiboapi.com"},
    "fortnite": {"url": "https://fortnite-api.com/v2/news", "path": "data.br.image", "type": "image", "site": "fortnite-api.com"},
    "pubg": {"url": "https://api.pubg.com/shards/steam/samples", "path": "data.id", "type": "text", "site": "pubg.com"},
    "placegoat": {"url": "https://placegoat.com/400/300", "path": None, "type": "direct_image", "site": "placegoat.com"},
    "placekitten": {"url": "https://placekitten.com/400/300", "path": None, "type": "direct_image", "site": "placekitten.com"},
    "beard": {"url": "https://placebeard.it/400/300", "path": None, "type": "direct_image", "site": "placebeard.it"},
}

# --- ENGINE ---
async def fetch(url, headers=None):
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers, timeout=10) as resp:
            if resp.status == 200:
                if "application/json" in resp.headers.get("Content-Type", ""):
                    return await resp.json()
                return await resp.text()
    return None

def get_val(data, path):
    if not path: return data
    try:
        for key in path.split('.'):
            data = data[int(key)] if isinstance(data, list) else data[key]
        return data
    except: return "Error Parsing"

# --- DYNAMIC COMMAND REGISTRATION ---
def create_command(name, cfg):
    @bot.command(name=name)
    async def _cmd(ctx):
        emb = discord.Embed(color=random.randint(0, 0xFFFFFF), title=f"!{name} (via {cfg['site']})")
        try:
            if cfg['type'] == 'direct_image':
                emb.set_image(url=cfg['url'])
            else:
                headers = {"Accept": "application/json"} if cfg['type'] == 'json_text' else None
                data = await fetch(cfg['url'], headers)
                val = get_val(data, cfg['path'])
                
                if cfg['type'] == 'image': emb.set_image(url=val)
                else: emb.description = f"**{val}**"
        except: emb.description = "❌ API Offline"
        await ctx.send(embed=emb)
    return _cmd

for n, c in APIS.items(): create_command(n, c)

@bot.event
async def on_ready():
    print(f"🔥 ONLINE | Loaded {len(APIS)} Unique Sites")

@bot.command()
async def help(ctx):
    e = discord.Embed(title="🚀 Mega API Bot", description=f"Using **{len(APIS)}** different website APIs!", color=0x00ff00)
    e.add_field(name="Examples", value="`!cat`, `!joke`, `!space`, `!poke`, `!bitcoin`, `!waifu`, `!weather`, `!github`...", inline=False)
    await ctx.send(embed=e)

bot.run(TOKEN)
"""

# --- 4. STARTUP ENGINE ---
def run_bot():
    # Setup new loop for this specific background thread
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    
    # Passing 'globals()' ensures functions can see each other
    exec(RAW_CODE, globals())

if FIRST_RUN:
    thread = threading.Thread(target=run_bot, daemon=True)
    thread.start()
    st.success("🚀 Bot launched for the first time!")
else:
    st.info("ℹ️ Bot is already running in the background.")

# Show a small clock so the user knows the page is "alive"
st.divider()
st.caption(f"Last page refresh: {time.strftime('%H:%M:%S')}")
