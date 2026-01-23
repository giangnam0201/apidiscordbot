from aiohttp import web
import os
import asyncio
import time
import logging
import platform
import psutil

# ---------------- CONFIG ----------------
START_TIME = time.time()
APP_NAME = "Discord API Master Bot"

logging.basicConfig(
    level=logging.INFO,
    format="🌐 [WEB] %(asctime)s | %(levelname)s | %(message)s",
)

# Optional: attach bot later
BOT = None

def attach_bot(bot):
    global BOT
    BOT = bot


# ---------------- HELPERS ----------------
def uptime():
    seconds = int(time.time() - START_TIME)
    mins, sec = divmod(seconds, 60)
    hrs, mins = divmod(mins, 60)
    days, hrs = divmod(hrs, 24)
    return f"{days}d {hrs}h {mins}m {sec}s"


def system_stats():
    return {
        "cpu_percent": psutil.cpu_percent(),
        "memory_percent": psutil.virtual_memory().percent,
        "python": platform.python_version(),
        "platform": platform.system(),
    }


# ---------------- ROUTES ----------------
async def home(request):
    return web.Response(
        text=f"✅ {APP_NAME} is running.\nUptime: {uptime()}",
        content_type="text/plain",
    )


async def health(request):
    return web.json_response({
        "status": "ok",
        "uptime": uptime(),
    })


async def ping(request):
    start = time.perf_counter()
    await asyncio.sleep(0)
    latency = round((time.perf_counter() - start) * 1000, 2)
    return web.json_response({"ping_ms": latency})


async def stats(request):
    data = {
        "app": APP_NAME,
        "uptime": uptime(),
        "system": system_stats(),
    }

    if BOT:
        data["discord"] = {
            "guilds": len(BOT.guilds),
            "users": sum(g.member_count or 0 for g in BOT.guilds),
            "latency_ms": round(BOT.latency * 1000, 2),
        }

    return web.json_response(data)


# ---------------- SERVER ----------------
async def start_webserver():
    app = web.Application()
    app.add_routes([
        web.get("/", home),
        web.get("/health", health),
        web.get("/ping", ping),
        web.get("/stats", stats),
    ])

    runner = web.AppRunner(app)
    await runner.setup()

    port = int(os.environ.get("PORT", 10000))
    site = web.TCPSite(runner, "0.0.0.0", port)
    await site.start()

    logging.info(f"Server running on 0.0.0.0:{port}")

    # Keep alive forever
    while True:
        await asyncio.sleep(3600)
