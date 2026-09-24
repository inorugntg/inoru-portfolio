<script setup lang="ts">
import { Icon } from '@iconify/vue';
import { useLanguageSwitcher } from '@/composables/useLanguageSwitcher';
import { useCursorHover } from '@/directives/useCursorHover';
import { useThemeStore } from '@/stores/theme';
import { DarkTheme, LightTheme } from '@/constants/app';

const { t } = useLanguageSwitcher();

const vCursorHover = useCursorHover();

const themeStore = useThemeStore();

</script>

<template>
    <footer
        class="footer"
        :class="{ 'footer-dark-theme': themeStore.theme === DarkTheme,
                  'footer-light-theme': themeStore.theme === LightTheme }"
    >
        <h3 class="info">
            {{ t('footer.text') }}
        </h3>

        <!-- icons visible on footer while screen is small -->
        <div class="icons">
            <a
                class="link"
                target="_blank"
                rel="noopener noreferrer"
                aria-label="LinkedIn"
                href="https://www.linkedin.com/in/inoru-akhmad-5082b0270/"
                v-cursor-hover
            >
                <Icon icon="logos:linkedin-icon" width="22" class="linkedin-icon" />
            </a>

            <a
                class="link"
                target="_blank"
                rel="noopener noreferrer"
                aria-label="GitHub"
                href="https://github.com/inorugntg"
                v-cursor-hover
            >
                <Icon icon="akar-icons:github-fill" width="22" />
            </a>

            <a
                class="link"
                aria-label="Gmail"
                href="mailto:inoru375@gmail.com"
                v-cursor-hover
            >
                <Icon icon="logos:google-gmail" width="22" class="gmail-icon" />
            </a>
        </div>

        <!-- icons on left side of screen while screen is big (Fixed di kiri bawah) -->
        <div class="icons-on-big-screens">
            <a
                class="link"
                target="_blank"
                rel="noopener noreferrer"
                aria-label="LinkedIn"
                href="https://www.linkedin.com/in/inoru-akhmad-5082b0270/"
                v-cursor-hover
            >
                <Icon icon="logos:linkedin-icon" width="34" class="linkedin-icon" />
            </a>

            <a
                class="link"
                target="_blank"
                rel="noopener noreferrer"
                aria-label="GitHub"
                href="https://github.com/inorugntg"
                v-cursor-hover
            >
                <Icon icon="akar-icons:github-fill" width="34" />
            </a>

            <a
                class="link"
                aria-label="Gmail"
                href="mailto:inoru375@gmail.com"
                v-cursor-hover
            >
                <Icon icon="logos:google-gmail" width="34" class="gmail-icon" />
            </a>
        </div>
    </footer>
</template>

<style lang="less" scoped>
@import '@/styles/variables.less';

.footer {
    display: flex;
    align-items: center;
    justify-content: center;
    flex-wrap: wrap;
    min-height: 4rem;
    min-width: 100%;
    border-top: solid @blue-color 0.1rem;

    a {
        text-decoration: none;
        color: inherit;
        cursor: pointer;
    }
    .linkedin-icon {
        background-color: white;
        border-radius: 4px;
    }
    .info {
        text-align: center;
        padding-right: 0.3rem;
        font-family: 'LatoFontLight', serif;
        font-size: 0.95rem;
    }
    .icons {
        display: flex;
        align-items: center;
        gap: 1rem;
        padding: 0.5rem 0;

        .link {
            display: flex;
            align-items: center;
        }
    }
    .icons-on-big-screens {
        display: none;
        align-items: center;
        justify-content: space-evenly;
        flex-direction: column;
        position: fixed;
        bottom: 2rem;
        left: 1rem;
        width: 3.5rem;
        height: 9.5rem;
        z-index: 10;

        a {
            display: flex;
            align-items: center;
            justify-content: center;
            width: 100%;
            transition: transform ease @hover-time;

            &:hover {
                transform: scale(1.18);
            }
        }
    }
}

@media (min-width: @first-breakpoint) {
    .footer {
        .info {
            font-size: 1.1rem;
            padding-right: 0.7rem;
        }
        .icons {
            padding-top: 0.2rem;
        }
    }
}

@media (min-width: @footer-icons-breakpoint) {
    .footer {
        .icons {
            display: none;
        }

        .icons-on-big-screens {
            display: flex;
        }
    }
}

.footer-dark-theme {
    background-color: #dark[background-color-on-element];
}
.footer-light-theme {
    background-color: #light[background-color-on-element];
}

</style>
