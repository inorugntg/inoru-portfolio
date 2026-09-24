<script setup lang="ts">
import AnimateSplitLetters from '@/components/LandingPage/AnimateSplitLetters.vue';
import { useLanguageSwitcher } from '@/composables/useLanguageSwitcher';
import { useCursorHover } from '@/directives/useCursorHover';
import { FadeUpRight } from '@/constants/app';

const { t } = useLanguageSwitcher();
const vCursorHover = useCursorHover();

</script>

<template>
    <section class="landing-page">
        <div class="hero-wrapper">
            <div
                :data-aos="FadeUpRight"
                class="text"
            >
                <h2 class="my-name-is">{{ t('landingPage.myNameIs') }}</h2>

                <h1 class="name">
                    <AnimateSplitLetters
                        :text="t('landingPage.name')"
                    />
                </h1>

                <h3 class="tagline">
                    {{ t('landingPage.tagline') }}
                </h3>

                <p class="sub-tagline">
                    {{ t('landingPage.subTagline') }}
                </p>

                <div class="cta-actions">
                    <a
                        href="#projects"
                        class="btn-primary"
                        v-cursor-hover
                    >
                        {{ t('landingPage.viewProjects') }}
                    </a>
                </div>
            </div>
        </div>
    </section>
</template>

<style lang="less" scoped>
@import '@/styles/variables.less';

.landing-page {
    display: flex;
    align-items: center;
    justify-content: center;
    min-width: 100%;
    min-height: 70vh;
    margin: auto;
    padding: 2rem 1.6rem;

    .hero-wrapper {
        display: flex;
        flex-direction: column;
        align-items: flex-start;
        justify-content: center;
        width: 100%;
        max-width: 44rem;
    }

    .text {
        width: 100%;

        .my-name-is {
            font-size: 1.8rem;
            font-family: 'FontCaveat', serif;
            color: lighten(@blue-color, 15%);
        }

        .name {
            display: block;
            margin-bottom: 0.5rem;
            font-family: 'LatoFontBold', serif;
            font-size: 3.2rem;
            color: @blue-color;
            line-height: 1.1;
        }

        .tagline {
            font-size: 1.3rem;
            font-family: 'LatoFontBold', serif;
            margin-bottom: 0.8rem;
            color: inherit;
            letter-spacing: 0.02rem;
        }

        .sub-tagline {
            font-size: 1.1rem;
            line-height: 1.7rem;
            font-family: 'LatoFontRegular', serif;
            opacity: 0.9;
            margin-bottom: 1.6rem;
            max-width: 38rem;
        }

        .cta-actions {
            display: flex;
            gap: 1rem;
            flex-wrap: wrap;

            a {
                display: inline-flex;
                align-items: center;
                justify-content: center;
                text-decoration: none;
                cursor: pointer;
                font-family: 'LatoFontBold', serif;
                padding: 0.75rem 1.8rem;
                border-radius: 0.6rem;
                font-size: 1.05rem;
                transition: transform ease @hover-time, background-color ease @hover-time, color ease @hover-time, border-color ease @hover-time, box-shadow ease @hover-time;
            }

            .btn-primary {
                background-color: @blue-color;
                color: #0a1929;
                border: solid @blue-color 0.15rem;
                box-shadow: 0 0 15px fade(@blue-color, 35%);

                &:hover {
                    transform: translateY(-2px);
                    background-color: lighten(@blue-color, 10%);
                    box-shadow: 0 0 22px fade(@blue-color, 60%);
                }
            }
        }
    }
}

@media (min-width: @first-breakpoint) {
    .landing-page {
        min-height: calc(100vh - @navbar-height - @navbar-border);

        .hero-wrapper {
            max-width: 48rem;
        }

        .text {
            .my-name-is {
                font-size: 2.5rem;
            }
            .name {
                font-size: 4.5rem;
            }
            .tagline {
                font-size: 1.5rem;
            }
            .sub-tagline {
                font-size: 1.25rem;
                line-height: 1.9rem;
            }
        }
    }
}

</style>

