"""Pomoć za scenarij: produži scene prema dužini glasa i pomjeri zvučne efekte."""
import os
from animacija import wav_len


def uskladi(scenes, sfx, glas_prefix, lead=0.25, pad=0.7):
    voice = []; t0 = 0.0; new = []
    for i, (dur, fn) in enumerate(scenes):
        vp = glas_prefix + '%d.wav' % (i + 1)
        if os.path.exists(vp):
            dur = max(dur, wav_len(vp) + lead + pad); voice.append((t0 + lead, vp))
        new.append((dur, fn)); t0 += dur
    old = [sum(s[0] for s in scenes[:i]) for i in range(len(scenes))]
    nov = [sum(s[0] for s in new[:i]) for i in range(len(new))]
    def remap(tt):
        i = max(k for k in range(len(old)) if old[k] <= tt)
        return nov[i] + (tt - old[i])
    return new, [(remap(tt), k) for (tt, k) in sfx], voice
