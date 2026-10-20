"""src/original.html(정리기 원본) + oremas-addon.html → index.html
원본이 바뀌면 src/original.html 만 바꾸고 python build.py 를 다시 돌린다."""
import pathlib,sys
root=pathlib.Path(__file__).parent
base=(root/'src'/'original.html').read_text(encoding='utf-8')
addon=(root/'oremas-addon.html').read_text(encoding='utf-8')
i=base.lower().rfind('</body>')
out=base[:i]+'\n'+addon+'\n'+base[i:] if i>=0 else base+'\n'+addon
(root/'index.html').write_text(out,encoding='utf-8')
print('index.html',len(out),'bytes')
