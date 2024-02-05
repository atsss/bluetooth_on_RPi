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

async def connect_to_device(device_name):
    devices = await bleak.discover()
    target_device = next((device for device in devices if device.name == device_name), None)

    if target_device:
        async with bleak.BleakClient(target_device.address) as client:
            await client.connect()

            # ここにBluetoothデバイスへの操作を記述

            await client.disconnect()
    else:
        print(f"Device '{device_name}' not found.")

# async def play_mp3(file_path):
#     pygame.mixer.init()
#     pygame.mixer.music.load(file_path)
#     pygame.mixer.music.play()
#
#     while pygame.mixer.music.get_busy():
#         pygame.time.Clock().tick(10)

async def main(device_name, mp3_file_path):
    await list_devices()
    # await connect_to_device(device_name)
    # await play_mp3(mp3_file_path)

if __name__ == "__main__":
    # Bluetoothデバイスの名前
    bluetooth_device_name = "YourBluetoothDeviceName"

    # 再生するMP3ファイルのパス
    mp3_file_path = "path/to/your/file.mp3"

    asyncio.run(main(bluetooth_device_name, mp3_file_path))
