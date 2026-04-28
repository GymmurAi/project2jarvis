#!/usr/bin/env python3
"""
auto-summary.py - Memory Management Script
Keeps MEMORY.md lean by auto-summarizing when it exceeds 200 lines.
Features: colorful output, memory health score, archiving to lessons-learned.md
"""

import os
import sys
import time
from datetime import datetime

try:
    from colorama import init
    init()
except ImportError:
    pass

# ANSI Color codes
class C:
    R = '\033[0m'
    B = '\033[1m'
    G = '\033[32m'
    Y = '\033[33m'
    C = '\033[36m'
    W = '\033[37m'
    BG = '\033[92m'
    BY = '\033[93m'
    BC = '\033[96m'
    BW = '\033[97m'
    BR = '\033[91m'
    BM = '\033[95m'

def spinner(duration=2):
    chars = ['|', '/', '-', '\\']
    end = time.time() + duration
    i = 0
    while time.time() < end:
        sys.stdout.write(f'\r{chars[i % 4]} Processing...')
        sys.stdout.flush()
        time.sleep(0.1)
        i += 1
    sys.stdout.write('\r' + ' ' * 20 + '\r')
    sys.stdout.flush()

def progress(cur, total, width=40, prefix="", suffix=""):
    pct = min(100, int(100 * cur / total))
    filled = int(width * cur / total)
    bar = '#' * filled + '-' * (width - filled)
    sys.stdout.write(f'\r{prefix} |{bar}| {pct}% {suffix}')
    sys.stdout.flush()
    if cur >= total:
        print()

def health_score(lines, threshold=200):
    if lines <= threshold:
        return min(100, int((lines / threshold) * 100)), C.BG, "EXCELLENT"
    over = lines - threshold
    score = max(0, int(100 - (over / (threshold * 1.5)) * 100))
    if score >= 60:
        return score, C.BY, "FAIR"
    elif score >= 30:
        return score, C.Y, "POOR"
    else:
        return score, C.BR, "CRITICAL"

def extract_important(lines, keep=0.4):
    if not lines:
        return [], []
    scored = []
    for i, line in enumerate(lines):
        s = 0
        if line.strip().startswith('#'):
            s += 10
        kws = ['important', 'critical', 'key', 'todo', 'fix', 'bug', 'decision',
               'architect', 'security', 'performance', 'api', 'endpoint', 'config']
        for kw in kws:
            if kw in line.lower():
                s += 3
        if line.strip():
            s += 1
        if len(line) < 100 and line.strip():
            s += 1
        s += (i / len(lines)) * 2
        scored.append((s, i, line))
    scored.sort(reverse=True)
    keep_n = max(10, int(len(lines) * keep))
    top = sorted(scored[:keep_n], key=lambda x: x[1])
    discarded = sorted(scored[keep_n:], key=lambda x: x[1])
    return [t[2] for t in top], [t[2] for t in discarded]

def main():
    print()
    print(f"{C.BC}{C.B}=============================================={C.R}")
    print(f"{C.BC}{C.B}           MEMORY AUTO-SUMMARIZER              {C.R}")
    print(f"{C.BC}{C.B}=============================================={C.R}")
    print()

    cwd = os.getcwd()
    mem = os.path.join(cwd, "MEMORY.md")
    arch_dir = os.path.join(cwd, "03_Knowledge_Base")
    arch = os.path.join(arch_dir, "lessons-learned.md")

    if not os.path.exists(mem):
        print(f"{C.Y}MEMORY.md not found. Creating...{C.R}")
        with open(mem, 'w', encoding='utf-8') as f:
            f.write(f"# MEMORY.md\n\nCreated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        print(f"{C.BG}MEMORY.md created!{C.R}\n")
        return

    print(f"{C.W}Scanning: {mem}{C.R}")
    spinner(1.5)
    print()

    with open(mem, 'r', encoding='utf-8') as f:
        content = f.read()
    lines = content.split('\n')
    count = len(lines)

    print(f"{C.W}Memory Analysis Complete!{C.R}")
    print('=' * 60)

    score, color, status = health_score(count)
    print(f"{C.W}Memory Health: {color}{C.B}{score}/100 {status}{C.R}")

    bar_w = 50
    filled = int(bar_w * score / 100)
    bar = color + '#' * filled + C.BC + '_' * (bar_w - filled)
    print(f"   |{bar}{C.R}|")
    print()

    print(f"{C.W}Lines:   {C.BC}{count}{C.R}")
    print(f"{C.W}Threshold: {C.Y}200{C.R}")
    print(f"{C.W}Keep:      {C.BG}40%{C.R}")
    print()

    if count <= 200:
        print(f"{C.BG}Memory is healthy! No summarization needed.{C.R}")
        print('=' * 60)
        print(f"\n{C.BM}Memory check complete! Lean and mean!{C.R}\n")
        return

    over = count - 200
    print(f"{C.BY}Memory overload! ({over} lines over limit){C.R}")
    print()
    print(f"{C.W}Starting auto-summarization...{C.R}")
    print()

    for i in range(5):
        progress(i+1, 5, prefix=f"{C.C}Processing:{C.R}", suffix=f"Step {i+1}/5")
    print()

    print(f"{C.W}Identifying important content...{C.R}")
    spinner(1)
    important, discarded = extract_important(lines, 0.4)
    print(f"{C.BG}Found {len(important)} key lines!{C.R}")
    print()

    print(f"{C.W}Archiving removed content...{C.R}")
    os.makedirs(arch_dir, exist_ok=True)

    ts = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    entry = f"\n\n---\n## Archived: {ts}\n\n"
    entry += f"From MEMORY.md ({count} -> {len(important)} lines)\n\n"
    entry += '\n'.join(discarded) + '\n'

    with open(arch, 'a', encoding='utf-8') as f:
        f.write(entry)

    print(f"{C.BG}Archived to: 03_Knowledge_Base/lessons-learned.md{C.R}")
    print()

    print(f"{C.W}Writing optimized MEMORY.md...{C.R}")
    hdr = f"# MEMORY.md\n\nAuto-summarized on {ts}\n"
    hdr += f"Reduced {count} -> {len(important)} lines (kept 40%)\n\n---\n\n"

    with open(mem, 'w', encoding='utf-8') as f:
        f.write(hdr)
        f.write('\n'.join(important))
        f.write('\n')

    print(f"{C.BG}MEMORY.md optimized!{C.R}")
    print()

    ns, nc, nst = health_score(len(important))
    print('=' * 60)
    print(f"{C.W}FINAL RESULTS:{C.R}")
    print('=' * 60)
    print(f"  Before: {C.Y}{count} lines{C.R}")
    print(f"  After:  {C.BG}{len(important)} lines{C.R}")
    print(f"  Health: {nc}{ns}/100 {nst}{C.R}")
    print(f"  Saved:  {C.BC}{count - len(important)} lines archived{C.R}")
    print('=' * 60)
    print()
    print(f"{C.BM}Memory optimization complete! Your memory is now lean!{C.R}")
    print()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{C.Y}Interrupted.{C.R}\n")
        sys.exit(0)
    except Exception as e:
        print(f"\n{C.BR}Error: {e}{C.R}\n")
        sys.exit(1)
