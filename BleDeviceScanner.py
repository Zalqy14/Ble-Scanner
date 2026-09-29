import asyncio
import aiohttp
from bleak import BleakScanner

# Scan For BLE devices
async def scan():
    print("Scanning...")
    devices = await BleakScanner.discover(timeout=10,return_adv=True)
    # Print the BLE devices detected
    async with aiohttp.ClientSession() as session:
        for address,(device,adv) in devices.items():
            print(f"Device: {device}, manufacturer: {adv.manufacturer_data}")
            # We Scan the Mac address
            vendor = await mac_scan(session,address)
            print(f"Device Name after scan: {vendor}")
            await asyncio.sleep (2)
        return devices

async def mac_scan(session,mac):
    url = f"https://api.macvendors.com/{mac}"
    # We use the shared session to make an async GET request
    async with session.get(url) as response:
        if response.status == 200:
            return await response.text()
        return "Mac address not found"


if __name__ == "__main__":
    asyncio.run(scan())