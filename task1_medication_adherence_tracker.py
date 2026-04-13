# ============================================
# TASK 1 - Medication Adherence Tracker
# Course: Programming for Problem Solving Lab
# Student: Dasari Sai Balaji
# Roll No: 25951A66G0
# Branch: CSM-C
# ============================================

def classify_adherence(missed, delayed):
    """Classify adherence as Good, Average, or Poor."""
    if missed == 0 and delayed <= 2:
        return "Good"
    elif missed <= 2 and delayed <= 5:
        return "Average"
    else:
        return "Poor"

def track_patient(patient_name, doses):
    """Track missed and delayed doses for a patient."""
    missed = 0
    delayed = 0
    for status, delay in doses:
        if status == 0:
            missed += 1
        elif delay > 0:
            delayed += 1
    classification = classify_adherence(missed, delayed)
    print(f"\nPatient: {patient_name}")
    print(f"Missed Doses  : {missed}")
    print(f"Delayed Doses : {delayed}")
    print(f"Adherence     : {classification}")

# Main program
n = int(input("Enter number of patients: "))
for _ in range(n):
    name = input("Enter patient name: ")
    d = int(input("Enter number of doses: "))
    doses = []
    for i in range(d):
        status = int(input(f"  Dose {i+1} taken (1) or missed (0): "))
        delay = int(input(f"  Delay in minutes (0 if none): "))
        doses.append((status, delay))
    track_patient(name, doses)
