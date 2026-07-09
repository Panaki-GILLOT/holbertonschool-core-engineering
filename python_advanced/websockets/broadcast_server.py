#!/usr/bin/env python3
"""
A WebSocket server that broadcasts messages to all connected clients
"""
import asyncio
from websockets.asyncio.server import serve
from websockets.exceptions import ConnectionClosed

connected_clients = set()


async def broadcast(message):
    """Sends the message to every currently connected client"""
    for client in list(connected_clients):
        try:
            await client.send(message)
        except ConnectionClosed:
            pass


async def connection_handler(websocket):
    """Tracks connected clients and broadcasts each received message"""
    connected_clients.add(websocket)
    try:
        async for message in websocket:
            await broadcast(f"B:{message}")
    finally:
        connected_clients.discard(websocket)


async def main():
    """Starts the broadcast WebSocket server on localhost:8765"""
    async with serve(connection_handler, "localhost", 8765):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
