import subprocess
import webbrowser

def launch_actions(actions):
    for action in actions:
        if action.startswith("http"):
            webbrowser.open(action)
        else:
            subprocess.Popen(action, shell=True)
