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
        description: "Aplikasi SaaS multi-tenant untuk manajemen action plan, proposal, dan monitoring timeline project karyawan.",
        tech: ["Next.js 14", "Prisma", "PostgreSQL", "NextAuth", "Tailwind CSS", "shadcn/ui"],
        features: [
            "RBAC 4 level role (Super Admin, Admin Operasional, Manager, PIC)",
            "Server Components + caching untuk performa optimal",
            "Kanban Board, Kalender Gantt, dan Export PDF",
            "Sistem notifikasi in-app + cron job overdue otomatis"
        ],
        liveDemo: "https://promap-v2-3fpn.vercel.app"
    },
    {
        title: "Randumart — E-Commerce Website (2026)",
        description: "Website e-commerce toko herbal, oleh-oleh umrah, dan souvenir dengan checkout via WhatsApp.",
        tech: ["Next.js", "Prisma", "PostgreSQL", "Tailwind CSS", "NextAuth"],
        features: [
            "Bundling & Hamper features with automated stock management",
            "Dynamic Promo Banner system (Flash Sale, Percent Discount, Custom)",
            "Order state machine (PENDING → PAID → SHIPPED → COMPLETED)",
            "Auto-increment rating & reviewCount upon order PAID"
        ],
        liveDemo: "https://randumart-vercel-deploy.vercel.app"
    }
];

export const projectsId: ProjectItem[] = [
    {
        title: "ProMaP — Project Management Platform (2026)",
        description: "Aplikasi SaaS multi-tenant untuk manajemen action plan, proposal, dan monitoring timeline project karyawan.",
        tech: ["Next.js 14", "Prisma", "PostgreSQL", "NextAuth", "Tailwind CSS", "shadcn/ui"],
        features: [
            "RBAC 4 level role (Super Admin, Admin Operasional, Manager, PIC)",
            "Server Components + caching untuk performa optimal",
            "Kanban Board, Kalender Gantt, dan Export PDF",
            "Sistem notifikasi in-app + cron job overdue otomatis"
        ],
        liveDemo: "https://promap-v2-3fpn.vercel.app"
    },
    {
        title: "Randumart — E-Commerce Website (2026)",
        description: "Website e-commerce toko herbal, oleh-oleh umrah, dan souvenir dengan checkout via WhatsApp.",
        tech: ["Next.js", "Prisma", "PostgreSQL", "Tailwind CSS", "NextAuth"],
        features: [
            "Fitur Bundling & Parsel dengan auto-stock management",
            "Sistem Promo Banner dinamis (Flash Sale, Diskon Persen, Custom)",
            "State machine order (PENDING → PAID → SHIPPED → COMPLETED)",
            "Auto-increment rating & reviewCount saat order PAID"
        ],
        liveDemo: "https://randumart-vercel-deploy.vercel.app"
    }
];

export const projectsEn: ProjectItem[] = [
    {
        title: "ProMaP — Project Management Platform (2026)",
        description: "Multi-tenant SaaS application for managing employee action plans, proposals, and project timeline monitoring.",
        tech: ["Next.js 14", "Prisma", "PostgreSQL", "NextAuth", "Tailwind CSS", "shadcn/ui"],
        features: [
            "4-level RBAC roles (Super Admin, Operational Admin, Manager, PIC)",
            "Server Components + caching for optimal performance",
            "Kanban Board, Gantt Calendar, and PDF Export",
            "In-app notification system + automated overdue cron jobs"
        ],
        liveDemo: "https://promap-v2-3fpn.vercel.app"
    },
    {
        title: "Randumart — E-Commerce Website (2026)",
        description: "E-commerce website for herbal products, umrah souvenirs, and hampers with checkout via WhatsApp.",
        tech: ["Next.js", "Prisma", "PostgreSQL", "Tailwind CSS", "NextAuth"],
        features: [
            "Bundling & Hamper features with automated stock management",
            "Dynamic Promo Banner system (Flash Sale, Percent Discount, Custom)",
            "Order state machine (PENDING → PAID → SHIPPED → COMPLETED)",
            "Auto-increment rating & reviewCount upon order PAID"
        ],
        liveDemo: "https://randumart-vercel-deploy.vercel.app"
    }
];

export const getProjects = (locale?: string): ProjectItem[] => {
    if (locale && (locale.startsWith('en') || locale === 'en')) {
        return projectsEn;
    }
    return projectsId;
};
