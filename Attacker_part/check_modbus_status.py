# A simple tool to check if a Modbus PLC is responsive.

from pymodbus.client import ModbusTcpClient
import sys

# --- CONFIGURATION ---


PLC_IP = "your Lubuntu VM's IP address"
PLC_PORT = 502 

print(f"--- Checking status of Modbus device at {PLC_IP}:{PLC_PORT} ---")

# Create the client with a short timeout.
# If the device is under a DoS attack, we don't want to wait forever.
client = ModbusTcpClient(PLC_IP, port=PLC_PORT, timeout=3)

try:
    # Try to connect
    is_open = client.connect()

    if is_open:
        print("[*] Connection successful. Attempting to read data...")
        # Try to read one register
        response = client.read_holding_registers(address=0, count=1)

        if not response.isError():
            value = response.registers[0]
            print(f"\n[+] SUCCESS: Device is ONLINE and responsive. Read value: {value}")
        else:
            # This can happen if the device is busy but not completely down.
            print(f"\n[-] WARNING: Device connected but failed to respond to read request. Error: {response}")
    else:
        print("\n[-] FAILURE: Could not connect to the device. It may be offline or under attack.")

except Exception as e:
    print(f"\n[-] CRITICAL FAILURE: An exception occurred. The device is unresponsive. Error: {e}")

finally:
    client.close()
    print("--- Status check complete ---")