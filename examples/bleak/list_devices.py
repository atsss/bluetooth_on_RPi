import asyncio
import os
from bleak import BleakScanner

async def list_devices():
    devices = await BleakScanner.discover()

    if devices:
        for device in devices:
            print(f'{device.name} found')
    else:
        print("Device not found.")

async def main():
    await list_devices()

if __name__ == "__main__":
    asyncio.run(main())
