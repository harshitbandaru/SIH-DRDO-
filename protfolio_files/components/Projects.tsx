'use client';

import React from 'react';
import Image from 'next/image';
import { motion } from 'framer-motion';
import { ExternalLink, Github, Monitor, Sparkles } from 'lucide-react';
import { PORTFOLIO_DATA, ProjectItem } from '@/data/portfolio';

export default function Projects() {
  const { projects } = PORTFOLIO_DATA;

  return (
    <section
      id="projects"
      className="relative min-h-screen w-full py-28 px-6 md:px-12 bg-[#0a0e1a] overflow-hidden"
    >
      {/* Background Subtle Glows */}
      <div className="absolute top-1/4 left-10 w-[500px] h-[500px] bg-accent-cyan/10 rounded-full blur-[180px] pointer-events-none" />
      <div className="absolute bottom-1/4 right-10 w-[500px] h-[500px] bg-accent-pink/10 rounded-full blur-[180px] pointer-events-none" />

      <div className="relative z-10 max-w-6xl mx-auto">
        {/* Section Header */}
        <div className="mb-20">
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            transition={{ duration: 0.5 }}
            className="text-xs font-mono tracking-widest text-accent-pink uppercase mb-3"
          >
            // 03 . Work Showcase
          </motion.div>
          <motion.h2
            initial={{ opacity: 0, y: 30 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            transition={{ duration: 0.7 }}
            className="text-4xl sm:text-6xl font-black font-cabinet tracking-tight text-white mb-4"
          >
            SELECTED PROJECTS
          </motion.h2>
          <motion.p
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            transition={{ duration: 0.7, delay: 0.1 }}
            className="text-slate-400 text-base sm:text-lg max-w-2xl"
          >
            A curated showcase of recent digital applications, motion-heavy interfaces, and interactive WebGL experiences.
          </motion.p>
        </div>

        {/* Projects Stack (Z-Pattern Layout) */}
        <div className="space-y-24">
          {projects.map((project: ProjectItem, index: number) => {
            const isEven = index % 2 === 0;
            return (
              <motion.div
                key={project.id}
                initial={{ opacity: 0, y: 50 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true, margin: '-100px' }}
                transition={{ duration: 0.8, ease: [0.16, 1, 0.3, 1] }}
                className="relative rounded-[32px] bg-white/[0.04] border border-white/20 backdrop-blur-3xl p-6 sm:p-10 lg:p-12 overflow-hidden shadow-2xl group transition-all duration-500 hover:border-white/35"
              >
                {/* Corner Ambient Glow Spheres inside Card */}
                <div className="absolute -top-24 -left-24 w-64 h-64 bg-accent-cyan/20 rounded-full blur-[100px] pointer-events-none group-hover:bg-accent-cyan/35 transition-all duration-700" />
                <div className="absolute -bottom-24 -right-24 w-64 h-64 bg-accent-pink/20 rounded-full blur-[100px] pointer-events-none group-hover:bg-accent-pink/35 transition-all duration-700" />

                <div
                  className={`relative z-10 grid grid-cols-1 lg:grid-cols-12 gap-8 lg:gap-12 items-center ${
                    isEven ? '' : 'lg:flex-row-reverse'
                  }`}
                >
                  {/* Text Information Column */}
                  <div
                    className={`lg:col-span-6 space-y-6 ${
                      isEven ? 'lg:order-1' : 'lg:order-2'
                    }`}
                  >
                    {/* Index & Header */}
                    <div className="flex items-center gap-3">
                      <span className="text-xs font-mono text-accent-pink font-bold px-3 py-1 rounded-full bg-accent-pink/10 border border-accent-pink/20">
                        {project.number}
                      </span>
                      <span className="h-px flex-1 bg-white/10" />
                    </div>

                    <h3 className="text-3xl sm:text-4xl font-extrabold font-cabinet text-white group-hover:text-accent-pink transition-colors">
                      {project.title}
                    </h3>

                    <p className="text-slate-300 text-base leading-relaxed font-light">
                      {project.description}
                    </p>

                    {/* Tech Stack Badges */}
                    <div className="flex flex-wrap gap-2 pt-2">
                      {project.techStack.map((tech) => (
                        <span
                          key={tech}
                          className="px-3 py-1 rounded-full bg-white/5 border border-white/10 text-xs font-mono text-slate-300 tracking-wider"
                        >
                          {tech}
                        </span>
                      ))}
                    </div>

                    {/* Actions / CTA Buttons */}
                    <div className="flex items-center gap-4 pt-4">
                      <a
                        href={project.liveUrl}
                        target="_blank"
                        rel="noopener noreferrer"
                        className="inline-flex items-center gap-2 px-6 py-3 rounded-full bg-accent-pink text-[#0a0e1a] font-bold text-xs tracking-wider uppercase hover:bg-white hover:shadow-[0_0_25px_rgba(255,255,255,0.4)] transition-all duration-300"
                      >
                        <span>Live Preview</span>
                        <ExternalLink className="w-4 h-4" />
                      </a>

                      {project.githubUrl && (
                        <a
                          href={project.githubUrl}
                          target="_blank"
                          rel="noopener noreferrer"
                          className="p-3 rounded-full bg-white/5 border border-white/10 text-slate-300 hover:text-white hover:bg-white/15 hover:border-white/30 transition-all"
                          aria-label="View Source Code"
                        >
                          <Github className="w-4 h-4" />
                        </a>
                      )}
                    </div>
                  </div>

                  {/* Browser Mockup Window Column */}
                  <div
                    className={`lg:col-span-6 ${
                      isEven ? 'lg:order-2' : 'lg:order-1'
                    }`}
                  >
                    <div className="relative rounded-2xl border border-white/20 bg-[#0c101d] overflow-hidden shadow-2xl group-hover:border-accent-pink/40 group-hover:shadow-[0_0_40px_rgba(0,0,0,0.8)] transition-all duration-500">
                      
                      {/* macOS Window Title Bar */}
                      <div className="flex items-center justify-between px-4 py-3 bg-white/5 border-b border-white/10">
                        <div className="flex items-center gap-2">
                          <span className="w-3 h-3 rounded-full bg-rose-500/80 inline-block" />
                          <span className="w-3 h-3 rounded-full bg-amber-500/80 inline-block" />
                          <span className="w-3 h-3 rounded-full bg-emerald-500/80 inline-block" />
                        </div>
                        <div className="flex items-center gap-1.5 px-3 py-0.5 rounded-full bg-black/40 text-[11px] font-mono text-slate-400">
                          <Monitor className="w-3 h-3 text-accent-cyan" />
                          <span className="truncate max-w-[150px]">{project.title.toLowerCase().replace(/\s+/g, '')}.app</span>
                        </div>
                        <Sparkles className="w-3.5 h-3.5 text-accent-pink/50" />
                      </div>

                      {/* Mockup Screenshot Container */}
                      <div className="relative aspect-[16/10] w-full overflow-hidden bg-slate-950">
                        <Image
                          src={project.image}
                          alt={project.title}
                          fill
                          className="object-cover object-top group-hover:scale-105 transition-transform duration-700"
                        />
                        <div className="absolute inset-0 bg-gradient-to-t from-[#0a0e1a]/60 via-transparent to-transparent" />
                      </div>
                    </div>
                  </div>
                </div>
              </motion.div>
            );
          })}
        </div>
      </div>
    </section>
  );
}
