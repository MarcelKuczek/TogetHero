import main
import asyncio

async def client_things():
    await main.port_scan()

if __name__ == '__main__':
    asyncio.run(client_things())