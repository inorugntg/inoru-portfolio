<script setup lang="ts">
import { useLanguageSwitcher } from '@/composables/useLanguageSwitcher';
import { useCursorHover } from '@/directives/useCursorHover';
import { EnglishLanguage, IndonesiaLanguage } from '@/constants/app';

const { t, changeLanguage } = useLanguageSwitcher();

const vCursorHover = useCursorHover();

</script>

<template>
    <div data-aos="zoom-in-up">
        <button
            class="change-language-button"
            v-cursor-hover
            @click="changeLanguage(IndonesiaLanguage);"
        >
            <img
                src="@/assets/images/flags/ina.png"
                class="flag"
                width="50"
                height="50"
                :alt="t('navbar.images.indonesiaFlag')"
            >
        </button>

        <button
            class="change-language-button"
            v-cursor-hover
            @click="changeLanguage(EnglishLanguage);"
        >
            <img
                src="@/assets/images/flags/en.png"
                class="flag"
                width="50"
                height="50"
                :alt="t('navbar.images.greatBritainFlag')"
            >
        </button>
    </div>
</template>

<style lang="less" scoped>
@import '@/styles/variables.less';

.change-language-button {
    position: relative;
    width: 2.5rem;
    height: 2.5rem;
    color: inherit;
    border: none;
    background-color: transparent;
    cursor: pointer;
}
.flag {
    max-width: 80%;
    height: auto;
}

@media (min-width: @first-breakpoint) {
    .change-language-button {
        width: 3rem;
        height: 3rem;
    }
}

</style>
