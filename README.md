# PPS-TASK-ASSIGNMENT
# 🐍 Programming for Problem Solving – Task Assignment

**Student:** Dasari Sai Balaji  
**Roll No:** 25951A66G0  
**Branch:** CSM-C  
**Course:** Programming for Problem Solving Laboratory (ACSE07)  
**Institute:** Institute of Aeronautical Engineering, Hyderabad  

---

## 📁 Repository Structure

```
PPS_Tasks/
│
├── task1_medication_adherence_tracker.py
├── task2_email_verification.py
├── task3_food_ordering_system.py
└── README.md
```

---

## ✅ Task 1 – Medication Adherence Tracker

### 📌 Description
A Python program that tracks missed and delayed doses for each patient and classifies their medication adherence as **Good**, **Average**, or **Poor** based on defined rules.

### 📏 Constraints
- 1 <= N <= 10^5 (number of scheduled doses)
- 0 <= delay <= 1440 (minutes)
- Dose status: 1 = Taken, 0 = Missed

### 🏷️ Classification Rules
| Classification | Condition |
|----------------|-----------|
| Good           | missed = 0 AND delayed <= 2 |
| Average        | missed <= 2 AND delayed <= 5 |
| Poor           | Otherwise |

### ▶️ How to Run
```bash
python task1_medication_adherence_tracker.py
```

### 💻 Sample Output
```
Enter number of patients: 1
Enter patient name: Arjun
Enter number of doses: 3
  Dose 1 taken (1) or missed (0): 1
  Delay in minutes (0 if none): 10
  Dose 2 taken (1) or missed (0): 0
  Delay in minutes (0 if none): 0
  Dose 3 taken (1) or missed (0): 1
  Delay in minutes (0 if none): 5

Patient: Arjun
Missed Doses  : 1
Delayed Doses : 2
Adherence     : Average
```

---

## ✅ Task 2 – Email ID Verification

### 📌 Description
A Python program that verifies whether a given email ID is valid based on a set of structural rules including character checks, @ count, domain validation, and length constraints.

### 📏 Constraints
- 1 <= length of email <= 100
- Exactly one `@` character required
- At least one `.` must appear after `@`
- No spaces allowed
- Local part: only alphanumeric, underscores, hyphens, or periods
- Only printable ASCII characters allowed

### ▶️ How to Run
```bash
python task2_email_verification.py
```

### 💻 Sample Output
```
Enter email ID: dasari.saibalaji@gmail.com
Result : Valid Email ID

Enter email ID: dasari sai@gmail.com
Result : Spaces not allowed

Enter email ID: dasarisaibalaji@gmailcom
Result : Domain must contain at least one dot after @
```

---

## ✅ Task 3 – Food Ordering System

### 📌 Description
A Python program that displays a food menu, accepts orders from the user, validates item IDs and quantities, and calculates the total bill automatically.

### 🍽️ Menu
| Item ID | Item      | Price    |
|---------|-----------|----------|
| 1       | Pizza     | Rs. 200  |
| 2       | Burger    | Rs. 120  |
| 3       | Sandwich  | Rs. 100  |

### 📏 Constraints
- 1 <= n <= 100 (number of order items)
- item_id must be one of {1, 2, 3}
- 1 <= quantity <= 1000

### ▶️ How to Run
```bash
python task3_food_ordering_system.py
```

### 💻 Sample Output
```
===== MENU =====
1. Pizza - Rs.200
2. Burger - Rs.120
3. Sandwich - Rs.100
================
How many items to order? 2
Enter item ID (1-3): 1
Enter quantity: 2
Added: Pizza x2 = Rs.400
Enter item ID (1-3): 2
Enter quantity: 1
Added: Burger x1 = Rs.120

Total Bill: Rs.520
```

---

## 🛠️ Requirements
- Python 3.x
- No external libraries required

---

## 📹 Video Explanation
A video walkthrough explaining all three tasks, their logic, and live code execution is available in the repository.

---

## 📜 License
© 2026 Dasari Sai Balaji. All rights reserved.
