#!/usr/bin/env python3
"""Static generator: python3 generator/build.py -> writes the site into the repo root."""
import os, json, html, sys, shutil
from PIL import Image
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from data import *
import logo as L
G = os.path.dirname(os.path.abspath(__file__)); R = os.path.abspath(os.path.join(G, '..'))
BASE = os.environ.get('BASE', BASE)
VER = '1'
e = html.escape
U = lambda s: html.unescape(s)

I = {
 'phone':'<path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2"/>',
 'msg':'<path d="M21 12a8 8 0 0 1-11.6 7.1L4 20l1-4.6A8 8 0 1 1 21 12z"/>',
 'arrow':'<path d="M5 12h14M13 6l6 6-6 6"/>',
 'left':'<path d="M19 12H5M11 6l-6 6 6 6"/>',
 'x':'<path d="M6 6l12 12M18 6L6 18"/>',
 'plus':'<path d="M12 5v14M5 12h14"/>',
 'pin':'<path d="M12 21s-7-6.2-7-11.5A7 7 0 0 1 19 9.5C19 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/>',
 'clock':'<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
 'star':'<path d="M12 3l2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1L3.2 9.5l6.1-.9z"/>',
 'check':'<path d="M5 12.5l4.5 4.5L19 7"/>',
 'cal':'<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/>',
 'nav':'<path d="M3 11l18-8-8 18-2-8z"/>',
 'engine':'<path d="M4 10h2V8h3V6h6v2h2l2 2h2v7h-2l-2 2H8l-2-2H4z"/><path d="M2 11v5M10 6V4h4"/>',
 'battery':'<rect x="3" y="7" width="18" height="12" rx="1.5"/><path d="M7 7V5h3v2M14 7V5h3v2M6 13h3.5M7.75 11.25v3.5M14.5 13H18"/>',
 'brake':'<circle cx="12" cy="12" r="5.5"/><path d="M5.2 6.2a9 9 0 0 0 0 11.6M18.8 6.2a9 9 0 0 1 0 11.6M12 9v3.6M12 15.2v.1"/>',
 'oil':'<path d="M3 11h9l3 2.5 6-3v1.8l-6 5.7H5a2 2 0 0 1-2-2z"/><path d="M6.5 11V8.5h3V11M3 9l2 1.5M20.5 16.5c0 1-.6 1.6-1.2 1.6s-1.2-.6-1.2-1.6.6-1.6 1.2-2.6c.6 1 1.2 1.6 1.2 2.6z"/>',
 'temp':'<path d="M12 3v10M10 3h4M9 6h3M9 9h3"/><circle cx="12" cy="15.5" r="2.6"/><path d="M3 21c2-1.4 4 1.4 6 0s4 1.4 6 0 4 1.4 6 0"/>',
 'tire':'<path d="M6.4 5.4a8 8 0 0 0-.2 12.6h11.6a8 8 0 0 0-.2-12.6"/><path d="M4.5 21h15M12 8v5M12 15.6v.1"/>',
 'snow':'<path d="M12 3v18M4.2 7.5l15.6 9M4.2 16.5l15.6-9M9.5 4.5L12 6.5l2.5-2M9.5 19.5l2.5-2 2.5 2"/>',
 'steer':'<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="2.5"/><path d="M3.3 10.5h6.2M14.5 10.5h6.2M12 14.5V21"/>',
 'truck':'<path d="M2 6h11v10H2zM13 9h4l4 4v3h-8z"/><circle cx="6" cy="17.5" r="2"/><circle cx="17" cy="17.5" r="2"/>',
 'wrench':'<path d="M14.7 6.3a4 4 0 0 0-5.4 5.4L3 18l3 3 6.3-6.3a4 4 0 0 0 5.4-5.4l-2.5 2.5-2.4-.6-.6-2.4z"/>',
 'shield':'<path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z"/><path d="M8.5 12l2.5 2.5 4.5-5"/>',
 'sofa':'<path d="M4 11V8a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v3"/><path d="M2 13a2 2 0 0 1 4 0v1h12v-1a2 2 0 0 1 4 0v5H2zM5 18v2M19 18v2"/>',
 'key':'<circle cx="8" cy="15" r="4"/><path d="M11 12l9-9M17 6l3 3M14 9l2 2"/>',
 'car':'<path d="M3 16v-4l2.2-5h13.6l2.2 5v4"/><path d="M3 16h18v3h-3v-2H6v2H3z"/><path d="M6.5 13h.1M17.5 13h.1"/>',
 'chat':'<path d="M4 5h16v11H9l-5 4z"/><path d="M8 9h8M8 12h5"/>',
 'cash':'<rect x="2" y="6" width="20" height="12" rx="2"/><circle cx="12" cy="12" r="2.5"/><path d="M6 12h.1M18 12h.1"/>',
 'fb':'<path d="M14 8h3V4h-3a4 4 0 0 0-4 4v2H7v4h3v7h4v-7h3l1-4h-4V8.5a.5.5 0 0 1 .5-.5z"/>',
 'g':'<path d="M20 12.2c0-.6 0-1.2-.2-1.7H12v3.3h4.5a3.9 3.9 0 0 1-1.7 2.5"/><path d="M19.6 8A8.5 8.5 0 1 0 20.4 13"/>',
}
def ic(n, cls=''):
    return f'<svg class="ic {cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{I[n]}</svg>'

_dims = {}
def dims(name):
    if name not in _dims: _dims[name] = Image.open(os.path.join(R, 'img', name)).size
    return _dims[name]
def img(k, alt, small=False, eager=False, cls='', sizes=None):
    f = f'{k}-s.webp' if small else f'{k}.webp'
    w, h = dims(f)
    ld = 'fetchpriority="high"' if eager else 'loading="lazy" decoding="async"'
    big = dims(k+'.webp')[0] > dims(k+'-s.webp')[0]
    srcset = '' if (small or not big) else f' srcset="img/{k}-s.webp {dims(k+"-s.webp")[0]}w, img/{k}.webp {w}w" sizes="{sizes or "(max-width:860px) 100vw, 50vw"}"'
    c = f' class="{cls}"' if cls else ''
    return f'<img src="img/{f}"{srcset} width="{w}" height="{h}" alt="{e(alt)}" {ld}{c}>'

PAGES = [('index.html','Home'),('services.html','Services'),('shop.html','The Shop'),('about.html','About'),('reviews.html','Reviews'),('contact.html','Contact')]
STAR5 = '<span class="stars" aria-hidden="true">' + ''.join(f'<svg viewBox="0 0 24 24">{I["star"]}</svg>' for _ in range(5)) + '</span>'
def stars(n=4.6):
    return f'<span class="stars-w" role="img" aria-label="{n} out of 5 stars"><span class="stars-bg">{STAR5}</span><span class="stars-fg" style="width:{n/5*100:.0f}%">{STAR5}</span></span>'
DIA = '<i class="dia" aria-hidden="true"></i>'

def head(page, title, desc, crumbs_ld, extra_ld=None):
    url = BASE + ('' if page == 'index.html' else page)
    lds = [business_ld()] + ([crumbs_ld] if crumbs_ld else []) + (extra_ld or [])
    ld = ''.join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>' for x in lds)
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{e(title)}</title><meta name="description" content="{e(desc)}">
<link rel="canonical" href="{url}"><meta name="theme-color" content="#13213A">
<meta property="og:type" content="website"><meta property="og:site_name" content="{e(NAME)}"><meta property="og:title" content="{e(title)}"><meta property="og:description" content="{e(desc)}"><meta property="og:url" content="{url}"><meta property="og:image" content="{BASE}img/og.jpg"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta property="og:locale" content="en_US">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{e(title)}"><meta name="twitter:description" content="{e(desc)}"><meta name="twitter:image" content="{BASE}img/og.jpg">
<link rel="icon" href="favicon.svg" type="image/svg+xml"><link rel="icon" href="favicon.ico" sizes="any"><link rel="apple-touch-icon" href="apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=Libre+Franklin:wght@400;500;600;700;800&family=Prata&family=Yellowtail&display=swap" rel="stylesheet">
<link rel="stylesheet" href="styles.css?v={VER}">{ld}</head>'''

DAYS = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
def hm(m): return f"{m//60:02d}:{m%60:02d}"
def business_ld():
    spec=[]
    for d,o,c in HOURS:
        if o is not None and d!='Friday': spec.append(d)
    hs=[{"@type":"OpeningHoursSpecification","dayOfWeek":["Monday","Tuesday","Wednesday","Thursday"],"opens":"07:30","closes":"17:30"},
        {"@type":"OpeningHoursSpecification","dayOfWeek":"Friday","opens":"07:30","closes":"17:00"}]
    return {"@context":"https://schema.org","@type":"AutoRepair","@id":BASE+"#business","name":NAME,"legalName":LEGAL,"slogan":"Honest service since 1975",
      "description":"Family-friendly auto repair shop in Gainesville, Florida since 1975 with ASE certified technicians and a comfortable lobby: diagnostics and check-engine lights, brakes, tires and alignment, steering and suspension, oil changes and maintenance, engine, electrical, battery, A/C, transmission and exhaust. Classic cars, daily drivers and fleet vehicles.",
      "foundingDate":"1975","url":BASE,"telephone":TEL,"image":BASE+"img/og.jpg","logo":BASE+"brand/logo-sign.svg",
      "address":{"@type":"PostalAddress","streetAddress":STREET,"addressLocality":CITY,"addressRegion":REGION,"postalCode":ZIP,"addressCountry":"US"},
      "geo":{"@type":"GeoCoordinates","latitude":GEO[0],"longitude":GEO[1]},
      "areaServed":{"@type":"City","name":"Gainesville, FL"},
      "openingHoursSpecification":hs,
      "specialOpeningHoursSpecification":[{"@type":"OpeningHoursSpecification","validFrom":k,"validThrough":k,"description":f"{v}: hours might differ"} for k,v in list(HOLIDAYS.items())[:2]],
      "hasMap":MAPS_LONG,"sameAs":[MAPS_LONG,FB],
      "aggregateRating":{"@type":"AggregateRating","ratingValue":RATING,"reviewCount":str(REVIEWS),"bestRating":"5"},
      "amenityFeature":[{"@type":"LocationFeatureSpecification","name":n,"value":True} for n in ["Comfortable customer lobby","ASE certified technicians","Loaner vehicle (ask when booking)"]],
      "hasOfferCatalog":{"@type":"OfferCatalog","name":"Auto repair services","itemListElement":[{"@type":"Offer","itemOffered":{"@type":"Service","name":U(s[1]),"description":U(s[4])}} for s in SVC]},
      "review":[{"@type":"Review","author":{"@type":"Person","name":r['name']},"reviewBody":r['text']} for r in REVIEWS_LIST]}

def crumbs(page, label):
    items = [{"@type":"ListItem","position":1,"name":"Home","item":BASE}]
    if page != 'index.html': items.append({"@type":"ListItem","position":2,"name":label,"item":BASE+page})
    return {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":items}

def nav(page):
    links = ''.join(f'<li><a href="{p}"{" aria-current=page" if p==page else ""}>{l}</a></li>' for p,l in PAGES)
    mlinks = ''.join(f'<a class="mm-l" href="{p}"{" aria-current=page" if p==page else ""} style="--d:{i}"><span>0{i+1}</span>{l}</a>' for i,(p,l) in enumerate(PAGES))
    return f'''<a class="skip" href="#main">Skip to content</a><div class="pbar" aria-hidden="true"><i></i></div>
<header class="nav"><div class="nav-in"><a class="brand" href="index.html" aria-label="{e(NAME)} home"><img class="b-l" src="brand/logo-horizontal-light.svg" alt="{e(NAME)}, since 1975" width="628" height="175"><img class="b-d" src="brand/logo-horizontal-dark.svg" alt="" width="628" height="175" aria-hidden="true"></a>
<nav aria-label="Main"><ul>{links}</ul></nav>
<div class="acts"><a class="btn line sm" href="contact.html#book">{ic('cal')}<span>Book</span></a><a class="btn red sm mag" href="tel:{TEL}">{ic('phone')}<span>{PHONE}</span></a></div>
<button class="menu-btn" aria-expanded="false" aria-controls="mmenu" aria-label="Open menu"><i></i><i></i></button></div></header>
<div class="mmenu" id="mmenu" aria-hidden="true"><nav aria-label="Mobile">{mlinks}</nav>
<div class="mm-foot"><a class="btn red" href="tel:{TEL}">{ic('phone')}Call {PHONE}</a><a class="btn line-l" href="contact.html#book">{ic('cal')}Request an appointment</a><p>{STREET}, {CITY}</p></div></div>'''

def badge(cls=''):
    return f'<span class="live {cls}" data-live><i></i><span>Hours today</span></span>'

def hours_rows():
    out=[]
    for i,(d,o,c) in enumerate(HOURS):
        v = 'Closed' if o is None else f'{fmt(o)} \u2013 {fmt(c)}'
        out.append(f'<tr data-day="{i}"><th scope="row">{d}</th><td>{v}</td></tr>')
    order = out[1:]+out[:1]
    return f'<table class="hrs"><caption class="sr">Shop hours (Eastern time)</caption>{"".join(order)}</table>'

def footer():
    links = ''.join(f'<li><a href="{p}">{l}</a></li>' for p,l in PAGES)
    return f'''<footer class="foot"><div class="foot-band" aria-hidden="true"><span>{(" \u25c6 ".join(["HONEST SERVICE","SINCE 1975","GAINESVILLE, FLORIDA","ASE CERTIFIED TECHNICIANS",DOOR.upper()])+" \u25c6 ")*3}</span></div><div class="wrap">
<div class="foot-top"><img src="brand/logo-sign.svg" alt="{e(NAME)} sign logo" width="640" height="420" loading="lazy" class="foot-logo">
<div><p class="foot-big">Honest service<br>since <em>1975.</em></p><p class="foot-ph"><a href="tel:{TEL}">{PHONE}</a></p></div></div>
<div class="foot-grid">
<div><h3>Pages</h3><ul>{links}</ul></div>
<div><h3>Visit</h3><p><a href="{DIR}" rel="noopener" target="_blank">{STREET}<br>{CITY}, {REGION} {ZIP}</a></p><p><a href="tel:{TEL}">{PHONE}</a></p></div>
<div><h3>Hours</h3><p>Mon\u2013Thu 7:30 AM \u2013 5:30 PM<br>Fri 7:30 AM \u2013 5:00 PM<br>Sat &amp; Sun closed</p><p>{badge('sm')}</p></div>
<div><h3>Find us</h3><p><a href="{MAPS}" rel="noopener" target="_blank">{ic('g')}Google: {RATING}\u2605 ({REVIEWS})</a></p><p><a href="{FB}" rel="noopener" target="_blank">{ic('fb')}Facebook: {FB_PCT}% recommend</a></p></div>
</div>
<div class="foot-bot"><span>\u00a9 2026 {e(LEGAL)}</span><span>Auto repair in Gainesville, FL since 1975</span><span>Demo design by RGWebD</span></div></div></footer>
<div class="mbar"><a href="tel:{TEL}" class="btn red">{ic('phone')}Call now</a><a href="{DIR}" class="btn line-d" rel="noopener" target="_blank">{ic('nav')}Directions</a></div>
<div class="demo" role="note"><span>Design preview by <b>RGWebD</b></span><button aria-label="Dismiss preview note">{ic('x')}</button></div>
<script src="script.js?v={VER}" defer></script></body></html>'''

def page_hero(key, alt, eyebrow, h1, lede, label, extra=''):
    return f'''<section class="phero"><div class="wrap phero-in"><div class="ph-copy"><nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a><span aria-hidden="true">\u25c6</span><span aria-current="page">{label}</span></nav>
<span class="eyebrow">{eyebrow}</span><h1 class="h1 split"><span class="ln"><span>{h1}</span></span></h1><p class="lede rv">{lede}</p>{extra}</div>
<figure class="ph-art rv"><div class="frame">{img(key, alt, eager=True, sizes="(max-width:860px) 92vw, 46vw")}</div><span class="frame-tag">{DIA}{e(CAP.get(key,(alt,))[0])}</span></figure></div></section>'''

def cta_band(variant='photo'):
    return f'''<section class="cta" aria-labelledby="cta-h"><div class="cta-sky" aria-hidden="true"></div><div class="wrap cta-in">
<div class="cta-sign rv" aria-hidden="true">{sign_inline('sgc')}</div>
<div class="cta-copy"><span class="eyebrow light">Bring it by</span><h2 class="h2 split" id="cta-h"><span class="ln"><span>Look for the sign on</span></span><span class="ln"><span><em>NE 19th Drive.</em></span></span></h2>
<p class="rv">Call ahead or stop in at {STREET}. Tell us what it\u2019s doing and we\u2019ll tell you straight what it needs.</p>
<div class="cta-row rv"><a class="btn red xl mag" href="tel:{TEL}">{ic('phone')}Call {PHONE}</a><a class="btn line-l xl" href="{DIR}" rel="noopener" target="_blank">{ic('nav')}Get directions</a></div>
<p class="rv cta-live">{badge()}</p></div></div></section>'''

def sign_inline(cls):
    """the roadside sign as inline SVG with animatable parts"""
    W=640; cx=320
    dia=lambda i:f'M{cx} {8+i}L{W-8-i*1.62:.1f} 206L{cx} {412-i}L{8+i*1.62:.1f} 206Z'
    dm=L.centered('DAVE MAYS',L.SERIF,128,cx,186,track=2,sx=.80)
    return (f'<svg class="sg {cls}" viewBox="0 0 640 560" role="img" aria-label="{e(NAME)} roadside sign: Dave Mays Automotive, since 1975">'
      f'<g class="sg-posts" fill="#1E3766"><rect x="150" y="300" width="34" height="260" rx="3"/><rect x="456" y="300" width="34" height="260" rx="3"/></g>'
      f'<g class="sg-board"><path fill="{L.EDGE}" d="{dia(0)}"/><path fill="#fff" d="{dia(12)}"/><path class="sg-line" fill="none" stroke="{L.EDGE}" stroke-width="2.5" d="{dia(21)}"/></g>'
      f'<g class="sg-name">{L.extrude(dm)}</g>'
      f'<g class="sg-ban">{L.banner(0,W,210,52,"AUTOMOTIVE",34)}</g>'
      f'<g class="sg-since"><path fill="{L.TEAL}" d="{L.centered("Since",L.SERIF,46,cx,318)}{L.centered("1975",L.SERIF,40,cx,360,track=1.5)}"/></g></svg>')

def marq(items, cls=''):
    row=''.join(f'<span>{t}</span><i aria-hidden="true">\u25c6</i>' for t in items)
    return f'<div class="banner-marq {cls}" aria-label="Services: {", ".join(items)}"><b class="bm-cap l" aria-hidden="true"></b><div class="bm-track" aria-hidden="true"><div>{row}{row}</div></div><b class="bm-cap r" aria-hidden="true"></b></div>'

def gauge(cls, label, maxv, val, ticks, unit, dec=0, sub=''):
    """semi-circle dial; needle angle set by CSS var --g (0..1) from JS"""
    tk=''
    import math
    n=len(ticks)-1
    for i,t in enumerate(ticks):
        a=math.radians(180-180*i/n); x1=100+78*math.cos(a); y1=100-78*math.sin(a); x2=100+66*math.cos(a); y2=100-66*math.sin(a)
        tx=100+52*math.cos(a); ty=100-52*math.sin(a)+4
        tk+=f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}"/><text x="{tx:.1f}" y="{ty:.1f}">{t}</text>'
    minor=''
    for i in range(n*4+1):
        a=math.radians(180-180*i/(n*4)); minor+=f'<line x1="{100+78*math.cos(a):.1f}" y1="{100-78*math.sin(a):.1f}" x2="{100+73*math.cos(a):.1f}" y2="{100-73*math.sin(a):.1f}"/>'
    return f'''<figure class="gauge {cls}" style="--g:{val/maxv:.4f}"><svg viewBox="0 0 200 118" aria-hidden="true"><path class="g-arc" d="M18 100A82 82 0 0 1 182 100"/><path class="g-fill" pathLength="1" d="M18 100A82 82 0 0 1 182 100"/><g class="g-minor">{minor}</g><g class="g-ticks">{tk}</g><g class="g-needle"><path d="M97 100L100 30L103 100Z"/><circle cx="100" cy="100" r="8"/></g></svg>
<figcaption><b><span data-to="{val}" data-dec="{dec}">0</span>{unit}</b><span>{label}</span>{sub}</figcaption></figure>'''

def odo(value, label):
    digits=''.join(f'<span class="od-d" style="--n:{ch}"><span>{"".join(f"<i>{n}</i>" for n in range(10))}</span></span>' if ch.isdigit() else f'<span class="od-s">{ch}</span>' for ch in value)
    return f'<div class="odo" role="img" aria-label="{label}"><span class="od-w">{digits}</span></div>'

def rv_ticket(r, n, full=False, cls='slide'):
    txt = r['text'] if full else r['pull']
    body = ''.join(f'<p>{e(p)}</p>' for p in txt.split('\n') if p.strip())
    return f'''<article class="ticket {cls}"><div class="tk-top"><span>Repair order</span><span>No. {1975+n:04d}</span></div>
<div class="tk-row"><span>Customer</span><b>{e(r["name"])}</b></div><div class="tk-row"><span>Job</span><b>{e(r["tag"])}</b></div>
<div class="tk-stars">{STAR5}<small>Google \u00b7 {e(r["age"])}</small></div><blockquote>{body}</blockquote>
{'' if full else '<a class="tk-more" href="reviews.html">Read the full review '+ic('arrow')+'</a>'}<span class="tk-stamp" aria-hidden="true">Paid in full<br>\u2605 thank you \u2605</span></article>'''

def home():
    t = f'{NAME} | Honest Auto Repair in Gainesville, FL Since 1975'
    d = f'Gainesville auto repair since 1975. ASE certified technicians, a comfortable lobby, loaner vehicle and a 2-year/20,000-mile warranty on most parts and labor. {RATING}\u2605 from {REVIEWS} Google reviews. Call {PHONE}.'
    lights = ''.join(f'<button class="lt {c}" data-k="{k}" aria-pressed="{"true" if i==0 else "false"}" aria-controls="dash-read"><span class="lt-i">{ic(k)}</span><span class="lt-l">{lab}</span></button>' for i,(k,lab,c,_,_,_) in enumerate(DASH))
    reads = ''.join(f'<div class="rd" data-k="{k}"{"" if i==0 else " hidden"}><span class="rd-k {c}">{ic(k)}{lab}</span><p class="rd-m">{m}</p><p class="rd-w"><b>What we do:</b> {w}</p><a class="rd-a" href="services.html#{s}">See {U([x for x in SVC if x[0]==s][0][1]).lower()} {ic("arrow")}</a></div>' for i,(k,lab,c,m,w,s) in enumerate(DASH))
    why = [
     ('chat','Straight talk, every time','The good, the bad or the ugly, with the reasons, before any work begins.','James Crosby','They shoot it to you straight, the good, bad, or ugly.'),
     ('cash','Options for your budget','What has to happen now, what can wait, and what isn\u2019t worth the money.','rene morrissey','Giving a range of repair options and timing to accommodate budgets.'),
     ('key','Ask about a loaner','We keep a loaner vehicle, so a repair doesn\u2019t have to cost you a day of work.','Karen Swinea','They also have a loaner vehicle so you don\u2019t have to miss time off work.'),
     ('sofa','A lobby worth waiting in','Big windows, comfortable seats, and restrooms one regular calls the cleanest around.','Tina Perkins','And they have the cleanest bathrooms.'),
    ]
    whyh = ''.join(f'<li class="why-i rv" style="--d:{i}"><span class="why-n">{ic(icn)}</span><div><h3>{h}</h3><p>{p}</p><q>{e(qq)}</q> <cite>{e(who)}</cite></div></li>' for i,(icn,h,p,who,qq) in enumerate(why))
    tiles = ''.join(f'<a class="st tilt rv" href="services.html#{k}" style="--d:{i%4}"><span class="st-img">{img(ph,U(ti),small=True)}</span><span class="st-ic">{ic(icn)}</span><span class="st-t">{ti}</span><span class="st-s">{sh}</span><span class="st-go">{ic("arrow")}</span></a>' for i,(k,ti,ph,ins,sh,lo,bl,pr,icn) in enumerate(SVC[:6]))
    slides = ''.join(rv_ticket(r,i) for i,r in enumerate([REVIEWS_LIST[x] for x in (0,1,2,4,5,6,7)]))
    teas = [('shop.html','The Shop','Lifts, the alignment rack, the lobby and a few classics.','g07','A look around'),
            ('about.html','About us','Our sign, our crew and how we\u2019ve done it since 1975.','g01','Since 1975'),
            ('reviews.html','Reviews',f'{RATING} stars from {REVIEWS} Google reviews, in their own words.',None,'Word of mouth'),
            ('contact.html','Visit &amp; book','Hours, directions and an appointment request.',None,'Come on by')]
    teah=''
    for i,(href,ti,p,ph,ey) in enumerate(teas):
        art = img(ph,ti,small=True) if ph else (f'<span class="te-big">{RATING}<small>\u2605</small></span>' if 'rev' in href else f'<span class="te-big te-map">{ic("pin")}</span>')
        teah+=f'<a class="te rv" href="{href}" style="--d:{i}"><span class="te-art">{art}</span><span class="te-e">{ey}</span><span class="te-t">{ti}</span><span class="te-p">{p}</span><span class="te-go">{ic("arrow")}</span></a>'
    return f'''{head('index.html',t,d,crumbs('index.html','Home'))}<body class="home">{nav('index.html')}
<div class="loader" aria-hidden="true"><div class="ld-in">{sign_inline('ld')}</div></div>
<main id="main">
<section class="hero" aria-labelledby="h1"><div class="hero-bg" aria-hidden="true"><span class="bigout">1975</span></div>
<div class="wrap hero-in"><div class="h-copy">
<span class="eyebrow">{DIA}Auto repair \u00b7 Gainesville, Florida \u00b7 Since 1975</span>
<h1 class="h1 split" id="h1"><span class="ln"><span>Honest repairs,</span></span><span class="ln"><span>straight answers,</span></span><span class="ln"><span><em>since 1975.</em></span></span></h1>
<p class="lede rv">ASE certified technicians, a comfortable lobby while you wait, and a 2-year/20,000-mile warranty on most parts and labor. Look for the red-and-white sign on NE 19th Drive.</p>
<div class="cta-row rv"><a class="btn red xl mag" href="tel:{TEL}">{ic('phone')}Call {PHONE}</a><a class="btn line xl" href="contact.html#book">{ic('cal')}Request an appointment</a></div>
<div class="trust rv"><a class="tr-g" href="reviews.html"><b>{RATING}</b><span>{stars(4.6)}<small>{REVIEWS} Google reviews</small></span></a><a class="tr-g fb" href="{FB}" rel="noopener" target="_blank"><b>{FB_PCT}%</b><span><small>recommend on Facebook</small><small>({FB_N} reviews)</small></span></a>{badge()}</div></div>
<figure class="h-art rv"><div class="h-frame"><div class="h-photo">{img('g16','The Dave Mays Automotive crew standing in front of the shop and its red-and-white roadside sign',eager=True,sizes="(max-width:860px) 94vw, 52vw")}</div>
<button class="pin" style="--x:21%;--y:30%" aria-expanded="false"><span class="sr">About the sign</span>{ic('plus')}<span class="pin-tip">The sign out front. If you\u2019re in Gainesville, you\u2019ve probably driven past it.</span></button>
<button class="pin" style="--x:54%;--y:62%" aria-expanded="false"><span class="sr">About the crew</span>{ic('plus')}<span class="pin-tip">ASE certified technicians. Reviewers know them by name.</span></button>
<button class="pin" style="--x:20%;--y:52%" aria-expanded="false"><span class="sr">About the address</span>{ic('plus')}<span class="pin-tip">2905 NE 19th Dr. You\u2019ve found us.</span></button></div>
<figcaption class="h-cap"><span>{DIA}{STREET}</span><span>Gainesville, FL</span></figcaption>
<div class="seal" aria-hidden="true"><svg viewBox="0 0 200 200"><defs><path id="sealc" d="M100 100m-74 0a74 74 0 1 1 148 0a74 74 0 1 1-148 0"/></defs><text><textPath href="#sealc" textLength="462" lengthAdjust="spacing">HONEST SERVICE \u25c6 SINCE 1975 \u25c6 GAINESVILLE \u25c6 </textPath></text></svg><span>2yr<br><small>20K MI</small></span></div></figure>
</div></section>
{marq(["Diagnostics","Brakes","Tires","Alignment","Steering &amp; suspension","Oil changes","A/C","Engine","Electrical","Batteries","Exhaust","Transmission","Filters","Classic cars","Fleets"])}
<section class="dash sec" aria-labelledby="dash-h"><div class="wrap">
<div class="sec-head"><span class="eyebrow light rv">{DIA}What\u2019s your dash telling you?</span><h2 class="h2 split" id="dash-h"><span class="ln"><span>Tap a light. <em>We\u2019ll explain it.</em></span></span></h2></div>
<div class="cluster rv">
{gauge('g-rate','Google rating',5,4.6,['0','1','2','3','4','5'],'',1,f'<small>{REVIEWS} reviews</small>')}
<div class="cl-mid"><div class="lights" role="group" aria-label="Dashboard warning lights">{lights}</div>
<div class="readout" id="dash-read" aria-live="polite">{reads}</div>
<div class="cl-odo"><span>Serving Gainesville since</span>{odo('1975','Since 1975')}</div></div>
{gauge('g-war','Warranty, most parts &amp; labor',24,24,['0','6','12','18','24'],' mo','0','<small class="g-odo">'+odo('20,000','20,000 miles')+'<em>miles</em></small>')}
</div><p class="dash-note rv">General guidance only. When a red light comes on, pull over safely and call us at <a href="tel:{TEL}">{PHONE}</a>.</p></div></section>
<section class="why sec" aria-labelledby="why-h"><div class="wrap why-in">
<figure class="why-art rv"><div class="arch">{img('g17','The bright Dave Mays Automotive lobby with tall windows, red armchairs and a gray sofa',sizes="(max-width:860px) 92vw, 40vw")}</div><figcaption>{DIA}The lobby</figcaption><span class="why-badge"><span>ASE<small>certified techs</small></span></span></figure>
<div><span class="eyebrow rv">{DIA}The Dave Mays way</span><h2 class="h2 split" id="why-h"><span class="ln"><span>Why Gainesville keeps</span></span><span class="ln"><span><em>coming back.</em></span></span></h2>
<ul class="why-l">{whyh}</ul></div></div></section>
<section class="svc sec" aria-labelledby="svc-h"><div class="wrap">
<div class="sec-head row"><div><span class="eyebrow rv">{DIA}Services</span><h2 class="h2 split" id="svc-h"><span class="ln"><span>Bumper to bumper, <em>under one roof.</em></span></span></h2></div><a class="btn line rv" href="services.html">All services {ic('arrow')}</a></div>
<div class="st-grid">{tiles}</div>
<div class="workon rv"><span class="wo-l">We work on</span>{"".join(f'<span class="wo-p">{DIA}{w}</span>' for w in WORK_ON)}<a href="services.html#fleet">Classics &amp; fleets {ic('arrow')}</a></div></div></section>
<section class="rvband sec" aria-labelledby="rv-h"><div class="wrap rv-in"><div class="rv-side"><span class="eyebrow light rv">{DIA}Reviews</span><h2 class="h2 split" id="rv-h"><span class="ln"><span>Signed off by</span></span><span class="ln"><span><em>our customers.</em></span></span></h2>
<div class="rv-score rv"><b>{RATING}</b>{stars(4.6)}<span>{REVIEWS} Google reviews</span></div><a class="btn line-l rv" href="reviews.html">Read them all {ic('arrow')}</a></div>
<div class="car rv" data-car><div class="car-track">{slides}</div><div class="car-ui"><button class="prev" aria-label="Previous review">{ic('left')}</button><div class="car-dots"></div><button class="next" aria-label="Next review">{ic('arrow')}</button></div></div></div></section>
<section class="teasers sec" aria-label="More about Dave Mays"><div class="wrap te-grid">{teah}</div></section>
{cta_band()}</main>{footer()}'''

def services():
    t=f'Auto Repair Services in Gainesville, FL | {NAME}'
    d=f'Diagnostics, brakes, tires and alignment, steering and suspension, oil changes, engine, electrical, battery, A/C, transmission and exhaust. Classic cars, daily drivers and fleets. Call {PHONE}.'
    jump=''.join(f'<a href="#{s[0]}">{ic(s[8])}{s[1]}</a>' for s in SVC)
    secs=''
    for i,(k,ti,ph,ins,sh,lo,bl,(who,qq),icn) in enumerate(SVC):
        inset = f'<span class="sv-inset">{img(ins,CAP[ins][0],small=True)}</span>' if ins else ''
        secs+=f'''<section class="sv{" alt" if i%2 else ""}" id="{k}" aria-labelledby="sv-{k}"><div class="wrap sv-in">
<figure class="sv-art rv"><div class="frame">{img(ph,CAP[ph][0],sizes="(max-width:860px) 92vw, 46vw")}</div>{inset}<span class="sv-num">0{i+1}</span></figure>
<div class="sv-copy"><span class="eyebrow rv">{ic(icn)}{sh}</span><h2 class="h2 split" id="sv-{k}"><span class="ln"><span>{ti}</span></span></h2><p class="rv">{lo}</p>
<ul class="ticks rv">{"".join(f"<li>{ic('check')}{b}</li>" for b in bl)}</ul>
<blockquote class="sv-q rv"><p>\u201c{e(qq)}\u201d</p><cite>{e(who)} \u00b7 Google review</cite></blockquote>
<a class="btn red rv" href="tel:{TEL}">{ic('phone')}Call about {U(ti).split(",")[0].split(" &")[0].lower()}</a></div></div></section>'''
    steps=[('phone','Call or stop by',f'Call {PHONE} or come in to {STREET}. Tell us what it\u2019s doing, sounding like or warning you about.'),
           ('engine','We diagnose it','We find the actual cause. Sometimes we\u2019ve researched it before you even arrive.'),
           ('chat','You get options','What it needs now, what can wait, and what isn\u2019t worth the money, with the reasons.'),
           ('wrench','We fix it right','Our ASE certified technicians do the work while you relax in the lobby. Ask about our loaner vehicle.'),
           ('shield','Backed by a warranty','Most parts and labor carry a 2-year/20,000-mile warranty. We stand behind our work.')]
    sth=''.join(f'<li class="stp rv" style="--d:{i}"><span class="stp-n">{ic(icn)}</span><b>{h}</b><p>{p}</p></li>' for i,(icn,h,p) in enumerate(steps))
    return f'''{head('services.html',t,d,crumbs('services.html','Services'))}<body>{nav('services.html')}<main id="main">
{page_hero('g15','A technician beside the blue alignment rack inside the shop','Services \u00b7 Gainesville auto repair','Everything your car needs, <em>under one roof.</em>','Diagnostics to alignments, oil changes to A/C, on classic cars, daily drivers and fleet vehicles.','Services')}
<nav class="jump" aria-label="Jump to a service"><div class="wrap jump-in">{jump}</div></nav>
{secs}
<section class="how sec" aria-labelledby="how-h"><div class="wrap"><div class="sec-head"><span class="eyebrow light rv">{DIA}How a visit works</span><h2 class="h2 split" id="how-h"><span class="ln"><span>No surprises, <em>start to finish.</em></span></span></h2></div>
<ol class="steps">{sth}</ol>
<div class="war rv"><span class="war-b">2<small>years</small></span><span class="war-b">20,000<small>miles</small></span><p>Warranty on most parts and labor. Ask us what\u2019s covered on your repair.</p></div></div></section>
{cta_band()}</main>{footer()}'''

def shop():
    t=f'The Shop: Photos | {NAME}, Gainesville FL'
    d=f'Photos of {NAME}: the shop floor and lifts, alignment rack, the comfortable lobby, classic trucks and the roadside sign at {ADDR}.'
    order=['g03','g17','g08','g15','g07','f08','g02','f10','f07','sign','g09','f11','f01','f03','g10']
    gh=''
    for i,k in enumerate(order):
        cap,tag=CAP[k]
        gh+=f'<li class="gi rv {tag}" data-tag="{tag}" style="--d:{i%3}"><button class="gi-b" data-full="img/{k}.webp" data-cap="{e(cap)}" aria-label="Open photo: {e(cap)}">{img(k,cap,small=True)}<span class="gi-c">{DIA}{e(cap)}</span></button></li>'
    f=''.join(f'<button class="fbtn" data-f="{k}" aria-pressed="{"true" if k=="all" else "false"}">{l}</button>' for k,l in [('all','All'),('shop','Shop floor'),('lobby','Lobby'),('classic','Classics'),('outside','Outside')])
    return f'''{head('shop.html',t,d,crumbs('shop.html','The Shop'),[{"@context":"https://schema.org","@type":"ImageGallery","name":"Dave Mays Automotive shop photos","image":[f"{BASE}img/{k}.webp" for k in order]}])}<body>{nav('shop.html')}<main id="main">
<section class="phero gal-h"><div class="wrap"><nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a><span aria-hidden="true">\u25c6</span><span aria-current="page">The Shop</span></nav><span class="eyebrow">{DIA}A look around</span><h1 class="h1 split"><span class="ln"><span>Come see <em>the shop.</em></span></span></h1><p class="lede rv">Lifts, the alignment rack, the lobby and the odd classic in for work. Every photo here is the real shop.</p>
<div class="filters rv" role="group" aria-label="Filter photos">{f}</div></div></section>
<section class="sec gal"><div class="wrap"><ul class="gal-grid">{gh}</ul></div></section>
<div class="lbx" hidden role="dialog" aria-modal="true" aria-label="Photo viewer"><figure><img alt=""><figcaption></figcaption></figure><button class="lbx-x" aria-label="Close">{ic('x')}</button><button class="lbx-p" aria-label="Previous photo">{ic('left')}</button><button class="lbx-n" aria-label="Next photo">{ic('arrow')}</button></div>
{gfx_cta()}</main>{footer()}'''

def gfx_cta():
    return f'''<section class="cta gfx" aria-labelledby="cta-h"><div class="wrap cta-g"><span class="cta-out" aria-hidden="true">SINCE 1975</span><h2 class="h2 split" id="cta-h"><span class="ln"><span>Like what you see? <em>Bring it in.</em></span></span></h2>
<div class="cta-row rv"><a class="btn red xl mag" href="tel:{TEL}">{ic('phone')}Call {PHONE}</a><a class="btn line-l xl" href="contact.html#book">{ic('cal')}Request an appointment</a></div><p class="rv cta-live">{badge()}</p></div></section>'''

def about():
    t=f'About Us: Gainesville Auto Repair Since 1975 | {NAME}'
    d=f'{NAME} has served Gainesville, FL since 1975: ASE certified technicians, a comfortable lobby, a loaner vehicle and honest, straight answers. Visit us at {ADDR}.'
    vals=[('shield','ASE certified technicians','Our technicians are ASE certified, and reviewers know them by name.'),
          ('sofa','A comfortable lobby','A clean, relaxed space with big windows while we take care of your car.'),
          ('key','Loaner vehicle','Ask about our loaner so a repair doesn\u2019t cost you a day of work.'),
          ('car','Classics, daily drivers, fleets','From a vintage pickup to the company trucks to the family minivan.')]
    vh=''.join(f'<li class="val rv" style="--d:{i}"><span>{ic(icn)}</span><h3>{h}</h3><p>{p}</p></li>' for i,(icn,h,p) in enumerate(vals))
    chips=''.join(f'<li>{c}</li>' for c in TOPICS)
    return f'''{head('about.html',t,d,crumbs('about.html','About'))}<body>{nav('about.html')}<main id="main">
{page_hero('g01','The Dave Mays Automotive team, six technicians and staff in matching shirts, outside the shop','About \u00b7 Since 1975','Gainesville\u2019s shop, <em>since 1975.</em>','Waiting on your vehicle doesn\u2019t have to mean waiting around. That\u2019s how we\u2019ve looked after Gainesville since 1975.','About')}
<section class="sec story" aria-labelledby="st-h"><div class="wrap story-in">
<div><span class="eyebrow rv">{DIA}Our story</span><h2 class="h2 split" id="st-h"><span class="ln"><span>Customers and their cars</span></span><span class="ln"><span><em>come first.</em></span></span></h2>
<p class="rv">{NAME} has been fixing Gainesville\u2019s cars since 1975. We believe no job is too big: classic cars, day-to-day vehicles and fleet vehicles all roll through our bays.</p>
<p class="rv">What hasn\u2019t changed is how we do it. We tell you straight what your car needs, give you options that fit your budget, and stand behind our work with a 2-year/20,000-mile warranty on most parts and labor.</p>
<p class="rv">Some customers have been coming for decades. One family has brought all six of their cars to us over almost 30 years. Another drives up from St. Petersburg.</p>
<p class="door rv">\u201c{DOOR}\u201d <small>\u2014 on our front door</small></p></div>
<figure class="sign-photo rv"><div class="postcard">{img('sign','The Dave Mays Automotive roadside sign: a white diamond with red Dave Mays lettering, an Automotive banner and Since 1975',sizes="(max-width:860px) 92vw, 44vw")}<span class="pc-stamp" aria-hidden="true">GAINESVILLE<br>FLA.</span></div>
<figcaption>{DIA}The sign out front. Our new logo is drawn straight from it.</figcaption></figure></div></section>
<section class="sec vals" aria-labelledby="v-h"><div class="wrap"><div class="sec-head"><span class="eyebrow rv">{DIA}What you get here</span><h2 class="h2 split" id="v-h"><span class="ln"><span>The little things <em>add up.</em></span></span></h2></div><ul class="val-grid">{vh}</ul></div></section>
<section class="sec lobby" aria-labelledby="lb-h"><div class="wrap lobby-in">
<figure class="lb-a rv">{img('g02','Lobby seating with a red armchair and car magazines on a coffee table',small=True)}</figure>
<div><span class="eyebrow light rv">{DIA}The lobby</span><h2 class="h2 split" id="lb-h"><span class="ln"><span>Wait in <em>comfort.</em></span></span></h2><p class="rv">Tall windows, comfortable seats, magazines on the table and restrooms our customers call the cleanest around. Stay while we work, or ask about the loaner and get on with your day.</p>
<h3 class="rv chips-h">What customers mention most</h3><ul class="chips rv">{chips}</ul></div>
<figure class="lb-b rv">{img('g17','The bright lobby with tall windows, red armchairs and a gray sofa',small=True)}</figure></div></section>
{cta_band()}</main>{footer()}'''

def reviews():
    t=f'Reviews: {RATING} Stars from {REVIEWS} Google Reviews | {NAME}'
    d=f'Read what Gainesville drivers say about {NAME}: {RATING} stars from {REVIEWS} Google reviews and {FB_PCT}% recommend on Facebook.'
    cards=''.join(rv_ticket(r,i,full=True,cls='rv') for i,r in enumerate(REVIEWS_LIST))
    ex=''.join(f'<li class="rv"><q>{e(x["text"])}</q><cite>{e(x["name"])} \u00b7 Google review (excerpt)</cite></li>' for x in EXCERPTS)
    return f'''{head('reviews.html',t,d,crumbs('reviews.html','Reviews'))}<body>{nav('reviews.html')}<main id="main">
<section class="phero rvhero"><div class="wrap rvh-in"><div><nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a><span aria-hidden="true">\u25c6</span><span aria-current="page">Reviews</span></nav><span class="eyebrow">{DIA}Word of mouth since 1975</span><h1 class="h1 split"><span class="ln"><span>In their <em>own words.</em></span></span></h1><p class="lede rv">Ten Google reviews, quoted word for word. Typos and all.</p></div>
<div class="rvh-score rv"><div class="big"><b data-to="4.6" data-dec="1">0</b>{stars(4.6)}<span>{REVIEWS} Google reviews</span><a href="{MAPS}" rel="noopener" target="_blank">See them on Google {ic('arrow')}</a></div><div class="big fb"><b><span data-to="98">0</span>%</b><span>recommend us on Facebook ({FB_N} reviews)</span><a href="{FB}" rel="noopener" target="_blank">Facebook page {ic('arrow')}</a></div></div></div></section>
<section class="sec rvwall"><div class="wrap"><div class="tk-grid">{cards}</div>
<ul class="excerpts">{ex}</ul></div></section>
{cta_band()}</main>{footer()}'''

def contact():
    t=f'Contact &amp; Hours | {NAME}, {ADDR}'
    d=f'Visit {NAME} at {ADDR}. Call {PHONE}. Open Monday to Thursday 7:30 AM to 5:30 PM, Friday 7:30 AM to 5:00 PM.'
    faqs=[('What are your hours?','Monday to Thursday 7:30 AM to 5:30 PM and Friday 7:30 AM to 5:00 PM. We\u2019re closed Saturday and Sunday. Holiday hours may vary, so call ahead around holidays.'),
          ('Where are you?',f'{ADDR}. Look for the red-and-white diamond sign out front.'),
          ('Do you offer a warranty?','Yes. Most of our parts and labor carry a 2-year/20,000-mile warranty. Ask us what\u2019s covered on your specific repair.'),
          ('Is there a loaner car?','We have a loaner vehicle. Ask about it when you call to set up your repair.'),
          ('What vehicles do you work on?','Classic cars, day-to-day vehicles and fleet vehicles.'),
          ('Are your technicians certified?','Yes, our technicians are ASE certified.'),
          ('Can I wait while you work?','Yes. Our comfortable lobby gives you a clean, relaxed space while we take care of your car.')]
    faqh=''.join(f'<details class="fq rv"><summary>{q}{ic("plus")}</summary><p>{a}</p></details>' for q,a in faqs)
    fld={"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faqs]}
    opts=''.join(f'<option>{U(s[1])}</option>' for s in SVC)
    return f'''{head('contact.html',U(t),d,crumbs('contact.html','Contact'),[fld])}<body>{nav('contact.html')}<main id="main">
{page_hero('g10','The shop front door with Dave Mays Automotive lettering, phone number and hours','Contact \u00b7 Hours \u00b7 Directions','Come see us on <em>NE 19th Drive.</em>',f'Call {PHONE}, stop by, or send an appointment request below.','Contact')}
<section class="sec ct" aria-label="Contact details"><div class="wrap ct-in"><div class="ct-info">
<a class="ct-line rv" href="tel:{TEL}"><span>{ic('phone')}</span><div><small>Call the shop</small><b class="ct-big">{PHONE}</b></div></a>
<a class="ct-line rv" href="{DIR}" rel="noopener" target="_blank"><span>{ic('pin')}</span><div><small>Address</small><b>{STREET}<br>{CITY}, {REGION} {ZIP}</b><em>Get directions {ic('arrow')}</em></div></a>
<div class="ct-line rv"><span>{ic('clock')}</span><div><small>Hours (Eastern)</small>{badge('sm')}{hours_rows()}<p class="hol" data-hol hidden></p></div></div></div>
<form class="ct-form rv" id="book" data-sms="{TEL}" novalidate><div class="ro-head"><span>Appointment request</span><span>{NAME}</span></div><h2>Tell us what it\u2019s doing</h2>
<div class="fr"><label>Your name<input name="name" autocomplete="name" required></label><label>Your phone<input name="phone" type="tel" autocomplete="tel" required></label></div>
<div class="fr"><label>Year / make / model<input name="car" placeholder="e.g. 2014 Subaru Forester"></label><label>Preferred day<input name="date" type="date"></label></div>
<label>Service<select name="svc">{opts}<option>Not sure yet</option></select></label>
<label>What\u2019s going on?<textarea name="msg" rows="4" placeholder="Noises, warning lights, when it started..."></textarea></label>
<div class="fr2"><button class="btn red xl mag" type="submit">{ic('msg')}Text this request</button><a class="btn line xl" href="tel:{TEL}">{ic('phone')}Or call</a></div><p class="muted small">This opens your phone\u2019s messaging app with the details filled in. Nothing is sent until you hit send. Calling is the surest way to reach the shop.</p></form>
</div></section>
<section class="sec faqs" aria-labelledby="fq-h"><div class="wrap faq-in"><div><span class="eyebrow rv">{DIA}FAQ</span><h2 class="h2 split" id="fq-h"><span class="ln"><span>Quick <em>answers.</em></span></span></h2><figure class="ext rv">{img('g07','The Dave Mays Automotive building on NE 19th Drive under a blue sky',small=True)}<figcaption>{DIA}{STREET}</figcaption></figure></div><div class="faq-list">{faqh}</div></div></section>
<section class="sec mapsec" aria-label="Map"><div class="wrap"><div class="map rv"><iframe title="Map to Dave Mays Automotive, {ADDR}" src="https://maps.google.com/maps?q=Dave+Mays+Automotive,+2905+NE+19th+Dr,+Gainesville,+FL+32609&amp;z=15&amp;output=embed" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe></div></div></section>
</main>{footer()}'''

def notfound():
    b='/davemaysautomotive-demo/'
    s=f'''{head('404.html','Page not found | '+NAME,'This page could not be found.',None)}<body class="nf">{nav('404.html')}<main id="main"><section class="nf-in"><div class="wrap"><div class="nf-light" aria-hidden="true">{ic('engine')}</div><span class="eyebrow">{DIA}404 \u00b7 Wrong turn</span><h1 class="h1">This page took a <em>wrong turn.</em></h1><p class="lede">The page you\u2019re looking for isn\u2019t here. Head back home or give us a call.</p><div class="cta-row"><a class="btn red" href="index.html">Back to home</a><a class="btn line" href="tel:{TEL}">{ic('phone')}{PHONE}</a></div></div></section></main>{footer()}'''
    s=s.replace('<head><meta charset="utf-8">',f'<head><meta charset="utf-8"><base href="{b}">',1).replace('<link rel="canonical"','<meta name="robots" content="noindex"><link rel="canonical"',1)
    return s

def main():
    out={'index.html':home(),'services.html':services(),'shop.html':shop(),'about.html':about(),'reviews.html':reviews(),'contact.html':contact(),'404.html':notfound()}
    for k,v in out.items(): open(os.path.join(R,k),'w').write(v)
    shutil.copy(os.path.join(G,'styles.css'),os.path.join(R,'styles.css')); shutil.copy(os.path.join(G,'script.js'),os.path.join(R,'script.js'))
    open(os.path.join(R,'robots.txt'),'w').write(f'User-agent: *\nAllow: /\nSitemap: {BASE}sitemap.xml\n')
    urls=''.join(f'<url><loc>{BASE}{"" if p=="index.html" else p}</loc><changefreq>monthly</changefreq><priority>{"1.0" if p=="index.html" else "0.8"}</priority></url>' for p,_ in PAGES)
    open(os.path.join(R,'sitemap.xml'),'w').write(f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>\n')
    llm=f"""# {NAME}
> Auto repair shop in Gainesville, Florida, serving customers since 1975 (as stated by the business). ASE certified technicians, comfortable customer lobby, loaner vehicle. Rated {RATING}/5 from {REVIEWS} Google reviews; {FB_PCT}% recommend on Facebook ({FB_N} reviews).

- Address: {ADDR}
- Phone: {PHONE}
- Hours (Eastern): Mon-Thu 7:30 AM-5:30 PM; Fri 7:30 AM-5:00 PM; Sat-Sun closed. Holiday hours may vary.
- Warranty: 2 years / 20,000 miles on most parts and labor (ask what covers your repair).
- Vehicles: classic cars, day-to-day vehicles, fleet vehicles.
- Pricing: not published; call for a quote.
- Google: {MAPS_LONG}
- Facebook: {FB}

## Services
""" + ''.join(f"- {U(s[1])}: {U(s[4])} ({', '.join(U(b) for b in s[6])})\n" for s in SVC) + f"""
## Pages
- [Home]({BASE}): overview, dashboard-light guide, why customers return, services, reviews
- [Services]({BASE}services.html): each service and how a visit works
- [The Shop]({BASE}shop.html): photo gallery of the shop, lobby and classics
- [About]({BASE}about.html): history since 1975, the roadside sign, the lobby
- [Reviews]({BASE}reviews.html): ten Google reviews quoted word for word
- [Contact]({BASE}contact.html): phone, address, hours, appointment request (opens a text message), FAQ, map
"""
    open(os.path.join(R,'llms.txt'),'w').write(llm)
    print('built',len(out),'pages')
if __name__=='__main__': main()
