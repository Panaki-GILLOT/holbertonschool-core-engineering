#!/usr/bin/env python3
"""
A WebSocket server that validates incoming messages
"""
import asyncio
from websockets.asyncio.server import serve
from websockets.exceptions import ConnectionClosed


async def connection_handler(websocket):
    """Rejects empty messages and echoes back valid ones with an OK: prefix"""
    try:
        async for message in websocket:
            if len(message.strip()) == 0:
                await websocket.send("ERR:EMPTY")
            else:
                await websocket.send(f"OK:{message}")
    except ConnectionClosed:
        pass


async def main():
    """Starts the validation WebSocket server on localhost:8765"""
    async with serve(connection_handler, "localhost", 8765):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
