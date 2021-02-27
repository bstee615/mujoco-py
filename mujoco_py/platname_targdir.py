import sys
if sys.platform.startswith("darwin"):
    platname = "osx"
elif sys.platform.startswith("linux"):
    platname = "linux"
elif sys.platform.startswith("windows") or sys.platform.startswith("win32"):
    platname = "win"
targdir = "mujoco_%s"%platname

