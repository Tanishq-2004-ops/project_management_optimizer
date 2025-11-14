Project Management Optimizer
A small Streamlit app that schedules tasks (jobs) to maximize total profit using a greedy job sequencing algorithm.

Features
Upload a CSV of tasks or edit the sample table in the UI.
Computes an optimized set of jobs and the total profit.
Visualizes the scheduled jobs and provides a downloadable CSV of the result.

Repository layout
app.py — Streamlit application (entrypoint / UI).
job_scheduling.py — Greedy job sequencing algorithm used by the app.
requirements.txt — Python dependencies.
Prerequisites
Python 3.8+
pip

Run the app
From the project root:
streamlit run app.py

Streamlit will print a local URL (e.g., http://localhost:8501) — open it in your browser.
Expected input CSV format
The uploaded CSV must include these columns (headers are case-sensitive):

id — unique job identifier (string)
deadline — integer deadline (slot number)
profit — integer profit/value for completing the job

Output / UI behavior
Table of scheduled jobs (id, deadline, profit).
Total profit displayed.
Downloadable CSV (optimized_schedule.csv) of the scheduled jobs.
Timeline visualization and profit chart.
