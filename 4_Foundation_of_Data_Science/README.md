# 4. Foundation of Data Science (25ITC31)

This folder contains the complete Data Science pipeline, scripts, and analytical visualizations for the **Smart Campus Event Management and Student Participation Analysis System** (Scenario 6), designed in strict alignment with the **25ITC31 - Foundations of Data Science** syllabus.

## Deliverables in this Directory
* `event_data_analysis.py`: Python script executing database extraction, data cleaning, z-score statistical profiling, pivot table generation, and 6 Matplotlib/Seaborn charts.
* `FDS_Analysis_Report.md`: Full academic report documenting the Data Science roadmap, preprocessing, summary statistics, pivot tables, and visual interpretations.
* `visualizations/`:
  * `1_registrations_vs_attendance.png`: Bar chart comparing event enrollments against attendance.
  * `2_department_participation.png`: Donut chart showing department participation share.
  * `3_dept_event_heatmap.png`: Heatmap cross-tabulating departments vs event categories.
  * `4_year_wise_participation_boxplot.png`: Box plot showing participation by year of study.
  * `5_registration_lead_time_hist.png`: Histogram with KDE for registration lead times.
  * `6_event_category_distribution.png`: Bar chart of enrollments by event category.
* `screenshots/fds_execution_screenshot.png`: Terminal screenshot of the pipeline execution.
* `sample_inputs_outputs.txt`: Complete terminal output log of data cleaning, descriptive stats, and chart creation.

## How to Run
```bash
# Execute the complete FDS pipeline
python event_data_analysis.py
```
