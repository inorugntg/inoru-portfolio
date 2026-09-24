<script setup lang="ts">
import { computed } from 'vue';
import ProjectsItem from '@/components/Projects/ProjectsItem.vue';
import { useLanguageSwitcher } from '@/composables/useLanguageSwitcher';
import { FadeDown, FadeLeft, FadeRight } from '@/constants/app';
import { getProjects } from '@/data/portfolio';

const { t, currentLanguage } = useLanguageSwitcher();

const projectList = computed(() => getProjects(currentLanguage.value));

</script>

<template>
    <section
        id="projects"
        class="projects"
    >
        <h2 :data-aos="FadeDown" class="title">{{ t('projects.title') }}</h2>

        <div class="items">
            <ProjectsItem
                v-for="(project, index) in projectList"
                :key="index"
                :title="project.title"
                :content="project.description"
                :features="project.features"
                :technologies="project.tech"
                :online="project.liveDemo"
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
        max-width: 46rem;
        padding-bottom: 7rem;

        .title {
            min-height: 4rem;
        }
    }
}
</style>
