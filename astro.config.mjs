// @ts-check
import { defineConfig } from 'astro/config';
import react from '@astrojs/react';
import tailwind from '@astrojs/tailwind';

// https://astro.build/config
export default defineConfig({
  // Replace with your GitHub Pages URL
  site: 'https://github.com/KordjanCode',

  // Replace with your repository name, or leave blank if deploying to a root domain
  base: '',

  integrations: [react(),
    tailwind({
      applyBaseStyles: false,
    }),
  ],
});

// base: '/Macar_Website/'