def predict_peak_performance(minutes, mood, time_of_day, problem, coping):

    # Simple rule based logic (for now)
    score = 0

    if mood in ["Happy", "Motivated"]:
        score += 40
    else:
        score += 20

    if time_of_day in ["Morning", "Evening"]:
        score += 30
    else:
        score += 20

    if problem == "None":
        score += 20
    else:
        score += 10

    if coping in ["Pomodoro", "Revision"]:
        score += 10
    else:
        score += 5

    # --------------------
    # Performance Status
    # --------------------

    if score >= 80:
        status = "High Peak Performance"
        recommendation = "Continue studying during this time and mood for best results."
    elif score >= 60:
        status = "Medium Peak Performance"
        recommendation = "Improve focus using Pomodoro or short breaks."
    else:
        status = "Low Peak Performance"
        recommendation = "Change study time, mood or environment to improve output."

    # --------------------
    # RETURN FORMAT Flask EXPECTS
    # --------------------

    return {
        "score": score,
        "status": status,
        "recommendation": recommendation
    }
