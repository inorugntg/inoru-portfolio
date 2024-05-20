<script setup lang="ts">
import ProjectsItem from '@/components/Projects/ProjectsItem.vue';
import { useLanguageSwitcher } from '@/composables/useLanguageSwitcher';
import { TechnologyType } from '@/types/TechnologyType';
import { FadeDown, FadeLeft, FadeRight } from '@/constants/app';

const { t } = useLanguageSwitcher();

type ProjectType = {
    titleKey: string,
    contentKey: string,
    github: string,
    online?: string,
    technologies: TechnologyType[]
};
const projects: ProjectType[] = [
    {
        titleKey: 'projects.projectsItems.shopSystem.title',
        contentKey: 'projects.projectsItems.shopSystem.content',
        github: 'https://github.com/Racheltbt20/ResepMakanan.git',
        technologies: [
            'php', 'laravel', 'javascript',
            'mysql', 'bootstrap'
        ]
    },
    {
        titleKey: 'projects.projectsItems.snakeWebApp.title',
        contentKey: 'projects.projectsItems.snakeWebApp.content',
        github: 'https://github.com/ahmadsyahani/futsool.git',
        technologies: [
            'php', 'laravel', 'javascript',
            'jquery', 'bootstrap', 'mysql'
        ]
    },
    {
        titleKey: 'projects.projectsItems.snakeGame.title',
        contentKey: 'projects.projectsItems.snakeGame.content',
        github: 'https://github.com/inorugntg/Blog-App-Node-React.git',
        technologies: ['javascript', 'css','node','react']
    },
    {
        titleKey: 'projects.projectsItems.minesweeper.title',
        contentKey: 'projects.projectsItems.minesweeper.content',
        github: 'https://github.com/inorugntg/Clinic_Management.git',
        technologies: ['javascript', 'css', 'bootstrap', 'php', 'laravel']
    }
];
</script>

<template>
    <section
        id="projects"
        class="projects"
    >
        <h2 :data-aos="FadeDown" class="title">{{ t('projects.title') }}</h2>

        <div class="items">
            <ProjectsItem
                v-for="(project, index) in projects"
                :key="index"
                :title="t(project.titleKey)"
                :content="t(project.contentKey)"
                :technologies="project.technologies"
                :github="project.github"
                :online="project.online"
                :animation="index % 2 === 0 ? FadeRight : FadeLeft"
            />
        </div>
    </section>
</template>

<style lang="less" scoped>
@import '@/styles/variables.less';

.projects {
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    min-width: 100%;
    min-height: 50vh;
    margin: auto;
    padding-bottom: 1rem;

    .title {
        float: left;
        width: 100%;
        min-height: 3rem;
        text-align: center;
        font-family: 'LatoFontBold', serif;
        font-size: 3rem;
        color: @blue-color;
    }
    .items {
        float: left;
        width: 100%;
        padding: 0.5rem;
    }
}

@media (min-width: @first-breakpoint) {
    .projects {
        min-width: 40rem;
        max-width: 42rem;
        padding-bottom: 7rem;

        .title {
            min-height: 4rem;
        }
    }
}
</style>
