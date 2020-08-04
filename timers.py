from collections import deque
from datetime import datetime
from math import ceil
from uuid import uuid4

timers = {}


def __total__(timer) -> tuple:
    title = timer.popleft()
    total = 0.0
    while len(timer):
        total += timer.pop() - timer.pop()
    return title, ceil(total)


def start_timer(title: str) -> uuid4:
    uid = str(uuid4())
    timers[uid] = deque([title, datetime.now().timestamp()])
    return uid


def stop_timer(uid: uuid4) -> tuple:
    timer = timers[uid]
    del timers[uid]
    timer.append(datetime.now().timestamp())
    return __total__(timer)


def pause_timer(uid: uuid4) -> bool:
    if not len(timers[uid]) % 2:
        timers[uid].append(datetime.now().timestamp())
        return True
    return False


def resume_timer(uid: uuid4) -> bool:
    if len(timers[uid]) % 2:
        timers[uid].append(datetime.now().timestamp())
        return True
    return False


def get_time(uid: uuid4) -> bool:
    return __total__(timers[uid])[-1]
