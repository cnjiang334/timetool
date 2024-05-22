import asyncio
from timetool import loop


class signal:
    def __init__(self):
        self.__num = id(self)

    def __str__(self):
        return str(self.__num)

    def clear(self):
        self.__num = -1

    def getnum(self):
        return self.__num


def clearTimeOut(s: signal):
    s.clear()


def setTimeOut(func, sec: float, *args, **kwargs) -> signal:
    s = signal()
    asyncio.run_coroutine_threadsafe(__timeOut(s, sec, func, *args, **kwargs), loop)
    return s


def setInterval(func, sec: float, *args, **kwargs) -> signal:
    s = signal()
    asyncio.run_coroutine_threadsafe(__interval(s, sec, func, *args, **kwargs), loop)
    return s


async def __timeOut(sign: signal, sec, func, *args, **kwargs):
    await asyncio.sleep(sec)
    if sign.getnum() != -1:
        func(*args, **kwargs)


async def __interval(sign: signal, sec, func, *args, **kwargs):
    while True:
        await asyncio.sleep(sec)
        if sign.getnum() != -1:
            func(*args, **kwargs)
        else:
            break
