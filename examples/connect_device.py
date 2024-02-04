import argparse
import asyncio
import os
from bleak import BleakScanner, BleakClient

async def connect_to_device(device_name):
    devices = await BleakScanner.discover()
    target_device = next((device for device in devices if device.name == device_name), None)

    if target_device:
        async with BleakClient(target_device.address) as client:
            print(f"Start connecting with device '{device_name}'.")
            await client.connect()
            print(f"Successed connecting with device '{device_name}'.")

            # ここにBluetoothデバイスへの操作を記述
            await asyncio.sleep(15)

            print(f"Start disconnecting with device '{device_name}'.")
            await client.disconnect()
            print(f"Successed disconnecting with device '{device_name}'.")
        print(f"Finish connecting with device '{device_name}'.")
    else:
        print(f"Device '{device_name}' not found.")

async def main(device_name):
    await connect_to_device(device_name)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
      formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument(
      '--deviceName',
      help='Name of Bluetooth device',
      required=True,
     )
    args = parser.parse_args()

    asyncio.run(main(args.deviceName))
