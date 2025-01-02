#FCFS Algorithm
#----------------------------

import matplotlib.pyplot as plt
import numpy as np


def fcfs(processes, burst_times, arrival_times):
    n = len(processes)
    waiting_times = [0] * n
    turnaround_times = [0] * n
    completion_times = [0] * n

    # First process completion time
    completion_times[0] = arrival_times[0] + burst_times[0]
    turnaround_times[0] = completion_times[0] - arrival_times[0]
    waiting_times[0] = turnaround_times[0] - burst_times[0]

    # Calculating waiting times and turnaround times for other processes
    for i in range(1, n):
        completion_times[i] = max(
            completion_times[i-1], arrival_times[i]) + burst_times[i]
        turnaround_times[i] = completion_times[i] - arrival_times[i]
        waiting_times[i] = turnaround_times[i] - burst_times[i]

    return waiting_times, turnaround_times, completion_times


def plot_fcfs(processes, burst_times, arrival_times, waiting_times, turnaround_times, completion_times):
    fig, ax = plt.subplots(2, 1, figsize=(10, 8))

    # Plotting Gantt Chart
    ax[0].barh(processes, burst_times, left=arrival_times,
               color='skyblue', edgecolor='black')
    ax[0].set_xlabel('Time')
    ax[0].set_ylabel('Processes')
    ax[0].set_title('FCFS Scheduling - Gantt Chart')

    # Plotting Turnaround and Waiting Times
    ax[1].bar(processes, waiting_times,
              color='lightgreen', label='Waiting Time')
    ax[1].bar(processes, turnaround_times, bottom=waiting_times,
              color='lightcoral', label='Turnaround Time')
    ax[1].set_xlabel('Processes')
    ax[1].set_ylabel('Time')
    ax[1].set_title('FCFS Scheduling - Waiting and Turnaround Times')
    ax[1].legend()

    plt.tight_layout()
    plt.show()


# Input data
n = int(input("Enter the number of processes: "))
processes = []
burst_times = []
arrival_times = []

for i in range(n):
    process_name = input(f"Enter process name for process {i+1}: ")
    processes.append(process_name)
    burst_time = int(input(f"Enter burst time for {process_name}: "))
    burst_times.append(burst_time)
    arrival_time = int(input(f"Enter arrival time for {process_name}: "))
    arrival_times.append(arrival_time)

# Calculate FCFS results
waiting_times, turnaround_times, completion_times = fcfs(
    processes, burst_times, arrival_times)

# Display the results
print("\nProcess\tBurst Time\tArrival Time\tCompletion Time\tWaiting Time\tTurnaround Time")
for i in range(n):
    print(f"{processes[i]}\t\t{burst_times[i]}\t\t{arrival_times[i]}\t\t{
          completion_times[i]} \t\t{waiting_times[i]}\t\t{turnaround_times[i]}")

# Plot the results
plot_fcfs(processes, burst_times, arrival_times,
          waiting_times, turnaround_times, completion_times)
