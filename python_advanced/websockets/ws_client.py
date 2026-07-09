#!/usr/bin/env python3
"""
A minimal WebSocket client
"""
import asyncio
import os
from websockets.asyncio.client import connect


async def connect_and_send(uri: str, text: str) -> str:
    """Opens a connection, sends one message, and returns the response"""
    async with connect(uri) as websocket:
        await websocket.send(text)
        return await websocket.recv()


async def main():
    """Sends 'demo' to the target server and prints its response"""
    uri = os.environ.get("WS_URI", "ws://localhost:8765")
    response = await connect_and_send(uri, "demo")
    print(response, end="")


if __name__ == "__main__":
    asyncio.run(main())
