import time
from aituber import AITuberSystem

import traceback

aitubersystem = AITuberSystem()
while True:
    try:
        aitubersystem.talk_with_comment()
    except Exception as e:
        print(traceback.format_exc())

        exit(200)
    time.sleep(10)
