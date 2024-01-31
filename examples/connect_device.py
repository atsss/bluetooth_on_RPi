import asyncio
import os
from bleak import BleakScanner, BleakClient

async def connect_to_device(device_name):
    devices = await BleakScanner.discover()
    target_device = next((device for device in devices if device.name == device_name), None)

    if target_device:
        print(f"Start connecting with device '{device_name}'.")
        async with BleakClient(target_device.address) as client:
            await client.connect()

            # ここにBluetoothデバイスへの操作を記述
            await asyncio.sleep(5)

            await client.disconnect()
        print(f"Finish connecting with device '{device_name}'.")
    else:
        print(f"Device '{device_name}' not found.")

async def main(device_name):
    await connect_to_device(device_name)

if __name__ == "__main__":
    bluetooth_device_name = "74-45-CE-95-6C-32"

    asyncio.run(main(bluetooth_device_name))
