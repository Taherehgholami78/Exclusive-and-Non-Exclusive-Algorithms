#SRT Algorithm
#------------------------------

import heapq
import matplotlib.pyplot as plt

# Process class to hold process details


class Process:
    def __init__(self, name, arrival_time, burst_time):
        self.name = name                 # Process name
        self.arrival_time = arrival_time  # Arrival time of the process
        self.burst_time = burst_time     # Burst time of the process
        # Remaining burst time (used for preemption)
        self.remaining_time = burst_time
        self.completion_time = 0         # Completion time for the process
        # Turnaround time (completion_time - arrival_time)
        self.turnaround_time = 0
        # Waiting time (turnaround_time - burst_time)
        self.waiting_time = 0

    def __lt__(self, other):
        # We compare based on remaining time to implement SRTF (min heap)
        return self.remaining_time < other.remaining_time


def srtf(processes):
    # Sort processes by arrival time
    processes.sort(key=lambda x: x.arrival_time)
    time = 0              # Current time in the scheduler
    completed = 0         # Number of processes completed
    n = len(processes)
    queue = []            # Min-heap queue for processes that are ready to execute
    i = 0                 # Index to track which process to add to the ready queue
    # To hold the Gantt chart data (process, start_time, end_time)
    gantt_chart = []

    while completed < n:
        # Add all processes that have arrived by the current time to the ready queue
        while i < n and processes[i].arrival_time <= time:
            heapq.heappush(queue, processes[i])
            i += 1

        if queue:
            # Get the process with the shortest remaining time
            current_process = heapq.heappop(queue)

            # Execute the process for one unit of time
            start_time = time
            time += 1
            current_process.remaining_time -= 1
            end_time = time

            # Add the process to the Gantt chart (start_time, end_time, process name)
            gantt_chart.append((current_process.name, start_time, end_time))

            # If the process is completed
            if current_process.remaining_time == 0:
                current_process.completion_time = time
                current_process.turnaround_time = current_process.completion_time - \
                    current_process.arrival_time
                current_process.waiting_time = current_process.turnaround_time - \
                    current_process.burst_time
                completed += 1
            else:
                # If it's not completed, push it back into the queue
                heapq.heappush(queue, current_process)
        else:
            # If no process is ready, just move time forward
            time += 1

    return gantt_chart, processes

# Visualization using Matplotlib


def plot_gantt_chart(gantt_chart):
    fig, ax = plt.subplots(figsize=(10, 5))

    # Creating bars for the Gantt chart
    for process_name, start_time, end_time in gantt_chart:
        ax.barh(process_name, end_time - start_time,
                left=start_time, color='skyblue')

    # Formatting the plot
    ax.set_xlabel('Time')
    ax.set_ylabel('Process')
    ax.set_title('Shortest Remaining Time First (SRTF) Scheduling')
    plt.grid(True)
    plt.show()

# Input data from the user


def get_input_data():
    n = int(input("Enter the number of processes: "))
    processes = []
    for i in range(n):
        name = input(f"Enter the name of process {i+1}: ")
        arrival_time = int(input(f"Enter arrival time for process {name}: "))
        burst_time = int(input(f"Enter burst time for process {name}: "))
        processes.append(Process(name, arrival_time, burst_time))
    return processes


# Main function to run the program
if __name__ == "__main__":
    processes = get_input_data()  # Get input data from the user
    gantt_chart, processes = srtf(processes)  # Run the SRTF algorithm

    # Plot the Gantt chart
    plot_gantt_chart(gantt_chart)

    # Print the results for each process
    print("\nProcess\tArrival Time\tBurst Time\tCompletion Time\tTurnaround Time\tWaitingTime")
    for p in processes:
        print(f"{p.name}\t\t{p.arrival_time}\t\t{p.burst_time}\t\t{
              p.completion_time} \t\t{p.turnaround_time}\t\t{p.waiting_time}")
