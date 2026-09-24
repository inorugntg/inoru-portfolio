<script setup lang="ts">
import { useLanguageSwitcher } from '@/composables/useLanguageSwitcher';
import { useThemeStore } from '@/stores/theme';
import { FadeDown, FadeUp, DarkTheme, LightTheme } from '@/constants/app';

const { t } = useLanguageSwitcher();
const themeStore = useThemeStore();

</script>

<template>
    <section
        id="about"
        class="about"
    >
        <h2 :data-aos="FadeDown" class="title">{{ t('about.title') }}</h2>

        <div
            :data-aos="FadeUp"
            class="about-card"
            :class="{ 'about-card-dark-theme': themeStore.theme === DarkTheme,
                      'about-card-light-theme': themeStore.theme === LightTheme }"
        >
            <p class="description">
                {{ t('about.description') }}
            </p>
        </div>
    </section>
</template>

<style lang="less" scoped>
@import '@/styles/variables.less';

.about {
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    min-width: 100%;
    margin: auto;
    padding-bottom: 2rem;

    .title {
        float: left;
        width: 100%;
        min-height: 3rem;
        text-align: center;
        font-family: 'LatoFontBold', serif;
        font-size: 3rem;
        color: @blue-color;
    }

    .about-card {
        display: flex;
        flex-direction: column;
        align-items: center;
        width: 90%;
        max-width: 44rem;
        margin-top: 1rem;
        padding: 1.8rem 1.6rem;
        border: solid @blue-color 0.2rem;
        border-radius: 1rem;
        box-shadow: 0 0 20px fade(@blue-color, 18%);
        transition: background-color ease @theme-switch-time, box-shadow ease @hover-time;

        &:hover {
            box-shadow: 0 0 25px fade(@blue-color, 35%);
        }

        .description {
            font-family: 'LatoFontRegular', serif;
            font-size: 1.15rem;
            line-height: 1.85rem;
            text-align: center;
            opacity: 0.95;
        }
    }
}

.about-card-dark-theme {
    background-color: #dark[background-color-on-element];
    color: #dark[text-color];
}

.about-card-light-theme {
    background-color: #light[background-color-on-element];
    color: #light[text-color];
}

@media (min-width: @first-breakpoint) {
    .about {
        min-width: 36rem;
        max-width: 44rem;
        padding-bottom: 5rem;

        .title {
            min-height: 4rem;
        }

        .about-card {
            padding: 2.2rem 2.5rem;

            .description {
                font-size: 1.25rem;
                line-height: 2rem;
            }
        }
    }
}

</style>
