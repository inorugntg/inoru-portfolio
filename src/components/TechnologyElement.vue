<script setup lang="ts">
import { computed } from 'vue';
import { Icon } from '@iconify/vue';
import { useThemeStore } from '@/stores/theme';
import { TechnologyType } from '@/types/TechnologyType';
import { DarkTheme, LightTheme } from '@/constants/app';

const themeStore = useThemeStore();

type TechnologyConfigType = {
    title: string,
    icon: string,
    width: number
};

type TechnologiesType = {
    [key in TechnologyType]: TechnologyConfigType;
};

const props = defineProps<{
    element: TechnologyType | string
}>();

const technologies: TechnologiesType = {
    php: {
        title: 'PHP',
        icon: 'logos:php',
        width: 48
    },
    laravel: {
        title: 'Laravel',
        icon: 'logos:laravel',
        width: 40
    },
    javascript: {
        title: 'JavaScript',
        icon: 'skill-icons:javascript',
        width: 35
    },
    jquery: {
        title: 'jQuery',
        icon: 'mdi:jquery',
        width: 42
    },
    sass: {
        title: 'Sass',
        icon: 'vscode-icons:file-type-sass',
        width: 42
    },
    less: {
        title: 'less',
        icon: 'logos:less',
        width: 42
    },
    bootstrap: {
        title: 'Bootstrap',
        icon: 'akar-icons:bootstrap-fill',
        width: 42
    },
    mysql: {
        title: 'MySQL',
        icon: 'logos:mysql',
        width: 52
    },
    postgresql: {
        title: 'PostgreSQL',
        icon: 'logos:postgresql',
        width: 42
    },
    git: {
        title: 'Git',
        icon: 'bi:git',
        width: 38
    },
    github: {
        title: 'GitHub',
        icon: 'akar-icons:github-fill',
        width: 38
    },
    python: {
        title: 'Python',
        icon: 'logos:python',
        width: 40
    },
    csharp: {
        title: 'C#',
        icon: 'vscode-icons:file-type-csharp2',
        width: 44
    },
    vue: {
        title: 'VueJS',
        icon: 'logos:vue',
        width: 35
    },
    redis: {
        title: 'Redis',
        icon: 'logos:redis',
        width: 40
    },
    pygame: {
        title: 'pygame',
        icon: 'noto:snake',
        width: 40
    },
    pyqt5: {
        title: 'PyQt5',
        icon: 'logos:qt',
        width: 40
    },
    pwa: {
        title: 'PWA',
        icon: 'logos:pwa',
        width: 36
    },
    css: {
        title: 'CSS',
        icon: 'logos:css-3',
        width: 30
    },
    java: {
        title: 'Java',
        icon: 'logos:java',
        width: 30
    },
    symfony: {
        title: 'Symfony',
        icon: 'logos:symfony',
        width: 40
    },
    docker: {
        title: 'Docker',
        icon: 'logos:docker-icon',
        width: 48
    },
    phpunit: {
        title: 'PHPUnit',
        icon: 'vscode-icons:file-type-phpunit',
        width: 38
    },
    typescript: {
        title: 'TypeScript',
        icon: 'skill-icons:typescript',
        width: 35
    },
    microservices: {
        title: 'Microservices',
        icon: 'carbon:microservices-1',
        width: 35
    },
    rabbitmq: {
        title: 'RabbitMQ',
        icon: 'logos:rabbitmq-icon',
        width: 30
    },
    tailwind: {
        title: 'Tailwind',
        icon: 'logos:tailwindcss-icon',
        width: 33
    },
    c: {
        title: 'C',
        icon: 'logos:c',
        width: 33
    },
    linux: {
        title: 'Linux',
        icon: 'flat-color-icons:linux',
        width: 41
    },
    nuxt: {
        title: 'Nuxt',
        icon: 'logos:nuxt-icon',
        width: 42
    },
    node: {
        title: 'Node',
        icon: 'logos:nodejs-icon',
        width: 38
    },
    react: {
        title: 'React',
        icon: 'logos:react',
        width: 38
    },
    graphql: {
        title: 'Graphql',
        icon: 'logos:graphql',
        width: 38
    },
    gitlab: {
        title: 'Gitlab',
        icon: 'logos:gitlab',
        width: 38
    },
    ubuntu: {
        title: 'Ubuntu',
        icon: 'logos:ubuntu',
        width: 38
    },
    cpp: {
        title: 'Cpp',
        icon: 'logos:cpp',
        width: 38
    },
    mongodb: {
        title: 'Mongodb',
        icon: 'logos:mongodb',
        width: 41
    },
    nextjs: {
        title: 'NextJS',
        icon: 'skill-icons:nextjs-light',
        width: 36
    },
    prisma: {
        title: 'Prisma',
        icon: 'skill-icons:prisma',
        width: 36
    },
    express: {
        title: 'Express.js',
        icon: 'skill-icons:expressjs-light',
        width: 38
    },
    swagger: {
        title: 'Swagger',
        icon: 'logos:swagger',
        width: 36
    },
    axios: {
        title: 'Axios',
        icon: 'logos:axios',
        width: 42
    },
    neon: {
        title: 'Neon DB',
        icon: 'logos:neon-icon',
        width: 36
    },
    restapi: {
        title: 'REST APIs',
        icon: 'carbon:api',
        width: 36
    },
    shadcn: {
        title: 'shadcn/ui',
        icon: 'simple-icons:shadcnui',
        width: 32
    },
    html5: {
        title: 'HTML5',
        icon: 'logos:html-5',
        width: 34
    },
    jwt: {
        title: 'JWT Auth',
        icon: 'logos:jwt-icon',
        width: 34
    },
    nextauth: {
        title: 'NextAuth',
        icon: 'tabler:shield-lock',
        width: 34
    },
    githubactions: {
        title: 'GitHub Actions',
        icon: 'skill-icons:githubactions-dark',
        width: 34
    },
    vercel: {
        title: 'Vercel',
        icon: 'logos:vercel-icon',
        width: 34
    },
    postman: {
        title: 'Postman',
        icon: 'logos:postman-icon',
        width: 34
    },
    prismastudio: {
        title: 'Prisma Studio',
        icon: 'skill-icons:prisma',
        width: 34
    },
    vscode: {
        title: 'VS Code',
        icon: 'logos:visual-studio-code',
        width: 34
    },
    figma: {
        title: 'Figma',
        icon: 'logos:figma',
        width: 30
    },
    sonarqube: {
        title: 'SonarQube',
        icon: 'simple-icons:sonarqube',
        width: 34
    },
    playwright: {
        title: 'Playwright',
        icon: 'logos:playwright',
        width: 34
    },
    jest: {
        title: 'Jest',
        icon: 'logos:jest',
        width: 34
    },
    vitest: {
        title: 'Vitest',
        icon: 'logos:vitest',
        width: 34
    },
    jmeter: {
        title: 'Apache JMeter',
        icon: 'simple-icons:apachejmeter',
        width: 34
    },
    npmaudit: {
        title: 'npm audit (SAST)',
        icon: 'logos:npm-icon',
        width: 34
    },
    nuclei: {
        title: 'Nuclei Scanner',
        icon: 'carbon:security',
        width: 32
    },
    nmap: {
        title: 'Nmap Scanner',
        icon: 'carbon:network-4',
        width: 32
    },
    katana: {
        title: 'Katana Engine',
        icon: 'carbon:search-advanced',
        width: 32
    },
    devtools: {
        title: 'DevTools & Code Audit',
        icon: 'tabler:device-desktop-analytics',
        width: 32
    },
    nginx: {
        title: 'Nginx',
        icon: 'logos:nginx',
        width: 36
    }
};

const aliasMap: Record<string, TechnologyType> = {
    'next.js 15': 'nextjs',
    'next.js 14': 'nextjs',
    'next.js': 'nextjs',
    'nextjs': 'nextjs',
    'react': 'react',
    'vue.js': 'vue',
    'vue': 'vue',
    'prisma': 'prisma',
    'prisma orm': 'prisma',
    'postgresql': 'postgresql',
    'postgres': 'postgresql',
    'postgresql (neon)': 'postgresql',
    'neon': 'neon',
    'nextauth': 'nextauth',
    'jwt auth': 'jwt',
    'jwt': 'jwt',
    'tailwind css': 'tailwind',
    'tailwind': 'tailwind',
    'shadcn/ui': 'shadcn',
    'shadcn': 'shadcn',
    'node.js': 'node',
    'node': 'node',
    'express.js': 'express',
    'express': 'express',
    'laravel': 'laravel',
    'rest api': 'restapi',
    'mysql': 'mysql',
    'git': 'git',
    'github': 'github',
    'github actions': 'githubactions',
    'docker': 'docker',
    'ubuntu': 'ubuntu',
    'vercel': 'vercel',
    'swagger': 'swagger',
    'postman': 'postman',
    'prisma studio': 'prismastudio',
    'vs code': 'vscode',
    'figma': 'figma',
    'axios': 'axios',
    'html5': 'html5',
    'css3': 'css',
    'sonarqube': 'sonarqube',
    'playwright': 'playwright',
    'jest': 'jest',
    'vitest': 'vitest',
    'vitest / jest': 'vitest',
    'apache jmeter': 'jmeter',
    'jmeter': 'jmeter',
    'npm audit': 'npmaudit',
    'npm audit (sast)': 'npmaudit',
    'nuclei scanner': 'nuclei',
    'nuclei': 'nuclei',
    'nmap scanner': 'nmap',
    'nmap': 'nmap',
    'katana engine': 'katana',
    'katana': 'katana',
    'devtools': 'devtools',
    'devtools & code audit': 'devtools',
    'nginx': 'nginx',
    'nginx reverse proxy': 'nginx'
};

const resolvedTech = computed(() => {
    const rawKey = props.element.toLowerCase().trim();
    const mappedKey = aliasMap[rawKey] || (rawKey as TechnologyType);
    if (technologies[mappedKey]) {
        return {
            title: props.element.includes('.') || props.element.includes(' ') || props.element.includes('/')
                ? props.element
                : technologies[mappedKey].title,
            icon: technologies[mappedKey].icon,
            width: technologies[mappedKey].width
        };
    }
    return {
        title: props.element,
        icon: 'tabler:code',
        width: 30
    };
});

</script>

<template>
    <div
        class="technology-element"
        :class="{ 'technology-element-dark-theme': themeStore.theme === DarkTheme,
                  'technology-element-light-theme': themeStore.theme === LightTheme }"
    >

        <div class="icon">
            <Icon
                :icon="resolvedTech.icon"
                :width="resolvedTech.width"
            />
        </div>

        <span class="title">{{ resolvedTech.title }}</span>

    </div>
</template>

<style lang="less" scoped>
@import '@/styles/variables.less';

.technology-element {
    display: flex;
    align-items: center;
    min-height: 3.2rem;
    padding: 0.2rem 0.5rem 0.2rem 0.2rem;
    border: solid @blue-color 0.12rem;
    border-radius: 1rem;
    box-shadow: 0 0 10px fade(@blue-color, 18%);

    transition: background-color ease @theme-switch-time,
                box-shadow ease @hover-time,
                transform ease @hover-time;

    &:hover {
        transform: translateY(-2px);
        box-shadow: 0 0 16px fade(@blue-color, 45%);
    }

    .icon {
        display: flex;
        align-items: center;
        padding-left: 0.5rem;
    }
    .title {
        padding: 0.5rem;
        font-family: 'LatoFontRegular', serif;
        font-size: 0.95rem;
    }
}

.technology-element-dark-theme {
    color: #dark[text-color];
    background-color: #dark[background-color-on-element];
}

.technology-element-light-theme {
    color: #light[text-color];
    background-color: #light[background-color-on-element];
}

</style>
