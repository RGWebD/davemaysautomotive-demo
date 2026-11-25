(()=>{
const RM=matchMedia('(prefers-reduced-motion: reduce)').matches,$=(s,c=document)=>c.querySelector(s),$$=(s,c=document)=>[...c.querySelectorAll(s)];
const FINE=matchMedia('(pointer:fine)').matches;
/* loader: the roadside sign goes up (home only, once per session) */
const ld=$('.loader');
if(ld){if(RM||sessionStorage.getItem('dm-ld')){ld.classList.add('done')}else{sessionStorage.setItem('dm-ld','1');requestAnimationFrame(()=>setTimeout(()=>ld.classList.add('run'),100));setTimeout(()=>ld.classList.add('done'),2200)}}
const ldOn=ld&&!ld.classList.contains('done');
/* reveals */
const io=new IntersectionObserver(es=>es.forEach(en=>{if(en.isIntersecting){en.target.classList.add('in');io.unobserve(en.target)}}),{threshold:.12,rootMargin:'0px 0px -6% 0px'});
$$('.rv,.split,.cta-sign').forEach(el=>RM?el.classList.add('in'):io.observe(el));
const sio=new IntersectionObserver(es=>es.forEach(en=>{if(en.isIntersecting){$$('.st',en.target).forEach(c=>c.classList.add('in'));sio.unobserve(en.target)}}),{threshold:.15});$$('.st-grid').forEach(g=>sio.observe(g));
const hh=$('.hero .split,.phero .split');if(hh&&!RM){io.unobserve(hh);setTimeout(()=>hh.classList.add('in'),ldOn?2000:120)}
/* counters, gauges, odometers */
function count(el){const to=parseFloat(el.dataset.to),dec=+el.dataset.dec||0;if(RM){el.textContent=to.toFixed(dec);return}
 const t0=performance.now(),d=1900;const step=t=>{const k=Math.min(1,(t-t0)/d),v=to*(1-Math.pow(1-k,3));el.textContent=v.toFixed(dec);if(k<1)requestAnimationFrame(step);else el.textContent=to.toFixed(dec)};requestAnimationFrame(step)}
const cio=new IntersectionObserver(es=>es.forEach(en=>{if(en.isIntersecting){const t=en.target;if(t.dataset.to)count(t);else t.classList.add('on');cio.unobserve(t)}}),{threshold:.35});
$$('[data-to],.gauge,.odo').forEach(el=>RM?(el.dataset.to?count(el):el.classList.add('on')):cio.observe(el));
/* dashboard warning lights */
const lights=$$('.lt');
lights.forEach(b=>b.addEventListener('click',()=>{lights.forEach(x=>x.setAttribute('aria-pressed',x===b));$$('.rd').forEach(r=>r.hidden=r.dataset.k!==b.dataset.k)}));
/* scroll: nav, progress, mobile bar, timeline */
const nav=$('.nav'),bar=$('.pbar'),mbar=$('.mbar'),steps=$('.steps');let tmax=0;
function onScroll(){const y=scrollY,h=document.documentElement.scrollHeight-innerHeight;
 nav&&nav.classList.toggle('scrolled',y>30);bar&&bar.style.setProperty('--p',h>0?(y/h).toFixed(4):0);
 mbar&&mbar.classList.toggle('show',y>innerHeight*.6);
 if(steps){const r=steps.getBoundingClientRect(),p=Math.min(1,Math.max(0,(innerHeight*.75-r.top)/r.height));tmax=Math.max(tmax,p);steps.style.setProperty('--tp',RM?1:tmax.toFixed(3))}}
addEventListener('scroll',onScroll,{passive:true});addEventListener('resize',onScroll);onScroll();
/* mobile menu */
const mb=$('.menu-btn'),mm=$('.mmenu');
if(mb&&mm){const set=o=>{mb.setAttribute('aria-expanded',o);mb.setAttribute('aria-label',o?'Close menu':'Open menu');mm.classList.toggle('open',o);mm.setAttribute('aria-hidden',!o);document.body.style.overflow=o?'hidden':'';if(o)setTimeout(()=>$('a',mm).focus(),300)};
 mb.addEventListener('click',()=>set(mb.getAttribute('aria-expanded')!=='true'));addEventListener('keydown',e=>{if(e.key==='Escape'&&mm.classList.contains('open')){set(false);mb.focus()}});$$('a',mm).forEach(a=>a.addEventListener('click',()=>set(false)))}
/* live open/closed badge, America/New_York. Mon-Thu 7:30-5:30, Fri 7:30-5:00 (door decal), Sat/Sun closed */
const HRS={0:null,1:[450,1050],2:[450,1050],3:[450,1050],4:[450,1050],5:[450,1020],6:null};
const HOL={'2026-11-26':'Thanksgiving','2026-11-27':'Black Friday','2026-12-24':'Christmas Eve','2026-12-25':'Christmas Day','2026-12-31':'New Year\u2019s Eve','2027-01-01':'New Year\u2019s Day'};
const DN=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'];
const fm=m=>{const h=Math.floor(m/60),mi=m%60;return (h%12||12)+(mi?':'+String(mi).padStart(2,'0'):'')+(h<12?' AM':' PM')};
function next(wd){for(let k=1;k<8;k++){const d=(wd+k)%7;if(HRS[d])return [k===1?'tomorrow':DN[d],HRS[d][0]]}}
function live(){const p=Object.fromEntries(new Intl.DateTimeFormat('en-US',{timeZone:'America/New_York',weekday:'short',hour:'numeric',minute:'numeric',hour12:false,year:'numeric',month:'2-digit',day:'2-digit'}).formatToParts(new Date()).map(x=>[x.type,x.value]));
 const wd=['Sun','Mon','Tue','Wed','Thu','Fri','Sat'].indexOf(p.weekday),m=(+p.hour%24)*60+(+p.minute),h=HRS[wd],key=`${p.year}-${p.month}-${p.day}`,hol=HOL[key];
 let txt,st;
 if(hol){txt=`${hol} \u00b7 holiday hours may vary, call ahead`;st='unk'}
 else if(h&&m>=h[0]&&m<h[1]){txt=`Open now \u00b7 until ${fm(h[1])}`;st='open'}
 else if(h&&m<h[0]){txt=`Closed \u00b7 opens ${fm(h[0])}`;st='closed'}
 else{const [d,o]=next(wd);txt=`Closed \u00b7 opens ${d} ${fm(o)}`;st='closed'}
 $$('[data-live]').forEach(b=>{b.querySelector('span').textContent=txt;b.classList.toggle('closed',st==='closed');b.classList.toggle('unk',st==='unk')});
 $$('.hrs tr').forEach(tr=>tr.classList.toggle('today',+tr.dataset.day===wd));
 const hn=$('[data-hol]');if(hn){hn.hidden=!hol;if(hol)hn.textContent=`${hol}: Google notes hours might differ today. Please call to confirm.`}}
live();setInterval(live,60000);
/* magnetic buttons (fine pointers only; no cursor follower) */
if(FINE&&!RM)$$('.mag').forEach(b=>{b.addEventListener('pointermove',e=>{const r=b.getBoundingClientRect();b.style.transform=`translate(${(e.clientX-r.left-r.width/2)*.14}px,${(e.clientY-r.top-r.height/2)*.24}px)`});b.addEventListener('pointerleave',()=>b.style.transform='')});
/* tilt cards */
if(FINE&&!RM)$$('.tilt').forEach(c=>{c.addEventListener('pointermove',e=>{const r=c.getBoundingClientRect(),x=(e.clientX-r.left)/r.width-.5,y=(e.clientY-r.top)/r.height-.5;c.style.setProperty('--ry',(x*8)+'deg');c.style.setProperty('--rx',(-y*8)+'deg')});c.addEventListener('pointerleave',()=>{c.style.setProperty('--ry','0deg');c.style.setProperty('--rx','0deg')})});
/* hero parallax */
const art=$('.h-frame'),seal=$('.seal'),big=$('.bigout');
if(art&&!RM){addEventListener('scroll',()=>{const y=scrollY;if(y<innerHeight*1.2){art.style.translate=`0 ${y*.05}px`;seal&&(seal.style.translate=`0 ${-y*.12}px`);big&&(big.style.translate=`${-y*.15}px 0`)}},{passive:true})}
/* hotspot pins */
$$('.pin').forEach(p=>p.addEventListener('click',e=>{e.stopPropagation();const o=p.getAttribute('aria-expanded')==='true';$$('.pin').forEach(q=>q.setAttribute('aria-expanded','false'));p.setAttribute('aria-expanded',!o)}));
document.addEventListener('click',()=>$$('.pin').forEach(q=>q.setAttribute('aria-expanded','false')));
/* reviews carousel (pauses on hover/focus) */
$$('[data-car]').forEach(car=>{const sl=$$('.slide',car),dots=$('.car-dots',car);let i=0,paused=false;
 sl.forEach((s,k)=>{const b=document.createElement('button');b.setAttribute('aria-label','Show review '+(k+1));b.addEventListener('click',()=>go(k));dots.appendChild(b)});
 function go(k){i=(k+sl.length)%sl.length;sl.forEach((s,n)=>{s.classList.toggle('on',n===i);s.setAttribute('aria-hidden',n!==i);$$('a',s).forEach(a=>a.tabIndex=n===i?0:-1)});$$('button',dots).forEach((d,n)=>d.setAttribute('aria-current',n===i))}
 $('.prev',car).addEventListener('click',()=>go(i-1));$('.next',car).addEventListener('click',()=>go(i+1));
 car.addEventListener('mouseenter',()=>paused=true);car.addEventListener('mouseleave',()=>paused=false);car.addEventListener('focusin',()=>paused=true);car.addEventListener('focusout',()=>paused=false);
 let sx=null;car.addEventListener('touchstart',e=>sx=e.touches[0].clientX,{passive:true});car.addEventListener('touchend',e=>{if(sx===null)return;const dx=e.changedTouches[0].clientX-sx;if(Math.abs(dx)>40)go(i+(dx<0?1:-1));sx=null});
 go(0);if(!RM)setInterval(()=>{if(!paused&&!document.hidden)go(i+1)},7000)});
/* gallery filter */
$$('.fbtn').forEach(b=>b.addEventListener('click',()=>{const f=b.dataset.f;$$('.fbtn').forEach(x=>x.setAttribute('aria-pressed',x===b));$$('.gi').forEach(g=>{g.classList.toggle('off',f!=='all'&&g.dataset.tag!==f);g.classList.add('in')})}));
/* lightbox: keyboard, swipe, focus trap */
const lb=$('.lbx');
if(lb){const im=$('img',lb),cap=$('figcaption',lb);let list=[],i=0,last=null;
 const vis=()=>$$('.gi:not(.off) .gi-b');
 function show(k){list=vis();i=(k+list.length)%list.length;const b=list[i];im.src=b.dataset.full;im.alt=b.dataset.cap;cap.textContent=b.dataset.cap}
 function open(b){last=b;lb.hidden=false;document.body.style.overflow='hidden';show(vis().indexOf(b));$('.lbx-x',lb).focus()}
 function close(){lb.hidden=true;document.body.style.overflow='';last&&last.focus()}
 $$('.gi-b').forEach(b=>b.addEventListener('click',()=>open(b)));
 $('.lbx-x',lb).addEventListener('click',close);$('.lbx-p',lb).addEventListener('click',()=>show(i-1));$('.lbx-n',lb).addEventListener('click',()=>show(i+1));
 lb.addEventListener('click',e=>{if(e.target===lb)close()});
 addEventListener('keydown',e=>{if(lb.hidden)return;if(e.key==='Escape')close();if(e.key==='ArrowRight')show(i+1);if(e.key==='ArrowLeft')show(i-1);
  if(e.key==='Tab'){const f=$$('button',lb);const a=f[0],z=f[f.length-1];if(e.shiftKey&&document.activeElement===a){e.preventDefault();z.focus()}else if(!e.shiftKey&&document.activeElement===z){e.preventDefault();a.focus()}}});
 let sx=null;lb.addEventListener('touchstart',e=>sx=e.touches[0].clientX,{passive:true});lb.addEventListener('touchend',e=>{if(sx===null)return;const dx=e.changedTouches[0].clientX-sx;if(Math.abs(dx)>40)show(i+(dx<0?1:-1));sx=null})}
/* appointment form -> prefilled text message */
$$('form[data-sms]').forEach(f=>f.addEventListener('submit',e=>{e.preventDefault();const d=new FormData(f);
 if(!d.get('name')||!d.get('phone')){f.reportValidity();$$('[required]',f).forEach(x=>{if(!x.value)x.focus()});return}
 const body=`Hi Dave Mays Automotive, I'd like to set up an appointment.\nName: ${d.get('name')}\nPhone: ${d.get('phone')}\nVehicle: ${d.get('car')||'-'}\nPreferred day: ${d.get('date')||'-'}\nService: ${d.get('svc')}\n${d.get('msg')||''}`;
 location.href=`sms:${f.dataset.sms}?&body=${encodeURIComponent(body)}`}));
/* demo pill */
const dm=$('.demo');if(dm){if(sessionStorage.getItem('dm-demo'))dm.classList.add('hide');$('button',dm).addEventListener('click',()=>{dm.classList.add('hide');sessionStorage.setItem('dm-demo','1')})}
})();
