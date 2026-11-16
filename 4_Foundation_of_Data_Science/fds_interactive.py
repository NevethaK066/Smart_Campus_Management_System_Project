# ==============================================================================
# VELALAR COLLEGE OF ENGINEERING AND TECHNOLOGY (AUTONOMOUS), ERODE - 12
# DEPARTMENT OF INFORMATION TECHNOLOGY | CLASS: 25IT3A&B | AY: 2026-27 (ODD)
# COURSE: 25ITC31 - FOUNDATIONS OF DATA SCIENCE (FDS)
# Interactive Data Science & Participation Analysis Console
# ==============================================================================

import os
import sys
import sqlite3
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Switch to script directory
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

# Database connection
db_paths = [
    "smart_campus.db",
    "../smart_campus.db",
    "../2_Database_Management_System/smart_campus.db"
]
db_path = next((p for p in db_paths if os.path.exists(p)), None)

if not db_path:
    print("[ERROR] smart_campus.db not found!")
    exit(1)

def load_clean_data():
    conn = sqlite3.connect(db_path)
    df_students = pd.read_sql_query("SELECT * FROM students;", conn)
    df_events = pd.read_sql_query("SELECT * FROM events;", conn)
    df_registrations = pd.read_sql_query("SELECT * FROM registrations;", conn)
    df_attendance = pd.read_sql_query("SELECT * FROM attendance;", conn)
    df_feedback = pd.read_sql_query("SELECT * FROM event_feedback;", conn)
    conn.close()

    # Merge into Master DataFrame
    df = df_registrations.merge(df_students, on="student_id", how="left") \
                         .merge(df_events, on="event_id", how="left") \
                         .merge(df_attendance, on="registration_id", how="left") \
                         .merge(df_feedback, on="registration_id", how="left")

    # Cleaning & Type Conversions
    df['attendance_status'] = df['attendance_status'].fillna('Not Recorded')
    df['certificate_status'] = df['certificate_status'].fillna('Pending')
    df['rating'] = df['rating'].fillna(df['rating'].median())
    df['remarks'] = df['remarks'].fillna('None')
    df['registration_date'] = pd.to_datetime(df['registration_date'])
    df['event_date'] = pd.to_datetime(df['event_date'])
    df['year_of_study'] = df['year_of_study'].astype(int)
    df['is_present'] = (df['attendance_status'] == 'Present').astype(int)
    df['lead_time_days'] = np.maximum((df['event_date'] - df['registration_date']).dt.days, 0)
    
    return df, df_students, df_events

df_master, df_students, df_events = load_clean_data()

def print_banner():
    print("=" * 95)
    print(" VELALAR COLLEGE OF ENGINEERING AND TECHNOLOGY (AUTONOMOUS), ERODE - 12")
    print(" DEPARTMENT OF INFORMATION TECHNOLOGY | CLASS: 25IT3A&B | AY: 2026-27 (ODD)")
    print(" 25ITC31 - FOUNDATIONS OF DATA SCIENCE: INTERACTIVE ANALYTICS CONSOLE")
    print("=" * 95)

def print_menu():
    print("\n------------------------- DATA SCIENCE ANALYTICS MENU -------------------------")
    print("  1. View Master Dataset Overview & Cleaned Schema (Unit 4: Data Quality)")
    print("  2. Compute Measures of Central Tendency & Variability (Unit 1: Statistics)")
    print("  3. View Student Participation Leaderboard & Standard (z) Scores (Unit 1)")
    print("  4. View Department vs. Event Category Pivot Table (Unit 3: Wrangling)")
    print("  5. [INTERACTIVE] Filter Participation Records by Department")
    print("  6. [INTERACTIVE] Look Up Any Student's Event History by Roll Number")
    print("  7. [INTERACTIVE] Display Chart On Screen (Matplotlib Window)")
    print("  8. Re-generate and Save All 6 High-Res Visualization Figures")
    print("  9. Exit Console")
    print("-------------------------------------------------------------------------------")

def show_dataset_overview():
    print("\n=== MASTER DATASET OVERVIEW (Cleaned & Preprocessed) ===")
    print(f"Total Registrations Logged : {len(df_master)}")
    print(f"Total Unique Students      : {df_master['student_id'].nunique()}")
    print(f"Total Campus Events        : {df_master['event_id'].nunique()}")
    print(f"Features (Columns) Count   : {df_master.shape[1]}")
    print("\nSample Cleaned Rows (Top 5):")
    cols = ['registration_id', 'student_id', 'name', 'department', 'event_name', 'attendance_status', 'lead_time_days']
    print(df_master[cols].head().to_string(index=False))

def show_statistics():
    print("\n=== DESCRIPTIVE STATISTICS & VARIABILITY (Syllabus Unit 1) ===")
    student_part = df_master.groupby('student_id')['registration_id'].count()
    
    mean_val = student_part.mean()
    median_val = student_part.median()
    mode_val = student_part.mode().iloc[0]
    std_val = student_part.std()
    var_val = student_part.var()
    min_val = student_part.min()
    max_val = student_part.max()
    iqr_val = np.percentile(student_part, 75) - np.percentile(student_part, 25)

    print(f"  • Mean Event Participation (Average) : {mean_val:.2f} events/student")
    print(f"  • Median Participation                : {median_val:.2f} events")
    print(f"  • Mode Participation                  : {mode_val} events")
    print(f"  • Standard Deviation (σ)              : {std_val:.2f}")
    print(f"  • Variance (σ²)                       : {var_val:.2f}")
    print(f"  • Range (Min - Max)                   : {min_val} to {max_val} events")
    print(f"  • Interquartile Range (IQR)           : {iqr_val:.2f}")

def show_z_scores():
    print("\n=== STUDENT PARTICIPATION LEADERBOARD & Z-SCORES (Syllabus Unit 1) ===")
    sp = df_master.groupby(['student_id', 'name', 'department']).agg(
        registered=('registration_id', 'count'),
        attended=('is_present', 'sum')
    ).reset_index()
    
    mean = sp['registered'].mean()
    std = sp['registered'].std()
    sp['z_score'] = (sp['registered'] - mean) / std

    print(f"Formula applied: z = (x - μ) / σ  [where μ = {mean:.2f}, σ = {std:.2f}]")
    print(sp.sort_values(by='registered', ascending=False).to_string(index=False))

def show_pivot_table():
    print("\n=== DEPARTMENT VS. EVENT CATEGORY PIVOT TABLE (Syllabus Unit 3) ===")
    pivot = pd.pivot_table(
        df_master,
        index='department',
        columns='category',
        values='registration_id',
        aggfunc='count',
        fill_value=0
    )
    print(pivot.to_string())

def filter_by_department():
    depts = sorted(df_master['department'].dropna().unique())
    print("\nAvailable Departments:")
    for i, d in enumerate(depts, 1):
        print(f"  {i}. {d}")
    
    choice = input("\nEnter Department Name or Number: ").strip()
    if choice.isdigit() and 1 <= int(choice) <= len(depts):
        selected_dept = depts[int(choice) - 1]
    else:
        selected_dept = choice

    filtered = df_master[df_master['department'].str.lower() == selected_dept.lower()]
    if filtered.empty:
        print(f"[WARN] No records found matching department: '{selected_dept}'")
        return
    
    print(f"\n--- PARTICIPATION ROSTER FOR: {selected_dept.upper()} ({len(filtered)} records) ---")
    cols = ['student_id', 'name', 'event_name', 'category', 'attendance_status']
    print(filtered[cols].to_string(index=False))

def lookup_student():
    sid = input("\nEnter Student Roll Number to look up (e.g., 25IT001 or 25IT150): ").strip()
    student_records = df_master[df_master['student_id'].str.lower() == sid.lower()]
    
    if student_records.empty:
        s_info = df_students[df_students['student_id'].str.lower() == sid.lower()]
        if not s_info.empty:
            s = s_info.iloc[0]
            print(f"\nStudent Profile: [{s['student_id']}] {s['name']} | Dept: {s['department']} | Year: {s['year_of_study']}")
            print("  -> This student is registered in the college, but has not yet enrolled in any events.")
        else:
            print(f"[WARN] No student found with Roll Number '{sid}'.")
        return

    s = student_records.iloc[0]
    print(f"\n==========================================================================================")
    print(f" STUDENT PARTICIPATION PROFILE: [{s['student_id']}] {s['name'].upper()}")
    print(f" Department: {s['department']} | Year of Study: {s['year_of_study']}th Year")
    print(f" Total Registered Events: {len(student_records)} | Attended Events: {student_records['is_present'].sum()}")
    print("==========================================================================================")
    for _, row in student_records.iterrows():
        print(f" • Event: {row['event_name']:<32} | Date: {str(row['event_date'])[:10]} | Status: {row['attendance_status']:<10} | Cert: {row['certificate_status']}")
    print("==========================================================================================")

def display_chart_interactive():
    print("\nSelect a chart to open in an interactive graphical window:")
    print("  1. Event Registrations vs. Actual Attendance (Bar Chart)")
    print("  2. Department-wise Participation Share (Donut Chart)")
    print("  3. Department vs. Event Category Engagement (Heatmap)")
    print("  4. Participation Distribution by Academic Year (Box Plot)")
    print("  5. Registration Lead Time Distribution (Histogram with KDE)")
    print("  6. Event Enrollments by Category (Horizontal Bar Chart)")
    
    ch = input("Enter choice (1-6): ").strip()
    plt.close('all')

    if ch == "1":
        event_summary = df_master.groupby('event_name').agg(
            total_reg=('registration_id', 'count'),
            attended=('is_present', 'sum')
        ).reset_index()
        indices = np.arange(len(event_summary))
        plt.figure(figsize=(10, 6))
        plt.bar(indices - 0.2, event_summary['total_reg'], width=0.4, label='Registrations', color='#3B82F6')
        plt.bar(indices + 0.2, event_summary['attended'], width=0.4, label='Attended', color='#10B981')
        plt.xticks(indices, [n[:18] + '..' if len(n)>18 else n for n in event_summary['event_name']], rotation=25, ha='right')
        plt.title('Campus Events: Registrations vs. Attendance (VCET 2026-27)', fontweight='bold')
        plt.legend()
        plt.tight_layout()
        plt.show()

    elif ch == "2":
        dept_counts = df_master['department'].value_counts()
        plt.figure(figsize=(8, 8))
        plt.pie(dept_counts, labels=dept_counts.index, autopct='%1.1f%%', startangle=140, pctdistance=0.75, wedgeprops=dict(width=0.4, edgecolor='white'))
        plt.title('Department-wise Event Participation Share', fontweight='bold')
        plt.tight_layout()
        plt.show()

    elif ch == "3":
        pivot = pd.pivot_table(df_master, index='department', columns='category', values='registration_id', aggfunc='count', fill_value=0)
        plt.figure(figsize=(10, 6))
        sns.heatmap(pivot, annot=True, fmt='d', cmap='YlGnBu')
        plt.title('Heatmap: Department vs. Category Engagement Matrix', fontweight='bold')
        plt.tight_layout()
        plt.show()

    elif ch == "4":
        sp = df_master.groupby(['student_id', 'year_of_study'])['registration_id'].count().reset_index()
        plt.figure(figsize=(9, 6))
        sns.boxplot(x='year_of_study', y='registration_id', data=sp, palette='Set2')
        plt.title('Participation Distribution by Academic Year of Study', fontweight='bold')
        plt.xlabel('Year of Study (1-4)')
        plt.ylabel('Events Registered')
        plt.tight_layout()
        plt.show()

    elif ch == "5":
        plt.figure(figsize=(9, 5))
        sns.histplot(df_master['lead_time_days'], kde=True, bins=10, color='#8B5CF6')
        plt.title('Registration Lead Time (Days in Advance)', fontweight='bold')
        plt.tight_layout()
        plt.show()

    elif ch == "6":
        cat_counts = df_master['category'].value_counts()
        plt.figure(figsize=(9, 5))
        sns.barplot(x=cat_counts.values, y=cat_counts.index, palette='crest')
        plt.title('Total Enrollments by Event Category', fontweight='bold')
        plt.tight_layout()
        plt.show()
    else:
        print("[WARN] Invalid chart selection.")

if __name__ == "__main__":
    print_banner()
    while True:
        print_menu()
        choice = input("Select an option (1-9): ").strip()
        if choice == "1":
            show_dataset_overview()
        elif choice == "2":
            show_statistics()
        elif choice == "3":
            show_z_scores()
        elif choice == "4":
            show_pivot_table()
        elif choice == "5":
            filter_by_department()
        elif choice == "6":
            lookup_student()
        elif choice == "7":
            display_chart_interactive()
        elif choice == "8":
            print("\nRe-running automated FDS pipeline...")
            import subprocess
            subprocess.run([sys.executable, "event_data_analysis.py"])
        elif choice == "9":
            print("\nExiting Foundations of Data Science Console. Goodbye!")
            break
        else:
            print("[WARN] Invalid option. Enter a number between 1 and 9.")
