"""Pravi originalnu podlogu za Reel (bez autorskih prava): lagani elektronski ritam.

Upotreba:
    python muzika.py izlaz.wav trajanje_sekundi [seme]

Seme (bilo koji broj ili tekst, npr. datum objave) bira tonalitet, akorde i melodiju,
pa svaki Reel zvuči malo drugačije. Isto seme uvijek daje istu muziku.
"""
import sys, wave, random, zlib
import numpy as np

SR = 44100


def note_freq(n):  # MIDI broj u Hz
    return 440.0 * 2 ** ((n - 69) / 12)


def env(n, a=0.01, r=0.3):
    t = np.arange(n) / SR
    e = np.minimum(1, t / a) * np.exp(-t / r)
    return e


def lowpass(x, alpha):
    y = np.empty_like(x); acc = 0.0
    for i, v in enumerate(x):
        acc += alpha * (v - acc); y[i] = acc
    return y


def saw(f, n):
    t = np.arange(n) / SR
    return 2 * ((t * f) % 1) - 1


def main(out, dur, seed="0"):
    rnd = random.Random(zlib.crc32(str(seed).encode()))
    bpm = rnd.choice([100, 105, 110, 115])
    beat = 60 / bpm
    root = rnd.choice([57, 59, 60, 62, 64])  # A, H, C, D, E
    progs = [[0, -4, 3, -2], [0, 5, -4, 3], [0, -3, 5, -5], [0, 3, -4, -2]]
    prog = rnd.choice(progs)
    minor = [0, 3, 7]; major = [0, 4, 7]
    n = int(dur * SR) + SR
    mix = np.zeros(n)
    bar = 4 * beat
    nbars = int(dur / bar) + 2
    for b in range(nbars):
        deg = prog[b % len(prog)]
        chord = minor if deg in (0, 5, -3) else major
        start = int(b * bar * SR)
        ln = int(bar * SR)
        if start >= n:
            break
        ln = min(ln, n - start)
        # pad: mekani akord
        pad = np.zeros(ln)
        for iv in chord:
            f = note_freq(root - 12 + deg + iv)
            pad += saw(f, ln) + saw(f * 1.004, ln)
        pad = lowpass(pad, 0.04) * 0.05
        fade = np.minimum(1, np.arange(ln) / (0.2 * SR)) * np.minimum(1, (ln - np.arange(ln)) / (0.2 * SR))
        mix[start:start + ln] += pad * fade
        # bas na svaku dobu
        for k in range(4):
            s = start + int(k * beat * SR); m = int(beat * 0.9 * SR)
            if s + m > n: break
            f = note_freq(root - 24 + deg)
            t = np.arange(m) / SR
            mix[s:s + m] += np.sin(2 * np.pi * f * t) * env(m, 0.005, 0.25) * 0.22
        # arpeđo osmine
        pattern = [0, 1, 2, 1, 2, 0, 1, 2] if rnd.random() < 0.5 else [0, 2, 1, 2, 0, 2, 1, 2]
        for k in range(8):
            s = start + int(k * beat / 2 * SR); m = int(beat / 2 * SR)
            if s + m > n: break
            f = note_freq(root + 12 + deg + chord[pattern[k]])
            t = np.arange(m) / SR
            tone = (np.sin(2 * np.pi * f * t) + 0.3 * np.sin(4 * np.pi * f * t)) * env(m, 0.003, 0.12)
            mix[s:s + m] += tone * 0.06
    # bubanj: kick na 1 i 3, hi-hat osmine
    nbeats = int(dur / beat) + 2
    for k in range(nbeats):
        s = int(k * beat * SR)
        if s >= n: break
        if k % 2 == 0:
            m = min(int(0.3 * SR), n - s); t = np.arange(m) / SR
            fsw = 120 * np.exp(-t * 18) + 45
            mix[s:s + m] += np.sin(2 * np.pi * np.cumsum(fsw) / SR) * env(m, 0.002, 0.12) * 0.45
        for h in (0, 0.5):
            hs = s + int(h * beat * SR); m = min(int(0.05 * SR), n - hs)
            if m <= 0: continue
            noise = np.random.default_rng(k * 2 + int(h * 2)).standard_normal(m)
            noise = noise - lowpass(noise, 0.3)
            mix[hs:hs + m] += noise * env(m, 0.001, 0.02) * (0.05 if h else 0.07)
    mix = mix[:int(dur * SR)]
    # utišavanje na kraju i normalizacija
    fo = int(1.5 * SR)
    mix[-fo:] *= np.linspace(1, 0, fo)
    mix[:int(0.3 * SR)] *= np.linspace(0, 1, int(0.3 * SR))
    mix = mix / (np.max(np.abs(mix)) + 1e-9) * 0.85
    pcm = (np.stack([mix, mix], 1) * 32767).astype(np.int16)
    w = wave.open(out, "wb"); w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes(pcm.tobytes()); w.close()
    print("snimljeno:", out, f"({bpm} bpm)")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(__doc__); sys.exit(1)
    main(sys.argv[1], float(sys.argv[2]), sys.argv[3] if len(sys.argv) > 3 else "0")
