from aiohttp import web
import os
import time
import logging
import threading
import platform

# Optional dependency
try:
    import psutil
except ImportError:
    psutil = None

APP_NAME = "API Discord Bot"
START_TIME = time.time()
PID = os.getpid()

logging.basicConfig(
    level=logging.INFO,
    format="🌐 [WEB] %(asctime)s | %(levelname)s | %(message)s",
)


# ---------------- HELPERS ----------------
def uptime():
    secs = int(time.time() - START_TIME)
    m, s = divmod(secs, 60)
    h, m = divmod(m, 60)
    d, h = divmod(h, 24)
    return f"{d}d {h}h {m}m {s}s"


def memory_usage():
    if not psutil:
        return None
    return round(psutil.Process(PID).memory_info().rss / 1024 / 1024, 2)


# ---------------- ROUTES ----------------
async def home(request):
    return web.Response(
        text=f"✅ {APP_NAME} running\nUptime: {uptime()}",
        content_type="text/plain",
    )


async def health(request):
    return web.json_response({
        "status": "ok",
        "uptime": uptime(),
    })


async def stats(request):
    data = {
        "app": APP_NAME,
        "uptime": uptime(),
        "pid": PID,
        "python": platform.python_version(),
        "platform": platform.system(),
    }

    mem = memory_usage()
    if mem:
        data["memory_mb"] = mem

    return web.json_response(data)


# ---------------- SERVER ----------------
def run_server():
    app = web.Application()
    app.add_routes([
        web.get("/", home),
        web.get("/health", health),
        web.get("/stats", stats),
    ])

    port = int(os.environ.get("PORT", 10000))
    logging.info(f"Web server starting on 0.0.0.0:{port}")

    web.run_app(
        app,
        host="0.0.0.0",
        port=port,
        print=None,     # disable aiohttp banner
        access_log=None # silence noisy logs
    )


def keep_alive():
    t = threading.Thread(target=run_server, daemon=True)
    t.start()
