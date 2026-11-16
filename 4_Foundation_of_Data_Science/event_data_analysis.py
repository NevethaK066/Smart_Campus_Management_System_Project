# ==============================================================================
# VELALAR COLLEGE OF ENGINEERING AND TECHNOLOGY (AUTONOMOUS), ERODE - 12
# DEPARTMENT OF INFORMATION TECHNOLOGY
# ACADEMIC YEAR: 2026-27 (ODD) | CLASS: 25IT3A&B
# COURSE: 25ITC31 - FOUNDATIONS OF DATA SCIENCE
# Scenario 6: Smart Campus Event Management and Student Participation Analysis
# Script: event_data_analysis.py
# ==============================================================================

import os
import sqlite3
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Output directories
VIS_DIR = os.path.join(os.path.dirname(__file__), "visualizations")
os.makedirs(VIS_DIR, exist_ok=True)

# Styling configuration
plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
sns.set_palette("tab10")
plt.rcParams['font.sans-serif'] = 'Arial'
plt.rcParams['font.size'] = 10

def banner(title):
    print("\n" + "=" * 90)
    print(f" {title}")
    print("=" * 90)

# ------------------------------------------------------------------------------
# STEP 1: DATABASE RETRIEVAL (Unit 2 & Syllabus Requirement)
# ------------------------------------------------------------------------------
banner("STEP 1: DATABASE RETRIEVAL & INTEGRATION FROM SQLITE")
db_paths = [
    os.path.join(os.path.dirname(__file__), "smart_campus.db"),
    os.path.join(os.path.dirname(__file__), "../2_Database_Management_System/smart_campus.db"),
    "smart_campus.db"
]

db_path = next((p for p in db_paths if os.path.exists(p)), None)
if not db_path:
    raise FileNotFoundError("smart_campus.db not found in project directories!")

print(f"[OK] Connecting to SQLite Database at: {os.path.abspath(db_path)}")
conn = sqlite3.connect(db_path)

# Extract raw relational tables into DataFrames
df_students = pd.read_sql_query("SELECT * FROM students;", conn)
df_events = pd.read_sql_query("SELECT * FROM events;", conn)
df_registrations = pd.read_sql_query("SELECT * FROM registrations;", conn)
df_attendance = pd.read_sql_query("SELECT * FROM attendance;", conn)
df_feedback = pd.read_sql_query("SELECT * FROM event_feedback;", conn)

conn.close()

print(f"  -> Retrieved {len(df_students)} Students")
print(f"  -> Retrieved {len(df_events)} Events")
print(f"  -> Retrieved {len(df_registrations)} Registrations")
print(f"  -> Retrieved {len(df_attendance)} Attendance records")
print(f"  -> Retrieved {len(df_feedback)} Feedback records")

# ------------------------------------------------------------------------------
# STEP 2: DATA INTEGRATION & CLEANING (Unit 4: Data Quality & Preprocessing)
# ------------------------------------------------------------------------------
banner("STEP 2: DATA CLEANING, TRANSFORMATION & FEATURE ENGINEERING")

# Merge into unified analytical DataFrame
df_master = df_registrations.merge(df_students, on="student_id", how="left") \
                            .merge(df_events, on="event_id", how="left") \
                            .merge(df_attendance, on="registration_id", how="left") \
                            .merge(df_feedback, on="registration_id", how="left")

print(f"Master Integrated Shape: {df_master.shape}")

# 1. Missing Value Detection and Imputation
print("\n[Data Quality] Null Values per Column Before Cleaning:")
nulls = df_master.isnull().sum()
print(nulls[nulls > 0].to_string())

# Impute missing attendance status for upcoming events or unlogged records
df_master['attendance_status'] = df_master['attendance_status'].fillna('Not Recorded')
df_master['certificate_status'] = df_master['certificate_status'].fillna('Pending')
df_master['rating'] = df_master['rating'].fillna(df_master['rating'].median())  # Impute median rating
df_master['remarks'] = df_master['remarks'].fillna('None')

# 2. Duplicate Detection
dupes = df_master.duplicated(subset=['student_id', 'event_id']).sum()
print(f"\n[Duplicate Check] Number of duplicate (student_id, event_id) pairs: {dupes}")
if dupes > 0:
    df_master = df_master.drop_duplicates(subset=['student_id', 'event_id'])
    print(f"  -> Dropped {dupes} duplicate rows.")

# 3. Data Type Conversions
df_master['registration_date'] = pd.to_datetime(df_master['registration_date'])
df_master['event_date'] = pd.to_datetime(df_master['event_date'])
df_master['year_of_study'] = df_master['year_of_study'].astype(int)

# 4. Feature Engineering
# Attended flag (Binary: 1 = Present, 0 = Absent / Not recorded)
df_master['is_present'] = (df_master['attendance_status'] == 'Present').astype(int)

# Registration Lead Time (Days between registration and event date)
df_master['lead_time_days'] = (df_master['event_date'] - df_master['registration_date']).dt.days
# Clip negative or 0 lead times for clean analysis
df_master['lead_time_days'] = np.maximum(df_master['lead_time_days'], 0)

print("\nSample Cleaned Master Records (Top 5):")
print(df_master[['registration_id', 'student_id', 'name', 'department', 'event_name', 'attendance_status', 'lead_time_days']].head().to_string(index=False))

# ------------------------------------------------------------------------------
# STEP 3: DESCRIPTIVE STATISTICS & VARIABILITY (Unit 1: Statistics & z-Scores)
# ------------------------------------------------------------------------------
banner("STEP 3: DESCRIPTIVE STATISTICS, VARIABILITY & Z-SCORE OUTLIER DETECTION")

# Student participation frequency
student_part = df_master.groupby(['student_id', 'name', 'department']).agg(
    total_events=('registration_id', 'count'),
    attended_events=('is_present', 'sum')
).reset_index()

mean_part = student_part['total_events'].mean()
std_part = student_part['total_events'].std()
median_part = student_part['total_events'].median()

# Calculate standard (z) scores (Unit 1)
student_part['z_score'] = (student_part['total_events'] - mean_part) / std_part

print(f"Measures of Central Tendency & Variability for Student Participation:")
print(f"  Mean Event Participation  : {mean_part:.2f}")
print(f"  Median Participation      : {median_part:.2f}")
print(f"  Standard Deviation        : {std_part:.2f}")
print(f"  Variance                  : {student_part['total_events'].var():.2f}")
print(f"  Range (Min - Max)         : {student_part['total_events'].min()} - {student_part['total_events'].max()}")

print("\nStudent Participation Distribution with Standard (z) Scores:")
print(student_part.sort_values(by='total_events', ascending=False).head(10).to_string(index=False))

# ------------------------------------------------------------------------------
# STEP 4: DATA WRANGLING & PIVOT TABLES (Unit 3: Pandas & NumPy)
# ------------------------------------------------------------------------------
banner("STEP 4: DATA WRANGLING & PIVOT TABLES")

# Pivot table: Department vs Event Category
pivot_dept_cat = pd.pivot_table(
    df_master,
    index='department',
    columns='category',
    values='registration_id',
    aggfunc='count',
    fill_value=0
)
print("Department vs. Event Category Participation Pivot Table:")
print(pivot_dept_cat.to_string())

# Event Performance Summary
event_summary = df_master.groupby(['event_id', 'event_name', 'category']).agg(
    total_registrations=('registration_id', 'count'),
    total_attended=('is_present', 'sum'),
    mean_lead_days=('lead_time_days', 'mean')
).reset_index()
event_summary['attendance_rate_pct'] = (event_summary['total_attended'] / event_summary['total_registrations']) * 100
print("\nEvent Summary Performance:")
print(event_summary.sort_values(by='total_registrations', ascending=False).to_string(index=False))

# ------------------------------------------------------------------------------
# STEP 5: EXPLORATORY DATA ANALYSIS & VISUALIZATION (Unit 5)
# ------------------------------------------------------------------------------
banner("STEP 5: GENERATING 6 SCIENTIFIC VISUALIZATIONS (Matplotlib & Seaborn)")

# ------------------------------------------------------------------------------
# Visualization 1: Bar Chart - Registrations vs Attendance
# ------------------------------------------------------------------------------
plt.figure(figsize=(10, 6))
bar_width = 0.35
indices = np.arange(len(event_summary))

plt.bar(indices - bar_width/2, event_summary['total_registrations'], width=bar_width, label='Registrations', color='#3B82F6', edgecolor='#1D4ED8')
plt.bar(indices + bar_width/2, event_summary['total_attended'], width=bar_width, label='Attended', color='#10B981', edgecolor='#047857')

plt.xlabel('Campus Event', fontweight='bold', fontsize=11)
plt.ylabel('Student Count', fontweight='bold', fontsize=11)
plt.title('Campus Events: Total Registrations vs. Actual Attendance (VCET 2026-27)', fontsize=13, fontweight='bold', pad=12)
plt.xticks(indices, [name[:18] + '..' if len(name) > 18 else name for name in event_summary['event_name']], rotation=25, ha='right')
plt.legend(frameon=True, facecolor='#FFFFFF')
plt.tight_layout()
p1 = os.path.join(VIS_DIR, "1_registrations_vs_attendance.png")
plt.savefig(p1, dpi=300)
plt.close()
print(f"[OK] Saved Chart 1: {p1}")

# ------------------------------------------------------------------------------
# Visualization 2: Donut Chart - Department Participation Distribution
# ------------------------------------------------------------------------------
dept_counts = df_master['department'].value_counts()
plt.figure(figsize=(8, 8))
colors = sns.color_palette('pastel')[0:len(dept_counts)]

wedges, texts, autotexts = plt.pie(
    dept_counts,
    labels=[d.replace("Engineering", "Engg") for d in dept_counts.index],
    autopct='%1.1f%%',
    startangle=140,
    colors=colors,
    pctdistance=0.75,
    wedgeprops=dict(width=0.4, edgecolor='white', lw=2)
)
for at in autotexts:
    at.set_fontsize(10)
    at.set_fontweight('bold')

plt.title('Department-wise Event Participation Share\nVelalar College of Engineering & Technology', fontsize=13, fontweight='bold')
plt.tight_layout()
p2 = os.path.join(VIS_DIR, "2_department_participation.png")
plt.savefig(p2, dpi=300)
plt.close()
print(f"[OK] Saved Chart 2: {p2}")

# ------------------------------------------------------------------------------
# Visualization 3: Heatmap - Department vs Event Category
# ------------------------------------------------------------------------------
plt.figure(figsize=(10, 6))
sns.heatmap(pivot_dept_cat, annot=True, fmt='d', cmap='YlGnBu', cbar_kws={'label': 'Registration Volume'}, lw=1, linecolor='white')
plt.title('Heatmap: Department vs. Event Category Engagement Matrix', fontsize=13, fontweight='bold', pad=12)
plt.xlabel('Event Category', fontweight='bold')
plt.ylabel('Department', fontweight='bold')
plt.xticks(rotation=20, ha='right')
plt.tight_layout()
p3 = os.path.join(VIS_DIR, "3_dept_event_heatmap.png")
plt.savefig(p3, dpi=300)
plt.close()
print(f"[OK] Saved Chart 3: {p3}")

# ------------------------------------------------------------------------------
# Visualization 4: Box Plot - Year-wise Participation Distribution
# ------------------------------------------------------------------------------
plt.figure(figsize=(9, 6))
sns.boxplot(x='year_of_study', y='total_events', data=student_part.merge(df_students[['student_id', 'year_of_study']], on='student_id'), hue='year_of_study', palette='Set2', legend=False)
sns.stripplot(x='year_of_study', y='total_events', data=student_part.merge(df_students[['student_id', 'year_of_study']], on='student_id'), color='black', alpha=0.5, jitter=0.2)
plt.title('Distribution of Student Event Participation by Academic Year of Study', fontsize=13, fontweight='bold', pad=12)
plt.xlabel('Academic Year of Study (1st to 4th Year)', fontweight='bold')
plt.ylabel('Events Registered per Student', fontweight='bold')
plt.tight_layout()
p4 = os.path.join(VIS_DIR, "4_year_wise_participation_boxplot.png")
plt.savefig(p4, dpi=300)
plt.close()
print(f"[OK] Saved Chart 4: {p4}")

# ------------------------------------------------------------------------------
# Visualization 5: Histogram with KDE - Attendance Rate & Lead Time Distribution
# ------------------------------------------------------------------------------
plt.figure(figsize=(10, 5))
sns.histplot(df_master['lead_time_days'], kde=True, bins=10, color='#8B5CF6', edgecolor='#6D28D9')
plt.title('Distribution of Registration Lead Time (Days in Advance)', fontsize=13, fontweight='bold', pad=12)
plt.xlabel('Lead Time (Days before Event)', fontweight='bold')
plt.ylabel('Number of Student Registrations', fontweight='bold')
plt.tight_layout()
p5 = os.path.join(VIS_DIR, "5_registration_lead_time_hist.png")
plt.savefig(p5, dpi=300)
plt.close()
print(f"[OK] Saved Chart 5: {p5}")

# ------------------------------------------------------------------------------
# Visualization 6: Event Category Share Bar Chart
# ------------------------------------------------------------------------------
plt.figure(figsize=(9, 5))
cat_series = df_master['category'].value_counts()
sns.barplot(x=cat_series.values, y=cat_series.index, hue=cat_series.index, palette='crest', legend=False)
plt.title('Total Enrollments by Event Category', fontsize=13, fontweight='bold', pad=12)
plt.xlabel('Total Registrations', fontweight='bold')
plt.ylabel('Event Category', fontweight='bold')
plt.tight_layout()
p6 = os.path.join(VIS_DIR, "6_event_category_distribution.png")
plt.savefig(p6, dpi=300)
plt.close()
print(f"[OK] Saved Chart 6: {p6}")

print("\n" + "=" * 90)
print(" FDS PIPELINE EXECUTION & VISUALIZATION COMPLETE!")
print(f" All 6 visualization figures saved to: {VIS_DIR}")
print("=" * 90)
