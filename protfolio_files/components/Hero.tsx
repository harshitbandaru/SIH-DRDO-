'use client';

import React from 'react';
import dynamic from 'next/dynamic';
import Image from 'next/image';
import { motion } from 'framer-motion';
import { ArrowUpRight, Sparkles } from 'lucide-react';
import { PORTFOLIO_DATA } from '@/data/portfolio';

// Dynamic import for Three.js Canvas component with SSR disabled
const HeroCanvas = dynamic(() => import('@/components/HeroCanvas'), {
  ssr: false,
  loading: () => <div className="absolute inset-0 bg-[#0a0e1a]" />,
});

export default function Hero() {
  const { hero } = PORTFOLIO_DATA;

  return (
    <section
      id="home"
      className="relative min-h-screen w-full flex items-center justify-center pt-24 pb-16 overflow-hidden bg-[#0a0e1a]"
    >
      {/* Three.js Interactive Canvas Background (Desktop) */}
      <div className="hidden lg:block absolute inset-0 z-0">
        <HeroCanvas />
        {/* Radial Dark Mask Overlay to blend canvas with content */}
        <div className="absolute inset-0 bg-radial-gradient from-transparent via-[#0a0e1a]/60 to-[#0a0e1a] pointer-events-none" />
        <div className="absolute inset-0 bg-gradient-to-t from-[#0a0e1a] via-transparent to-[#0a0e1a]/80 pointer-events-none" />
      </div>

      {/* Fallback Hero Subject Image (Mobile & Tablet Layout) */}
      <div className="block lg:hidden absolute inset-0 z-0 pointer-events-none">
        <Image
          src={hero.fallbackImage}
          alt="Hero Subject"
          fill
          className="object-cover object-center opacity-30 mix-blend-luminosity scale-105"
          priority
        />
        <div className="absolute inset-0 bg-gradient-to-b from-[#0a0e1a]/90 via-[#0a0e1a]/70 to-[#0a0e1a]" />
      </div>

      {/* Subtle Glow Spheres */}
      <div className="absolute top-1/3 left-1/4 w-[500px] h-[500px] bg-accent-pink/15 rounded-full blur-[180px] pointer-events-none animate-pulse-glow" />
      <div className="absolute bottom-1/4 right-1/4 w-[500px] h-[500px] bg-accent-cyan/15 rounded-full blur-[180px] pointer-events-none animate-pulse-glow" style={{ animationDelay: '2s' }} />

      {/* Main Content Container */}
      <div className="relative z-10 w-full max-w-6xl px-6 md:px-12 flex flex-col justify-center items-start">
        
        {/* Badge Indicator */}
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.6, delay: 0.2 }}
          className="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-white/5 border border-white/10 backdrop-blur-xl mb-6 shadow-lg shadow-black/40"
        >
          <Sparkles className="w-4 h-4 text-accent-pink animate-pulse" />
          <span className="text-xs font-mono tracking-widest text-slate-300 uppercase">
            Frontend Architect & Creative Developer
          </span>
        </motion.div>

        {/* Headline */}
        <motion.h1
          initial={{ opacity: 0, y: 30 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8, delay: 0.3, ease: [0.16, 1, 0.3, 1] }}
          className="text-6xl sm:text-8xl md:text-9xl font-black font-cabinet tracking-tight leading-none text-white mb-2"
        >
          <span className="text-shine inline-block">{hero.headline}</span>
        </motion.h1>

        {/* Subtitle */}
        <motion.div
          initial={{ opacity: 0, y: 30 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8, delay: 0.45, ease: [0.16, 1, 0.3, 1] }}
          className="text-2xl sm:text-4xl md:text-5xl font-extrabold font-cabinet tracking-wider text-slate-200 uppercase mb-8"
        >
          {hero.subtitle}
        </motion.div>

        {/* Subtext Paragraph */}
        <motion.p
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.7, delay: 0.6 }}
          className="max-w-2xl text-slate-400 text-base sm:text-lg leading-relaxed mb-10"
        >
          {hero.description}
        </motion.p>

        {/* CTA Glassmorphism Button */}
        <motion.div
          initial={{ opacity: 0, scale: 0.95 }}
          animate={{ opacity: 1, scale: 1 }}
          transition={{ duration: 0.6, delay: 0.75 }}
        >
          <a
            href={hero.ctaHref}
            className="group relative inline-flex items-center gap-3 px-8 py-4 rounded-full bg-accent-pink/10 border border-accent-pink/60 backdrop-blur-2xl text-white font-medium tracking-wider text-sm transition-all duration-500 hover:bg-accent-pink/20 hover:border-accent-pink hover:shadow-[0_0_30px_rgba(255,182,193,0.4)]"
          >
            <span>{hero.ctaText}</span>
            <div className="p-1 rounded-full bg-accent-pink text-[#0a0e1a] group-hover:translate-x-1 group-hover:-translate-y-1 transition-transform duration-300">
              <ArrowUpRight className="w-4 h-4 font-bold" />
            </div>
          </a>
        </motion.div>
      </div>

      {/* Bottom Gradient Fade */}
      <div className="absolute bottom-0 left-0 right-0 h-32 bg-gradient-to-t from-[#0a0e1a] to-transparent pointer-events-none" />
    </section>
  );
}
