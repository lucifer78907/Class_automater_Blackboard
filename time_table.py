from dotenv import load_dotenv
import os

load_dotenv()
# LINKS TO THE CLASSES
CN = f"{os.getenv('CN')}"
CN_LAB = f"{os.getenv('CN_LAB')}"
DSA_ANA = f"{os.getenv('DSA_ANA')}"
LS = f"{os.getenv('LS')}"
MI = f"{os.getenv('MI')}"
MI_LAB = f"{os.getenv('MI_LAB')}"
AI = f"{os.getenv('AI')}"
MATHS = f"{os.getenv('MATHS')}"
PYTHON = f"{os.getenv('PYTHON')}"
PROJECT = f"{os.getenv('PROJECT')}"
SS = f"{os.getenv('SS')}"
SOFT_ENG = f"{os.getenv('SOFT_ENG')}"
SOFT_ENG_LAB = f"{os.getenv('SOFT_ENG_LAB')}"

class_start_times = {
    "start1": (9, 40), "start2": (10, 30), "start3": (11, 20), "start4": (12, 10), "start5": (1, 00),
    "start6": (1, 50), "start7": (2, 40), "start8": (3, 30)
}

time_table = {
    "Monday": {
        "class1": (MI,*class_start_times["start1"]),
        "class2": (AI, *class_start_times["start2"]),
        "class3": (MATHS, *class_start_times["start3"]),
        "class4": (SOFT_ENG, *class_start_times["start4"]),
        "class5": (SOFT_ENG_LAB, *class_start_times["start6"]),
        "class6": (SOFT_ENG_LAB, *class_start_times["start7"])
    },
    "Tuesday": {
        "class1": (DSA_ANA, *class_start_times["start1"]),
        "class2": (CN, *class_start_times["start2"]),
        "class3": (MI, *class_start_times["start3"]),
        "class4": (LS, *class_start_times["start4"]),
        "class5": (MI_LAB, *class_start_times["start6"]),
        "class6": (MI_LAB, *class_start_times["start7"])
    }
}
