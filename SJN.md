#SJN Algorithm
#------------------------------


import matplotlib.pyplot as plt

class Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.completion_time = 0
        self.turnaround_time = 0
        self.waiting_time = 0
        self.start_time = 0

def get_process_input():
    n = int(input(" tedade faraiand ha ra vared konid: "))
    processes = []
    for i in range(n):
        arrival_time = int(input(f" zaman vorude faraiand ha {i+1}: "))
        burst_time = int(input(f"zaman ejraye faraiand ha {i+1}: "))
        processes.append(Process(i+1, arrival_time, burst_time))
    return processes


def sjn_non_preemptive(processes):
    processes.sort(key=lambda p: p.arrival_time)  
    time = 0
    completed_processes = 0
    n = len(processes)
    ready_queue = []

    while completed_processes < n:
        for process in processes:
            if process.arrival_time <= time and process not in ready_queue and process.completion_time == 0:
                ready_queue.append(process)

        if ready_queue:
            ready_queue.sort(key=lambda p: p.burst_time)
            current_process = ready_queue.pop(0)
            current_process.start_time = time
            time += current_process.burst_time
            current_process.completion_time = time
            current_process.turnaround_time = current_process.completion_time - current_process.arrival_time
            current_process.waiting_time = current_process.turnaround_time - current_process.burst_time
            completed_processes += 1
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

    print(f"\nmiangin zaman charkhesh : {total_turnaround_time / len(processes):.2f}")
    print(f" miangin zaman entazar : {total_waiting_time / len(processes):.2f}")

def plot_gantt_chart(processes):
    fig, gnt = plt.subplots()
    gnt.set_xlabel('zaman')
    gnt.set_ylabel('faraiand ha')

    gnt.set_yticks([i for i in range(1, len(processes) + 1)])
    gnt.set_yticklabels([f"P{process.pid}" for process in processes])

    max_time = max([process.completion_time for process in processes])
    gnt.set_xlim(0, max_time + 1)


    for i, process in enumerate(processes):
        gnt.barh(i + 1, process.burst_time, left=process.start_time, height=0.4)

    plt.title("(SJN)")
    plt.show()

if __name__ == "__main__":
    processes = get_process_input()

    processes = sjn_non_preemptive(processes)

    print_results(processes)

    plot_gantt_chart(processes)
