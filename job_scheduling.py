# job_scheduling.py

def job_sequencing(jobs):
    """
    jobs: list of dicts with keys - id (str), deadline (int), profit (int)
    Returns: (scheduled_jobs_list, total_profit, slot_assignments)
    """
    # Sort by profit descending
    jobs_sorted = sorted(jobs, key=lambda x: x['profit'], reverse=True)

    # Max deadline
    max_deadline = 0
    for job in jobs_sorted:
        if job['deadline'] > max_deadline:
            max_deadline = job['deadline']

    # Initialize slots (index 0 unused)
    slots = [-1] * (max_deadline + 1)    # stores job id or -1
    scheduled_jobs = []
    total_profit = 0

    for job in jobs_sorted:
        # place job in latest possible free slot <= deadline
        for d in range(job['deadline'], 0, -1):
            if slots[d] == -1:
                slots[d] = job['id']
                scheduled_jobs.append(job)
                total_profit += job['profit']
                break

    # Create slot assignment list for visualization: index -> job id or None
    slot_assignments = [None if s == -1 else s for s in slots]
    return scheduled_jobs, total_profit, slot_assignments
