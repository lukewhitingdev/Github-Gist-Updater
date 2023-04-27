import os
from shutil import rmtree
import subprocess

BUILD_PATH = "./build"
TEMP_PATH = "./temp"
SPEC_PATH = os.path.join(TEMP_PATH, "spec")

command = f"pyinstaller -F ..\src\gist_updater.py --distpath {BUILD_PATH} --workpath {TEMP_PATH} --specpath {SPEC_PATH} --noconfirm --clean --name Github-Gist-Updater"
proc = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT);

stdout = proc.communicate()[0].decode()

if(proc.returncode != 0):
    print("Something went wrong when generating build. See output below: \n")
    stdout_lines = stdout.split("\n");
    for line in stdout_lines:
        print(line)

    exit(1);

print("Generated executable.")

print("Cleaning up.")

rmtree(TEMP_PATH)

print("Finished.")