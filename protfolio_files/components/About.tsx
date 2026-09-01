'use client';

import React, { useState } from 'react';
import Image from 'next/image';
import { motion } from 'framer-motion';
import { Code2, Database, Layout, Cpu, CheckCircle2 } from 'lucide-react';
import { PORTFOLIO_DATA, ToolNode } from '@/data/portfolio';

const getCategoryIcon = (id: string) => {
  switch (id) {
    case 'frontend':
      return <Code2 className="w-5 h-5 text-accent-cyan" />;
    case 'backend':
      return <Database className="w-5 h-5 text-accent-pink" />;
    case 'ui':
      return <Layout className="w-5 h-5 text-accent-purple" />;
    default:
      return <Cpu className="w-5 h-5 text-white" />;
  }
};

export default function About() {
  const { about } = PORTFOLIO_DATA;
  const [activeNode, setActiveNode] = useState<string | null>(null);

  // Split title into words for staggered word reveal
  const titleWords = about.title.split(' ');

  return (
    <section
      id="about"
      className="relative min-h-screen w-full py-28 px-6 md:px-12 bg-[#0a0e1a] overflow-hidden"
    >
      {/* Background Image Blend Overlay */}
      <div className="absolute inset-0 z-0 pointer-events-none">
        <Image
          src={about.bgImage}
          alt="About Background"
          fill
          className="object-cover object-center opacity-25 mix-blend-overlay"
        />
        <div className="absolute inset-0 bg-radial-gradient from-transparent via-[#0a0e1a]/80 to-[#0a0e1a]" />
        <div className="absolute inset-0 bg-gradient-to-b from-[#0a0e1a] via-transparent to-[#0a0e1a]" />
      </div>

      {/* Glow Orbs */}
      <div className="absolute top-1/2 right-10 w-96 h-96 bg-accent-cyan/10 rounded-full blur-[160px] pointer-events-none" />
      <div className="absolute bottom-20 left-10 w-96 h-96 bg-accent-purple/15 rounded-full blur-[160px] pointer-events-none" />

      <div className="relative z-10 max-w-6xl mx-auto">
        {/* Section Header Tag */}
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.5 }}
          className="text-xs font-mono tracking-widest text-accent-pink uppercase mb-4"
        >
          // 02 . About & Skill Architecture
        </motion.div>

        {/* Staggered Word Reveal Title */}
        <div className="flex flex-wrap gap-x-3 gap-y-1 max-w-4xl mb-16">
          {titleWords.map((word, idx) => (
            <motion.span
              key={idx}
              initial={{ opacity: 0, y: 25 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{
                duration: 0.6,
                delay: idx * 0.08,
                ease: [0.16, 1, 0.3, 1],
              }}
              className="text-4xl sm:text-6xl font-black font-cabinet tracking-tight text-white"
            >
              {word}
            </motion.span>
          ))}
        </div>

        {/* Two-Column Grid Layout */}
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-12 lg:gap-16 items-center">
          
          {/* Left Column: Bio Paragraphs */}
          <motion.div
            initial={{ opacity: 0, x: -30 }}
            whileInView={{ opacity: 1, x: 0 }}
            viewport={{ once: true }}
            transition={{ duration: 0.7 }}
            className="lg:col-span-5 space-y-6"
          >
            {about.bio.map((paragraph, index) => (
              <p
                key={index}
                className="text-slate-300 text-base md:text-lg leading-relaxed font-light"
              >
                {paragraph}
              </p>
            ))}

            <div className="pt-4 flex flex-wrap gap-4 text-xs font-mono text-slate-400">
              <div className="flex items-center gap-2 px-3.5 py-2 rounded-full bg-white/5 border border-white/10">
                <span className="w-2 h-2 rounded-full bg-accent-cyan" />
                <span>Performance-Driven</span>
              </div>
              <div className="flex items-center gap-2 px-3.5 py-2 rounded-full bg-white/5 border border-white/10">
                <span className="w-2 h-2 rounded-full bg-accent-pink" />
                <span>Motion-Focused</span>
              </div>
              <div className="flex items-center gap-2 px-3.5 py-2 rounded-full bg-white/5 border border-white/10">
                <span className="w-2 h-2 rounded-full bg-accent-purple" />
                <span>Clean Architecture</span>
              </div>
            </div>
          </motion.div>

          {/* Right Column: Interactive Skill Tree Node Graph */}
          <motion.div
            initial={{ opacity: 0, scale: 0.95 }}
            whileInView={{ opacity: 1, scale: 1 }}
            viewport={{ once: true }}
            transition={{ duration: 0.8 }}
            className="lg:col-span-7 relative p-6 sm:p-8 rounded-3xl bg-white/[0.03] border border-white/15 backdrop-blur-2xl"
          >
            <div className="mb-6 flex items-center justify-between">
              <h3 className="text-xl font-bold font-cabinet text-white flex items-center gap-2">
                <Cpu className="w-5 h-5 text-accent-pink" />
                <span>Interactive Skill Architecture</span>
              </h3>
              <span className="text-xs font-mono text-slate-400">
                [Hover / Tap Nodes]
              </span>
            </div>

            {/* Central Node & Floating Tooltip Cards */}
            <div className="relative min-h-[420px] flex flex-col md:flex-row items-center justify-between gap-6">
              
              {/* Central Trigger Node Button */}
              <div className="relative z-20 flex flex-col items-center">
                <motion.button
                  whileHover={{ scale: 1.08 }}
                  whileTap={{ scale: 0.95 }}
                  onClick={() => setActiveNode(activeNode ? null : 'all')}
                  onMouseEnter={() => setActiveNode('all')}
                  onMouseLeave={() => setActiveNode(null)}
                  className={`w-24 h-24 rounded-full flex flex-col items-center justify-center border-2 transition-all duration-500 shadow-2xl cursor-pointer ${
                    activeNode
                      ? 'bg-accent-pink/20 border-accent-pink shadow-[0_0_40px_rgba(255,182,193,0.5)]'
                      : 'bg-white/10 border-white/30 hover:border-accent-pink hover:bg-accent-pink/10 shadow-[0_0_20px_rgba(0,0,0,0.5)]'
                  }`}
                >
                  <Cpu className="w-8 h-8 text-accent-pink mb-1 animate-pulse" />
                  <span className="text-[11px] font-bold tracking-wider text-white font-cabinet uppercase">
                    TOOLS
                  </span>
                </motion.button>
              </div>

              {/* Branching SVG Lines (Desktop) */}
              <svg className="hidden md:block absolute inset-0 w-full h-full pointer-events-none z-10">
                {/* Branch 1: Top Right (Frontend) */}
                <path
                  d="M 100 210 C 180 210, 220 70, 310 70"
                  fill="none"
                  stroke={activeNode === 'frontend' || activeNode === 'all' ? '#00F0FF' : 'rgba(255,255,255,0.15)'}
                  strokeWidth={activeNode === 'frontend' || activeNode === 'all' ? '2.5' : '1.5'}
                  strokeDasharray="6 4"
                  className="transition-all duration-300"
                />

                {/* Branch 2: Middle Right (Backend) */}
                <path
                  d="M 100 210 C 180 210, 220 210, 310 210"
                  fill="none"
                  stroke={activeNode === 'backend' || activeNode === 'all' ? '#FFB6C1' : 'rgba(255,255,255,0.15)'}
                  strokeWidth={activeNode === 'backend' || activeNode === 'all' ? '2.5' : '1.5'}
                  strokeDasharray="6 4"
                  className="transition-all duration-300"
                />

                {/* Branch 3: Bottom Right (UI Libraries) */}
                <path
                  d="M 100 210 C 180 210, 220 350, 310 350"
                  fill="none"
                  stroke={activeNode === 'ui' || activeNode === 'all' ? '#7000FF' : 'rgba(255,255,255,0.15)'}
                  strokeWidth={activeNode === 'ui' || activeNode === 'all' ? '2.5' : '1.5'}
                  strokeDasharray="6 4"
                  className="transition-all duration-300"
                />
              </svg>

              {/* Skill Node Cards Column */}
              <div className="relative z-20 w-full md:w-72 space-y-4">
                {about.toolNodes.map((node: ToolNode) => {
                  const isActive = activeNode === node.id || activeNode === 'all';
                  return (
                    <motion.div
                      key={node.id}
                      onMouseEnter={() => setActiveNode(node.id)}
                      onMouseLeave={() => setActiveNode(null)}
                      whileHover={{ x: 6 }}
                      className={`p-4 rounded-2xl border transition-all duration-300 cursor-pointer backdrop-blur-xl ${
                        isActive
                          ? 'bg-white/10 border-white/30 shadow-xl'
                          : 'bg-white/5 border-white/10 hover:border-white/20'
                      }`}
                      style={{
                        borderColor: isActive ? node.color : undefined,
                        boxShadow: isActive ? `0 0 25px ${node.color}33` : undefined,
                      }}
                    >
                      <div className="flex items-center gap-2.5 mb-2">
                        <div
                          className="p-1.5 rounded-lg"
                          style={{ backgroundColor: `${node.color}20` }}
                        >
                          {getCategoryIcon(node.id)}
                        </div>
                        <h4 className="font-bold text-sm text-white font-cabinet">
                          {node.title}
                        </h4>
                      </div>

                      <div className="flex flex-wrap gap-1.5">
                        {node.tools.map((tool) => (
                          <span
                            key={tool}
                            className="inline-flex items-center gap-1 px-2 py-0.5 rounded-md bg-white/5 text-[11px] text-slate-300 border border-white/5 font-mono"
                          >
                            <CheckCircle2 className="w-2.5 h-2.5 text-slate-400" />
                            {tool}
                          </span>
                        ))}
                      </div>
                    </motion.div>
                  );
                })}
              </div>
            </div>
          </motion.div>
        </div>
      </div>
    </section>
  );
}
