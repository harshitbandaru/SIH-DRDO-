'use client';

import React, { useRef, useMemo } from 'react';
import { Canvas, useFrame } from '@react-three/fiber';
import * as THREE from 'three';

function ParticleWave({ mouse }: { mouse: React.MutableRefObject<{ x: number; y: number }> }) {
  const pointsRef = useRef<THREE.Points>(null!);

  const { positions, colors, count } = useMemo(() => {
    const numRows = 70;
    const numCols = 70;
    const count = numRows * numCols;
    const positions = new Float32Array(count * 3);
    const colors = new Float32Array(count * 3);

    const color1 = new THREE.Color('#FFB6C1'); // Pink
    const color2 = new THREE.Color('#00F0FF'); // Cyan
    const color3 = new THREE.Color('#7000FF'); // Purple

    let i = 0;
    for (let r = 0; r < numRows; r++) {
      for (let c = 0; c < numCols; c++) {
        const u = r / numRows;
        const v = c / numCols;

        // Position spread
        const x = (r - numRows / 2) * 0.45;
        const z = (c - numCols / 2) * 0.45;
        const y = Math.sin(u * Math.PI * 4) * Math.cos(v * Math.PI * 4) * 0.5;

        positions[i * 3] = x;
        positions[i * 3 + 1] = y;
        positions[i * 3 + 2] = z;

        // Color interpolation
        const mixRatio = (u + v) / 2;
        let finalColor = new THREE.Color();
        if (mixRatio < 0.5) {
          finalColor.lerpColors(color1, color2, mixRatio * 2);
        } else {
          finalColor.lerpColors(color2, color3, (mixRatio - 0.5) * 2);
        }

        colors[i * 3] = finalColor.r;
        colors[i * 3 + 1] = finalColor.g;
        colors[i * 3 + 2] = finalColor.b;

        i++;
      }
    }
    return { positions, colors, count };
  }, []);

  useFrame(({ clock }) => {
    if (!pointsRef.current) return;
    const time = clock.getElapsedTime() * 0.8;
    const positionAttribute = pointsRef.current.geometry.attributes.position as THREE.BufferAttribute;
    const array = positionAttribute.array as Float32Array;

    let index = 0;
    const numRows = 70;
    const numCols = 70;
    
    // Smooth target mouse interaction
    const targetRotX = mouse.current.y * 0.15;
    const targetRotY = mouse.current.x * 0.2;

    pointsRef.current.rotation.x = THREE.MathUtils.lerp(pointsRef.current.rotation.x, 0.6 + targetRotX, 0.05);
    pointsRef.current.rotation.y = THREE.MathUtils.lerp(pointsRef.current.rotation.y, targetRotY, 0.05);
    pointsRef.current.rotation.z = time * 0.02;

    for (let r = 0; r < numRows; r++) {
      for (let c = 0; c < numCols; c++) {
        const u = r / numRows;
        const v = c / numCols;

        // Dynamic wave equation
        const wave1 = Math.sin(u * 6 + time * 1.5) * 0.6;
        const wave2 = Math.cos(v * 6 + time * 1.2) * 0.6;
        const wave3 = Math.sin((u + v) * 5 + time) * 0.4;

        array[index * 3 + 1] = wave1 + wave2 + wave3;
        index++;
      }
    }

    positionAttribute.needsUpdate = true;
  });

  return (
    <points ref={pointsRef}>
      <bufferGeometry>
        <bufferAttribute
          attach="attributes-position"
          args={[positions, 3]}
        />
        <bufferAttribute
          attach="attributes-color"
          args={[colors, 3]}
        />
      </bufferGeometry>
      <pointsMaterial
        size={0.12}
        vertexColors
        transparent
        opacity={0.75}
        sizeAttenuation
        blending={THREE.AdditiveBlending}
      />
    </points>
  );
}

export default function HeroCanvas() {
  const mouse = useRef({ x: 0, y: 0 });

  const handleMouseMove = (e: React.MouseEvent<HTMLDivElement>) => {
    const { innerWidth, innerHeight } = window;
    mouse.current.x = (e.clientX / innerWidth) * 2 - 1;
    mouse.current.y = -(e.clientY / innerHeight) * 2 + 1;
  };

  return (
    <div 
      className="absolute inset-0 z-0 pointer-events-auto"
      onMouseMove={handleMouseMove}
    >
      <Canvas
        camera={{ position: [0, 8, 16], fov: 45 }}
        gl={{ alpha: true, antialias: true }}
      >
        <ambientLight intensity={0.5} />
        <ParticleWave mouse={mouse} />
      </Canvas>
    </div>
  );
}
