# ==============================================================================
# VELALAR COLLEGE OF ENGINEERING AND TECHNOLOGY (AUTONOMOUS), ERODE - 12
# DEPARTMENT OF INFORMATION TECHNOLOGY
# HIGH-RESOLUTION ENTERPRISE ARCHITECTURE & DESIGN DIAGRAM GENERATOR
# Produces stunning, modern, publication-grade diagrams with card elevations,
# vibrant palette, clean typography, badge pills, and visual hierarchy.
# ==============================================================================

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.path import Path
import os

os.makedirs("1_Software_Engineering/diagrams", exist_ok=True)
os.makedirs("2_Database_Management_System/diagrams", exist_ok=True)

# ------------------------------------------------------------------------------
# CORE STYLING & DRAWING HELPERS
# ------------------------------------------------------------------------------
def create_canvas(title, subtitle="", category="SOFTWARE ENGINEERING ARCHITECTURE", figsize=(15, 10.5), bg="#0B132B"):
    fig, ax = plt.subplots(figsize=figsize, dpi=300)
    fig.patch.set_facecolor(bg)
    ax.set_facecolor(bg)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    # Top Institutional Header Banner
    header_box = patches.FancyBboxPatch((4, 91), 92, 7.5, boxstyle="round,pad=0.5", ec="#1E293B", fc="#1C2541", lw=1.5)
    ax.add_patch(header_box)
    
    # Category Tag Badge
    tag_box = patches.FancyBboxPatch((6, 95), 24, 2.2, boxstyle="round,pad=0.2", ec="#3B82F6", fc="#2563EB", lw=1)
    ax.add_patch(tag_box)
    ax.text(18, 96.1, category, fontsize=7.5, fontweight='bold', color="#FFFFFF", ha='center', va='center')

    # Title & Subtitle
    ax.text(50, 95.2, title, fontsize=13, fontweight='black', color="#F8FAFC", ha='center', va='center')
    if subtitle:
        ax.text(50, 92.5, subtitle, fontsize=9, fontstyle='italic', color="#94A3B8", ha='center', va='center')

    # Watermark / Meta Footer
    ax.text(50, 1.8, "Velalar College of Engineering and Technology (Autonomous) | Department of Information Technology | AY 2026-27 (ODD)",
            fontsize=7.5, color="#64748B", ha='center', va='center', fontweight='bold')
    
    return fig, ax

def draw_shadow_card(ax, x, y, w, h, ec="#38BDF8", fc="#1E293B", header_color="#0284C7", title="", radius=0.6):
    # Shadow offset
    shadow = patches.FancyBboxPatch((x + 0.4, y - 0.4), w, h, boxstyle=f"round,pad={radius}", ec="none", fc="#000000", alpha=0.35)
    ax.add_patch(shadow)
    # Main Card Body
    card = patches.FancyBboxPatch((x, y), w, h, boxstyle=f"round,pad={radius}", ec=ec, fc=fc, lw=1.6)
    ax.add_patch(card)
    # Header Banner if title present
    if title:
        header_h = min(2.8, h * 0.3)
        h_box = patches.FancyBboxPatch((x, y + h - header_h), w, header_h, boxstyle=f"round,pad={radius}", ec=header_color, fc=header_color, lw=1)
        ax.add_patch(h_box)
        ax.text(x + w / 2, y + h - header_h / 2, title, fontsize=9, fontweight='bold', color="#FFFFFF", ha='center', va='center')

def draw_pill_badge(ax, x, y, w, h, text, fc="#3B82F6", ec="#60A5FA", tc="#FFFFFF", fontsize=8):
    pill = patches.FancyBboxPatch((x - w/2, y - h/2), w, h, boxstyle="round,pad=0.3", ec=ec, fc=fc, lw=1.2)
    ax.add_patch(pill)
    ax.text(x, y, text, fontsize=fontsize, fontweight='bold', color=tc, ha='center', va='center')

def draw_curved_arrow(ax, x1, y1, x2, y2, color="#38BDF8", label="", rad=0.0, lw=1.6, ls="-"):
    connectionstyle = f"arc3,rad={rad}" if rad != 0.0 else "arc3,rad=0"
    ax.annotate(
        "", xy=(x2, y2), xytext=(x1, y1),
        arrowprops=dict(arrowstyle="-|>", color=color, lw=lw, linestyle=ls, connectionstyle=connectionstyle, mutation_scale=12)
    )
    if label:
        mid_x = (x1 + x2) / 2
        mid_y = (y1 + y2) / 2 + (rad * 8)
        lbl_box = patches.FancyBboxPatch((mid_x - len(label)*0.45, mid_y - 1.0), len(label)*0.9, 2.0,
                                         boxstyle="round,pad=0.2", ec="#475569", fc="#0F172A", lw=0.8, alpha=0.9)
        ax.add_patch(lbl_box)
        ax.text(mid_x, mid_y, label, fontsize=7.5, color="#E2E8F0", ha='center', va='center', fontweight='bold')

# ==============================================================================
# DIAGRAM 1: UML USE CASE DIAGRAM (ELEGANT ENTERPRISE REDESIGN)
# ==============================================================================
def render_use_case():
    fig, ax = create_canvas(
        "SMART CAMPUS EVENT MANAGEMENT SYSTEM - USE CASE MODEL",
        "UML Use Case Specification with Actors, Dependencies & Subsystem Boundary (Scenario 6)",
        category="UML SPECIFICATION (UNIT 2 & 3)"
    )

    # Glowing Subsystem Boundary
    sys_shadow = patches.FancyBboxPatch((24.4, 5.6), 51.2, 82.8, boxstyle="round,pad=1.2", ec="none", fc="#000000", alpha=0.4)
    ax.add_patch(sys_shadow)
    sys_bound = patches.FancyBboxPatch((24, 6), 52, 82, boxstyle="round,pad=1.2", ec="#38BDF8", fc="#0F172A", lw=2, linestyle="--")
    ax.add_patch(sys_bound)
    draw_pill_badge(ax, 50, 86, 32, 2.8, "PORTAL BOUNDARY: SMART EVENT SUITE", fc="#0369A1", ec="#38BDF8", fontsize=8.5)

    # Actor Cards Helper
    def draw_actor_card(x, y, title, role, tag, badge_col):
        draw_shadow_card(ax, x-9, y-7, 18, 14, ec=badge_col, fc="#1E293B", header_color=badge_col, title=f"[{tag}] {title}")
        ax.text(x, y + 1.5, f"Role: {role}", fontsize=8, color="#94A3B8", ha='center', fontweight='bold')
        # Avatar circle
        circ = patches.Circle((x, y - 2.8), 2.2, ec=badge_col, fc="#0F172A", lw=1.5)
        ax.add_patch(circ)
        ax.text(x, y - 2.8, tag, fontsize=10, fontweight='black', color="#F8FAFC", ha='center', va='center')

    draw_actor_card(12, 60, "Student", "Primary User", "STU", "#3B82F6")
    draw_actor_card(88, 68, "Coordinator", "Faculty Lead", "FAC", "#10B981")
    draw_actor_card(88, 28, "Data Analyst", "Administrator", "ADM", "#F59E0B")

    # Use Case Ellipses inside System Boundary
    use_cases = [
        (50, 77, "UC1: Register for Event", "#1E3A8A", "#60A5FA"),
        (50, 66, "UC2: Prevent Duplicate Reg.", "#78350F", "#FBBF24"),
        (50, 55, "UC3: View Scheduled Events", "#1E3A8A", "#60A5FA"),
        (50, 44, "UC4: Record Live Attendance", "#064E3B", "#34D399"),
        (50, 33, "UC5: Issue E-Certificate", "#78350F", "#FBBF24"),
        (50, 22, "UC6: Generate Event Reports", "#064E3B", "#34D399"),
        (50, 11, "UC7: Run FDS Analytics", "#4C1D95", "#A78BFA")
    ]

    for x, y, label, fc, ec in use_cases:
        # Ellipse with shadow
        sh = patches.Ellipse((x + 0.3, y - 0.3), 32, 6.2, ec="none", fc="#000000", alpha=0.35)
        ax.add_patch(sh)
        el = patches.Ellipse((x, y), 32, 6.2, ec=ec, fc=fc, lw=1.8)
        ax.add_patch(el)
        ax.text(x, y, label, fontsize=9, fontweight='black', color="#F8FAFC", ha='center', va='center')

    # Association Lines
    # Student associations
    ax.annotate("", xy=(34, 77), xytext=(20, 64), arrowprops=dict(arrowstyle="-", color="#60A5FA", lw=2))
    ax.annotate("", xy=(34, 55), xytext=(20, 60), arrowprops=dict(arrowstyle="-", color="#60A5FA", lw=2))

    # <<include>> Dependency UC1 -> UC2
    ax.annotate("", xy=(50, 69.2), xytext=(50, 73.8),
                arrowprops=dict(arrowstyle="-|>", color="#FBBF24", lw=1.8, linestyle="dashed", mutation_scale=12))
    draw_pill_badge(ax, 50, 71.5, 14, 1.8, "<<include>>", fc="#B45309", ec="#FCD34D", fontsize=7)

    # <<extend>> Dependency UC4 -> UC5
    ax.annotate("", xy=(50, 36.2), xytext=(50, 40.8),
                arrowprops=dict(arrowstyle="-|>", color="#34D399", lw=1.8, linestyle="dashed", mutation_scale=12))
    draw_pill_badge(ax, 50, 38.5, 14, 1.8, "<<extend>>", fc="#065F46", ec="#6EE7B7", fontsize=7)

    # Coordinator associations
    ax.annotate("", xy=(66, 77), xytext=(80, 70), arrowprops=dict(arrowstyle="-", color="#34D399", lw=2))
    ax.annotate("", xy=(66, 44), xytext=(80, 67), arrowprops=dict(arrowstyle="-", color="#34D399", lw=2))
    ax.annotate("", xy=(66, 22), xytext=(80, 64), arrowprops=dict(arrowstyle="-", color="#34D399", lw=2))

    # Analyst associations
    ax.annotate("", xy=(66, 22), xytext=(80, 30), arrowprops=dict(arrowstyle="-", color="#FBBF24", lw=2))
    ax.annotate("", xy=(66, 11), xytext=(80, 26), arrowprops=dict(arrowstyle="-", color="#FBBF24", lw=2))

    plt.tight_layout()
    out = "1_Software_Engineering/diagrams/1_use_case_diagram.png"
    plt.savefig(out, dpi=300)
    plt.close()
    print(f"[OK] Elegant Diagram 1 saved to: {out}")

# ==============================================================================
# DIAGRAM 2: DFD LEVEL 0 (CONTEXT LEVEL DIAGRAM - ELEGANT REDESIGN)
# ==============================================================================
def render_dfd_level_0():
    fig, ax = create_canvas(
        "DATA FLOW DIAGRAM (DFD) - LEVEL 0 (CONTEXT MODEL)",
        "System Information Boundary, External Entities & Primary Data Streams",
        category="REQUIREMENTS MODELING (UNIT 2)"
    )

    # Central Core Process (Glowing double circle)
    glow = patches.Circle((50, 48), 16.5, ec="#38BDF8", fc="#0284C7", alpha=0.25)
    ax.add_patch(glow)
    p_circ = patches.Circle((50, 48), 14.5, ec="#38BDF8", fc="#0F172A", lw=2.5)
    ax.add_patch(p_circ)
    
    draw_pill_badge(ax, 50, 56.5, 12, 2.2, "PROCESS 0.0", fc="#0284C7", ec="#38BDF8", fontsize=7.5)
    ax.text(50, 49, "SMART CAMPUS\nEVENT MANAGEMENT\n& ANALYTICS", fontsize=10, fontweight='black', color="#F8FAFC", ha='center', va='center')
    ax.text(50, 40.5, "(Central Application Hub)", fontsize=7.5, fontstyle='italic', color="#94A3B8", ha='center')

    # External Entities Cards
    entities = [
        (14, 70, "Student Participant", "[USER]", "#3B82F6", ["Profile Specs", "Registration Req.", "Post-Event Feedback"]),
        (14, 26, "Event Coordinator", "[FACULTY]", "#10B981", ["Event Schedule", "Capacity Quota", "Attendance Check-in"]),
        (86, 70, "Academic Dean / HOD", "[MGMT]", "#8B5CF6", ["Participation Reports", "Department Metrics", "Accreditation Data"]),
        (86, 26, "Data Analyst / Admin", "[ADMIN]", "#F59E0B", ["Analytical Queries", "Descriptive Stats", "Visual Distribution"])
    ]

    for x, y, name, tag, col, bullets in entities:
        draw_shadow_card(ax, x-10, y-9, 20, 18, ec=col, fc="#1E293B", header_color=col, title=f"{tag} {name}")
        curr_y = y + 2.5
        for b in bullets:
            ax.text(x - 8.5, curr_y, f"> {b}", fontsize=7.5, color="#E2E8F0", fontweight='bold')
            curr_y -= 2.2

    # Elegant curved data flow arrows with badges
    # Student -> System & System -> Student
    draw_curved_arrow(ax, 24, 70, 39, 57, color="#60A5FA", label="Registration Request", rad=0.08)
    draw_curved_arrow(ax, 38, 52, 24, 64, color="#38BDF8", label="Confirmation & E-Pass", rad=0.08, ls="--")

    # Coordinator -> System & System -> Coordinator
    draw_curved_arrow(ax, 24, 30, 38, 41, color="#34D399", label="Event Details & Attendance", rad=0.08)
    draw_curved_arrow(ax, 38, 38, 24, 24, color="#10B981", label="Participant Roster", rad=0.08, ls="--")

    # System -> Management
    draw_curved_arrow(ax, 62, 55, 76, 68, color="#A78BFA", label="Audit & Participation Reports", rad=-0.08)

    # Analyst <-> System
    draw_curved_arrow(ax, 76, 30, 62, 42, color="#FBBF24", label="Query Pipeline", rad=-0.08)
    draw_curved_arrow(ax, 62, 38, 76, 24, color="#F59E0B", label="Z-Scores & Visual Charts", rad=-0.08, ls="--")

    plt.tight_layout()
    out = "1_Software_Engineering/diagrams/2_dfd_level_0.png"
    plt.savefig(out, dpi=300)
    plt.close()
    print(f"[OK] Elegant Diagram 2 saved to: {out}")

# ==============================================================================
# DIAGRAM 3: DFD LEVEL 1 (DECOMPOSED PROCESS ARCHITECTURE)
# ==============================================================================
def render_dfd_level_1():
    fig, ax = create_canvas(
        "DATA FLOW DIAGRAM (DFD) - LEVEL 1 (DETAILED DECOMPOSITION)",
        "Subsystem Functional Processes, Data Store Repositories & Relational Flows",
        category="FUNCTIONAL DECOMPOSITION (UNIT 2)"
    )

    # 5 Functional Processes (Cards with numbered badge)
    processes = [
        (22, 75, "1.0", "Student Profile\nManagement", "#3B82F6", "[P1]"),
        (78, 75, "2.0", "Event Scheduling\n& Capacity Setup", "#10B981", "[P2]"),
        (50, 50, "3.0", "Registration &\nDuplicate Engine", "#F59E0B", "[P3]"),
        (22, 25, "4.0", "Attendance &\nParticipation Logger", "#06B6D4", "[P4]"),
        (78, 25, "5.0", "FDS Report &\nVisualization Engine", "#8B5CF6", "[P5]")
    ]

    for x, y, num, name, col, tag in processes:
        draw_shadow_card(ax, x-9, y-6, 18, 12, ec=col, fc="#1E293B", header_color=col, title=f"PROC {num}")
        ax.text(x, y - 1, f"{tag}\n{name}", fontsize=8.5, fontweight='bold', color="#F8FAFC", ha='center', va='center')

    # 4 Data Stores (Cylinder-like dual line boxes)
    stores = [
        (22, 50, "D1: STUDENTS_STORE", "#0284C7"),
        (78, 50, "D2: EVENTS_STORE", "#059669"),
        (50, 75, "D3: REGISTRATIONS_STORE", "#D97706"),
        (50, 25, "D4: ATTENDANCE_STORE", "#7C3AED")
    ]

    for x, y, label, col in stores:
        # Open data store symbol
        sh = patches.Rectangle((x-9.8, y-3.8), 20, 7.6, ec="none", fc="#000000", alpha=0.35)
        ax.add_patch(sh)
        box = patches.Rectangle((x-10, y-4), 20, 8, ec=col, fc="#0F172A", lw=1.8)
        ax.add_patch(box)
        # Top/bottom green bars representing store open lines
        ax.plot([x-10, x+10], [y+4, y+4], color=col, lw=3)
        ax.plot([x-10, x+10], [y-4, y-4], color=col, lw=3)
        ax.text(x, y, f"[STORE] {label}", fontsize=8, fontweight='bold', color="#F8FAFC", ha='center', va='center')

    # External Entities
    draw_shadow_card(ax, 3, 70, 10, 10, ec="#64748B", fc="#1E293B", header_color="#475569", title="Student")
    ax.text(8, 74, "STUDENT", fontsize=8, fontweight='bold', color="#FFFFFF", ha='center')

    draw_shadow_card(ax, 87, 70, 10, 10, ec="#64748B", fc="#1E293B", header_color="#475569", title="Faculty")
    ax.text(92, 74, "FACULTY", fontsize=8, fontweight='bold', color="#FFFFFF", ha='center')

    # Flow arrows
    draw_curved_arrow(ax, 13, 75, 13, 75, color="#94A3B8")
    draw_curved_arrow(ax, 22, 69, 22, 54, color="#38BDF8", label="Insert Profile")
    draw_curved_arrow(ax, 78, 69, 78, 54, color="#34D399", label="Schedule Event")
    
    # Store reads to 3.0
    draw_curved_arrow(ax, 32, 50, 41, 50, color="#38BDF8", label="Verify Student")
    draw_curved_arrow(ax, 68, 50, 59, 50, color="#34D399", label="Check Capacity")
    draw_curved_arrow(ax, 50, 56, 50, 71, color="#FBBF24", label="Commit Registration")

    # D3 to 4.0
    draw_curved_arrow(ax, 43, 71, 26, 31, color="#FBBF24", label="Roster Info")
    draw_curved_arrow(ax, 31, 25, 40, 25, color="#06B6D4", label="Checkin Log")

    # Stores to 5.0 Analytics
    draw_curved_arrow(ax, 60, 25, 69, 25, color="#A78BFA", label="Attendance Data")
    draw_curved_arrow(ax, 57, 71, 74, 31, color="#A78BFA", label="Registration Metrics")

    plt.tight_layout()
    out = "1_Software_Engineering/diagrams/3_dfd_level_1.png"
    plt.savefig(out, dpi=300)
    plt.close()
    print(f"[OK] Elegant Diagram 3 saved to: {out}")

# ==============================================================================
# DIAGRAM 4: SYSTEM ARCHITECTURE (STACKED MULTI-TIER WITH GLOW & BUS)
# ==============================================================================
def render_system_architecture():
    fig, ax = create_canvas(
        "MULTI-TIER ENTERPRISE SYSTEM ARCHITECTURE",
        "Coupling Presentation, Java Business Services, JDBC DAO Persistence & Python Data Science Warehouse",
        category="SYSTEM DESIGN & ARCHITECTURE (UNIT 3)"
    )

    layers = [
        (76, "TIER 1: PRESENTATION & CLIENT INTERACTION LAYER", [
            ("Java Interactive Console UI", "CLI Menu Terminal (Main.java)", "[UI]", "#3B82F6"),
            ("Automated Test Runner", "TestCaseRunner Suite (100% Pass)", "[TEST]", "#10B981"),
            ("FDS Analytics Dashboard", "Matplotlib / Seaborn Visualizer", "[VIZ]", "#8B5CF6"),
            ("SQL Query Shell Console", "Live SQLite Command Interface", "[CLI]", "#F59E0B")
        ], "#0369A1", "#38BDF8"),

        (54, "TIER 2: APPLICATION & BUSINESS LOGIC LAYER (Java OOP)", [
            ("EventManagementService", "Core Business Workflow & Validation", "[SRV]", "#3B82F6"),
            ("Duplicate Prevention Engine", "Unique Constraint & Exception Thrower", "[DUP]", "#EF4444"),
            ("Java Streams API Aggregator", "Department Grouping & Metrics", "[STM]", "#10B981"),
            ("Async Notification Service", "Multithreaded E-Pass Dispatcher", "[THD]", "#F59E0B")
        ], "#92400E", "#FBBF24"),

        (32, "TIER 3: PERSISTENCE & DATA ACCESS LAYER (DAO Pattern)", [
            ("StudentDAO", "CRUD & Roll Number Verification", "[DAO]", "#3B82F6"),
            ("EventDAO", "Capacity Check & Event Scheduling", "[DAO]", "#10B981"),
            ("RegistrationDAO", "Transaction Lock & Attendance Log", "[DAO]", "#F59E0B"),
            ("SQLite JDBC Driver Pool", "Version 3.45.1.0 with SLF4J Bridge", "[JDBC]", "#8B5CF6")
        ], "#065F46", "#34D399"),

        (10, "TIER 4: RELATIONAL DATABASE & SCIENTIFIC WAREHOUSE", [
            ("Relational DB: smart_campus.db", "ACID Compliant SQLite Storage Engine", "[RDB]", "#3B82F6"),
            ("Tables & Integrity Rules", "students, events, registrations, att", "[TBL]", "#10B981"),
            ("Summary Database Views", "view_event_summary (Real-time yield)", "[VIEW]", "#F59E0B"),
            ("Python FDS Analytics Pipeline", "Pandas DataFrame, NumPy, SciPy Stats", "[FDS]", "#8B5CF6")
        ], "#5B21B6", "#A78BFA")
    ]

    for y, title, components, header_col, border_col in layers:
        # Layer Container Card with Shadow
        sh = patches.FancyBboxPatch((6.4, y - 0.4), 87.2, 16.8, boxstyle="round,pad=0.8", ec="none", fc="#000000", alpha=0.35)
        ax.add_patch(sh)
        layer_box = patches.FancyBboxPatch((6, y), 88, 17, boxstyle="round,pad=0.8", ec=border_col, fc="#131D3B", lw=1.8)
        ax.add_patch(layer_box)

        # Layer Title Banner
        draw_pill_badge(ax, 50, y + 15.5, 52, 2.2, title, fc=header_col, ec=border_col, fontsize=8)

        # 4 Sub-Component Cards
        card_w = 19.5
        gap = 1.8
        start_x = 8.5
        for i, (c_name, c_desc, c_icon, c_acc) in enumerate(components):
            cx = start_x + i * (card_w + gap)
            cy = y + 1.8
            draw_shadow_card(ax, cx, cy, card_w, 10.5, ec=c_acc, fc="#1C2541", header_color=c_acc, title=f"{c_icon} {c_name}")
            ax.text(cx + card_w/2, cy + 3.5, c_desc, fontsize=7, color="#CBD5E1", ha='center', va='center', wrap=True)

    # Inter-layer Connection Buses
    for y_arrow in [73, 51, 29]:
        ax.annotate("", xy=(22, y_arrow - 4), xytext=(22, y_arrow),
                    arrowprops=dict(arrowstyle="<|-|>", color="#38BDF8", lw=2, mutation_scale=12))
        ax.annotate("", xy=(50, y_arrow - 4), xytext=(50, y_arrow),
                    arrowprops=dict(arrowstyle="<|-|>", color="#FBBF24", lw=2, mutation_scale=12))
        ax.annotate("", xy=(78, y_arrow - 4), xytext=(78, y_arrow),
                    arrowprops=dict(arrowstyle="<|-|>", color="#34D399", lw=2, mutation_scale=12))

    plt.tight_layout()
    out = "1_Software_Engineering/diagrams/4_system_architecture.png"
    plt.savefig(out, dpi=300)
    plt.close()
    print(f"[OK] Elegant Diagram 4 saved to: {out}")

# ==============================================================================
# DIAGRAM 5: UML CLASS DIAGRAM (ENTERPRISE OBJECT-ORIENTED BLUEPRINT)
# ==============================================================================
def render_class_diagram():
    fig, ax = create_canvas(
        "UML CLASS DIAGRAM - OBJECT MODEL & ARCHITECTURAL PATTERN",
        "Entities, DAO Layer, Interfaces, Exceptions & Service Orchestration (Unit 1 & 2)",
        category="STRUCTURAL DESIGN (UNIT 3)",
        figsize=(15, 11)
    )

    def draw_uml_class(x, y, w, h, class_name, stereotype, attributes, methods, header_col="#1D4ED8", border_col="#3B82F6"):
        # Shadow
        sh = patches.Rectangle((x+0.3, y-0.3), w, h, ec="none", fc="#000000", alpha=0.35)
        ax.add_patch(sh)
        # Class Box
        box = patches.Rectangle((x, y), w, h, ec=border_col, fc="#131D3B", lw=1.6)
        ax.add_patch(box)
        # Header Box
        header_h = 3.6
        h_box = patches.Rectangle((x, y + h - header_h), w, header_h, ec=border_col, fc=header_col, lw=1.2)
        ax.add_patch(h_box)
        ax.text(x + w/2, y + h - 1.2, f"<<{stereotype}>>", fontsize=7, color="#E2E8F0", ha='center')
        ax.text(x + w/2, y + h - 2.6, class_name, fontsize=9.5, fontweight='black', color="#FFFFFF", ha='center')

        # Attributes section
        attr_h = len(attributes) * 1.6 + 1.2
        ax.plot([x, x + w], [y + h - header_h - attr_h, y + h - header_h - attr_h], color=border_col, lw=1)
        curr_y = y + h - header_h - 1.4
        for a in attributes:
            ax.text(x + 0.8, curr_y, a, fontsize=7.2, color="#93C5FD", fontfamily="monospace")
            curr_y -= 1.6

        # Methods section
        curr_y = y + h - header_h - attr_h - 1.4
        for m in methods:
            ax.text(x + 0.8, curr_y, m, fontsize=7.2, color="#86EFAC", fontfamily="monospace")
            curr_y -= 1.6

    # Model Classes: Student, Event, Registration, Attendance
    draw_uml_class(5, 54, 26, 32, "Student", "Entity Model", [
        "- studentId: String",
        "- name: String",
        "- department: String",
        "- yearOfStudy: int",
        "- email: String",
        "- phone: String"
    ], [
        "+ getStudentId(): String",
        "+ getName(): String",
        "+ getDepartment(): String",
        "+ getYearOfStudy(): int",
        "+ displayProfile(): void"
    ], header_col="#1E3A8A", border_col="#3B82F6")

    draw_uml_class(69, 54, 26, 32, "Event", "Entity Model", [
        "- eventId: String",
        "- eventName: String",
        "- category: String",
        "- eventDate: LocalDate",
        "- venue: String",
        "- maxParticipants: int",
        "- status: String"
    ], [
        "+ getEventId(): String",
        "+ isFull(current): boolean",
        "+ getCategory(): String",
        "+ getMaxParticipants(): int",
        "+ getStatus(): String"
    ], header_col="#1E3A8A", border_col="#3B82F6")

    draw_uml_class(37, 52, 26, 34, "Registration", "Relationship Entity", [
        "- registrationId: int",
        "- studentId: String",
        "- eventId: String",
        "- registrationDate: Timestamp",
        "- status: String",
        "- studentName: String",
        "- attendanceStatus: String"
    ], [
        "+ getRegistrationId(): int",
        "+ getStudentId(): String",
        "+ getEventId(): String",
        "+ getStatus(): String",
        "+ isEligible(): boolean"
    ], header_col="#065F46", border_col="#10B981")

    # Lower Service & DAO Classes
    draw_uml_class(5, 8, 30, 36, "AttendanceRecord", "Entity Model", [
        "- attendanceId: int",
        "- registrationId: int",
        "- attendanceStatus: String",
        "- checkinTime: Timestamp",
        "- certificateStatus: String",
        "- remarks: String"
    ], [
        "+ markPresent(): void",
        "+ markAbsent(): void",
        "+ issueCertificate(): void",
        "+ getSummary(): String"
    ], header_col="#1E3A8A", border_col="#3B82F6")

    draw_uml_class(42, 8, 53, 36, "EventManagementService", "Business Service Layer", [
        "- studentDAO: StudentDAO",
        "- eventDAO: EventDAO",
        "- registrationDAO: RegistrationDAO",
        "- notificationThread: Thread"
    ], [
        "+ registerStudentForEvent(studId, evtId): int",
        "+ preventDuplicateRegistration(sId, eId): void",
        "+ recordAttendance(regId, status, rem): void",
        "+ displayEventReport(eventId): void",
        "+ getDepartmentRegistrationSummary(): Map",
        "+ sendAsyncNotification(sId, email, evt): void"
    ], header_col="#92400E", border_col="#F59E0B")

    # Associations & Multiplicity annotations
    # Student (1) --- (0..*) Registration
    ax.plot([31, 37], [70, 70], color="#94A3B8", lw=2)
    ax.text(32, 71.5, "1", color="#F8FAFC", fontsize=8.5, fontweight='bold')
    ax.text(35.2, 71.5, "0..*", color="#F8FAFC", fontsize=8.5, fontweight='bold')

    # Event (1) --- (0..*) Registration
    ax.plot([63, 69], [70, 70], color="#94A3B8", lw=2)
    ax.text(64, 71.5, "0..*", color="#F8FAFC", fontsize=8.5, fontweight='bold')
    ax.text(67.5, 71.5, "1", color="#F8FAFC", fontsize=8.5, fontweight='bold')

    # Registration (1) --- (1) Attendance
    ax.plot([45, 45, 20, 20], [52, 46, 46, 44], color="#94A3B8", lw=2)
    ax.text(46, 48, "1", color="#F8FAFC", fontsize=8.5, fontweight='bold')
    ax.text(21, 45, "1", color="#F8FAFC", fontsize=8.5, fontweight='bold')

    # Dependency dashed arrow Service to Registration
    ax.annotate("", xy=(50, 52), xytext=(50, 44),
                arrowprops=dict(arrowstyle="-|>", color="#F59E0B", lw=1.8, linestyle="dashed", mutation_scale=12))

    plt.tight_layout()
    out = "1_Software_Engineering/diagrams/5_class_diagram.png"
    plt.savefig(out, dpi=300)
    plt.close()
    print(f"[OK] Elegant Diagram 5 saved to: {out}")

# ==============================================================================
# DIAGRAM 6: UML SEQUENCE DIAGRAM (DYNAMIC CALL LIFELINE FLOW)
# ==============================================================================
def render_sequence_diagram():
    fig, ax = create_canvas(
        "UML SEQUENCE DIAGRAM - REGISTRATION & DUPLICATE CHECK FLOW",
        "Synchronous Messages, Alternate Control Fragments, Return Signatures & Asynchronous Threading (FR3)",
        category="DYNAMIC BEHAVIOR MODEL (UNIT 3)"
    )

    lifelines = [
        (14, "Student\n(Client)", "[STU]", "#3B82F6"),
        (38, "Main / CLI\n(Boundary)", "[CLI]", "#10B981"),
        (62, "EventService\n(Controller)", "[SRV]", "#F59E0B"),
        (86, "SQLite Database\n(Entity / Store)", "[DB]", "#8B5CF6")
    ]

    for x, name, tag, col in lifelines:
        draw_shadow_card(ax, x-9, 78, 18, 9, ec=col, fc="#1E293B", header_color=col, title=f"{tag} {name.split()[0]}")
        ax.text(x, 80.5, name, fontsize=7.5, color="#FFFFFF", ha='center', fontweight='bold')
        # Vertical Lifeline (Dashed line)
        ax.plot([x, x], [78, 8], color="#475569", lw=1.5, linestyle="--")

    # Sequence Messages with activation bars
    messages = [
        (14, 38, 73, "1: selectEvent('EVT101', '25IT001')", "#38BDF8", False),
        (38, 62, 67, "2: registerForEvent('25IT001', 'EVT101')", "#38BDF8", False),
        (62, 86, 61, "3: SELECT COUNT(*) FROM registrations WHERE...", "#94A3B8", False),
        (86, 62, 55, "4: Returns existing_count = 1", "#10B981", True),
        
        # Branch 1 Label
        (62, 62, 49, "[ALT 1: Duplicate Exists (count > 0)]", "#EF4444", False),
        (62, 38, 44, "5a: throw DuplicateRegistrationException", "#EF4444", True),
        (38, 14, 39, "6a: Show Error: 'Duplicate Registration Blocked!'", "#EF4444", False),
        
        # Branch 2 Label
        (62, 62, 33, "[ALT 2: Valid Registration (count == 0 & Space Avail)]", "#10B981", False),
        (62, 86, 28, "5b: INSERT INTO registrations VALUES(...)", "#34D399", False),
        (86, 62, 22, "6b: Return generated_id (#51)", "#34D399", True),
        (62, 38, 17, "7b: Return Success & Trigger AsyncNotifier Daemon", "#F59E0B", True),
        (38, 14, 12, "8b: Display Pass Confirmation & Details", "#38BDF8", False)
    ]

    for x1, x2, y, text, col, is_ret in messages:
        if x1 == x2:
            draw_pill_badge(ax, x1, y, 38, 2.2, text, fc="#1E293B", ec=col, tc=col, fontsize=7.5)
        else:
            ls = "--" if is_ret else "-"
            ax.annotate("", xy=(x2, y), xytext=(x1, y),
                        arrowprops=dict(arrowstyle="-|>", color=col, lw=1.6, linestyle=ls, mutation_scale=10))
            mid_x = (x1 + x2) / 2
            ax.text(mid_x, y + 1.2, text, fontsize=7.2, color="#F8FAFC", ha='center', fontweight='bold')

    plt.tight_layout()
    out = "1_Software_Engineering/diagrams/6_sequence_diagram.png"
    plt.savefig(out, dpi=300)
    plt.close()
    print(f"[OK] Elegant Diagram 6 saved to: {out}")

# ==============================================================================
# DIAGRAM 7: UML ACTIVITY DIAGRAM (STUDENT LIFECYCLE WORKFLOW)
# ==============================================================================
def render_activity_diagram():
    fig, ax = create_canvas(
        "UML ACTIVITY DIAGRAM - PARTICIPATION & ATTENDANCE PIPELINE",
        "Control Flow, Decision Logic Nodes, Exception Branches & Institutional Reporting (FR1-FR5)",
        category="PROCESS WORKFLOW MODEL (UNIT 3)"
    )

    # Start Node
    sh_st = patches.Circle((50.2, 87.8), 2.2, ec="none", fc="#000000", alpha=0.35)
    ax.add_patch(sh_st)
    start_c = patches.Circle((50, 88), 2.0, ec="#38BDF8", fc="#0284C7", lw=2)
    ax.add_patch(start_c)
    ax.text(50, 90.6, "START", fontsize=7.5, fontweight='black', color="#38BDF8", ha='center')

    def draw_action_box(x, y, w, h, text, fc="#1E293B", ec="#38BDF8"):
        draw_shadow_card(ax, x - w/2, y - h/2, w, h, ec=ec, fc=fc, header_color=ec)
        ax.text(x, y, text, fontsize=8, fontweight='bold', color="#F8FAFC", ha='center', va='center')

    def draw_decision_diamond(x, y, text):
        sh = patches.Polygon([[x+0.2, y+3.3], [x+6.2, y-0.2], [x+0.2, y-3.7], [x-5.8, y-0.2]], ec="none", fc="#000000", alpha=0.35)
        ax.add_patch(sh)
        dia = patches.Polygon([[x, y+3.5], [x+6, y], [x, y-3.5], [x-6, y]], ec="#F59E0B", fc="#78350F", lw=1.8)
        ax.add_patch(dia)
        ax.text(x, y, text, fontsize=7, fontweight='black', color="#FDE68A", ha='center', va='center')

    # Activity Actions
    draw_action_box(50, 80, 32, 4.8, "Browse Active Campus Events Catalog", ec="#3B82F6")
    draw_action_box(50, 71, 32, 4.8, "Select Event & Submit Roll Number", ec="#3B82F6")
    
    draw_decision_diamond(50, 61, "Duplicate?")
    draw_action_box(82, 61, 24, 4.8, "Reject: Duplicate Exception", fc="#450A0A", ec="#EF4444")
    
    draw_decision_diamond(50, 50, "Full?")
    draw_action_box(82, 50, 24, 4.8, "Reject: Capacity Reached", fc="#450A0A", ec="#EF4444")

    draw_action_box(50, 39, 32, 4.8, "Confirm Enrollment & Dispatch E-Pass", ec="#10B981")
    draw_action_box(50, 29, 32, 4.8, "On Event Day: Student Check-in", ec="#06B6D4")

    draw_decision_diamond(50, 19, "Present?")
    draw_action_box(20, 19, 22, 4.8, "Mark Absent (No Cert)", fc="#1E293B", ec="#94A3B8")
    draw_action_box(50, 9, 34, 4.8, "Mark Present & Auto-Issue E-Certificate", ec="#10B981")

    # End Node (Bullseye)
    sh_end = patches.Circle((82.2, 38.8), 2.5, ec="none", fc="#000000", alpha=0.35)
    ax.add_patch(sh_end)
    end_out = patches.Circle((82, 39), 2.5, ec="#EF4444", fc="none", lw=2)
    end_in = patches.Circle((82, 39), 1.6, ec="none", fc="#EF4444")
    ax.add_patch(end_out)
    ax.add_patch(end_in)
    ax.text(82, 35.5, "TERMINATE", fontsize=7, fontweight='bold', color="#EF4444", ha='center')

    # Flow Connectors with Labels
    draw_curved_arrow(ax, 50, 86, 50, 82.4, color="#38BDF8")
    draw_curved_arrow(ax, 50, 77.6, 50, 73.4, color="#38BDF8")
    draw_curved_arrow(ax, 50, 68.6, 50, 64.5, color="#38BDF8")

    # Decision 1 Duplicate -> Yes / No
    draw_curved_arrow(ax, 56, 61, 70, 61, color="#EF4444", label="[Yes]")
    draw_curved_arrow(ax, 82, 58.6, 82, 41.5, color="#EF4444")
    draw_curved_arrow(ax, 50, 57.5, 50, 53.5, color="#34D399", label="[No]")

    # Decision 2 Full -> Yes / No
    draw_curved_arrow(ax, 56, 50, 70, 50, color="#EF4444", label="[Yes]")
    draw_curved_arrow(ax, 82, 47.6, 82, 41.5, color="#EF4444")
    draw_curved_arrow(ax, 50, 46.5, 50, 41.4, color="#34D399", label="[No]")

    # Flow down to check-in
    draw_curved_arrow(ax, 50, 36.6, 50, 31.4, color="#34D399")
    draw_curved_arrow(ax, 50, 26.6, 50, 22.5, color="#34D399")

    # Decision 3 Present -> Yes / No
    draw_curved_arrow(ax, 44, 19, 31, 19, color="#94A3B8", label="[No]")
    draw_curved_arrow(ax, 50, 15.5, 50, 11.4, color="#34D399", label="[Yes]")

    plt.tight_layout()
    out = "1_Software_Engineering/diagrams/7_activity_diagram.png"
    plt.savefig(out, dpi=300)
    plt.close()
    print(f"[OK] Elegant Diagram 7 saved to: {out}")

# ==============================================================================
# DIAGRAM 8: ENTITY-RELATIONSHIP (ER) DIAGRAM (DBMS SPECIFICATION)
# ==============================================================================
def render_er_diagram():
    fig, ax = create_canvas(
        "ENTITY-RELATIONSHIP (ER) RELATIONAL ARCHITECTURE MODEL",
        "Conceptual ER Schema with Primary Keys, Foreign Key Cardinalities & Referential Integrity (25ITT31)",
        category="DATABASE MODELING & NORMALIZATION (UNIT 2 & 3)"
    )

    def draw_entity_table(x, y, w, h, table_name, pk_list, attr_list, col="#3B82F6"):
        # Shadow
        sh = patches.FancyBboxPatch((x+0.3, y-0.3), w, h, boxstyle="round,pad=0.5", ec="none", fc="#000000", alpha=0.35)
        ax.add_patch(sh)
        # Entity Card Box
        card = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.5", ec=col, fc="#131D3B", lw=1.8)
        ax.add_patch(card)
        # Table Header Banner
        header_h = 3.4
        h_box = patches.FancyBboxPatch((x, y + h - header_h), w, header_h, boxstyle="round,pad=0.5", ec=col, fc=col, lw=1)
        ax.add_patch(h_box)
        ax.text(x + w/2, y + h - header_h/2, f"ENTITY: {table_name}", fontsize=9, fontweight='black', color="#FFFFFF", ha='center', va='center')

        # Primary Key Row
        curr_y = y + h - header_h - 1.8
        for pk in pk_list:
            ax.text(x + 0.8, curr_y, f"[PK] {pk}", fontsize=7.5, fontweight='bold', color="#FCD34D", fontfamily="monospace")
            curr_y -= 1.8

        # Divider
        ax.plot([x, x + w], [curr_y + 0.6, curr_y + 0.6], color="#334155", lw=1)
        curr_y -= 0.8

        # Attributes
        for a in attr_list:
            ax.text(x + 0.8, curr_y, f"• {a}", fontsize=7.2, color="#E2E8F0", fontfamily="monospace")
            curr_y -= 1.8

    def draw_relationship_diamond(x, y, w, h, text, col="#F59E0B"):
        sh = patches.Polygon([[x+0.2, y+h/2-0.2], [x+w/2+0.2, y-0.2], [x+0.2, y-h/2-0.2], [x-w/2+0.2, y-0.2]],
                             ec="none", fc="#000000", alpha=0.35)
        ax.add_patch(sh)
        dia = patches.Polygon([[x, y+h/2], [x+w/2, y], [x, y-h/2], [x-w/2, y]], ec=col, fc="#78350F", lw=1.8)
        ax.add_patch(dia)
        ax.text(x, y, text, fontsize=7.5, fontweight='black', color="#FDE68A", ha='center', va='center')

    # Draw the 5 Normalized Relational Entities
    draw_entity_table(5, 52, 26, 30, "STUDENTS", ["student_id: VARCHAR(15)"], [
        "name: VARCHAR(100)",
        "department: VARCHAR(50)",
        "year_of_study: INT(1-4)",
        "email: VARCHAR(100) [UNQ]",
        "phone: VARCHAR(15)",
        "created_at: TIMESTAMP"
    ], col="#3B82F6")

    draw_entity_table(69, 52, 26, 30, "EVENTS", ["event_id: VARCHAR(15)"], [
        "event_name: VARCHAR(150)",
        "category: VARCHAR(50)",
        "event_date: DATE",
        "venue: VARCHAR(100)",
        "max_participants: INT",
        "organizer_dept: VARCHAR",
        "status: VARCHAR(20)"
    ], col="#10B981")

    draw_entity_table(37, 46, 26, 34, "REGISTRATIONS", ["registration_id: INT [PK]"], [
        "student_id: VARCHAR* [FK]",
        "event_id: VARCHAR* [FK]",
        "registration_date: TIME",
        "status: VARCHAR(20)",
        "----------------------",
        "CONSTRAINT [UNIQUE]:",
        "(student_id, event_id)",
        "-> PREVENTS DUPLICATE!"
    ], col="#F59E0B")

    draw_entity_table(5, 8, 28, 30, "ATTENDANCE", ["attendance_id: INT [PK]"], [
        "registration_id: INT* [FK]",
        "attendance_status: VARCHAR",
        "checkin_time: TIMESTAMP",
        "certificate_status: VARCHAR",
        "remarks: VARCHAR(255)"
    ], col="#06B6D4")

    draw_entity_table(67, 8, 28, 30, "EVENT_FEEDBACK", ["feedback_id: INT [PK]"], [
        "registration_id: INT* [FK]",
        "rating: INT (1 to 5)",
        "comments: TEXT",
        "submitted_at: TIMESTAMP"
    ], col="#8B5CF6")

    # Relationship Diamonds
    draw_relationship_diamond(34, 66, 12, 6, "REGISTERS\n(1 : N)")
    draw_relationship_diamond(66, 66, 12, 6, "ENROLLS\n(1 : N)")
    draw_relationship_diamond(34, 25, 12, 6, "LOGS\n(1 : 1)")
    draw_relationship_diamond(66, 25, 12, 6, "PROVIDES\n(1 : 0..1)")

    # Connectors with cardinalities
    # STUDENTS --- REGISTERS --- REGISTRATIONS
    ax.plot([31, 34], [66, 66], color="#38BDF8", lw=2)
    ax.plot([34, 37], [66, 66], color="#F59E0B", lw=2)
    draw_pill_badge(ax, 32, 68, 5, 1.6, "1", fc="#0284C7", ec="#38BDF8", fontsize=7)
    draw_pill_badge(ax, 36, 68, 5, 1.6, "N", fc="#B45309", ec="#F59E0B", fontsize=7)

    # EVENTS --- ENROLLS --- REGISTRATIONS
    ax.plot([69, 66], [66, 66], color="#34D399", lw=2)
    ax.plot([66, 63], [66, 66], color="#F59E0B", lw=2)
    draw_pill_badge(ax, 68, 68, 5, 1.6, "1", fc="#047857", ec="#34D399", fontsize=7)
    draw_pill_badge(ax, 64, 68, 5, 1.6, "N", fc="#B45309", ec="#F59E0B", fontsize=7)

    # REGISTRATIONS --- LOGS --- ATTENDANCE
    ax.plot([45, 34], [46, 25], color="#F59E0B", lw=2)
    ax.plot([34, 33], [25, 25], color="#06B6D4", lw=2)
    draw_pill_badge(ax, 43, 40, 5, 1.6, "1", fc="#B45309", ec="#F59E0B", fontsize=7)
    draw_pill_badge(ax, 35, 22, 5, 1.6, "1", fc="#0891B2", ec="#06B6D4", fontsize=7)

    # REGISTRATIONS --- PROVIDES --- FEEDBACK
    ax.plot([55, 66], [46, 25], color="#F59E0B", lw=2)
    ax.plot([66, 67], [25, 25], color="#8B5CF6", lw=2)
    draw_pill_badge(ax, 57, 40, 5, 1.6, "1", fc="#B45309", ec="#F59E0B", fontsize=7)
    draw_pill_badge(ax, 65, 22, 8, 1.6, "0..1", fc="#6D28D9", ec="#8B5CF6", fontsize=7)

    plt.tight_layout()
    out = "2_Database_Management_System/diagrams/er_diagram.png"
    plt.savefig(out, dpi=300)
    plt.close()
    print(f"[OK] Elegant Diagram 8 saved to: {out}")

if __name__ == "__main__":
    print("=" * 80)
    print(" GENERATING 8 HIGH-RESOLUTION ELEGANT ENTERPRISE DIAGRAMS")
    print("=" * 80)
    render_use_case()
    render_dfd_level_0()
    render_dfd_level_1()
    render_system_architecture()
    render_class_diagram()
    render_sequence_diagram()
    render_activity_diagram()
    render_er_diagram()
    print("=" * 80)
    print(" ALL 8 ELEGANT DIAGRAMS GENERATED & REPLACED SUCCESSFULLY!")
    print("=" * 80)
