#!/usr/bin/env python3
"""
A minimal WebSocket echo server
"""
import asyncio
from websockets.asyncio.server import serve


async def connection_handler(websocket):
    """Sends back every text message received on the connection"""
    async for message in websocket:
        await websocket.send(message)


async def main():
    """Starts the WebSocket server on localhost:8765"""
    async with serve(connection_handler, "localhost", 8765):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
