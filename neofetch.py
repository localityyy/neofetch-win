#do not look at src :sob:
#this code is so dirty
#i didnt do cleanup


import psutil, platform, ctypes, time, subprocess, os
from colorama import Back, init

init()

windows_10 = [
    "                                ..,",
    "                    ....,,:;+ccllll",
    "      ...,,+:;  cllllllllllllllllll",
    ",cclllllllllll  lllllllllllllllllll",
    "llllllllllllll  lllllllllllllllllll",
    "llllllllllllll  lllllllllllllllllll",
    "llllllllllllll  lllllllllllllllllll",
    "llllllllllllll  lllllllllllllllllll",
    "llllllllllllll  lllllllllllllllllll",
    "                                   ",
    "llllllllllllll  lllllllllllllllllll",
    "llllllllllllll  lllllllllllllllllll",
    "llllllllllllll  lllllllllllllllllll",
    "llllllllllllll  lllllllllllllllllll",
    "llllllllllllll  lllllllllllllllllll",
    "llllllllllllll  lllllllllllllllllll",
    "`'ccllllllllll  lllllllllllllllllll",
    "       `' \\*::  :ccllllllllllllllll",
    "                       ````''*::cll",
    "                                 ``"
]

windows_11 = [
    "████████████████  ████████████████",
    "████████████████  ████████████████",
    "████████████████  ████████████████",
    "████████████████  ████████████████",
    "████████████████  ████████████████",
    "████████████████  ████████████████",
    "████████████████  ████████████████",
    "                                  ",
    "████████████████  ████████████████",
    "████████████████  ████████████████",
    "████████████████  ████████████████",
    "████████████████  ████████████████",
    "████████████████  ████████████████",
    "████████████████  ████████████████",
    "████████████████  ████████████████"
]

theme_name = ctypes.create_unicode_buffer(260)
color_name = ctypes.create_unicode_buffer(260)
size = ctypes.c_int(0)
result = ctypes.windll.uxtheme.GetCurrentThemeName(
    theme_name,
    ctypes.sizeof(theme_name) // 2,
    color_name,
    ctypes.sizeof(color_name) // 2,
    ctypes.byref(size)
)
if result == 0:
    themename = "Err"
else:
    themename = theme_name.value
d = int(time.time() - psutil.boot_time()) // (24 * 3600)
h = (int(time.time() - psutil.boot_time()) % (24 * 3600)) // 3600
m = (int(time.time() - psutil.boot_time()) % 3600) // 60
uptime = ""
if d > 0:
    uptime = f"{d} day{'s' if d > 1 else ''}"
elif h > 0:
    uptime = f"{h} hour{'s' if h > 1 else ''}"
elif m > 0:
    uptime = f"{m} min{'s' if m > 1 else ''}"
else:
    uptime = "less than a minute"
neofetch = [
f"{os.getlogin()}@{platform.node()}",
"-"*len(f"{os.getlogin()}@{platform.node()}"),
f"\033[38;2;51;143;117mOS\033[0m: {platform.system()} {platform.release()}",
f"\033[38;2;51;143;117mHost\033[0m: {subprocess.check_output("wmic csproduct get name").decode().split('\n')[1].strip()}",
f"\033[38;2;51;143;117mKernel\033[0m: {platform.win32_ver()[1]}",
f"\033[38;2;51;143;117mUptime\033[0m: {uptime}",
f"\033[38;2;51;143;117mPackages\033[0m: {len(psutil.pids())}",
f"\033[38;2;51;143;117mShell\033[0m: {platform.python_build()[0]}",
f"\033[38;2;51;143;117mResolution\033[0m: {ctypes.windll.user32.GetSystemMetrics(0)}x{ctypes.windll.user32.GetSystemMetrics(1)}",
f"\033[38;2;51;143;117mDE\033[0m: Explorer",
f"\033[38;2;51;143;117mWM\033[0m: {platform.platform()}",
f"\033[38;2;51;143;117mTheme\033[0m: {theme_name.value.split('\\')[-1].replace('.msstyles','')}",
f"\033[38;2;51;143;117mIcons\033[0m: Default",
f"\033[38;2;51;143;117mTerminal\033[0m: Command Prompt",
f"\033[38;2;51;143;117mCPU\033[0m: {subprocess.check_output("wmic cpu get name", shell=True).decode().strip().split('\n')[1].strip()} ({psutil.cpu_count(logical=False)}) @ {psutil.cpu_freq().current:.1f}GHz",
f"\033[38;2;51;143;117mGPU\033[0m: {platform.processor()}",
f"\033[38;2;51;143;117mGPU\033[0m: {subprocess.check_output("wmic path win32_videocontroller get name", shell=True).decode().strip().split('\n')[1].strip()}",
f"\033[38;2;51;143;117mMemory\033[0m: {psutil.virtual_memory().used // (1024 * 1024)}MiB / {psutil.virtual_memory().total // (1024 * 1024)}MiB",
f"""{Back.BLACK}   [48;2;237;21;21m   [0m[48;2;16;209;22m   [48;2;246;115;0m   [0m[48;2;29;152;243m   [0m\033[48;2;154;88;182m   \033[0m\033[48;2;26;187;156m   \033[0m[48;2;252;252;252m   [0m{Back.RESET}""",
f"""\033[48;2;127;140;141m   \033[0m\033[48;2;191;57;43m   \033[0m[48;2;28;219;154m   [0m[48;2;253;188;75m   [0m[48;2;61;173;233m   [0m[48;2;141;67;173m   [0m[48;2;21;159;133m   [0m[48;2;252;252;252m   [0m"""
]
neofetchmod = ""
def do(ver, neofetch, neofetchmod):
    neofetchmod += f"\n\033[38;2;51;143;117m"
    for art_line, neofetch_line in zip(ver, neofetch):
        neofetchmod += f"\033[38;2;51;143;117m{art_line}\033[0m  \033[38;2;51;143;117m{neofetch_line}\033[0m\n"
    print(neofetchmod)
if platform.system() == "Windows":
    if platform.win32_ver()[0] == "10":
        do(windows_10, neofetch, neofetchmod)
    elif platform.win32_ver()[0] == "11":
        do(windows_11, neofetch, neofetchmod)
