import queue

#队列
q = queue.Queue(40)

for i in range(0,100,2):
    # print(i)
    q.put(i)
    if q.full():
        break

print(q.full(),q.qsize())

while q.empty() is not True:
    print(q.get())

print(q.empty(),q.qsize())


