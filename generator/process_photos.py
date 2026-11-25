from PIL import Image, ImageFilter, ImageOps
import imagehash, os, itertools
SRC='/workspace/davemays-research/photos/'
OUT=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','img'); os.makedirs(OUT,exist_ok=True)
# placement plan: see README / report. Dropped: g05 (near-dup of g15), g06 g12 (customer cars, no context), g11 (business across the street),
# g13 (500px, stock-looking), g14 (empty bay view), f02 f04 f05 (repeat exteriors / lot), f06 (customers at counter), f09 (dim pit)
KEEP=['g16','g01','g17','g02','g03','g15','g09','g08','g07','g10','f01','f03','f07','f08','f10','f11','sign']
CLONE={}
BLUR={'g01':[(1820,535,1915,612)]}   # dumpster hauler's label
CROP={'g07':(0,60,2000,1200),'g10':(110,180,910,1480),'g02':(0,250,1500,1800)}
hs={}
for k in KEEP:
    im=ImageOps.exif_transpose(Image.open(SRC+k+('.png' if k=='sign' else '.jpg'))).convert('RGB')
    for b,src in CLONE.get(k,[]):
        w,h=b[2]-b[0],b[3]-b[1]; patch=im.crop((src[0],src[1],src[0]+w,src[1]+h))
        m=Image.new('L',(w,h),0); m.paste(255,(8,0,w-8,h-8)); m=m.filter(ImageFilter.GaussianBlur(6))
        im.paste(patch,b[:2],m)
    for b in BLUR.get(k,[]):
        pad=10; bb=(max(0,b[0]-pad),max(0,b[1]-pad),min(im.width,b[2]+pad),min(im.height,b[3]+pad))
        reg=im.crop(bb)
        for _ in range(3): reg=reg.filter(ImageFilter.GaussianBlur(12))
        m=Image.new('L',reg.size,0); m.paste(255,(pad,pad,reg.width-pad,reg.height-pad)); m=m.filter(ImageFilter.GaussianBlur(5))
        im.paste(reg,bb[:2],m)
    if k in CROP: im=im.crop(CROP[k])
    hs[k]=imagehash.phash(im)
    big=im.copy(); big.thumbnail((1600,1600)); big.save(f'{OUT}/{k}.webp','WEBP',quality=82,method=6)
    sm=im.copy(); sm.thumbnail((720,720)); sm.save(f'{OUT}/{k}-s.webp','WEBP',quality=78,method=6)
    print(k, im.size)
for a,b in itertools.combinations(hs,2):
    if hs[a]-hs[b]<14: print('close',a,b,hs[a]-hs[b])
og=Image.open(SRC+'g16.jpg').convert('RGB'); w,h=og.size
og=og.crop((0,int(h*.02),w,int(h*.02)+int(w*630/1200))).resize((1200,630)); og.save(f'{OUT}/og-base.jpg',quality=85)
print('done')
