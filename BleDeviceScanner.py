import asyncio,requests
from bleak import BleakScanner

# Scan For BLE devices
async def scan():
    print("Scanning...")
    devices = await BleakScanner.discover(timeout=10,return_adv=True)
    # Print the BLE devices detected
    for address,(device,adv) in devices.items():
        print(f"Device: {device}, Advertisement: {adv}")
        # We Scan the Mac address
        print(f"Device Name after scan: {mac_scan(address)}")
        await asyncio.sleep (1)
    return devices

def mac_scan(mac):
    url = f"https://api.macvendors.com/{mac}"
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        return response.text
    return "Mac address not found"


if __name__ == "__main__":
    asyncio.run(scan())