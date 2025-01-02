#MLFQ Algorithm
#--------------------------------

import queue
import matplotlib.pyplot as plt

class Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.completion_time = 0
        self.turnaround_time = 0
        self.waiting_time = 0
        self.start_times = []  
        
def get_process_input():
    n = int(input("tedad faraiand ra vared konid  : "))
    processes = []
    for i in range(n):
        arrival_time = int(input(f"  zaman vorood faraiand {i+1}: "))
        burst_time = int(input(f" zaman ejraye faraiand  {i+1}: "))
        processes.append(Process(i+1, arrival_time, burst_time))

    return processes

def mfq(processes, quanta):
    queues = [queue.Queue() for _ in range(len(quanta))]
    time = 0
    process_index = 0
    completed_processes = 0
    n = len(processes)

    while completed_processes < n:
        
        while process_index < n and processes[process_index].arrival_time <= time:
            queues[0].put(processes[process_index])
            process_index += 1
        
        for i in range(len(quanta)):
            if not queues[i].empty():
                process = queues[i].get()
                if process.remaining_time > quanta[i]:
                    process.start_times.append(time)  

                    time += quanta[i]
                    process.remaining_time -= quanta[i]
                     
                    if i + 1 < len(quanta):
                        queues[i+1].put(process)
                    else:
                        queues[i].put(process)  
                else:
                    process.start_times.append(time)  
                    time += process.remaining_time
                    process.remaining_time = 0
                    process.completion_time = time
                    process.turnaround_time = process.completion_time - process.arrival_time
                    process.waiting_time = process.turnaround_time - process.burst_time
                    completed_processes += 1
                break
        else:
            time += 1  

    return processes

def print_results(processes):
    total_waiting_time = 0
    total_turnaround_time = 0
    print("PID\tArrival\tBurst\tCompletion\tTurnaround\tWaiting")
    for process in processes:
        total_waiting_time += process.waiting_time
        total_turnaround_time += process.turnaround_time
        print(f"{process.pid}\t{process.arrival_time}\t{process.burst_time}\t"
              f"{process.completion_time}\t\t{process.turnaround_time}\t\t{process.waiting_time}")

    print(f"\miangin zaman charkhesh  : {total_turnaround_time / len(processes):.2f}")
    print(f"miangine zaman entezar  : {total_waiting_time / len(processes):.2f}")


def plot_gantt_chart(processes):

    fig, gnt = plt.subplots()
    gnt.set_xlabel('zaman')
    gnt.set_ylabel('faraiand ha')

    gnt.set_yticks([i for i in range(1, len(processes) + 1)])
    gnt.set_yticklabels([f"P{process.pid}" for process in processes])

    
    max_time = max([process.completion_time for process in processes])
    gnt.set_xlim(0, max_time + 1)

    
    for i, process in enumerate(processes):
        for start_time in process.start_times:
            gnt.barh(i + 1, process.burst_time, left=start_time, height=0.4)

    plt.title("MFQ")
    plt.show()

if __name__ == "__main__":

    processes = get_process_input()
    quanta = [4, 8, 16]     
    processes = mfq(processes, quanta)
    print_results(processes)
    plot_gantt_chart(processes)
