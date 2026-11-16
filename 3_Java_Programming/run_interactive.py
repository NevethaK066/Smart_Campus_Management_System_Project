import os
import subprocess
import sys

# Determine workspace paths
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

jdk_paths = [
    r"C:\Program Files\Java\jdk-26.0.2\bin\java.exe",
    r"C:\Program Files\Java\jdk-17\bin\java.exe",
    r"C:\Program Files\Java\latest\bin\java.exe"
]
java_exe = "java"
for p in jdk_paths:
    if os.path.exists(p):
        java_exe = p
        break

java_cmd = [
    java_exe,
    "--enable-native-access=ALL-UNNAMED",
    "-cp",
    "bin;lib/*",
    "com.vcet.events.Main"
]

try:
    subprocess.run(java_cmd)
except KeyboardInterrupt:
    print("\nSession exited.")
