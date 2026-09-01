import type { Metadata } from 'next';
import './globals.css';

export const metadata: Metadata = {
  title: 'ECHO — Modern Developer Portfolio',
  description: 'Motion-heavy developer portfolio featuring interactive WebGL canvas graphics, dynamic skill architecture, and responsive glassmorphism UI.',
  keywords: ['Developer Portfolio', 'Next.js', 'React', 'Three.js', 'Framer Motion', 'TypeScript', 'Frontend Architect'],
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html
      lang="en"
      className="scroll-smooth"
      style={{
        // @ts-ignore
        '--font-josefin': '"Josefin Sans", sans-serif',
        '--font-poppins': 'Poppins, sans-serif',
        '--font-lexend': 'Lexend, sans-serif',
      }}
    >
      <body className="bg-[#0a0e1a] text-slate-100 antialiased selection:bg-accent-pink selection:text-[#0a0e1a]">
        {children}
      </body>
    </html>
  );
}

