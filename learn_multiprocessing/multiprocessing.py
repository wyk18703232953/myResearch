import multiprocessing
import time
import os
from multiprocessing import Process, Pool, Queue, Pipe, Value, Array, Lock

# 1. 基本的进程创建和运行
def worker_function(name, duration):
    """模拟一个耗时的工作任务"""
    print(f"进程 {name} (PID: {os.getpid()}) 开始工作，预计耗时 {duration} 秒...")
    time.sleep(duration)
    print(f"进程 {name} (PID: {os.getpid()}) 完成工作。")

def demo_basic_process():
    print("\n=== 1. 演示基本进程创建 ===")
    # 创建进程对象
    p1 = Process(target=worker_function, args=("Worker-1", 2))
    p2 = Process(target=worker_function, args=("Worker-2", 3))

    # 启动进程
    p1.start()
    p2.start()

    # 等待进程完成
    p1.join()
    p2.join()
    print("所有基本进程任务完成。\n")

# 2. 使用进程池
def square_number(n):
    """计算一个数的平方"""
    print(f"进程 {os.getpid()} 正在计算 {n} 的平方...")
    time.sleep(0.1) # 模拟一些计算时间
    return n * n

def demo_process_pool():
    print("=== 2. 演示进程池 ===")
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # 创建一个进程池，默认使用 CPU 核心数
    with Pool() as pool:
        # 使用 pool.map 并行计算列表中每个数的平方
        results = pool.map(square_number, numbers)

    print(f"输入: {numbers}")
    print(f"输出 (平方): {results}")
    print("进程池任务完成。\n")

# 3. 进程间通信 - Queue
def producer(queue):
    """向队列中放入数据"""
    items = ["item_1", "item_2", "item_3"]
    for item in items:
        print(f"生产者放入: {item}")
        queue.put(item)
        time.sleep(0.5) # 模拟生产时间
    print("生产者完成生产。")

def consumer(queue):
    """从队列中取出数据"""
    while True:
        try:
            item = queue.get(timeout=2) # 设置超时，避免无限等待
            print(f"消费者取出: {item}")
            time.sleep(1) # 模拟消费时间
        except:
            print("消费者在超时时间内未收到任何数据，退出。")
            break

def demo_queue_communication():
    print("=== 3. 演示进程间通信 (Queue) ===")
    # 创建一个队列
    q = Queue()

    # 创建生产者和消费者进程
    p_producer = Process(target=producer, args=(q,))
    p_consumer = Process(target=consumer, args=(q,))

    p_producer.start()
    p_consumer.start()

    p_producer.join()
    p_consumer.join()
    print("队列通信演示完成。\n")

# 4. 进程间通信 - Pipe
def sender(conn):
    """通过连接发送数据"""
    messages = ["Hello", "from", "sender", "process!"]
    for msg in messages:
        print(f"发送者发送: {msg}")
        conn.send(msg)
        time.sleep(0.3)
    conn.send("END") # 发送结束信号
    conn.close()

def receiver(conn):
    """通过连接接收数据"""
    while True:
        msg = conn.recv()
        if msg == "END":
            print("接收者收到结束信号，退出。")
            break
        print(f"接收者收到: {msg}")

def demo_pipe_communication():
    print("=== 4. 演示进程间通信 (Pipe) ===")
    # 创建一个管道
    parent_conn, child_conn = Pipe()

    # 创建发送者和接收者进程
    p_sender = Process(target=sender, args=(child_conn,))
    p_receiver = Process(target=receiver, args=(parent_conn,))

    p_sender.start()
    p_receiver.start()

    p_sender.join()
    p_receiver.join()
    print("管道通信演示完成。\n")

# 5. 共享内存 - Value 和 Array
def modify_shared_data(shared_value, shared_array, lock):
    """修改共享的 Value 和 Array"""
    with lock: # 使用锁确保操作的原子性
        print(f"进程 {os.getpid()} 修改共享数据前 - Value: {shared_value.value}, Array: {list(shared_array[:])}")
        shared_value.value += 100
        for i in range(len(shared_array)):
            shared_array[i] += shared_array[i] # 将数组中每个元素翻倍
        print(f"进程 {os.getpid()} 修改共享数据后 - Value: {shared_value.value}, Array: {list(shared_array[:])}")

def demo_shared_memory():
    print("=== 5. 演示共享内存 (Value, Array) ===")
    # 创建一个共享的整数值 (i 代表整型, 初始值为 0)
    shared_val = Value('i', 0)
    # 创建一个共享的整数数组 (i 代表整型, 长度为 5, 初始值为 [1, 2, 3, 4, 5])
    shared_arr = Array('i', [1, 2, 3, 4, 5])
    # 创建一个锁
    lock = Lock()

    print(f"主进程 - Value: {shared_val.value}, Array: {list(shared_arr[:])}")

    # 创建两个进程来修改共享数据
    p1 = Process(target=modify_shared_data, args=(shared_val, shared_arr, lock))
    p2 = Process(target=modify_shared_data, args=(shared_val, shared_arr, lock))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print(f"所有进程完成后 - Value: {shared_val.value}, Array: {list(shared_arr[:])}")
    print("共享内存演示完成。\n")

if __name__ == "__main__":
    # 在 Windows 上，多进程代码必须放在 if __name__ == '__main__': 下面
    print("开始运行 Python 多进程示例程序...")

    demo_basic_process()
    demo_process_pool()
    demo_queue_communication()
    demo_pipe_communication()
    demo_shared_memory()
    time.sleep(10)
    print("所有多进程演示已完成！")