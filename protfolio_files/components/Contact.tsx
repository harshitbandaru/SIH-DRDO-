'use client';

import React, { useState } from 'react';
import { motion } from 'framer-motion';
import { Mail, Phone, MapPin, Send, CheckCircle, Plus } from 'lucide-react';
import { PORTFOLIO_DATA } from '@/data/portfolio';

export default function Contact() {
  const { contact } = PORTFOLIO_DATA;
  const [submitted, setSubmitted] = useState(false);
  const [loading, setLoading] = useState(false);
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    phone: '',
    message: '',
  });

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    // Simulate submission delay
    setTimeout(() => {
      setLoading(false);
      setSubmitted(true);
      setFormData({ name: '', email: '', phone: '', message: '' });
      setTimeout(() => setSubmitted(false), 5000);
    }, 1200);
  };

  return (
    <section
      id="contact"
      className="relative min-h-screen w-full py-28 px-6 md:px-12 bg-[#0a0e1a] overflow-hidden"
    >
      {/* Glow Orbs */}
      <div className="absolute top-1/3 left-1/4 w-96 h-96 bg-accent-pink/10 rounded-full blur-[160px] pointer-events-none" />
      <div className="absolute bottom-1/3 right-1/4 w-96 h-96 bg-accent-cyan/10 rounded-full blur-[160px] pointer-events-none" />

      <div className="relative z-10 max-w-6xl mx-auto">
        {/* Section Header */}
        <div className="mb-16 text-center max-w-2xl mx-auto">
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            transition={{ duration: 0.5 }}
            className="text-xs font-mono tracking-widest text-accent-pink uppercase mb-3"
          >
            // 04 . Get In Touch
          </motion.div>
          <motion.h2
            initial={{ opacity: 0, y: 30 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            transition={{ duration: 0.7 }}
            className="text-4xl sm:text-6xl font-black font-cabinet tracking-tight text-white mb-4"
          >
            {contact.heading}
          </motion.h2>
          <motion.p
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            transition={{ duration: 0.7, delay: 0.1 }}
            className="text-slate-400 text-base sm:text-lg"
          >
            {contact.subtitle}
          </motion.p>
        </div>

        {/* Main Glass Grid Container with Corner Accent + Markings */}
        <motion.div
          initial={{ opacity: 0, scale: 0.96 }}
          whileInView={{ opacity: 1, scale: 1 }}
          viewport={{ once: true }}
          transition={{ duration: 0.8 }}
          className="relative rounded-3xl bg-white/[0.03] border border-white/20 backdrop-blur-3xl p-8 sm:p-12 shadow-2xl overflow-hidden"
        >
          {/* Corner Accent '+' Markings */}
          <div className="absolute top-4 left-4 text-accent-pink/60">
            <Plus className="w-5 h-5" />
          </div>
          <div className="absolute top-4 right-4 text-accent-pink/60">
            <Plus className="w-5 h-5" />
          </div>
          <div className="absolute bottom-4 left-4 text-accent-pink/60">
            <Plus className="w-5 h-5" />
          </div>
          <div className="absolute bottom-4 right-4 text-accent-pink/60">
            <Plus className="w-5 h-5" />
          </div>

          <div className="grid grid-cols-1 lg:grid-cols-12 gap-12 items-start">
            
            {/* Left Info Cards Column */}
            <div className="lg:col-span-5 space-y-6">
              <h3 className="text-2xl font-bold font-cabinet text-white mb-6">
                Direct Contact
              </h3>

              {/* Email Card */}
              <div className="flex items-center gap-4 p-5 rounded-2xl bg-white/5 border border-white/10 hover:border-accent-pink/40 hover:bg-accent-pink/5 transition-all group">
                <div className="p-3 rounded-xl bg-accent-pink/10 text-accent-pink group-hover:scale-110 transition-transform">
                  <Mail className="w-6 h-6" />
                </div>
                <div>
                  <span className="text-xs font-mono uppercase text-slate-400">Email</span>
                  <a
                    href={`mailto:${contact.email}`}
                    className="block text-white font-medium text-sm sm:text-base hover:text-accent-pink transition-colors truncate"
                  >
                    {contact.email}
                  </a>
                </div>
              </div>

              {/* Phone Card */}
              <div className="flex items-center gap-4 p-5 rounded-2xl bg-white/5 border border-white/10 hover:border-accent-cyan/40 hover:bg-accent-cyan/5 transition-all group">
                <div className="p-3 rounded-xl bg-accent-cyan/10 text-accent-cyan group-hover:scale-110 transition-transform">
                  <Phone className="w-6 h-6" />
                </div>
                <div>
                  <span className="text-xs font-mono uppercase text-slate-400">Phone</span>
                  <a
                    href={`tel:${contact.phone}`}
                    className="block text-white font-medium text-sm sm:text-base hover:text-accent-cyan transition-colors"
                  >
                    {contact.phone}
                  </a>
                </div>
              </div>

              {/* Location Card */}
              <div className="flex items-center gap-4 p-5 rounded-2xl bg-white/5 border border-white/10 hover:border-accent-purple/40 hover:bg-accent-purple/5 transition-all group">
                <div className="p-3 rounded-xl bg-accent-purple/10 text-accent-purple group-hover:scale-110 transition-transform">
                  <MapPin className="w-6 h-6" />
                </div>
                <div>
                  <span className="text-xs font-mono uppercase text-slate-400">Location</span>
                  <span className="block text-white font-medium text-sm sm:text-base">
                    {contact.location}
                  </span>
                </div>
              </div>
            </div>

            {/* Right Contact Form Column */}
            <div className="lg:col-span-7">
              <form onSubmit={handleSubmit} className="space-y-6">
                <div className="grid grid-cols-1 sm:grid-cols-2 gap-6">
                  {/* Name Input */}
                  <div>
                    <label className="block text-xs font-mono uppercase tracking-wider text-slate-300 mb-2">
                      Your Name
                    </label>
                    <input
                      type="text"
                      required
                      value={formData.name}
                      onChange={(e) => setFormData({ ...formData, name: e.target.value })}
                      placeholder="Jane Doe"
                      className="w-full px-4 py-3.5 rounded-xl bg-white/5 border border-white/15 text-white placeholder-slate-500 focus:outline-none focus:border-accent-pink focus:ring-1 focus:ring-accent-pink transition-all font-sans text-sm"
                    />
                  </div>

                  {/* Email Input */}
                  <div>
                    <label className="block text-xs font-mono uppercase tracking-wider text-slate-300 mb-2">
                      Your Email
                    </label>
                    <input
                      type="email"
                      required
                      value={formData.email}
                      onChange={(e) => setFormData({ ...formData, email: e.target.value })}
                      placeholder="jane@example.com"
                      className="w-full px-4 py-3.5 rounded-xl bg-white/5 border border-white/15 text-white placeholder-slate-500 focus:outline-none focus:border-accent-pink focus:ring-1 focus:ring-accent-pink transition-all font-sans text-sm"
                    />
                  </div>
                </div>

                {/* Phone Input */}
                <div>
                  <label className="block text-xs font-mono uppercase tracking-wider text-slate-300 mb-2">
                    Phone Number (Optional)
                  </label>
                  <input
                    type="tel"
                    value={formData.phone}
                    onChange={(e) => setFormData({ ...formData, phone: e.target.value })}
                    placeholder="+1 (555) 000-0000"
                    className="w-full px-4 py-3.5 rounded-xl bg-white/5 border border-white/15 text-white placeholder-slate-500 focus:outline-none focus:border-accent-pink focus:ring-1 focus:ring-accent-pink transition-all font-sans text-sm"
                  />
                </div>

                {/* Message Input */}
                <div>
                  <label className="block text-xs font-mono uppercase tracking-wider text-slate-300 mb-2">
                    Your Message
                  </label>
                  <textarea
                    required
                    rows={4}
                    value={formData.message}
                    onChange={(e) => setFormData({ ...formData, message: e.target.value })}
                    placeholder="Tell me about your project, goals, or inquiry..."
                    className="w-full px-4 py-3.5 rounded-xl bg-white/5 border border-white/15 text-white placeholder-slate-500 focus:outline-none focus:border-accent-pink focus:ring-1 focus:ring-accent-pink transition-all font-sans text-sm resize-none"
                  />
                </div>

                {/* Submit Button */}
                <motion.button
                  whileHover={{ scale: 1.02 }}
                  whileTap={{ scale: 0.98 }}
                  type="submit"
                  disabled={loading || submitted}
                  className="w-full py-4 rounded-xl bg-accent-pink text-[#0a0e1a] font-bold text-sm tracking-wider uppercase flex items-center justify-center gap-2 hover:bg-white hover:shadow-[0_0_30px_rgba(255,182,193,0.4)] transition-all duration-300 disabled:opacity-70 cursor-pointer"
                >
                  {loading ? (
                    <span className="animate-pulse">Sending Message...</span>
                  ) : submitted ? (
                    <>
                      <CheckCircle className="w-5 h-5 text-emerald-900" />
                      <span>Message Sent Successfully!</span>
                    </>
                  ) : (
                    <>
                      <span>Send Message</span>
                      <Send className="w-4 h-4" />
                    </>
                  )}
                </motion.button>
              </form>
            </div>
          </div>
        </motion.div>
      </div>
    </section>
  );
}
