# main.py

import os
import asyncio
from datetime import date
from dotenv import load_dotenv

from colorama import Fore, Style, init

from droidrun import DroidAgent, AgentConfig
from droidrun.config_manager import DroidrunConfig
from llama_index.llms.openai_like import OpenAILike

from prompt import phonepe_goal, googlepay_goal, paytm_goal

load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))

# ---------------- INIT COLORAMA ----------------
init(autoreset=True)

# ---------------- CONSTANTS ----------------
DEVICE_PIN = "5 4 8 9"
CSV_FILENAME = "all_upi_transactions.csv"


# ---------------- UI HELPERS ----------------

def print_banner():
    banner = f"""
{Fore.CYAN}{Style.BRIGHT}
 ███████╗██╗███╗   ██╗██████╗ ██████╗  ██████╗ ██╗██████╗ 
 ██╔════╝██║████╗  ██║██╔══██╗██╔══██╗██╔═══██╗██║██╔══██╗
 █████╗  ██║██╔██╗ ██║██║  ██║██████╔╝██║   ██║██║██║  ██║
 ██╔══╝  ██║██║╚██╗██║██║  ██║██╔══██╗██║   ██║██║██║  ██║
 ██║     ██║██║ ╚████║██████╔╝██║  ██║╚██████╔╝██║██████╔╝
 ╚═╝     ╚═╝╚═╝  ╚═══╝╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝╚═════╝
{Style.RESET_ALL}
{Fore.YELLOW}{Style.BRIGHT}      FinDroid – UPI Transaction Extractor{Style.RESET_ALL}
"""
    print(banner)


def print_agent_status(agent_name: str, color=Fore.BLUE):
    print(f"\n{color}{Style.BRIGHT}Running Agent: {agent_name}{Style.RESET_ALL}")
    print(f"{color}{'=' * 50}{Style.RESET_ALL}")


# ---------------- MAIN ----------------

async def main():
    print_banner()

    # -------- USER INPUT (DATE) --------
    user_date = input(
        f"{Fore.CYAN}Enter target date (YYYY-MM-DD) [default: today]: {Style.RESET_ALL}"
    ).strip()

    if not user_date:
        user_date = date.today().isoformat()

    print(f"{Fore.GREEN}Using target date: {user_date}{Style.RESET_ALL}")

    # -------- USER INPUT (APP) --------
    print(
        f"""
{Fore.CYAN}Select app:
  1 → PhonePe
  2 → Google Pay
  3 → Paytm
"""
    )

    app_choice = input(
        f"{Fore.CYAN}Enter choice [1/2/3]: {Style.RESET_ALL}"
    ).strip()

    app_map = {
        "1": "phonepe",
        "2": "gpay",
        "3": "paytm",
    }

    if app_choice not in app_map:
        print(f"{Fore.RED}Invalid choice. Exiting.{Style.RESET_ALL}")
        return

    app = app_map[app_choice]

    # -------- ENV CHECK --------
    api_key = os.environ.get("OPENROUTER_API_KEY")
    if not api_key:
        print(f"{Fore.RED}OPENROUTER_API_KEY not set{Style.RESET_ALL}")
        return

    # -------- PATH --------
    script_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(script_dir, CSV_FILENAME)

    # -------- DROIDRUN CONFIG --------
    config = DroidrunConfig(
        agent=AgentConfig(max_steps=150)
    )

    llm = OpenAILike(
        api_key=os.environ.get("OPENROUTER_API_KEY"),
        api_base="https://openrouter.ai/api/v1",
        model="mistralai/devstral-2512:free"
    )

    # -------- SELECT PROMPT --------
    if app == "phonepe":
        goal = phonepe_goal(csv_path, user_date, DEVICE_PIN)
        agent_name = "PhonePe"
    elif app == "gpay":
        goal = googlepay_goal(csv_path, user_date, DEVICE_PIN)
        agent_name = "Google Pay"
    else:
        goal = paytm_goal(csv_path, user_date, DEVICE_PIN)
        agent_name = "Paytm"

    print_agent_status(agent_name)

    agent = DroidAgent(
        goal=goal,
        llms=llm,
        config=config
    )

    result = await agent.run()

    if not result.success:
        print(f"{Fore.RED}Agent failed: {result.reason}{Style.RESET_ALL}")
        return

    print(f"{Fore.GREEN}Extraction completed successfully{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}CSV updated at:{Style.RESET_ALL}")
    print(csv_path)


if __name__ == "__main__":
    asyncio.run(main())