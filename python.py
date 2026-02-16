
import requests
import sys
from colorama import Fore, Style, init

init(autoreset=True)  # auto reset color


# ---------- UI COLORS ----------
SUCCESS = Fore.GREEN
ERROR = Fore.RED
INFO = Fore.CYAN
WARNING = Fore.YELLOW
TITLE = Fore.MAGENTA
INPUT = Fore.CYAN


# ---------- HEADER ----------
print(TITLE + """
      
░█████████  ░██                                                                                  ░██                                                     ░██ ░██       ░██               ░██                        
░██     ░██ ░██                                                                                  ░██                                                     ░██           ░██               ░██                        
░██     ░██ ░████████   ░███████  ░████████   ░███████     ░████████  ░██    ░██ ░█████████████  ░████████   ░███████  ░██░████    ░██    ░██  ░██████   ░██ ░██ ░████████  ░██████   ░████████  ░███████  ░██░████ 
░█████████  ░██    ░██ ░██    ░██ ░██    ░██ ░██    ░██    ░██    ░██ ░██    ░██ ░██   ░██   ░██ ░██    ░██ ░██    ░██ ░███        ░██    ░██       ░██  ░██ ░██░██    ░██       ░██     ░██    ░██    ░██ ░███     
░██         ░██    ░██ ░██    ░██ ░██    ░██ ░█████████    ░██    ░██ ░██    ░██ ░██   ░██   ░██ ░██    ░██ ░█████████ ░██          ░██  ░██   ░███████  ░██ ░██░██    ░██  ░███████     ░██    ░██    ░██ ░██      
░██         ░██    ░██ ░██    ░██ ░██    ░██ ░██           ░██    ░██ ░██   ░███ ░██   ░██   ░██ ░███   ░██ ░██        ░██           ░██░██   ░██   ░██  ░██ ░██░██   ░███ ░██   ░██     ░██    ░██    ░██ ░██      
░██         ░██    ░██  ░███████  ░██    ░██  ░███████     ░██    ░██  ░█████░██ ░██   ░██   ░██ ░██░█████   ░███████  ░██            ░███     ░█████░██ ░██ ░██ ░█████░██  ░█████░██     ░████  ░███████  ░██                                                                                                                                                                                                  
""")

print(INFO + "Made by: kush pandit")
print(INFO + "Github: https://github.com/kushdeveloper68/")
print("=" * 80)


# ---------- MAIN FUNCTION ----------
def verify_number(number, api_key):

    # Input validation
    if not api_key.strip():
        print(ERROR + "❌ API key cannot be empty")
        return

    if not number.isdigit():
        print(ERROR + "❌ Phone must contain only numbers")
        return

    url = f"https://api.veriphone.io/v2/verify?phone={number}&key={api_key}"

    try:
        print(INFO + "🔍 Fetching data from server...")

        response = requests.get(url, timeout=10)
        data = response.json()

    except requests.exceptions.ConnectionError:
        print(ERROR + "❌ Internet or API server unreachable")
        return

    except requests.exceptions.Timeout:
        print(ERROR + "❌ Request timeout — server slow")
        return

    except requests.exceptions.RequestException as e:
        print(ERROR + f"❌ Unexpected error: {e}")
        return

    except ValueError:
        print(ERROR + "❌ Invalid response from server")
        return

    # ---------- API RESPONSE HANDLING ----------
    if data.get("code") == 401:
        print(ERROR + "❌ Invalid or inactive API key")
        return

    elif data.get("code") == 400:
        print(ERROR + "❌ Invalid phone number format")
        return

    elif data.get("code") == 500:
        print(ERROR + "❌ Server error — try later")
        return

    elif data.get("phone_valid") is False:
        print(ERROR + "❌ Phone number is not valid")
        return

    # ---------- SUCCESS OUTPUT ----------
    print(SUCCESS + "\n✅ PHONE DETAILS\n")
    for key, value in data.items():
        print(f"{SUCCESS}{key}: {Style.RESET_ALL}{value}")


# ---------- MENU ----------
print(TITLE + "=" * 35 + " COMMANDS " + "=" * 35)
print(INFO + """
1. Validate phone number
2. Help
3. Exit
""")


# ---------- SAFE INPUT ----------
try:
    command = int(input(INPUT + "Enter command (1,2,3): "))
except ValueError:
    print(ERROR + "❌ Enter a valid number")
    sys.exit()


# ---------- COMMAND HANDLER ----------
match command:

    case 1:
        print(TITLE + "=" * 30 + " ENTER CREDENTIALS " + "=" * 30)

        api_key = input(INPUT + "Enter API key: ")
        number = input(INPUT + "Enter phone number: ")

        verify_number(number, api_key)

    case 2:
        print(TITLE + "=" * 35 + " HELP " + "=" * 35)
        print(INFO + """
• Choose option 1 to validate phone number
• Enter your Veriphone API key
• Enter phone without spaces or symbols
Example: +9198765432**
""")

    case 3:
        print(SUCCESS + "Thanks for using the tool")

    case _:
        print(ERROR + "❌ Invalid command")
