from keyword_listener import wait_for_keyword
from clap_detector import detect_claps
from launcher import launch_actions
from config_loader import load_config

config = load_config()

keyword = config["keyword"]
actions_map = config["actions"]

print("System ready. Say the keyword...")

if wait_for_keyword(keyword):
    print("Keyword detected. Clap now!")

    claps = detect_claps()
    print("Claps detected:", claps)

    action = actions_map.get(str(claps))
    if action:
        launch_actions(action)
    else:
        print("No action configured for", claps, "claps")
