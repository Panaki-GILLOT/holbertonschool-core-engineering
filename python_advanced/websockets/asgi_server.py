#!/usr/bin/env python3
"""
An ASGI application serving a browser chat client and a WebSocket echo endpoint
"""
import os

from starlette.applications import Starlette
from starlette.responses import FileResponse
from starlette.routing import Route, WebSocketRoute

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


async def homepage(request):
    """Serves the browser chat client page"""
    return FileResponse(os.path.join(BASE_DIR, "index.html"))


async def chat_js(request):
    """Serves the browser chat client script"""
    return FileResponse(
        os.path.join(BASE_DIR, "chat.js"), media_type="application/javascript"
    )


async def styles_css(request):
    """Serves the browser chat client stylesheet"""
    return FileResponse(os.path.join(BASE_DIR, "styles.css"), media_type="text/css")


async def websocket_endpoint(websocket):
    """Echoes back every text message received on the connection"""
    await websocket.accept()
    async for message in websocket.iter_text():
        await websocket.send_text(message)


app = Starlette(routes=[
    Route("/", homepage),
    Route("/chat.js", chat_js),
    Route("/styles.css", styles_css),
    WebSocketRoute("/ws", websocket_endpoint),
])
