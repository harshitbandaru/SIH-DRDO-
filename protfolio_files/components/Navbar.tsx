'use client';

import React, { useState, useEffect } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { Github, Linkedin, Instagram, Menu, X, ArrowUpRight } from 'lucide-react';
import { PORTFOLIO_DATA, SocialLink } from '@/data/portfolio';

const getSocialIcon = (iconName: SocialLink['iconName']) => {
  switch (iconName) {
    case 'Github':
      return <Github className="w-4 h-4" />;
    case 'Linkedin':
      return <Linkedin className="w-4 h-4" />;
    case 'Instagram':
      return <Instagram className="w-4 h-4" />;
    default:
      return <Github className="w-4 h-4" />;
  }
};

export default function Navbar() {
  const [isOpen, setIsOpen] = useState(false);
  const [scrolled, setScrolled] = useState(false);

  useEffect(() => {
    const handleScroll = () => {
      if (window.scrollY > 40) {
        setScrolled(true);
      } else {
        setScrolled(false);
      }
    };
    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  // Lock body scroll when drawer is open
  useEffect(() => {
    if (isOpen) {
      document.body.style.overflow = 'hidden';
    } else {
      document.body.style.overflow = 'unset';
    }
  }, [isOpen]);

  return (
    <>
      <header className="fixed top-0 left-0 right-0 z-50 flex items-center justify-center px-4 py-6 pointer-events-none">
        <motion.div
          initial={{ y: -50, opacity: 0 }}
          animate={{ y: 0, opacity: 1 }}
          transition={{ duration: 0.7, ease: [0.16, 1, 0.3, 1] }}
          className={`pointer-events-auto flex items-center justify-between w-full max-w-5xl px-5 py-3 rounded-full border transition-all duration-300 ${
            scrolled
              ? 'bg-[#0a0e1a]/80 backdrop-blur-3xl border-white/20 shadow-2xl shadow-black/80'
              : 'bg-[#0a0e1a]/50 backdrop-blur-3xl border-white/15'
          }`}
        >
          {/* Left Brand & Menu Toggle */}
          <div className="flex items-center gap-3">
            <button
              onClick={() => setIsOpen(!isOpen)}
              className="p-2 rounded-full bg-white/5 border border-white/10 hover:bg-white/15 hover:border-white/25 transition-all text-white focus:outline-none"
              aria-label="Toggle Menu"
            >
              {isOpen ? (
                <X className="w-5 h-5 text-accent-pink" />
              ) : (
                <Menu className="w-5 h-5 text-white" />
              )}
            </button>
            <a
              href="#home"
              className="text-lg font-bold tracking-widest text-white font-cabinet hover:text-accent-pink transition-colors"
            >
              {PORTFOLIO_DATA.brandName}
            </a>
          </div>

          {/* Center Navigation Links (Desktop) */}
          <nav className="hidden md:flex items-center gap-8">
            {PORTFOLIO_DATA.navLinks.map((link) => (
              <a
                key={link.id}
                href={link.href}
                className="text-sm font-medium text-slate-300 hover:text-accent-pink transition-colors flex items-center gap-1.5 group"
              >
                <span className="text-[11px] font-mono text-accent-pink/70 group-hover:text-accent-pink">
                  {link.number}
                </span>
                <span>{link.label}</span>
              </a>
            ))}
          </nav>

          {/* Right Social Icon Pills */}
          <div className="flex items-center gap-2">
            {PORTFOLIO_DATA.socialLinks.map((social) => (
              <a
                key={social.name}
                href={social.url}
                target="_blank"
                rel="noopener noreferrer"
                className="p-2.5 rounded-full bg-white/5 border border-white/10 text-slate-300 hover:text-accent-pink hover:border-accent-pink/50 hover:bg-accent-pink/10 hover:shadow-[0_0_15px_rgba(255,182,193,0.35)] transition-all duration-300"
                aria-label={social.name}
              >
                {getSocialIcon(social.iconName)}
              </a>
            ))}
          </div>
        </motion.div>
      </header>

      {/* Staggered Navigation Drawer Menu */}
      <AnimatePresence>
        {isOpen && (
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            transition={{ duration: 0.4 }}
            className="fixed inset-0 z-40 bg-[#0a0e1a]/95 backdrop-blur-3xl flex flex-col justify-between p-8 md:p-16"
          >
            {/* Background Glow Orbs */}
            <div className="absolute top-1/4 left-10 w-96 h-96 bg-accent-pink/10 rounded-full blur-[140px] pointer-events-none" />
            <div className="absolute bottom-1/4 right-10 w-96 h-96 bg-accent-cyan/10 rounded-full blur-[140px] pointer-events-none" />

            {/* Top Empty Space offset for header */}
            <div className="h-20" />

            {/* Nav Drawer Links Container */}
            <div className="max-w-4xl mx-auto w-full flex flex-col justify-center flex-1">
              <span className="text-xs uppercase tracking-widest text-accent-pink/70 font-mono mb-6">
                // Navigation
              </span>
              <div className="space-y-4 md:space-y-6">
                {PORTFOLIO_DATA.navLinks.map((link, idx) => (
                  <motion.div
                    key={link.id}
                    initial={{ x: -60, opacity: 0 }}
                    animate={{ x: 0, opacity: 1 }}
                    exit={{ x: -40, opacity: 0 }}
                    transition={{
                      duration: 0.5,
                      delay: idx * 0.1,
                      ease: [0.16, 1, 0.3, 1],
                    }}
                  >
                    <a
                      href={link.href}
                      onClick={() => setIsOpen(false)}
                      className="group flex items-baseline gap-4 md:gap-8 text-4xl md:text-7xl font-bold font-cabinet text-white hover:text-accent-pink transition-all duration-300"
                    >
                      <span className="text-lg md:text-2xl font-mono text-accent-pink/60 group-hover:text-accent-pink">
                        {link.number}
                      </span>
                      <span>{link.label}</span>
                      <ArrowUpRight className="w-8 h-8 md:w-12 md:h-12 opacity-0 group-hover:opacity-100 group-hover:translate-x-2 group-hover:-translate-y-2 transition-all duration-300 text-accent-pink" />
                    </a>
                  </motion.div>
                ))}
              </div>
            </div>

            {/* Bottom Drawer Footer */}
            <motion.div
              initial={{ y: 20, opacity: 0 }}
              animate={{ y: 0, opacity: 1 }}
              transition={{ delay: 0.4 }}
              className="max-w-4xl mx-auto w-full pt-8 border-t border-white/10 flex flex-col sm:flex-row items-center justify-between gap-4 text-slate-400 text-sm"
            >
              <div className="flex items-center gap-2">
                <span className="w-2.5 h-2.5 rounded-full bg-emerald-400 animate-pulse" />
                <span>{PORTFOLIO_DATA.footer.statusText}</span>
              </div>

              <div className="flex items-center gap-6">
                {PORTFOLIO_DATA.socialLinks.map((social) => (
                  <a
                    key={social.name}
                    href={social.url}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="hover:text-accent-pink transition-colors font-medium"
                  >
                    {social.name}
                  </a>
                ))}
              </div>
            </motion.div>
          </motion.div>
        )}
      </AnimatePresence>
    </>
  );
}
