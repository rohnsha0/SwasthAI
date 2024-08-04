// @ts-check
// `@type` JSDoc annotations allow editor autocompletion and type checking
// (when paired with `@ts-check`).
// There are various equivalent ways to declare your Docusaurus config.
// See: https://docusaurus.io/docs/api/docusaurus-config

import {themes as prismThemes} from 'prism-react-renderer';

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'SwasthAI',
  tagline: 'Your Health Our Priority',
  favicon: 'img/logoSQT.png',

  // Set the production url of your site here
  url: 'https://swasthai.rohanshaw.me',
  // Set the /<baseUrl>/ pathname under which your site is served
  // For GitHub pages deployment, it is often '/<projectName>/'
  baseUrl: '/',

  // GitHub pages deployment config.
  // If you aren't using GitHub pages, you don't need these.
  organizationName: 'rohnsha0', // Usually your GitHub org/user name.
  projectName: 'SwasthAI', // Usually your repo name.

  onBrokenLinks: 'ignore',
  onBrokenMarkdownLinks: 'ignore',

  // Even if you don't use internationalization, you can use this field to set
  // useful metadata like html lang. For example, if your site is Chinese, you
  // may want to replace "en" with "zh-Hans".
  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  presets: [
    [
      'classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({

        docs: {
          sidebarPath: './sidebars.js',
          // Please change this to your repo.
          // Remove this to remove the "edit this page" links.
          //editUrl:
            //'https://github.com/facebook/docusaurus/tree/main/packages/create-docusaurus/templates/shared/',
        },
        blog: {
          showReadingTime: true,
          // Please change this to your repo.
          // Remove this to remove the "edit this page" links.
          //editUrl:
          //  'https://github.com/facebook/docusaurus/tree/main/packages/create-docusaurus/templates/shared/',
        },
        theme: {
          customCss: './src/css/custom.css',
        },
      }),
    ],
  ],

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      // Replace with your project's social card
      image: 'https://i.postimg.cc/PrC9PpsT/image1.jpg',
      navbar: {
        title: 'SwasthAI',
        logo: {
          alt: 'SwasthAI Logo',
          src: 'img/logoSQT.png',
        },
        items: [
          {
            to: '/try',
            label: 'Try It Out',
            position: 'left',
          },
          {
            type: 'docSidebar',
            sidebarId: 'tutorialSidebar',
            position: 'right',
            label: 'Documentation',
          },
          {to: '/blog', label: 'Blog', position: 'right'},
          {
            href: 'https://github.com/rohnsha0/SwasthAI-androidApp',
            label: 'GitHub',
            position: 'right',
          },
        ],
      },
      footer: {
        style: 'dark',
        links: [
          {
            title: 'Docs',
            items: [
              {
                label: 'About Us',
                to: '/docs/about',
              },
            ],
          },
          {
            title: 'Contact Developer',
            items: [
              {
                label: 'LinkedIn',
                href: 'https://www.linkedin.com/in/rohnsha0/',
              },
              {
                label: 'Github',
                href: 'https://github.com/rohnsha0',
              },
              //{
                //label: 'Twitter',
                //href: 'https://twitter.com/docusaurus',
              //},
            ],
          },
          {
            title: 'More',
            items: [
              {
                label: 'Blog',
                to: '/blog',
              },
              {
                label: 'GitHub',
                href: 'https://github.com/rohnsha0/SwasthAI',
              },
            ],
          },
        ],
        copyright: `Copyright © ${new Date().getFullYear()} SwasthAI. Built with ❤️ by Rohan Shaw.`,
      },
      prism: {
        theme: prismThemes.github,
        darkTheme: prismThemes.dracula,
      },
      colorMode: {
        defaultMode: 'light',
        disableSwitch: false,
        respectPrefersColorScheme: true,
      },
    }),
};

export default config;
