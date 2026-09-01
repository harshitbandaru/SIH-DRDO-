export interface NavLink {
  id: string;
  label: string;
  href: string;
  number: string;
}

export interface SocialLink {
  name: string;
  url: string;
  iconName: 'Github' | 'Linkedin' | 'Instagram' | 'Twitter';
}

export interface HeroData {
  brandName: string;
  headline: string;
  subtitle: string;
  description: string;
  ctaText: string;
  ctaHref: string;
  fallbackImage: string;
}

export interface ToolNode {
  id: string;
  category: string;
  title: string;
  color: string;
  tools: string[];
}

export interface AboutData {
  bgImage: string;
  title: string;
  bio: string[];
  toolNodes: ToolNode[];
}

export interface SongCard {
  id: string;
  title: string;
  artist: string;
  image: string;
  genre?: string;
}

export interface ProjectItem {
  id: string;
  number: string;
  title: string;
  description: string;
  techStack: string[];
  image: string;
  liveUrl: string;
  githubUrl?: string;
}

export interface ContactInfo {
  heading: string;
  subtitle: string;
  email: string;
  phone: string;
  location: string;
}

export interface PortfolioConfig {
  brandName: string;
  navLinks: NavLink[];
  socialLinks: SocialLink[];
  hero: HeroData;
  about: AboutData;
  songs: SongCard[];
  projects: ProjectItem[];
  contact: ContactInfo;
  footer: {
    brandName: string;
    tagline: string;
    statusText: string;
    copyright: string;
  };
}

export const PORTFOLIO_DATA: PortfolioConfig = {
  brandName: 'ECHO',
  
  navLinks: [
    { id: 'home', label: 'Home', href: '#home', number: '01' },
    { id: 'about', label: 'About', href: '#about', number: '02' },
    { id: 'projects', label: 'Projects', href: '#projects', number: '03' },
    { id: 'contact', label: 'Contact', href: '#contact', number: '04' },
  ],

  socialLinks: [
    { name: 'GitHub', url: 'https://github.com', iconName: 'Github' },
    { name: 'LinkedIn', url: 'https://linkedin.com', iconName: 'Linkedin' },
    { name: 'Instagram', url: 'https://instagram.com', iconName: 'Instagram' },
  ],

  hero: {
    brandName: 'ECHO',
    headline: 'Crafting',
    subtitle: 'SEAMLESS DIGITAL EXPERIENCES',
    description: 'Frontend Architect & Creative Developer pushing the boundaries of web motion, 3D interactive graphics, and ultra-responsive user interfaces.',
    ctaText: 'EXPLORE WORK',
    ctaHref: '#projects',
    fallbackImage: '/portfolio/hero-subject.png',
  },

  about: {
    bgImage: '/portfolio/about-bg.png',
    title: 'I TURN VISION INTO DIGITAL REALITY.',
    bio: [
      'I am a passionate Frontend Architect and Creative Developer dedicated to crafting high-performance web experiences. My work sits at the intersection of aesthetic precision, fluid animations, and robust modern software architecture.',
      'With expertise spanning React, Next.js, Framer Motion, and Three.js, I build digital applications that do not just function flawlessly, but captivate users at first glance.',
    ],
    toolNodes: [
      {
        id: 'frontend',
        category: 'Frontend Core',
        title: 'Frontend Tools',
        color: '#00F0FF',
        tools: ['JavaScript (ES6+)', 'TypeScript', 'React.js', 'Next.js (App Router)', 'HTML5 & Semantic Web', 'Web Performance'],
      },
      {
        id: 'backend',
        category: 'Backend & APIs',
        title: 'Backend Tools',
        color: '#FFB6C1',
        tools: ['Node.js', 'Express.js', 'Supabase', 'Firebase', 'PostgreSQL', 'RESTful & GraphQL APIs'],
      },
      {
        id: 'ui',
        category: 'Styling & Motion',
        title: 'UI Libraries',
        color: '#7000FF',
        tools: ['Tailwind CSS', 'CSS3 / SCSS', 'Framer Motion', 'Three.js / React Three Fiber', 'GSAP', 'Lucide Icons'],
      },
    ],
  },

  songs: [
    {
      id: 'song-1',
      title: 'Back To Black',
      artist: 'Amy Winehouse',
      image: '/portfolio/black-to-back.png',
      genre: 'Soul / R&B',
    },
    {
      id: 'song-2',
      title: 'Beanie',
      artist: 'Chezile',
      image: '/portfolio/beanie-song.png',
      genre: 'Indie Pop',
    },
    {
      id: 'song-3',
      title: 'Feel It Still',
      artist: 'Portugal. The Man',
      image: '/portfolio/feel-it-still.png',
      genre: 'Alternative Rock',
    },
    {
      id: 'song-4',
      title: 'Feel Me',
      artist: 'Selena Gomez',
      image: '/portfolio/feel-me.png',
      genre: 'Electropop',
    },
    {
      id: 'song-5',
      title: 'I Was Never There',
      artist: 'The Weeknd',
      image: '/portfolio/I-was-never-there.png',
      genre: 'R&B / Synth',
    },
    {
      id: 'song-6',
      title: 'Not Like Us',
      artist: 'Kendrick Lamar',
      image: '/portfolio/not-like-us.png',
      genre: 'Hip Hop',
    },
    {
      id: 'song-7',
      title: 'When I Grow Up',
      artist: 'NF',
      image: '/portfolio/when-i-grow-up.png',
      genre: 'Hip Hop',
    },
    {
      id: 'song-8',
      title: 'Hold On',
      artist: 'Justin Bieber',
      image: '/portfolio/hold.jpg',
      genre: 'Pop',
    },
    {
      id: 'song-9',
      title: 'Easy On Me',
      artist: 'Adele',
      image: '/portfolio/easy-on-me.jpg',
      genre: 'Pop / Ballad',
    },
  ],

  projects: [
    {
      id: 'project-1',
      number: '01 / 03',
      title: 'Echo Studio Platform',
      description: 'An interactive WebGL motion studio application with real-time 3D particle canvas controls, glassmorphic layout system, and responsive web animations.',
      techStack: ['NEXT.JS', 'TYPESCRIPT', 'THREE.JS', 'FRAMER MOTION', 'TAILWIND CSS'],
      image: '/portfolio/echo-studio.png',
      liveUrl: 'https://echo-studio.dev',
      githubUrl: 'https://github.com',
    },
    {
      id: 'project-2',
      number: '02 / 03',
      title: 'Jishnu Developer Portfolio',
      description: 'A high-impact developer portfolio featuring dynamic SVG skill node graphs, infinite music carousel, and custom dark mode styling.',
      techStack: ['REACT', 'TAILWIND CSS', 'FRAMER MOTION', 'TYPESCRIPT'],
      image: '/portfolio/jishnu-portfolio.png',
      liveUrl: 'https://jishnu-portfolio.dev',
      githubUrl: 'https://github.com',
    },
    {
      id: 'project-3',
      number: '03 / 03',
      title: 'Mocha & Miso Artisan Brand',
      description: 'A sleek e-commerce showcase application with smooth product transitions, custom dark glass theme, and intuitive contact experience.',
      techStack: ['NEXT.JS', 'SUPABASE', 'TAILWIND CSS', 'REST API'],
      image: '/portfolio/mocha-miso.jpg',
      liveUrl: 'https://mocha-miso.dev',
      githubUrl: 'https://github.com',
    },
  ],

  contact: {
    heading: "LET'S CONNECT",
    subtitle: 'Have a project in mind, an exciting position, or just want to brainstorm innovative web experiences? Drop a message below!',
    email: 'contact@echo-portfolio.dev',
    phone: '+1 (555) 839-2041',
    location: 'San Francisco, CA / Remote',
  },

  footer: {
    brandName: 'ECHO',
    tagline: 'Crafting seamless digital experiences through code, motion, and design.',
    statusText: 'Open to work',
    copyright: `© ${new Date().getFullYear()} ECHO. Built with Next.js, Framer Motion & Three.js.`,
  },
};
