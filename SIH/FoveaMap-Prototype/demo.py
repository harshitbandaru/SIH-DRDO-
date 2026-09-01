"""
FoveaMap Prototype Entry Point
Allows running: python demo.py
"""

from foveamap.demo import run_demo

if __name__ == "__main__":
    run_demo(save_anim=True, max_frames=40)
