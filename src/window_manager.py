import win32gui
import win32api
import win32con
import time


def tile_windows_grid(window_keywords, timeout=10):
    screen_w = win32api.GetSystemMetrics(0)
    screen_h = win32api.GetSystemMetrics(1)

    half_w = screen_w // 2
    half_h = screen_h // 2

    start = time.time()
    matched = []

    def find_windows():
        found = []

        def handler(hwnd, _):
            if not win32gui.IsWindowVisible(hwnd):
                return

            title = win32gui.GetWindowText(hwnd)
            if not title:
                return

            for key in window_keywords:
                if key.lower() in title.lower():
                    found.append(hwnd)
                    break

        win32gui.EnumWindows(handler, None)
        return found

    # 🔑 WAIT until all windows appear (WhatsApp is slow)
    while time.time() - start < timeout:
        matched = find_windows()
        if len(matched) >= len(window_keywords):
            break
        time.sleep(0.5)

    if len(matched) < len(window_keywords):
        print(f"⚠️ Only found {len(matched)} of {len(window_keywords)} windows")

    positions = [
        (0, 0),                    # top-left
        (half_w, 0),               # top-right
        (0, half_h),               # bottom-left
        (half_w, half_h)           # bottom-right
    ]

    for hwnd, (x, y) in zip(matched, positions):
        # 🔑 FORCE WhatsApp out of maximized/hidden state
        win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)

        win32gui.SetWindowPos(
            hwnd,
            win32con.HWND_TOP,
            x, y,
            half_w, half_h,
            win32con.SWP_SHOWWINDOW | win32con.SWP_NOZORDER
        )
