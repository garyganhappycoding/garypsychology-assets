# Usage: python3 tools/contact.py carousels/NN-name  -> contact.png (all slides on one sheet, for quick review)
import sys,glob,os
from PIL import Image
d=sys.argv[1];fs=sorted(glob.glob(os.path.join(d,'slide-*.png')));cols=5 if len(fs)>8 else 4
w,h=432,540;rows=(len(fs)+cols-1)//cols;m=Image.new('RGB',(cols*w,rows*h),'white')
for k,f in enumerate(fs): m.paste(Image.open(f).resize((w,h)),((k%cols)*w,(k//cols)*h))
m.save(os.path.join(d,'contact.png'));print(os.path.join(d,'contact.png'))
