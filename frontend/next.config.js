/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  output: 'standalone',
  webpack: (config) => {
    return config;
  },
  // Garantir que o CSS seja processado corretamente
  transpilePackages: ['@tailwindcss/postcss'],
}

module.exports = nextConfig
