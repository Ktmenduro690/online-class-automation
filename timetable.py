import timetable
import time
import title
import description

from main import checkclass

timetable.every().hour.at(":01").do(checkClass)

x = []
x.append([])
x[0].append([])
x.append(title).append(time).append(description)

print(*x , sep = "\n")
