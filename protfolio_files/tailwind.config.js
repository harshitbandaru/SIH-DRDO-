/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './app/**/*.{js,ts,jsx,tsx,mdx}',
    './components/**/*.{js,ts,jsx,tsx,mdx}',
    './data/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  theme: {
    extend: {
      colors: {
        bg: {
          dark: '#0a0e1a',
          card: 'rgba(255, 255, 255, 0.04)',
          pill: 'rgba(10, 14, 26, 0.5)',
        },
        accent: {
          pink: '#FFB6C1',
          cyan: '#00F0FF',
          purple: '#7000FF',
        },
      },
      fontFamily: {
        josefin: ['var(--font-josefin)', 'sans-serif'],
        poppins: ['var(--font-poppins)', 'sans-serif'],
        lexend: ['var(--font-lexend)', 'sans-serif'],
        cabinet: ['Cabinet Grotesk', 'var(--font-lexend)', 'sans-serif'],
      },
      animation: {
        marquee: 'marquee 35s linear infinite',
        'marquee-fast': 'marquee 20s linear infinite',
        'pulse-glow': 'pulseGlow 4s ease-in-out infinite',
        shine: 'textShine 6s ease-in-out infinite',
        float: 'float 6s ease-in-out infinite',
      },
      keyframes: {
        marquee: {
          '0%': { transform: 'translateX(0%)' },
          '100%': { transform: 'translateX(-50%)' },
        },
        pulseGlow: {
          '0%, 100%': { opacity: '0.4', transform: 'scale(1)' },
          '50%': { opacity: '0.8', transform: 'scale(1.08)' },
        },
        textShine: {
          '0%, 100%': { 'background-size': '200% 200%', 'background-position': 'left center' },
          '50%': { 'background-size': '200% 200%', 'background-position': 'right center' },
        },
        float: {
          '0%, 100%': { transform: 'translateY(0px)' },
          '50%': { transform: 'translateY(-10px)' },
        },
      },
      backdropBlur: {
        '3xl': '64px',
      },
    },
  },
  plugins: [require('@tailwindcss/typography')],
};
