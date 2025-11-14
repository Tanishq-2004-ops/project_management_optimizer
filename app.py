import streamlit as st
import pandas as pd
from job_scheduling import job_sequencing
import plotly.graph_objects as go  # changed from express

# --- Streamlit Page Setup ---
st.set_page_config(page_title="Project Management Optimizer", layout="centered")

st.title("📊 Project Management Optimizer")
st.write("Schedule tasks to maximize profit using the Greedy Job Sequencing Algorithm.")

# --- Sidebar for Input Options ---
st.sidebar.header("Input Options")
uploaded_file = st.sidebar.file_uploader("Upload CSV (columns: id,deadline,profit)", type=["csv"])

# --- Data Input ---
if uploaded_file:
    df_input = pd.read_csv(uploaded_file)
else:
    st.sidebar.write("Or use / edit sample data below:")
    sample_data = [
        {"id": "T1", "deadline": 2, "profit": 100},
        {"id": "T2", "deadline": 1, "profit": 19},
        {"id": "T3", "deadline": 2, "profit": 27},
        {"id": "T4", "deadline": 1, "profit": 25},
        {"id": "T5", "deadline": 3, "profit": 15},
    ]
    df_input = pd.DataFrame(sample_data)
    df_input = st.data_editor(df_input, num_rows="dynamic")

# --- Validate Input ---
required_cols = {"id", "deadline", "profit"}
if not required_cols.issubset(set(df_input.columns)):
    st.error("Input must have columns: id, deadline, profit")
    st.stop()

df_input["deadline"] = df_input["deadline"].astype(int)
df_input["profit"] = df_input["profit"].astype(int)
jobs = df_input.to_dict(orient="records")

# --- Button to Run the Algorithm ---
if st.button("Optimize Schedule"):
    scheduled_jobs, total_profit, slot_assignments = job_sequencing(jobs)

    # --- Output Section ---
    st.subheader("✅ Scheduled Jobs")
    df_output = pd.DataFrame(scheduled_jobs)
    st.table(df_output)

    st.success(f"💰 Total Profit: {total_profit}")

    # --- Download Results as CSV ---
    csv_data = df_output.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="⬇️ Download Scheduled Jobs as CSV",
        data=csv_data,
        file_name="optimized_schedule.csv",
        mime="text/csv"
    )

    # --- Slot Assignments Table ---
    st.subheader("📅 Slot Assignments (Timeline View)")
    slot_df = pd.DataFrame({
        "Slot": list(range(len(slot_assignments))),
        "Job": slot_assignments
    })
    st.table(slot_df[1:])  # skip index 0

    # --- Profit Bar Chart ---
    if len(scheduled_jobs) > 0:
        st.subheader("💹 Profit Comparison")
        st.bar_chart(df_output.set_index("id")["profit"])

        # --- Fixed Gantt Chart Visualization ---
        gantt_data = []
        for i, job in enumerate(scheduled_jobs, start=1):
            gantt_data.append({
                "Task": job["id"],
                "Slot": i,
                "Profit": job["profit"]
            })

        fig = go.Figure()

        for row in gantt_data:
            fig.add_trace(go.Bar(
                x=[1],  # each bar has width 1
                y=[row["Task"]],
                orientation='h',
                name=row["Task"],
                hovertext=f"Profit: {row['Profit']}",
                text=f"{row['Task']} (₹{row['Profit']})",
                textposition="inside"
            ))

        fig.update_layout(
            title="🗓 Task Schedule (Slot-based Timeline)",
            xaxis_title="Time Slots",
            yaxis_title="Tasks",
            barmode='stack',
            height=400
        )

        st.plotly_chart(fig, use_container_width=True)

else:
    st.info("Upload a CSV or use the editable table, then click **Optimize Schedule**.")
