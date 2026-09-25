"""Render a local PDF preview of the Overleaf-ready Computer Modern CV.

The editable source is main.tex. This preview follows its content and geometry;
pdfLaTeX in Overleaf remains the authoritative renderer for main.tex.
"""

from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.platypus import (
    HRFlowable,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "assets" / "docs" / "CV_ChendongXin.pdf"
PAGE_WIDTH, _ = A4
MARGIN_X = 52.44  # 1.85 cm, matching main.tex
MARGIN_Y = 42.52  # 1.50 cm
WIDTH = PAGE_WIDTH - 2 * MARGIN_X
INDENT = 14.17   # 0.50 cm
BLUE = "#0000cc"
ROW_WIDTH = WIDTH - 26  # include Platypus frame padding, then indent 0.5 cm
PUB_WIDTH = WIDTH - 38  # number at +26 pt, text at +40 pt

pdfmetrics.registerFontFamily(
    "Times-Roman", normal="Times-Roman", bold="Times-Bold",
    italic="Times-Italic", boldItalic="Times-BoldItalic",
)


NAME = ParagraphStyle(
    "name", fontName="Times-Bold", fontSize=18.5, leading=22,
    alignment=TA_CENTER,
)
CONTACT = ParagraphStyle(
    "contact", fontName="Times-Roman", fontSize=10.7, leading=13,
    alignment=TA_CENTER,
)
BODY = ParagraphStyle(
    "body", fontName="Times-Roman", fontSize=10.7, leading=13,
    alignment=TA_LEFT,
)
BODY_INDENT = ParagraphStyle("body_indent", parent=BODY, leftIndent=INDENT)
DATE = ParagraphStyle("date", parent=BODY, alignment=TA_RIGHT)
ROLE = ParagraphStyle("role", parent=BODY, fontName="Times-Italic")
ROLE_RIGHT = ParagraphStyle("role_right", parent=ROLE, alignment=TA_RIGHT)
SECTION = ParagraphStyle(
    "section", fontName="Times-Bold", fontSize=11, leading=13,
)
NUMBER = ParagraphStyle("number", parent=BODY)


def para(content, style=BODY):
    return Paragraph(content, style)


def table(rows, widths, align="LEFT"):
    result = Table(rows, colWidths=widths, hAlign=align)
    result.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
    ]))
    return result


def section(label):
    return [
        Spacer(1, 9), para(label, SECTION), Spacer(1, 2),
        HRFlowable(width="100%", thickness=0.4, color=colors.black),
        Spacer(1, 5),
    ]


def education(school, date, degree):
    return [
        table([
            [para(f"<b>{school}</b>"), para(date, DATE)],
            [para(f"<i>{degree}</i>"), ""],
        ], [ROW_WIDTH - 125, 125], "RIGHT"),
        Spacer(1, 5),
    ]


def paper(number, content):
    return [
        table([[para(f"{number}.", NUMBER), para(content)]],
              [14, PUB_WIDTH - 14], "RIGHT"),
        Spacer(1, 6),
    ]


def experience(org, date, role, location):
    return [
        table([
            [para(f"<b>{org}</b>"), para(date, DATE)],
            [para(role, ROLE), para(location, ROLE_RIGHT)],
        ], [ROW_WIDTH - 133, 133], "RIGHT"),
        Spacer(1, 8),
    ]


def award(content, date):
    return table(
        [[para(content), para(date, DATE)]],
        [ROW_WIDTH - 80, 80], "RIGHT",
    )


def activity(title, date, detail):
    return [
        table([
            [para(f"<b>{title}</b>"), para(date, DATE)],
            [para(detail), ""],
        ], [ROW_WIDTH - 80, 80], "RIGHT"),
        Spacer(1, 5),
    ]


def link(url, label="[Paper]"):
    return f'<font color="{BLUE}"><link href="{url}">{label}</link></font>'


def build():
    story = [
        para("CHENDONG XIN", NAME), Spacer(1, 6),
        para(
            link("https://star-xcd.github.io/", "https://star-xcd.github.io/")
            + " &nbsp;|&nbsp; cxin34@gatech.edu", CONTACT,
        ),
        Spacer(1, 3),
    ]

    story += section("EDUCATION")
    story += education(
        "Georgia Institute of Technology", "08/2026-now",
        "Ph.D. in Robotics, Advisor: Prof. Danfei Xu",
    )
    story += education(
        "Tsinghua University", "08/2022-06/2026",
        "Bachelor of Engineering in Automation (GPA 3.92/4.0; Rank 18/145)",
    )

    story += section("RESEARCH INTEREST")
    story.append(para(
        "My research explores how robots can learn dexterous, contact-rich "
        "manipulation from human data and physical interaction. I focus on "
        "physics-grounded robot learning, multisensory demonstrations and "
        "interventions, and full-stack systems that operate reliably in the "
        "real world.", BODY_INDENT,
    ))

    story += section("PUBLICATIONS")
    story += paper(1,
        'Xiaomeng Xu<super>*</super>, Yifan Hou<super>*</super>, '
        '<b>Chendong Xin</b>, Zeyi Liu, Shuran Song, '
        '<i>Compliant Residual DAgger: Improving Real-World Contact-Rich '
        'Manipulation with Human Corrections</i>. The International Journal '
        'of Robotics Research (IJRR 2026), Best '
        'Paper Award at the Human-to-Robot Workshop (CoRL 2025). '
        + link("https://compliant-residual-dagger.github.io/files/CR_DAgger_extended.pdf")
    )
    story += paper(2,
        '<b>Chendong Xin</b><super>*</super>, Mingrui Yu<super>*</super>, '
        'Yongpeng Jiang, Zhefeng Zhang, Xiang Li, '
        '<i>Analyzing Key Objectives in Human-to-Robot Retargeting for Dexterous '
        'Manipulation</i>. IEEE Robotics and Automation Practice (RA-P 2026). '
        + link("https://doi.org/10.1109/RAP.2026.3656110")
    )
    story.append(para("* authors with equal contribution"))

    story += section("RESEARCH EXPERIENCE")
    story += experience(
        "Stanford University, REALab", "06/2025-09/2025",
        "Undergraduate Visiting Researcher, Advisor: Prof. Shuran Song", "Stanford, CA",
    )
    story += experience(
        "Tsinghua University, Intelligent Robotic Manipulation Lab", "2023-2026",
        "Research Assistant, Advisor: Prof. Xiang Li", "Beijing, China",
    )

    story += section("ACTIVITIES")
    story += activity(
        "ICRA 2025 Robotic Grasping and Manipulation Competition (RGMC)", "05/2025",
        "Team Leader, Picking-in-Clutter Track (1st Place). "
        "<i>Hybrid Gripper and Adaptive Strategy for Robust Grasping in Clutter: "
        "RGMC Champion Solution</i>. "
        + link("https://drive.google.com/file/d/1JeVUZnuA85vtoRfEPpvAHd7XtUSx0bg3/view", "[Workshop Paper]"),
    )
    story += activity(
        "FIRST Robotics Competition, Team 6907", "2019-2023",
        "Team Member and Mentor",
    )

    story += section("AWARDS")
    story += [
        award("Outstanding Graduate and Outstanding Bachelor's Thesis, Tsinghua University", "06/2026"),
        award("Best Paper Award, Human-to-Robot Workshop (CoRL 2025)", "09/2025"),
        award("1st Place, ICRA RGMC Picking-in-Clutter Track (team leader)", "05/2025"),
        award("HanDe Scholarship, Tsinghua University (ranked 4/145)", "2024"),
    ]

    story += section("TECHNICAL SKILLS")
    story.append(table([
        [para("<b>Computer Languages</b>"), para("Python, C/C++, MATLAB, Verilog")],
        [para("<b>Tools</b>"), para("PyTorch, ROS/ROS2, Git, SolidWorks, Multisim")],
        [para("<b>Robot Platforms</b>"), para("UR5/UR5e, Franka Emika Panda, LEAP Hand")],
    ], [138, ROW_WIDTH - 138], "RIGHT"))

    doc = SimpleDocTemplate(
        str(OUTPUT), pagesize=A4,
        leftMargin=MARGIN_X, rightMargin=MARGIN_X,
        topMargin=MARGIN_Y, bottomMargin=MARGIN_Y,
        title="Chendong Xin - Curriculum Vitae", author="Chendong Xin",
    )
    doc.build(story)
    print(OUTPUT)


if __name__ == "__main__":
    build()
