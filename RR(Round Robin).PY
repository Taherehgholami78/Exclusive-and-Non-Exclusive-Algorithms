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
        
        self.end_times = []  


def get_process_input():
    n = int(input("tedad faraiand ra vared konid: "))
    processes = []
    for i in range(n):
        arrival_time = int(input(f" zaman vorud faraiand {i+1}: "))
        burst_time = int(input(f"zaman ejraye faraiand {i+1}: "))
        processes.append(Process(i+1, arrival_time, burst_time))
    return processes


def round_robin(processes, quantum):
    time = 0  
    ready_queue = []  
    process_index = 0  
    completed_processes = 0
    n = len(processes)

    while completed_processes < n:
        while process_index < n and processes[process_index].arrival_time <= time:
            ready_queue.append(processes[process_index])
            process_index += 1

        if ready_queue:
            process = ready_queue.pop(0)  
            if process.remaining_time > quantum:
                process.start_times.append(time)
                time += quantum
                process.remaining_time -= quantum
                ready_queue.append(process)   

 
                process.end_times.append(time)
            else:
                process.start_times.append(time)
                time += process.remaining_time
                process.remaining_time = 0
                process.completion_time = time
                process.turnaround_time = process.completion_time - process.arrival_time
                process.waiting_time = process.turnaround_time - process.burst_time
                completed_processes += 1
                process.end_times.append(time)
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

    print(f"\  miangin zaman charkhesh: {total_turnaround_time / len(processes):.2f}")
    print(f" miangin zaman entezar : {total_waiting_time / len(processes):.2f}")

def plot_gantt_chart(processes):
    fig, gnt = plt.subplots()
    gnt.set_xlabel('time')
    gnt.set_ylabel('faraiand')

    gnt.set_yticks([i for i in range(1, len(processes) + 1)])

    gnt.set_yticklabels([f"P{process.pid}" for process in processes])

    max_time = max([process.completion_time for process in processes])
    gnt.set_xlim(0, max_time + 1)

    for i, process in enumerate(processes):
        for start_time, end_time in zip(process.start_times, process.end_times):
            gnt.barh(i + 1, end_time - start_time, left=start_time, height=0.4)

    plt.title(" Round Robin")
    plt.show()

if __name__ == "__main__":
    processes = get_process_input()
    quantum = int(input("kuvantom zamani ra vared konid: "))


    processes = round_robin(processes, quantum)

    print_results(processes)

    plot_gantt_chart(processes)
