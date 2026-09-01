'use client';

import React from 'react';
import { PORTFOLIO_DATA } from '@/data/portfolio';
import { ArrowUp } from 'lucide-react';

export default function Footer() {
  const { footer, navLinks, socialLinks } = PORTFOLIO_DATA;

  const scrollToTop = () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  return (
    <footer className="relative w-full bg-[#070a13] text-slate-400 pt-16 pb-12 px-6 md:px-12 border-t border-white/10">
      {/* Radial Top Gradient Separator Border Line */}
      <div className="absolute top-0 left-1/2 -translate-x-1/2 w-3/4 h-[1px] bg-gradient-to-r from-transparent via-accent-pink/60 to-transparent" />

      <div className="max-w-6xl mx-auto">
        <div className="grid grid-cols-1 md:grid-cols-12 gap-10 pb-12 border-b border-white/10">
          
          {/* Brand & Slogan Column */}
          <div className="md:col-span-5 space-y-4">
            <a
              href="#home"
              className="text-3xl font-black font-cabinet tracking-widest text-white hover:text-accent-pink transition-colors inline-block"
            >
              {footer.brandName}
            </a>
            <p className="text-sm text-slate-400 max-w-sm leading-relaxed">
              {footer.tagline}
            </p>

            {/* Live Status Badge */}
            <div className="inline-flex items-center gap-2.5 px-4 py-2 rounded-full bg-emerald-950/40 border border-emerald-500/30 text-emerald-400 text-xs font-mono">
              <span className="w-2 h-2 rounded-full bg-emerald-400 animate-pulse" />
              <span>{footer.statusText}</span>
            </div>
          </div>

          {/* Quick Links Column */}
          <div className="md:col-span-3 space-y-3">
            <h4 className="text-xs font-mono uppercase tracking-widest text-slate-200">
              Navigation
            </h4>
            <ul className="space-y-2 text-sm">
              {navLinks.map((link) => (
                <li key={link.id}>
                  <a
                    href={link.href}
                    className="hover:text-accent-pink transition-colors flex items-center gap-2"
                  >
                    <span className="text-[11px] font-mono text-slate-500">{link.number}</span>
                    <span>{link.label}</span>
                  </a>
                </li>
              ))}
            </ul>
          </div>

          {/* Connect & Socials Column */}
          <div className="md:col-span-4 space-y-3">
            <h4 className="text-xs font-mono uppercase tracking-widest text-slate-200">
              Connect
            </h4>
            <ul className="space-y-2 text-sm">
              {socialLinks.map((social) => (
                <li key={social.name}>
                  <a
                    href={social.url}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="hover:text-accent-pink transition-colors"
                  >
                    {social.name}
                  </a>
                </li>
              ))}
            </ul>
          </div>
        </div>

        {/* Bottom Bar: Copyright & Back To Top */}
        <div className="pt-8 flex flex-col sm:flex-row items-center justify-between gap-4 text-xs font-mono text-slate-500">
          <p>{footer.copyright}</p>

          <button
            onClick={scrollToTop}
            className="flex items-center gap-2 px-3 py-1.5 rounded-full bg-white/5 border border-white/10 hover:bg-white/10 hover:text-white transition-all text-slate-400 cursor-pointer"
          >
            <span>Back to top</span>
            <ArrowUp className="w-3.5 h-3.5 text-accent-pink" />
          </button>
        </div>
      </div>
    </footer>
  );
}
