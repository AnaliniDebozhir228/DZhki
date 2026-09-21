import os
import sys
import platform
from datetime import datetime

folder = os.getcwd()
python_version = sys.version
system_info = platform.system()
computer_name = platform.node()

now = datetime.now()

print("Операционные системы и среды")
print()
print("Текущая папка:")
print(folder)
print()
print("Операционная система:")
print(system_info)
print()
print("Имя компьютера:")
print(computer_name)
print()
print("Версия Python:")
print(python_version.split()[0])
print()
print("Текущая дата и время:")
print(now)
