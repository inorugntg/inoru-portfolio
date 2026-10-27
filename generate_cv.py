import os
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, HRFlowable
from reportlab.pdfgen import canvas

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            # You can add page numbers if desired, but user's sample has no page numbers
            super().showPage()
        super().save()

def create_cv(output_path):
    # A4 dimensions: 595.27 x 841.89 points
    # Margins: 36pt top/bottom (0.5 in), 46pt left/right (0.64 in)
    doc = SimpleDocTemplate(
        output_path,
        pagesize=A4,
        leftMargin=44,
        rightMargin=44,
        topMargin=36,
        bottomMargin=36
    )

    styles = getSampleStyleSheet()

    # Custom Black & White ATS Styles in Times New Roman
    header_name = ParagraphStyle(
        'HeaderName',
        fontName='Times-Bold',
        fontSize=15.5,
        leading=18,
        alignment=1, # Center
        textColor=colors.black,
        spaceAfter=2
    )

    header_sub = ParagraphStyle(
        'HeaderSub',
        fontName='Times-Bold',
        fontSize=11.5,
        leading=14,
        alignment=1, # Center
        textColor=colors.black,
        spaceAfter=3
    )

    header_contact = ParagraphStyle(
        'HeaderContact',
        fontName='Times-Roman',
        fontSize=10.5,
        leading=13.5,
        alignment=1, # Center
        textColor=colors.black,
        spaceAfter=2
    )

    header_links = ParagraphStyle(
        'HeaderLinks',
        fontName='Times-Roman',
        fontSize=10.5,
        leading=13.5,
        alignment=1, # Center
        textColor=colors.black,
        spaceAfter=8
    )

    section_heading = ParagraphStyle(
        'SectionHeading',
        fontName='Times-Bold',
        fontSize=11.5,
        leading=14,
        textColor=colors.black,
        spaceBefore=7,
        spaceAfter=2,
        keepWithNext=True
    )

    body_text = ParagraphStyle(
        'BodyTextCustom',
        fontName='Times-Roman',
        fontSize=10.5,
        leading=13.2,
        alignment=4, # Justified
        textColor=colors.black,
        spaceAfter=5
    )

    job_title = ParagraphStyle(
        'JobTitle',
        fontName='Times-Roman',
        fontSize=10.5,
        leading=13.5,
        textColor=colors.black,
        spaceBefore=4,
        spaceAfter=2.5,
        keepWithNext=True
    )

    bullet_style = ParagraphStyle(
        'BulletCustom',
        fontName='Times-Roman',
        fontSize=10.2,
        leading=12.8,
        alignment=4, # Justified
        leftIndent=14,
        firstLineIndent=-14,
        textColor=colors.black,
        spaceAfter=2.6
    )

    project_title_style = ParagraphStyle(
        'ProjectTitle',
        fontName='Times-Bold',
        fontSize=11,
        leading=13.8,
        textColor=colors.black,
        spaceBefore=4,
        spaceAfter=2,
        keepWithNext=True
    )

    project_desc_style = ParagraphStyle(
        'ProjectDesc',
        fontName='Times-Roman',
        fontSize=10.5,
        leading=13.2,
        alignment=4,
        textColor=colors.black,
        spaceAfter=2
    )

    project_meta_style = ParagraphStyle(
        'ProjectMeta',
        fontName='Times-Roman',
        fontSize=10.5,
        leading=13.2,
        textColor=colors.black,
        spaceAfter=2
    )

    skills_style = ParagraphStyle(
        'SkillsStyle',
        fontName='Times-Roman',
        fontSize=10.5,
        leading=13.5,
        textColor=colors.black,
        spaceAfter=3.2
    )

    story = []

    # ==================== PAGE 1 ====================
    # Header
    story.append(Paragraph("INORU AKHMAD", header_name))
    story.append(Paragraph("FULL STACK WEB DEVELOPER", header_sub))
    story.append(Paragraph("Surabaya, Indonesia | +62 899-4580-104 | inoru375@gmail.com", header_contact))
    story.append(Paragraph(
        '<a href="https://linkedin.com/in/inoru-akhmad-5082b0270"><u>LinkedIn</u></a> | '
        '<a href="https://github.com/inorugntg"><u>GitHub</u></a> | '
        '<a href="https://inoru-portfolio.vercel.app"><u>Portfolio</u></a>',
        header_links
    ))

    # Professional Summary
    story.append(Paragraph("PROFESSIONAL SUMMARY", section_heading))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.black, spaceBefore=1, spaceAfter=4))
    story.append(Paragraph(
        "Full Stack Web Developer with a Software Engineering background and currently pursuing a Bachelor's degree in Information Systems. "
        "Experienced in building REST APIs, backend architecture, and modern responsive web interfaces using React, Next.js, Laravel, Node.js, and PostgreSQL. "
        "Focused on efficient APIs, secure authentication, automated testing (Jest, Vitest, Playwright), SonarQube Quality Gate compliance, "
        "multi-layer security audits (SAST, Nmap, Katana, Nuclei), Core Web Vitals, and database query optimization.",
        body_text
    ))

    # Professional Experience
    story.append(Paragraph("PROFESSIONAL EXPERIENCE", section_heading))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.black, spaceBefore=1, spaceAfter=4))

    # Sobat UMKM Pro
    story.append(Paragraph(
        "<b>Sobat UMKM Pro — Sidoarjo</b> | <b>IT Operational (Intern)</b> | August 2026 – Present",
        job_title
    ))
    exp1_bullets = [
        "Develop UI/UX and backend for ProMaP (Project Management Platform) using Next.js 14/15 (App Router), Tailwind CSS, shadcn/ui, Prisma ORM, and PostgreSQL (Neon), deployed in production on Hostinger VPS with Nginx reverse proxy.",
        "Design and implement REST APIs with JWT authentication, 4-level RBAC (Super Admin, Operational Admin, Manager, PIC), and multi-tenant data isolation per company.",
        "Optimize application performance and database queries using Server Components, precise Prisma selects, caching (unstable_cache + revalidateTag), dynamic imports, and Suspense to reduce First Load JS and prevent N+1 queries.",
        "Build Randumart e-commerce business features including automatic rating and reviewCount increments after PAID orders, automatic stock decrement, and dynamic promotional banners with countdown timers.",
        "Implement an order state machine (PENDING → MENUNGGU_BAYAR → PAID → PROCESSING → SHIPPED → COMPLETED) with flexible transition validation.",
        "Integrate the frontend with REST APIs using Axios and NextAuth (Google SSO + Credentials), while implementing on-page SEO and Core Web Vitals improvements.",
        "Conduct Static Application Security Testing (SAST) using SonarQube and Jest/Vitest unit testing framework generating LCOV coverage reports, resolving accessibility (S1082) and sorting issues (S2871), boosting coverage from 9.6% to 58.4% with 0 security/reliability issues, 190/190 business tests passed (100%), and achieving Quality Gate PASSED status.",
        "Perform vulnerability assessments (npm audit) to mitigate 16 package vulnerabilities (ranging from Moderate to Critical/RCE) across dependencies, remediating body-parser DoS (CVE-2026-111181), zod memory exhaustion (CVE-2023-54404), and fast-uri spoofing (CVE-2026-110306) to achieve 0 vulnerabilities, implementing strict TLS/SSL database connection rules and host whitelisting to prevent SSRF.",
        "Execute Automated E2E Testing using Playwright across 13 core application modules—including authentication, RBAC management, Kanban board, Gantt chart calendar, and analytics dashboards—achieving a 100% test pass rate.",
        "Conduct Penetration & Network Security Testing using Nmap (verifying open web ports 80/443 under Nginx while database ports 3306/5432, SSH 22, and Redis 6379 are filtered), Katana Engine (mapping 35 routes/endpoints and validating middleware session redirects), Nuclei Scanner (evaluating ModSecurity WAF & hCDN resilience), and DevTools audit (enforcing HSTS, X-Frame-Options: SAMEORIGIN, nosniff, and API rate limiting)."
    ]
    for b in exp1_bullets:
        story.append(Paragraph(f"&bull;&nbsp;&nbsp;{b}", bullet_style))

    # CV. Arfa Nusantara Teknologi
    story.append(Paragraph(
        "<b>CV. Arfa Nusantara Teknologi — Surabaya</b> | <b>Web Developer (Intern)</b> | October 2022 – March 2023",
        job_title
    ))
    exp2_bullets = [
        "Developed an employee attendance status website using Vue.js, Tailwind CSS, Laravel, and REST APIs.",
        "Built, maintained, and integrated REST APIs for internal attendance data management functionality.",
        "Optimized backend and interface performance through query optimization and caching, while ensuring responsive behavior across mobile, tablet, and desktop devices.",
        "Collaborated across teams and used Git and GitHub for version control."
    ]
    for b in exp2_bullets:
        story.append(Paragraph(f"&bull;&nbsp;&nbsp;{b}", bullet_style))

    # ==================== PAGE 2 ====================
    story.append(PageBreak())

    # Projects
    story.append(Paragraph("PROJECTS", section_heading))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.black, spaceBefore=1, spaceAfter=4))

    story.append(Paragraph("ProMaP — Project Management Platform (2026)", project_title_style))
    story.append(Paragraph(
        "Multi-tenant SaaS application with REST API, JWT authentication, 4-level RBAC, modern UI, analytics dashboard, and Kanban board.",
        project_desc_style
    ))
    story.append(Paragraph(
        "<b>Tech Stack:</b> Next.js 15, Tailwind CSS, shadcn/ui, Recharts, Prisma ORM, PostgreSQL (Neon), NextAuth, SonarQube, Playwright, Nginx.",
        project_meta_style
    ))
    story.append(Paragraph(
        '<b>Link:</b> <a href="https://promapv2.sobatumkmpro.com/"><u>https://promapv2.sobatumkmpro.com/</u></a>',
        project_meta_style
    ))
    story.append(Spacer(1, 4))

    story.append(Paragraph("Randumart — Full Stack E-Commerce (2026)", project_title_style))
    story.append(Paragraph(
        "E-commerce website featuring an order state machine, automatic stock management, dynamic promotional banners, responsive UI, and checkout flow.",
        project_desc_style
    ))
    story.append(Paragraph(
        "<b>Tech Stack:</b> Next.js, Tailwind CSS, shadcn/ui, Axios, Prisma ORM, PostgreSQL (Neon), NextAuth.",
        project_meta_style
    ))
    story.append(Paragraph(
        '<b>Link:</b> <a href="https://www.randumart.shop/"><u>https://www.randumart.shop/</u></a>',
        project_meta_style
    ))
    story.append(Spacer(1, 6))

    # Education
    story.append(Paragraph("EDUCATION", section_heading))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.black, spaceBefore=1, spaceAfter=4))
    story.append(Paragraph(
        "<b>Universitas Terbuka</b> — Information Systems (Semester 3) | 2025 – Present",
        body_text
    ))
    story.append(Paragraph(
        "<b>SMK Negeri 1 Surabaya</b> — Software Engineering | 2021 – 2024",
        body_text
    ))
    story.append(Spacer(1, 4))

    # Technical Skills
    story.append(Paragraph("TECHNICAL SKILLS", section_heading))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.black, spaceBefore=1, spaceAfter=4))

    skills = [
        ("Frontend", "React, Next.js, Vue.js, Tailwind CSS, shadcn/ui, Axios, HTML5, CSS3, TypeScript"),
        ("Backend", "Node.js, Express.js, Laravel, REST API, JWT Authentication, NextAuth, API Rate Limiting"),
        ("Database", "PostgreSQL, MySQL, Prisma ORM, Neon"),
        ("DevOps & Tools", "Git, GitHub, GitHub Actions (CI/CD), Docker, Ubuntu, Nginx, Vercel, Figma, Swagger, Postman, Prisma Studio, VS Code"),
        ("Unit Testing", "SonarQube, Playwright, Vitest, Jest, Apache Jmeter"),
        ("Security Testing", "Npm Audit, Nuclei Scanner, Nmap Scanner, Katana Engine, DevTools"),
        ("Soft Skills", "Communication, Problem Solving, Adaptability, Collaboration, Time Management")
    ]
    for category, items in skills:
        story.append(Paragraph(f"<b>{category}:</b> {items}", skills_style))

    doc.build(story)
    print(f"CV successfully generated at: {output_path}")

if __name__ == "__main__":
    out_dir = r"d:\Portfolio\inoru-portfolio\public\cv"
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "INORU_AKHMAD_CV.pdf")
    create_cv(target)
