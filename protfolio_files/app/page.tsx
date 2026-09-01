import Navbar from '@/components/Navbar';
import Hero from '@/components/Hero';
import About from '@/components/About';
import MusicCarousel from '@/components/MusicCarousel';
import Projects from '@/components/Projects';
import Contact from '@/components/Contact';
import Footer from '@/components/Footer';

export default function Home() {
  return (
    <main className="relative min-h-screen w-full bg-[#0a0e1a] text-slate-100 overflow-x-hidden">
      <Navbar />
      <Hero />
      <About />
      <MusicCarousel />
      <Projects />
      <Contact />
      <Footer />
    </main>
  );
}
