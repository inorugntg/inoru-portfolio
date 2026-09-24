<script setup lang="ts">
import { useLanguageSwitcher } from '@/composables/useLanguageSwitcher';
import { useCursorHover } from '@/directives/useCursorHover';
import { useThemeStore } from '@/stores/theme';
import { FadeDown, FadeUp, DarkTheme, LightTheme } from '@/constants/app';
import { Icon } from '@iconify/vue';

const { t } = useLanguageSwitcher();
const vCursorHover = useCursorHover();
const themeStore = useThemeStore();

</script>

<template>
    <section
        id="contact"
        class="contact"
    >
        <h2 :data-aos="FadeDown" class="title">{{ t('contact.title') }}</h2>

        <div
            :data-aos="FadeUp"
            class="contact-container"
            :class="{ 'contact-dark-theme': themeStore.theme === DarkTheme,
                      'contact-light-theme': themeStore.theme === LightTheme }"
        >
            <div class="contact-item">
                <Icon
                    icon="mdi:map-marker"
                    width="30"
                    class="item-icon"
                />
                <span class="text">{{ t('contact.location') }}</span>
            </div>

            <a
                class="contact-item contact-link"
                href="mailto:inoru375@gmail.com"
                v-cursor-hover
            >
                <Icon
                    icon="clarity:email-solid"
                    width="28"
                    class="item-icon"
                />
                <span class="text">inoru375@gmail.com</span>
            </a>

            <div class="social-links">
                <a
                    class="social-btn"
                    href="https://www.linkedin.com/in/inoru-akhmad-5082b0270/"
                    target="_blank"
                    rel="noopener noreferrer"
                    v-cursor-hover
                >
                    <Icon icon="logos:linkedin-icon" width="24" class="linkedin-icon" />
                    <span>LinkedIn</span>
                </a>

                <a
                    class="social-btn"
                    href="https://github.com/inorugntg"
                    target="_blank"
                    rel="noopener noreferrer"
                    v-cursor-hover
                >
                    <Icon icon="akar-icons:github-fill" width="24" />
                    <span>GitHub</span>
                </a>
            </div>
        </div>

    </section>
</template>

<style lang="less" scoped>
@import '@/styles/variables.less';

.contact {
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    min-width: 100%;
    margin: auto;
    padding-bottom: 2.5rem;

    .title {
        float: left;
        width: 100%;
        min-height: 3rem;
        text-align: center;
        font-family: 'LatoFontBold', serif;
        font-size: 3rem;
        color: @blue-color;
    }

    .contact-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        gap: 1.2rem;
        width: 90%;
        max-width: 32rem;
        margin-top: 1.5rem;
        padding: 2rem 1.8rem;
        border: solid @blue-color 0.18rem;
        border-radius: 1rem;
        box-shadow: 0 0 20px fade(@blue-color, 20%);
        transition: background-color ease @theme-switch-time, box-shadow ease @hover-time;

        &:hover {
            box-shadow: 0 0 28px fade(@blue-color, 35%);
        }

        .contact-item {
            display: flex;
            align-items: center;
            gap: 0.8rem;
            font-size: 1.15rem;
            color: inherit;
            text-decoration: none;

            .item-icon {
                color: @blue-color;
                flex-shrink: 0;
            }

            .text {
                font-family: 'LatoFontRegular', serif;
            }
        }

        .contact-link {
            transition: color ease @hover-time;
            &:hover {
                color: @blue-color;
            }
        }

        .social-links {
            display: flex;
            gap: 1.2rem;
            margin-top: 0.6rem;
            flex-wrap: wrap;
            justify-content: center;

            .social-btn {
                display: flex;
                align-items: center;
                gap: 0.5rem;
                padding: 0.5rem 1.2rem;
                border: solid @blue-color 0.12rem;
                border-radius: 0.8rem;
                text-decoration: none;
                color: inherit;
                font-size: 1rem;
                font-family: 'LatoFontBold', serif;
                background-color: fade(@blue-color, 8%);
                transition: transform ease @hover-time, border-color ease @hover-time, background-color ease @hover-time, box-shadow ease @hover-time;

                &:hover {
                    border-color: lighten(@blue-color, 15%);
                    background-color: fade(@blue-color, 18%);
                    transform: translateY(-2px);
                    box-shadow: 0 0 14px fade(@blue-color, 30%);
                }

                .linkedin-icon {
                    background-color: white;
                    border-radius: 4px;
                }
            }
        }
    }
}

.contact-dark-theme {
    background-color: #dark[background-color-on-element];
    color: #dark[text-color];
}

.contact-light-theme {
    background-color: #light[background-color-on-element];
    color: #light[text-color];
}

@media (min-width: @first-breakpoint) {
    .contact {
        min-width: 36rem;
        max-width: 44rem;
        padding-bottom: 7rem;

        .title {
            min-height: 4rem;
        }

        .contact-container {
            width: 100%;
            padding: 2.2rem 2.2rem;

            .contact-item {
                font-size: 1.25rem;
            }
        }
    }
}

</style>
