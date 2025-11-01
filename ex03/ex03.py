import os
import datetime

COLORS = {
    "info": "\033[94m",
    "debug": "\033[90m",
    "warning": "\033[93m",
    "error": "\033[91m",
    "reset": "\033[0m"
}

def smart_log(*args, **kwargs) -> None:

    level = kwargs.get("level", "info").lower()
    timestamp = kwargs.get("timestamp", True)
    save_to = kwargs.get("save_to", None)
    color = kwargs.get("color", True)

    message = " ".join(str(arg) for arg in args)
    time_str = datetime.datetime.now().strftime("%H:%M:%S") if timestamp else ""
    log_line = f"{time_str} [{level.upper()}] {message}" if time_str else f"[{level.upper()}] {message}"

    if color and level in COLORS:
        print(f"{COLORS[level]}{log_line}{COLORS['reset']}")
    else:
        print(log_line)

    if save_to:
        dir_name = os.path.dirname(save_to)
        if dir_name and not os.path.exists(dir_name):
            os.makedirs(dir_name)
        with open(save_to, "a", encoding="utf-8") as f:
            f.write(log_line + "\n")


if __name__ == "__main__":
    username = "alice"

    smart_log("System started successfully.", level="info")
    smart_log("User", username, "logged in", level="debug", timestamp=True)
    smart_log("Low disk space detected!", level="warning", save_to="logs/system.log")
    smart_log("Model", "training", "failed!", level="error", color=True, save_to="logs/errors.log")
    smart_log("Process end", level="info", color=False, save_to="logs/errors.log")
