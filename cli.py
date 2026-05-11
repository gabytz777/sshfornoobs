import time
import itertools
import threading
from ssh_client import run_ssh_commands

done = False

def spinner():
    for c in itertools.cycle(["|", "/", "-", "\\"]):
        if done:
            break
        print(f"Loading stats... {c}", end="\r")
        time.sleep(0.1)

def main():
    global done

    print("=== SSH Noob Dashboard (CLI) ===")
    host = input("Host/IP: ")
    username = input("Username: ")
    password = input("Password: ")

    done = False
    t = threading.Thread(target=spinner)
    t.start()

    try:
        stats = run_ssh_commands(host, username, password)
        done = True
        t.join()
        print(" " * 40, end="\r")

        print("\n=== STATS ===")
        for k, v in stats.items():
            print(f"\n[{k.upper()}]\n{v}")

    except Exception as e:
        done = True
        t.join()
        print(" " * 40, end="\r")
        print("\nError:", e)

if __name__ == "__main__":
    main()
