import time
from backend.blockchain.blockchain import Blockchain
from backend.config import SECONDS

blockchain = Blockchain()

times = []

total_blocks = 0

total_time = 0

for i in range(1000):
    start_time = time.time_ns()
    blockchain.add_block(i)
    end_time = time.time_ns()

    time_to_mine = (end_time - start_time) / SECONDS

    times.append(time_to_mine)

    average_time = sum(times) / len(times)

    total_blocks += 1

    total_time += time_to_mine

    print(f'New block difficulty: {blockchain.chain[-1].difficulty}')
    print(f'Time to mine new block: {time_to_mine}s')
    print(f'Average time to add blocks: {average_time}s')
    print(f'Total number of blocks: {total_blocks}')
    print(f'Total time to mine: {total_time}\n')
