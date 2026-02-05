import time

from keyword_listener import wait_for_keyword
from clap_detector import detect_claps
from launcher import launch_actions
from window_manager import tile_windows_grid
from config_loader import load_config


def main():
    config = load_config()

    keyword = config.get("keyword", "jarvis")
    actions_map = config.get("actions", {})
    layout = config.get("layout", "grid")

    print("🧠 Voice–Clap Launcher running")
    print(f"🎙️ Say the keyword: {keyword}")

    while True:
        # 1️⃣ Wait for keyword
        if not wait_for_keyword(keyword):
            continue

        print("✅ Keyword detected")
        print("👏 Listening for claps...")

        # 2️⃣ Detect claps
        clap_count = detect_claps()
        print(f"👏 Detected {clap_count} claps")

        # 3️⃣ Get actions
        actions = actions_map.get(str(clap_count))
        if not actions:
            print("⚠️ No action mapped for this clap count\n")
            time.sleep(1)
            continue

        # 4️⃣ Launch apps / URLs
        print("🚀 Launching applications...")
        launch_actions(actions)

        # Small delay so windows actually appear
        time.sleep(1)

        # 5️⃣ Apply layouts
        if layout == "grid" and clap_count == 3:
            tile_windows_grid([
                "YouTube Music",
                "ChatGPT",
                "WhatsApp",
                "SSN"
            ])

        elif layout == "grid" and clap_count == 4:
            tile_windows_grid([
                "Visual Studio Code",
                "Notepad",
                "Chrome",
                "PowerShell"
            ])

        print("✅ Done. Waiting again...\n")
        time.sleep(2)


if __name__ == "__main__":
    main()
