import websockets
import asyncio
import socket
import traceback

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.connect(('8.8.8.8', 53))
    My_IP = s.getsockname()[0]

async def port_scan():
    if not My_IP[:3] == '192' and  not My_IP[:3] == '10.' and not  My_IP[:3] == '172':
        print('This is not a private network: Shutting Down !')
        exit()

    ip_range = My_IP.split('.')
    ip_range.pop()
    ip_range = '.'.join(ip_range)

    i = 0
    while i < 255:
        i += 1
        target_ip = f"{ip_range}.{i}"
        uri= f"ws://{target_ip}:1111"
        try:
            connection = await asyncio.wait_for(websockets.connect(uri), timeout = 3)
            await connection.send("hello")
        except ConnectionRefusedError:
            print("Server connection refuse")
            pass
        except ConnectionError:
            pass
        except TimeoutError:
            pass
        except:
            traceback.print_exc()

async def register_client(websocket, _):
    async for message in websocket:
        print(message)

async def main():
    async with websockets.serve(register_client, 'localhost', 2222):
        await asyncio.Future()

if __name__ == '__main__':
    asyncio.run(main())

