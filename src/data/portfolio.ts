export interface ProjectItem {
    title: string;
    description: string;
    tech: string[];
    features: string[];
    liveDemo: string;
}

export const projects: ProjectItem[] = [
    {
        title: "ProMaP — Project Management Platform (2026)",
        description: "Aplikasi SaaS multi-tenant enterprise untuk manajemen action plan, proposal, dan monitoring timeline project karyawan dengan standar keamanan dan performa tinggi.",
        tech: ["Next.js 15", "Tailwind CSS", "shadcn/ui", "Prisma ORM", "PostgreSQL (Neon)", "NextAuth", "SonarQube", "Playwright", "Nginx"],
        features: [
            "RBAC 4 level role (Super Admin, Admin Operasional, Manager, PIC) & isolasi data multi-tenant",
            "Optimasi Server Components, unstable_cache, dynamic imports & query Prisma anti-N+1",
            "SonarQube Quality Gate PASSED (Coverage 58.4%), 190/190 Unit & Integration Tests (100% Pass)",
            "Automated E2E Testing Playwright pada 13 modul inti aplikasi dengan kelulusan 100%",
            "Audit Keamanan & Pen-testing (npm audit 0 vuln, Nmap port filtered, Katana crawler, Nuclei WAF, HSTS & Rate Limiting)",
            "Production ready: Nginx reverse proxy di Hostinger VPS dengan enkripsi SSL/TLS penuh"
        ],
        liveDemo: "https://promapv2.sobatumkmpro.com/"
    },
    {
        title: "Randumart — Full Stack E-Commerce (2026)",
        description: "Website e-commerce toko herbal, oleh-oleh umrah, dan parsel souvenir dengan fitur manajemen stok otomatis, promo banner dinamis, dan checkout via WhatsApp.",
        tech: ["Next.js", "Tailwind CSS", "shadcn/ui", "Axios", "Prisma ORM", "PostgreSQL (Neon)", "NextAuth"],
        features: [
            "Order state machine (PENDING → MENUNGGU_BAYAR → PAID → PROCESSING → SHIPPED → COMPLETED)",
            "Auto-increment rating & reviewCount serta auto-decrement stok setelah order berstatus PAID",
            "Sistem Promo Banner dinamis (Flash Sale, Diskon Persen, Custom) dengan countdown timer",
            "NextAuth (Google SSO + Credentials), checkout flow responsif, optimasi SEO & Core Web Vitals"
        ],
        liveDemo: "https://www.randumart.shop/"
    }
];

export const projectsId: ProjectItem[] = [
    {
        title: "ProMaP — Project Management Platform (2026)",
        description: "Aplikasi SaaS multi-tenant enterprise untuk manajemen action plan, proposal, dan monitoring timeline project karyawan dengan standar keamanan dan performa tinggi.",
        tech: ["Next.js 15", "Tailwind CSS", "shadcn/ui", "Prisma ORM", "PostgreSQL (Neon)", "NextAuth", "SonarQube", "Playwright", "Nginx"],
        features: [
            "RBAC 4 level role (Super Admin, Admin Operasional, Manager, PIC) & isolasi data multi-tenant",
            "Optimasi Server Components, unstable_cache, dynamic imports & query Prisma anti-N+1",
            "SonarQube Quality Gate PASSED (Coverage 58.4%), 190/190 Unit & Integration Tests (100% Pass)",
            "Automated E2E Testing Playwright pada 13 modul inti aplikasi dengan kelulusan 100%",
            "Audit Keamanan & Pen-testing (npm audit 0 vuln, Nmap port filtered, Katana crawler, Nuclei WAF, HSTS & Rate Limiting)",
            "Production ready: Nginx reverse proxy di Hostinger VPS dengan enkripsi SSL/TLS penuh"
        ],
        liveDemo: "https://promapv2.sobatumkmpro.com/"
    },
    {
        title: "Randumart — Full Stack E-Commerce (2026)",
        description: "Website e-commerce toko herbal, oleh-oleh umrah, dan parsel souvenir dengan fitur manajemen stok otomatis, promo banner dinamis, dan checkout via WhatsApp.",
        tech: ["Next.js", "Tailwind CSS", "shadcn/ui", "Axios", "Prisma ORM", "PostgreSQL (Neon)", "NextAuth"],
        features: [
            "Order state machine (PENDING → MENUNGGU_BAYAR → PAID → PROCESSING → SHIPPED → COMPLETED)",
            "Auto-increment rating & reviewCount serta auto-decrement stok setelah order berstatus PAID",
            "Sistem Promo Banner dinamis (Flash Sale, Diskon Persen, Custom) dengan countdown timer",
            "NextAuth (Google SSO + Credentials), checkout flow responsif, optimasi SEO & Core Web Vitals"
        ],
        liveDemo: "https://www.randumart.shop/"
    }
];

export const projectsEn: ProjectItem[] = [
    {
        title: "ProMaP — Project Management Platform (2026)",
        description: "Enterprise multi-tenant SaaS application for employee action plans, proposals, and project timeline monitoring engineered with high security and performance.",
        tech: ["Next.js 15", "Tailwind CSS", "shadcn/ui", "Prisma ORM", "PostgreSQL (Neon)", "NextAuth", "SonarQube", "Playwright", "Nginx"],
        features: [
            "4-level RBAC (Super Admin, Operational Admin, Manager, PIC) & strict multi-tenant data isolation",
            "Optimized Server Components, unstable_cache, dynamic imports & N+1-free Prisma queries",
            "SonarQube Quality Gate PASSED (58.4% Code Coverage), 190/190 Unit & Integration Tests (100% Pass)",
            "Automated Playwright E2E Testing across 13 core application modules with 100% pass rate",
            "Security Audit & Pen-testing (npm audit 0 vuln, Nmap filtered ports, Katana crawler, Nuclei WAF, HSTS & Rate Limiting)",
            "Production ready: Nginx reverse proxy on Hostinger VPS with full SSL/TLS"
        ],
        liveDemo: "https://promapv2.sobatumkmpro.com/"
    },
    {
        title: "Randumart — Full Stack E-Commerce (2026)",
        description: "Full-stack e-commerce platform for herbal goods, umrah souvenirs, and gift hampers with automated stock management, dynamic promo banners, and WhatsApp checkout.",
        tech: ["Next.js", "Tailwind CSS", "shadcn/ui", "Axios", "Prisma ORM", "PostgreSQL (Neon)", "NextAuth"],
        features: [
            "Order state machine (PENDING → MENUNGGU_BAYAR → PAID → PROCESSING → SHIPPED → COMPLETED)",
            "Auto-increment rating & reviewCount plus automated stock decrement upon PAID orders",
            "Dynamic Promo Banner system (Flash Sale, Percent Discount, Custom) with live countdown timers",
            "NextAuth (Google SSO + Credentials), responsive checkout flow, on-page SEO & Core Web Vitals"
        ],
        liveDemo: "https://www.randumart.shop/"
    }
];

export const getProjects = (locale?: string): ProjectItem[] => {
    if (locale && (locale.startsWith('en') || locale === 'en')) {
        return projectsEn;
    }
    return projectsId;
};
