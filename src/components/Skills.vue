<script setup lang="ts">
import TechnologyElement from '@/components/TechnologyElement.vue';
import { useLanguageSwitcher } from '@/composables/useLanguageSwitcher';
import { TechnologyType } from '@/types/TechnologyType';
import { FadeDown, FadeLeft, FadeRight } from '@/constants/app';

const { t } = useLanguageSwitcher();

type SkillCategory = {
    titleKey: string,
    skills: TechnologyType[]
};

const skillCategories: SkillCategory[] = [
    {
        titleKey: 'skills.categories.frontend',
        skills: ['react', 'nextjs', 'vue', 'tailwind', 'shadcn', 'axios', 'html5', 'css']
    },
    {
        titleKey: 'skills.categories.backend',
        skills: ['node', 'express', 'laravel', 'restapi', 'jwt', 'nextauth']
    },
    {
        titleKey: 'skills.categories.database',
        skills: ['postgresql', 'mysql', 'prisma', 'neon']
    },
    {
        titleKey: 'skills.categories.devops',
        skills: ['git', 'github', 'githubactions', 'docker', 'ubuntu', 'nginx', 'vercel']
    },
    {
        titleKey: 'skills.categories.testing',
        skills: ['sonarqube', 'playwright', 'vitest', 'jest', 'jmeter']
    },
    {
        titleKey: 'skills.categories.security',
        skills: ['npmaudit', 'nuclei', 'nmap', 'katana', 'devtools']
    },
    {
        titleKey: 'skills.categories.tools',
        skills: ['swagger', 'postman', 'prismastudio', 'vscode', 'figma']
    }
];

</script>

<template>
    <div id="skills" class="skills">
        <h2 class="title" :data-aos="FadeDown">{{ t('skills.title') }}</h2>

        <div
            v-for="(category, index) in skillCategories"
            :key="index"
            class="element"
            :data-aos="index % 2 === 0 ? FadeRight : FadeLeft"
        >
            <h3 class="title-smaller">{{ t(category.titleKey) }}</h3>

            <div class="content">
                <TechnologyElement
                    v-for="(technology, techIndex) in category.skills"
                    :key="techIndex"
                    :element="technology"
                />
            </div>
        </div>
    </div>
</template>

<style lang="less" scoped>
@import '@/styles/variables.less';

.skills {
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    margin: auto;
    min-width: 50%;
    padding-bottom: 2rem;

    .title {
        float: left;
        width: 100%;
        text-align: center;
        font-family: 'LatoFontBold', serif;
        font-size: 3rem;
        padding-bottom: 0.8rem;
        color: @blue-color;
    }

    .element {
        width: 100%;
        padding-top: 0.8rem;
        padding-bottom: 0.6rem;

        .title-smaller {
            width: 100%;
            text-align: center;
            font-size: 1.45rem;
            font-family: 'LatoFontBold', serif;
            padding-bottom: 0.4rem;
            color: lighten(@blue-color, 10%);
        }

        .content {
            display: flex;
            align-content: flex-start;
            justify-content: center;
            flex-wrap: wrap;
            gap: 0.6rem;
            width: 100%;
            padding-top: 0.4rem;
        }
    }
}

@media (min-width: @first-breakpoint) {
    .skills {
        min-width: 35rem;
        max-width: 46rem;
        padding-bottom: 7rem;

        .element {
            .title-smaller {
                text-align: left;
                padding-left: 0.2rem;
            }
            .content {
                justify-content: flex-start;
            }
        }
    }
}

</style>
