import pygetwindow as gw
import win32gui
import win32con
import win32com.client as comclt
import sys

def get_mblock_handle():
    """Search for and return the handle of the MBlock window."""
    mblock_windows = gw.getWindowsWithTitle("mBlock v5.4.3")
    if mblock_windows:
        return mblock_windows[0]._hWnd
    else:
        print("mBlock window not found.")
        return None

def enum_child_windows(hwnd, lParam):
    global child_windows
    child_windows.append(hwnd)
    return True

def get_child_windows(parent_hwnd):
    global child_windows
    child_windows = []
    win32gui.EnumChildWindows(parent_hwnd, enum_child_windows, None)
    return child_windows

def focusToMblock():
    """Focus the MBlock window."""
    hwnd = get_mblock_handle()
    if hwnd is None:
        print("Open mBlock application first")
        sys.exit(0)
    
    if win32gui.GetForegroundWindow() != hwnd:
        win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE)
        win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)

    wsh = comclt.Dispatch("WScript.Shell")
    wsh.AppActivate("mBlock v5.4.3")
