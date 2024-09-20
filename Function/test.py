def min_time_to_complete_tasks(num_threads, task_durations):
    """
    Calculate the minimum time required to complete all tasks using multiple threads.

    Args:
        num_threads (int): The number of threads available for executing tasks.
        task_durations (list of int): A list where each element represents the duration of a task.

    Returns:
        int: The minimum time required to complete all tasks.

    Approach:
        - This function simulates task allocation to threads. Each thread can execute only
          one task at a time. The goal is to minimize the total time taken by all threads
          to finish all tasks.
        - It maintains a list of when each thread will be available for the next task.
        - Tasks are assigned to the thread that will be free the earliest.

    Time Complexity:
        - O(T * N), where `T` is the number of tasks and `N` is the number of threads.
        - Each task assignment requires finding the earliest available thread, which takes O(N).

    """
    # Initialize the list to store the time when each thread will be free.
    thread_times = [0] * num_threads

    # Iterate over each task and assign it to the thread that becomes free the earliest.
    for duration in task_durations:
        # Find the index of the thread that is free the earliest
        earliest_thread = thread_times.index(min(thread_times))
        # Assign the task to this thread and update its next free time
        thread_times[earliest_thread] += duration

    # The minimum time to complete all tasks will be the maximum free time among all threads
    return max(thread_times)


# Example usage of the function:
if __name__ == "__main__":
    num_threads = 3
    task_durations = [2, 3, 4, 5, 6]
    print(min_time_to_complete_tasks(num_threads, task_durations))
