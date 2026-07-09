#!/usr/bin/env python3
"""
A WebSocket server that unicasts responses to the sending client
"""
import asyncio
from websockets.asyncio.server import serve

connected_clients = set()


async def connection_handler(websocket):
    """Tracks connected clients and replies only to the message sender"""
    connected_clients.add(websocket)
    try:
        async for message in websocket:
            await websocket.send(f"U:{message}")
    finally:
        connected_clients.remove(websocket)


async def main():
    """Starts the unicast WebSocket server on localhost:8765"""
    async with serve(connection_handler, "localhost", 8765):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
