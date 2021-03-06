import asyncio
from aiohttp import web
import aiohttp_jinja2
import jinja2
import pathlib
import re
import os


BASE_DIR = pathlib.Path(__file__).parent.absolute()
print(BASE_DIR)
TEMPLATE_PATH = str(BASE_DIR / "templates")


@aiohttp_jinja2.template("index.html")
async def handle(request):
    return {}


def init_func(argv=None, runner=False):
    app = web.Application()

    aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader(TEMPLATE_PATH))
    app.add_routes([web.get("/", handle)])

    if runner:
        return web.AppRunner(app)
    else:
        return app


def start_server():
    # web.run_app(init_func(), host="127.0.0.1", port=int(os.environ.get("PORT", "8080")))
    web.run_app(init_func())


def run_server():
    runner = init_func(runner=True)
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(runner.setup())
    site = web.TCPSite(runner, "0.0.0.0", 8080)
    loop.run_until_complete(site.start())
    loop.run_forever()
