Project Management Optimizer

A simple and interactive Streamlit application that schedules tasks using the Greedy Job Sequencing Algorithm to maximize total profit.
Upload your own CSV file or modify the sample table in the app, visualize scheduled tasks, and download the optimized output.

🚀 Features

📤 Upload a CSV of jobs or edit a sample dataset directly in the UI
⚙️ Greedy Job Sequencing to compute the maximum profit schedule
📊 Visual timeline and profit chart
📄 Display of the optimized job list (id, deadline, profit)
💰 Total profit shown clearly
⬇️ Download the optimized schedule as optimized_schedule.csv

✅ Prerequisites
Python 3.8+
pip (Python package manager)

▶️ How to Run
From the project root directory, run:
streamlit run app.py

📤 Output & UI Behavior

After uploading or editing data:
✔️ Application calculates an optimized schedule
✔️ Shows selected jobs with id, deadline, and profit
✔️ Displays total profit
✔️ Provides: Job timeline visualization, Profit chart
✔️ Allows downloading: optimized_schedule.csv

🧠 Algorithm Used

The app uses the Greedy Job Scheduling Algorithm:
Sort jobs by profit (highest first)
For each job, schedule it in the latest available slot before its deadline
Maximize the total profit
Implementation is in job_scheduling.py.
