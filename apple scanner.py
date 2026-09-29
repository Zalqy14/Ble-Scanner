import asyncio
from bleak import BleakScanner

# DataBase of Apple device types
APPLE_DEVICE_TYPES = {
    0x07: "AirPods/Beats",
    0x0c: "Apple Continuity (Handoff/Mac/iPhone)",
    0x10: "Nearby Action (AirDrop/Wifi Setup)",
    0x12: "FindMy Network (AirTag/Offline Apple Device)",
}

def appple_validation_scan(device , adv):
    apple_data = adv.manufacturer_data.get(76)
    if apple_data:
        # First position is the type
        type_indicator = apple_data[0]

        device_type = APPLE_DEVICE_TYPES.get(type_indicator, f"Unknown Apple Type")

        print(f"Apple Device Detected: {device_type}")
        print(f"    MAC: {device.address}\n")
async def scan():
    print("Scanning...")
    scanner = BleakScanner(appple_validation_scan)
    async with scanner:
        await asyncio.sleep(10)

if __name__ == "__main__":
    asyncio.run(scan())