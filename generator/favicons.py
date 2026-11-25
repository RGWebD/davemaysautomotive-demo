import asyncio, os, shutil
from playwright.async_api import async_playwright
from PIL import Image
B=os.path.abspath(os.path.join(os.path.dirname(__file__),'..','brand')); R=os.path.abspath(os.path.join(B,'..'))
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/usr/bin/google-chrome')
        pg=await b.new_page(viewport={'width':512,'height':512})
        open(f'{B}/_fav.html','w').write('<body style="margin:0;background:transparent"><img src="favicon.svg" style="width:512px;height:512px;display:block"></body>')
        await pg.goto(f'file://{B}/_fav.html'); await pg.wait_for_timeout(300)
        await pg.screenshot(path=f'{B}/favicon-512.png',omit_background=True)
        pg2=await b.new_page(viewport={'width':1200,'height':630})
        html=f'''<link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=Libre+Franklin:wght@700&family=Prata&display=swap" rel="stylesheet"><body style="margin:0;width:1200px;height:630px;background:#13213A;position:relative;overflow:hidden">
        <img src="file://{R}/img/g16.webp" style="position:absolute;right:0;top:0;width:720px;height:630px;object-fit:cover;object-position:62% 50%">
        <div style="position:absolute;left:0;top:0;width:640px;height:630px;background:linear-gradient(90deg,#13213A 70%,rgba(19,33,58,0))"></div>
        <img src="file://{B}/logo-sign.svg" style="position:absolute;left:60px;top:46px;width:330px">
        <div style="position:absolute;left:62px;top:290px;color:#fff;font:400 64px/1 'DM Serif Display';width:560px">Honest repairs,<br><i style="color:#FF6B76">since 1975.</i></div>
        <div style="position:absolute;left:0;right:0;bottom:0;background:#C8202F;color:#fff;border-top:4px solid #8E1424;font:400 24px 'Prata';letter-spacing:2px;padding:18px 62px">★ 4.6 · 163 Google reviews · Gainesville, FL · (352) 372-7617</div></body>'''
        open(f'{B}/_og.html','w').write(html)
        await pg2.goto(f'file://{B}/_og.html'); await pg2.wait_for_timeout(2500)
        await pg2.screenshot(path=f'{R}/img/og.jpg',type='jpeg',quality=86)
        await b.close()
asyncio.run(main())
im=Image.open(f'{B}/favicon-512.png').convert('RGBA')
for s in (16,32,180): im.resize((s,s),Image.LANCZOS).save(f'{B}/favicon-{s}.png')
im.resize((180,180),Image.LANCZOS).save(f'{R}/apple-touch-icon.png')
im.save(f'{R}/favicon.ico',sizes=[(16,16),(32,32),(48,48)])
shutil.copy(f'{B}/favicon.svg',f'{R}/favicon.svg')
os.remove(f'{B}/_og.html'); os.remove(f'{B}/_fav.html'); print('ok')
