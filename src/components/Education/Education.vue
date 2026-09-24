<script setup lang="ts">
import EducationItem from '@/components/Education/EducationItem.vue';
import { useLanguageSwitcher } from '@/composables/useLanguageSwitcher';
import { TechnologyType } from '@/types/TechnologyType';
import { FadeDown, FadeLeft, FadeRight } from '@/constants/app';

const { t } = useLanguageSwitcher();

type Education = {
    titleKey: string,
    contentKey: string,
    majorKey: string,
    period: string,
    url: string,
    technologies: TechnologyType[]
};
const educationItems: Education[] = [
    {
        titleKey: 'education.educationItems.universitasTerbuka.title',
        contentKey: 'education.educationItems.universitasTerbuka.content',
        majorKey: 'education.educationItems.universitasTerbuka.major',
        period: '2025 - Sekarang',
        url: 'https://www.ut.ac.id/',
        technologies: [
            'nextjs', 'typescript', 'javascript', 'node', 'mysql', 'postgresql'
        ]
    },
    {
        titleKey: 'education.educationItems.smkn1Surabaya.title',
        contentKey: 'education.educationItems.smkn1Surabaya.content',
        majorKey: 'education.educationItems.smkn1Surabaya.major',
        period: '2021 - 2024',
        url: 'http://www.smkn1-sby.sch.id/',
        technologies: [
            'php', 'laravel', 'javascript', 'mysql', 'python', 'java', 'ubuntu'
        ]
    }
];

</script>

<template>
    <section
        id="education"
        class="education"
    >
        <h2 :data-aos="FadeDown" class="title">{{ t('education.title') }}</h2>

        <div class="items">
            <EducationItem
                v-for="(education, index) in educationItems"
                :key="index"
                :title="t(education.titleKey)"
                :content="t(education.contentKey)"
                :major="t(education.majorKey)"
                :period="education.period"
                :url="education.url"
                :technologies="education.technologies"
                :animation="index % 2 === 0 ? FadeRight : FadeLeft"
            />
        </div>

    </section>
</template>

<style lang="less" scoped>
@import '@/styles/variables.less';

.education {
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    min-width: 100%;
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
    .education {
        min-width: 36rem;
        max-width: 38rem;
        padding-bottom: 7rem;

        .title {
            min-height: 4rem;
        }
    }
}

</style>
