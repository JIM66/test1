import multiprocessing
import time
from multiprocessing import Process

# def process(num):
#     time.sleep(num)
#     print('processing:', num)
# #
# if __name__ == '__main__':
#     for i in range(8):
#         p = multiprocessing.Process(target=process, args=(i,))
#         p.start()
#     print('CUP number:' + str(multiprocessing.cpu_count()))
#     for p in multiprocessing.active_children():
#         print('child process name:' + p.name + 'id:' + str(p.pid))
#     print('process end')

# # help(multiprocessing.Process)
# help(multiprocessing.Process.run)
# help(multiprocessing.Process.pid)
# help(multiprocessing.Process)


# 自定义类
# class MyProcess(Process):
#     def __init__(self, loop):
#         Process.__init__(self)
#         self.loop = loop
#
#     def run(self):
#         for count in range(self.loop):
#             time.sleep(1)
#             print('Pid' + str(self.pid) + "   " + 'LoopCount: ' + str(count))
#
# if __name__ == '__main__':
#     for i in range(2, 5):
#         p = MyProcess(i)
#         p.daemon = True
#         p.start()
#         p.join()
#
#     print('Main process end')

from multiprocessing import Process, Queue


def f(q): q.put([42, None, 'hello'])
if __name__ == '__main__':
    q = Queue()
    p = Process(target=f, args=(q,))
    p.start()
    print(q.get())  # prints "[42, None, 'hello']" p.join()



