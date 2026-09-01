'use client';

import React from 'react';
import Image from 'next/image';
import { motion } from 'framer-motion';
import { Music, Disc } from 'lucide-react';
import { PORTFOLIO_DATA } from '@/data/portfolio';

export default function MusicCarousel() {
  const { songs } = PORTFOLIO_DATA;

  // Duplicate song array to ensure seamless infinite scroll
  const duplicatedSongs = [...songs, ...songs];

  return (
    <section className="relative w-full py-20 bg-[#0a0e1a] overflow-hidden border-y border-white/10">
      {/* Background Subtle Gradient */}
      <div className="absolute inset-0 bg-gradient-to-r from-accent-pink/5 via-accent-cyan/5 to-accent-purple/5 pointer-events-none" />

      {/* Subtext Header */}
      <div className="max-w-6xl mx-auto px-6 mb-10 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4">
        <div className="flex items-center gap-3">
          <div className="p-2.5 rounded-full bg-accent-pink/10 border border-accent-pink/30 text-accent-pink">
            <Music className="w-5 h-5 animate-bounce" />
          </div>
          <div>
            <h3 className="text-xs font-mono tracking-widest text-accent-pink uppercase">
              // CURATED VIBES
            </h3>
            <p className="text-sm md:text-base font-semibold font-cabinet text-slate-200 uppercase tracking-wide">
              A FEW SONGS I CAN RECOMMEND IF YOU&apos;RE LOOKING FOR SOME FRESH TUNES :)
            </p>
          </div>
        </div>

        <div className="hidden sm:flex items-center gap-2 text-xs font-mono text-slate-400 bg-white/5 px-3 py-1.5 rounded-full border border-white/10">
          <Disc className="w-3.5 h-3.5 text-accent-cyan animate-spin" style={{ animationDuration: '6s' }} />
          <span>Infinite Soundscape</span>
        </div>
      </div>

      {/* Infinite Scroll Container */}
      <div className="relative w-full overflow-hidden group">
        
        {/* Left Side Mask Gradient Fade */}
        <div className="absolute top-0 bottom-0 left-0 w-24 md:w-44 z-10 bg-gradient-to-r from-[#0a0e1a] via-[#0a0e1a]/90 to-transparent pointer-events-none" />

        {/* Right Side Mask Gradient Fade */}
        <div className="absolute top-0 bottom-0 right-0 w-24 md:w-44 z-10 bg-gradient-to-l from-[#0a0e1a] via-[#0a0e1a]/90 to-transparent pointer-events-none" />

        {/* Marquee Track */}
        <div className="flex items-center gap-6 w-max animate-marquee group-hover:[animation-play-state:paused]">
          {duplicatedSongs.map((song, index) => (
            <motion.div
              key={`${song.id}-${index}`}
              whileHover={{ y: -8, scale: 1.03 }}
              transition={{ type: 'spring', stiffness: 300, damping: 20 }}
              className="relative flex-shrink-0 w-64 md:w-72 rounded-2xl bg-white/[0.04] border border-white/15 overflow-hidden backdrop-blur-xl group/card shadow-xl transition-all duration-300 hover:border-accent-pink/50 hover:shadow-[0_0_30px_rgba(255,182,193,0.2)]"
            >
              {/* Album Art with 16:10 aspect ratio */}
              <div className="relative w-full aspect-[16/10] overflow-hidden bg-slate-900">
                <Image
                  src={song.image}
                  alt={song.title}
                  fill
                  className="object-cover object-center group-hover/card:scale-110 transition-transform duration-500"
                />
                <div className="absolute inset-0 bg-gradient-to-t from-[#0a0e1a] via-transparent to-transparent opacity-80" />
                
                {/* Playing Badge */}
                <div className="absolute top-3 right-3 p-1.5 rounded-full bg-black/60 border border-white/20 backdrop-blur-md text-accent-pink">
                  <Disc className="w-3.5 h-3.5 group-hover/card:animate-spin" />
                </div>
              </div>

              {/* Card Meta Content */}
              <div className="p-4 flex flex-col justify-between">
                <div>
                  <h4 className="font-bold text-base text-white font-cabinet truncate group-hover/card:text-accent-pink transition-colors">
                    {song.title}
                  </h4>
                  <p className="text-xs text-slate-400 font-medium truncate mt-0.5">
                    {song.artist}
                  </p>
                </div>

                {song.genre && (
                  <span className="mt-3 inline-self-start text-[10px] font-mono uppercase tracking-wider text-accent-cyan/80 bg-accent-cyan/10 px-2.5 py-1 rounded-full border border-accent-cyan/20 w-fit">
                    {song.genre}
                  </span>
                )}
              </div>
            </motion.div>
          ))}
        </div>
      </div>
    </section>
  );
}
