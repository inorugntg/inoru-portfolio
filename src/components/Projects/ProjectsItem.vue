<script setup lang="ts">
import { Icon } from '@iconify/vue';
import TechnologyElement from '@/components/TechnologyElement.vue';
import { useCursorHover } from '@/directives/useCursorHover';
import { useLanguageSwitcher } from '@/composables/useLanguageSwitcher';
import { useThemeStore } from '@/stores/theme';
import { TechnologyType } from '@/types/TechnologyType';
import { AnimationType } from '@/types/AnimationType';
import { DarkTheme, LightTheme } from '@/constants/app';

const { t } = useLanguageSwitcher();
const vCursorHover = useCursorHover();
const themeStore = useThemeStore();

const props = defineProps<{
    title: string,
    content: string,
    features?: string[],
    technologies: (TechnologyType | string)[],
    online?: string,
    animation: AnimationType
}>();

</script>

<template>
    <div :data-aos="props.animation">
        <div
            class="projects-item"
            :class="{ 'projects-item-dark-theme': themeStore.theme === DarkTheme,
                      'projects-item-light-theme': themeStore.theme === LightTheme }"
        >
            <h3 class="title">
                {{ props.title }}
            </h3>

            <p class="content">
                {{ props.content }}
            </p>

            <!-- Fitur Utama (Bullet Points) -->
            <div v-if="props.features && props.features.length" class="features-wrapper">
                <ul class="features-list">
                    <li
                        v-for="(feature, idx) in props.features"
                        :key="idx"
                        class="feature-item"
                    >
                        <Icon icon="mdi:check-circle-outline" width="18" class="feature-icon" />
                        <span>{{ typeof feature === 'function' ? (feature as any)() : feature }}</span>
                    </li>
                </ul>
            </div>

            <!-- Tech Stack (Badge/Chip) -->
            <div class="technologies">
                <TechnologyElement
                    v-for="(technology, index) in props.technologies"
                    :key="index"
                    :element="technology"
                />
            </div>

            <!-- HANYA Link Live Demo -->
            <div class="below" v-if="props.online">
                <a
                    class="demo-button"
                    target="_blank"
                    rel="noopener noreferrer"
                    v-cursor-hover
                    :href="props.online"
                >
                    <span>{{ t('projects.viewDemo') }}</span>
                    <Icon icon="ci:external-link" width="22" />
                </a>
            </div>
        </div>
    </div>
</template>

<style lang="less" scoped>
@import '@/styles/variables.less';

.projects-item {
    display: flex;
    flex-direction: column;
    text-align: center;
    gap: 0.8rem;
    min-height: 10rem;
    width: 100%;
    border: solid @blue-color 0.2rem;
    border-radius: 1rem;
    box-shadow: 0 0 18px fade(@blue-color, 18%);
    padding: 1.2rem 1.4rem;
    margin-bottom: 2rem;

    transition: background-color ease @theme-switch-time,
                box-shadow ease @hover-time;

    &:hover {
        box-shadow: 0 0 25px fade(@blue-color, 35%);
    }

    .title {
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 0 auto;
        font-size: 1.45rem;
        font-family: 'LatoFontBold', serif;
        color: @blue-color;
    }

    .content {
        text-align: left;
        line-height: 1.6rem;
        font-family: 'LatoFontRegular', serif;
        font-size: 1.05rem;
        opacity: 0.95;
    }

    .features-wrapper {
        text-align: left;
        padding: 0.4rem 0;

        .features-list {
            list-style: none;
            padding: 0;
            margin: 0;
            display: flex;
            flex-direction: column;
            gap: 0.5rem;

            .feature-item {
                display: flex;
                align-items: flex-start;
                gap: 0.5rem;
                font-family: 'LatoFontRegular', serif;
                font-size: 0.98rem;
                line-height: 1.45rem;

                .feature-icon {
                    color: @blue-color;
                    flex-shrink: 0;
                    margin-top: 0.15rem;
                }
            }
        }
    }

    .technologies {
        display: flex;
        align-content: flex-start;
        justify-content: flex-start;
        flex-wrap: wrap;
        gap: 0.5rem;
        padding-top: 0.4rem;
    }

    .below {
        display: flex;
        justify-content: flex-start;
        align-items: center;
        padding-top: 0.6rem;

        .demo-button {
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            padding: 0.55rem 1.3rem;
            border-radius: 0.6rem;
            border: solid @blue-color 0.12rem;
            background-color: fade(@blue-color, 12%);
            color: inherit;
            text-decoration: none;
            font-family: 'LatoFontBold', serif;
            font-size: 0.95rem;
            box-shadow: 0 0 10px fade(@blue-color, 20%);
            transition: transform ease @hover-time, background-color ease @hover-time, box-shadow ease @hover-time, color ease @hover-time;

            &:hover {
                transform: translateY(-2px);
                background-color: @blue-color;
                color: #0a1929;
                box-shadow: 0 0 18px fade(@blue-color, 50%);
            }
        }
    }
}

@media (min-width: @first-breakpoint) {
    .projects-item {
        padding: 1.6rem 1.8rem;

        .title {
            font-size: 1.6rem;
            justify-content: flex-start;
            margin: 0;
        }

        .content {
            line-height: 1.7rem;
            font-size: 1.1rem;
        }

        .technologies {
            justify-content: flex-start;
        }
    }
}

.projects-item-dark-theme {
    background-color: #dark[background-color-on-element];
}

.projects-item-light-theme {
    background-color: #light[background-color-on-element];
}

</style>
