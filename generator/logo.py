"""Hand-built vector logo for Dave Mays Automotive, modelled on their roadside sign:
white diamond with navy/teal edge, red 3D serif 'DAVE MAYS', red banner 'AUTOMOTIVE' with diamond end-caps, teal 'Since 1975'. Text -> paths."""
import os
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.boundsPen import BoundsPen
HERE=os.path.dirname(os.path.abspath(__file__))
OUT=os.path.join(HERE,'..','brand'); os.makedirs(OUT,exist_ok=True)
RED='#C8202F'; RED_D='#7C1220'; NAVY='#16243F'; EDGE='#2B5671'; TEAL='#2F7486'; WHITE='#FFFFFF'; CREAM='#F7F3EA'
SERIF='DMSerifDisplay-Regular.ttf'; CAPS='Prata-Regular.ttf'
_f={}
def font(n):
    if n not in _f: _f[n]=TTFont(os.path.join(HERE,'fonts',n))
    return _f[n]
def text_path(s,fn,size,x,y,track=0,sx=1.0):
    f=font(fn); gs=f.getGlyphSet(); cmap=f.getBestCmap(); sc=size/f['head'].unitsPerEm
    pen=SVGPathPen(gs); cx=x
    for ch in s:
        g=cmap.get(ord(ch))
        if g is None: continue
        gs[g].draw(TransformPen(pen,(sc*sx,0,0,-sc,cx,y))); cx+=gs[g].width*sc*sx+track
    return pen.getCommands(), cx-track-x
def tbounds(s,fn,size,track=0,sx=1.0):
    f=font(fn); gs=f.getGlyphSet(); cmap=f.getBestCmap(); sc=size/f['head'].unitsPerEm
    pen=BoundsPen(gs); cx=0
    for ch in s:
        g=cmap.get(ord(ch)); gs[g].draw(TransformPen(pen,(sc*sx,0,0,-sc,cx,0))); cx+=gs[g].width*sc*sx+track
    return pen.bounds
def centered(s,fn,size,cx,y,track=0,sx=1.0):
    b=tbounds(s,fn,size,track,sx); w=b[2]-b[0]
    return text_path(s,fn,size,cx-w/2-b[0],y,track,sx)[0]

def extrude(d,face=RED,side=RED_D,depth=7,hl=True):
    """3D slab letters like the sign: stacked darker copies down-right, then the face."""
    s=''.join(f'<path transform="translate({i*.8:.1f} {i:.1f})" d="{d}"/>' for i in range(depth,0,-1))
    return (f'<g fill="{side}">{s}</g><path fill="{face}" d="{d}"/>'
            +(f'<path fill="none" stroke="#fff" stroke-opacity=".35" stroke-width="1" transform="translate(-.6 -.6)" d="{d}"/>' if hl else ''))

def banner(x0,x1,y,h,word,size,fill=RED,txt=WHITE,cap=WHITE,track=None):
    m=(y+h/2); p=h*.32
    d=f'M{x0+p} {y}H{x1-p}L{x1} {m}L{x1-p} {y+h}H{x0+p}L{x0} {m}Z'
    dm=lambda cx:f'M{cx} {m-h*.17}L{cx+h*.17} {m}L{cx} {m+h*.17}L{cx-h*.17} {m}Z'
    ins=h*.62
    w=x1-x0-2*ins-h*.4
    # fit tracking so the word spans the banner
    if track is None:
        b=tbounds(word,CAPS,size); track=(w-(b[2]-b[0]))/(len(word)-1)
    t=centered(word,CAPS,size,(x0+x1)/2,m+size*.36,track)
    return f'<path fill="{fill}" d="{d}"/><path fill="{cap}" d="{dm(x0+ins*.62)}{dm(x1-ins*.62)}"/><path fill="{txt}" d="{t}"/>'

def sign(mono=None, posts=False, dark=False):
    """Full sign emblem. viewBox 0 0 640 420 (posts extend to 560)."""
    c=lambda k:mono or k
    W,H=640,420; cx=320
    o=[]
    if posts:
        o.append(f'<g fill="{c(EDGE if dark else NAVY)}"><rect x="150" y="300" width="34" height="250" rx="3"/><rect x="456" y="300" width="34" height="250" rx="3"/></g>')
    dia=lambda i:f'M{cx} {8+i}L{W-8-i*1.62:.1f} 206L{cx} {412-i}L{8+i*1.62:.1f} 206Z'
    o.append(f'<path fill="{c(EDGE)}" d="{dia(0)}"/>')
    o.append(f'<path fill="{c(WHITE) if not mono else "none"}" d="{dia(12)}"/>' if not mono else f'<path fill="#fff" d="{dia(12)}"/>')
    o.append(f'<path fill="none" stroke="{c(EDGE)}" stroke-width="2.5" d="{dia(21)}"/>')
    dm=centered('DAVE MAYS',SERIF,128,cx,186,track=2,sx=.80)
    o.append(extrude(dm,face=c(RED),side=c(RED_D) if not mono else c(RED),depth=0 if mono else 7,hl=not mono))
    o.append(banner(0,W,210,52,'AUTOMOTIVE',34,fill=c(RED),txt='#fff',cap='#fff'))
    o.append(f'<path fill="{c(TEAL)}" d="{centered("Since",SERIF,46,cx,318)}{centered("1975",SERIF,40,cx,360,track=1.5)}"/>')
    return ''.join(o)

def mini(mono=None,dark=False):
    """Compact diamond mark for favicons/nav: diamond + red 3D DM monogram over a banner stripe. viewBox 0 0 100 100"""
    c=lambda k:mono or k
    o=([f'<path fill="#fff" d="M50 -1L101 50L50 101L-1 50Z"/>'] if dark else [])+[f'<path fill="{c(EDGE)}" d="M50 3L97 50L50 97L3 50Z"/>',
       f'<path fill="#fff" d="M50 13L87 50L50 87L13 50Z"/>',
       f'<path fill="{c(RED)}" d="M3 61H97L94 67.5L97 74H3L6 67.5Z"/>']
    d=centered('DM',SERIF,36,49,57,track=-1,sx=.82)
    o.append(extrude(d,face=c(RED),side=c(RED_D),depth=0 if mono else 3,hl=False))
    o.append(f'<path fill="#fff" d="M9 67.5L11.5 65L14 67.5L11.5 70ZM86 67.5L88.5 65L91 67.5L88.5 70Z"/>')
    return ''.join(o)

def fav():
    o=[f'<path fill="{EDGE}" d="M50 1L99 50L50 99L1 50Z"/>',f'<path fill="#fff" d="M50 14L86 50L50 86L14 50Z"/>',
       f'<path fill="{RED}" d="M1 56H99L96 63L99 70H1L4 63Z"/>']
    d=centered('DM',SERIF,52,50,53,track=-2,sx=.8)
    o.append(extrude(d,depth=3,hl=False))
    return ''.join(o)

def wordmark(dark=False, mono=None):
    """DAVE MAYS + banner + Since 1975 (no diamond). viewBox width ~ 470, height 150"""
    c=lambda k:mono or k
    dm=centered('DAVE MAYS',SERIF,96,225,82,track=1.5,sx=.80)
    o=[extrude(dm,face=c(RED),side=c(RED_D) if not dark else '#5A0C16',depth=0 if mono else 5,hl=not mono and not dark)]
    o.append(banner(8,442,96,36,'AUTOMOTIVE',24,fill=c(RED),txt='#fff' if not mono or dark else '#fff'))
    since=f'<path fill="{c("#8FC3CF" if dark else TEAL)}" d="{centered("Since 1975",SERIF,24,225,166,track=.5)}"/>'
    o.append(since)
    return ''.join(o)

def svg(vb,body,title='Dave Mays Automotive'):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" role="img" aria-label="{title}"><title>{title}</title>{body}</svg>'

def build():
    files={
     'logo-sign.svg':svg('0 0 640 420',sign()),
     'logo-sign-posts.svg':svg('0 0 640 560',sign(posts=True)),
     'logo-sign-mono-navy.svg':svg('0 0 640 420',sign(mono=NAVY)),
     'logo-emblem.svg':svg('0 0 100 100',mini()),
     'logo-emblem-mono.svg':svg('0 0 100 100',mini(mono=NAVY)),
     'logo-horizontal-light.svg':svg('0 0 628 175',f'<g transform="translate(0 4) scale(1.67)">{mini()}</g><g transform="translate(170 0)">{wordmark()}</g>'),
     'logo-horizontal-dark.svg':svg('0 0 628 175',f'<g transform="translate(0 4) scale(1.67)">{mini(dark=True)}</g><g transform="translate(170 0)">{wordmark(dark=True)}</g>'),
     'logo-stacked-light.svg':svg('0 0 460 300',f'<g transform="translate(180 0) scale(1)">{mini()}</g><g transform="translate(5 112)">{wordmark()}</g>'),
     'logo-stacked-dark.svg':svg('0 0 460 300',f'<g transform="translate(180 0)">{mini(dark=True)}</g><g transform="translate(5 112)">{wordmark(dark=True)}</g>'),
     'logo-wordmark-mono-white.svg':svg('0 0 460 175',wordmark(dark=True,mono='#fff').replace('fill="#fff" d="M','fill="#fff" d="M')),
     'favicon.svg':svg('0 0 100 100',fav()),
    }
    for k,v in files.items(): open(os.path.join(OUT,k),'w').write(v)
    print('wrote',len(files))
if __name__=='__main__': build()
