from pathlib import Path
import base64

ROOT = Path('.')
SRC = ROOT / '.banner-src' / 'gulf.b64'
IMG = ROOT / 'tgpu-gulf-hero-approved.jpg'
IMG.write_bytes(base64.b64decode(SRC.read_text(encoding='utf-8').strip()))

p = ROOT / 'index.html'
s = p.read_text(encoding='utf-8')
old = 'https://tgpugulf.com/tgpu-gulf/tgpu-gulf-brand.webp?v=20260921-brandfix3'
new = 'https://tgpugulf.com/tgpu-gulf/tgpu-gulf-hero-approved.jpg?v=20260922'
s = s.replace(old, new)
s = s.replace('<meta property="og:image:height" content="630">', '<meta property="og:image:height" content="675">')
hero = '<img class="approved-hero-art" src="tgpu-gulf-hero-approved.jpg" alt="TGPU Gulf — Malaysia and GCC opportunities, trade and collaboration" width="1200" height="675" fetchpriority="high" decoding="async">'
if 'class="approved-hero-art"' not in s:
    s = s.replace('<section class="hero">', '<section class="hero">' + hero, 1)
style = '''<style id="approved-hero-art-style">\n.approved-hero-art{display:block;width:min(1440px,calc(100% - 36px));height:auto;aspect-ratio:16/9;object-fit:cover;margin:0 auto 40px;border-radius:24px;box-shadow:0 28px 70px rgba(0,0,0,.32);border:1px solid rgba(255,255,255,.12)}\n@media(max-width:620px){.approved-hero-art{width:calc(100% - 20px);margin-bottom:24px;border-radius:16px}}\n</style>'''
if 'approved-hero-art-style' not in s:
    s = s.replace('</head>', style + '\n</head>', 1)
p.write_text(s, encoding='utf-8')

try:
    SRC.unlink()
except FileNotFoundError:
    pass
try:
    (ROOT/'.banner-src').rmdir()
except OSError:
    pass
for p in [ROOT/'.github/scripts/install-approved-hero.py', ROOT/'.github/workflows/install-approved-hero.yml']:
    try:
        p.unlink()
    except FileNotFoundError:
        pass
