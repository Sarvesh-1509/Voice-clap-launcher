import subprocess
import time

def launch_actions(actions):
    processes = []

    for action in actions:
        if action.startswith("chrome"):
            # Always force a NEW Chrome window
            proc = subprocess.Popen(
                f'start "" {action}',
                shell=True
            )
        else:
            proc = subprocess.Popen(action, shell=True)

        processes.append(proc)

    # Give windows time to appear
    time.sleep(3)

    return processes
