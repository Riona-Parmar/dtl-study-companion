import os
import csv

def get_digital_twin(day, planned_minutes, sessions, actual_minutes):

    BASE_DIR = os.path.dirname(__file__)
    CSV_PATH = os.path.join(BASE_DIR, "daily_progress.csv")

    # ----------------------------
    # Safety checks
    # ----------------------------

    if planned_minutes == 0:
        planned_minutes = 1

    # ----------------------------
    # Ideal progress
    # ----------------------------

    ideal_progress = day * planned_minutes

    # ----------------------------
    # Core calculations
    # ----------------------------

    lag = ideal_progress - actual_minutes

    if ideal_progress > 0:
        consistency = round((actual_minutes / ideal_progress) * 100, 2)
    else:
        consistency = 0

    # ----------------------------
    # Previous lag
    # ----------------------------

    previous_lag = None

    if os.path.exists(CSV_PATH):
        with open(CSV_PATH, "r") as file:
            rows = list(csv.reader(file))
            if len(rows) > 1:
                previous_lag = int(rows[-1][5])

    # ----------------------------
    # Trend logic
    # ----------------------------

    if previous_lag is not None:
        diff = lag - previous_lag
        if diff < 0:
            trend = "You are catching up with your Digital Twin."
        elif diff > 0:
            trend = "You are falling behind your Digital Twin."
        else:
            trend = "Your progress is stable."
    else:
        trend = "No previous data available."

    # ----------------------------
    # Feedback
    # ----------------------------

    if consistency >= 90:
        feedback = "Excellent consistency. Keep going!"
    elif consistency >= 70:
        feedback = "Good progress. Push a little more."
    else:
        feedback = "Low consistency. Improve your schedule."

    # ----------------------------
    # Catch-up plan
    # ----------------------------

    extra_minutes = 30

    if lag > 0:
        days_to_catch = max(1, lag // extra_minutes)
        catchup = f"Study {extra_minutes} extra minutes daily to recover in {days_to_catch} days."
    else:
        catchup = "You are ahead of your Digital Twin!"

    # ----------------------------
    # Save CSV
    # ----------------------------

    write_header = not os.path.exists(CSV_PATH)

    with open(CSV_PATH, "a", newline="") as file:
        writer = csv.writer(file)

        if write_header:
            writer.writerow([
                "day", "planned", "actual",
                "sessions", "ideal", "lag", "consistency"
            ])

        writer.writerow([
            day,
            planned_minutes,
            actual_minutes,
            sessions,
            ideal_progress,
            lag,
            consistency
        ])

    # ----------------------------
    # Return to Flask
    # ----------------------------

    return {
        "ideal": ideal_progress,
        "actual": actual_minutes,
        "lag": lag,
        "consistency": consistency,
        "trend": trend,
        "feedback": feedback,
        "catchup": catchup
    }
