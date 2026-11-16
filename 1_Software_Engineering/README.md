# 1. Software Engineering (25ITT33)

This folder contains the Software Engineering documentation, analysis models, architecture diagrams, and testing deliverables for the **Smart Campus Event Management and Student Participation Analysis System** (Scenario 6) aligned with syllabus **25ITT33 - Software Engineering**.

## Deliverables in this Directory
* `SRS_Document.md`: Complete Software Requirements Specification compliant with the IEEE Std 830-1998 standard, detailing product scope, functional and non-functional requirements, Agile development lifecycle, project estimation (COCOMO & FP), and embedded design diagrams.
* `Testing_Document.md`: Comprehensive testing report detailing verification & validation, cyclomatic complexity white-box analysis, boundary value analysis, test case matrix with sample inputs/outputs, and test metrics.
* `diagrams/`: Contains high-resolution PNG images for 7 architectural and design diagrams:
  1. `1_use_case_diagram.png`: UML Use Case Diagram with actors, use cases, include/extend relationships.
  2. `2_dfd_level_0.png`: DFD Level 0 Context Diagram.
  3. `3_dfd_level_1.png`: DFD Level 1 Detailed Decomposition with 5 processes and 4 data stores.
  4. `4_system_architecture.png`: Multi-Tier System Architecture Diagram (Presentation, Business, Data Access, Database/Analytics).
  5. `5_class_diagram.png`: UML Class Diagram detailing model, DAO, and service structure.
  6. `6_sequence_diagram.png`: UML Sequence Diagram illustrating student registration and duplicate validation flow.
  7. `7_activity_diagram.png`: UML Activity Diagram showing participation and attendance lifecycle.

## Requirements Traceability
All 6 Functional Requirements from the problem statement are formally specified in `SRS_Document.md` and validated in `Testing_Document.md`.
