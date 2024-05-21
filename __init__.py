import threading
import asyncio

loop = asyncio.new_event_loop()
flag = threading.Semaphore(0)


def main(loop, flag):
    asyncio.set_event_loop(loop)
    flag.release()
    loop.run_forever()


t = threading.Thread(target=main, args=(loop, flag))
t.setDaemon(True)
t.start()
flag.acquire()  # 确保loop初始化
