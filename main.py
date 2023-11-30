print("face mask check")

from Task1 import task1
from Task2 import task2
from Task3 import task3
import Scheduler
from Task1 import a

import cv2
import time

sche = Scheduler.Scheduler()

sche.SCH_Add_Task(task1,400,200)
while a == "Without face mask":
    if a == "With face mask":
        sche.SCH_Add_Task(task2, 400, 200)
        sche.SCH_Add_Task(task3, 400, 200)
    elif a == "Without face mask":
        sche.SCH_Add_Task(task2, 400, 200)
        sche.SCH_Add_Task(task3, 400, 200)