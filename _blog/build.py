#!/usr/bin/env python3
"""Genera el blog de Cotinusa Studio. Uso: python3 _blog/build.py (desde la raiz de la web)."""
import json, os, re, html, datetime
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE="https://www.cotinusastudio.es"
posts=json.load(open(os.path.join(ROOT,'_blog/posts.json'),encoding='utf-8'))
social=json.load(open(os.path.join(ROOT,'_blog/social.json'),encoding='utf-8'))
posts.sort(key=lambda p:p['date'],reverse=True)
MESES=['enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre']
def fecha(d): y,m,dd=map(int,d.split('-')); return f"{dd} de {MESES[m-1]} de {y}"
e=html.escape
ICON={"WhatsApp":"WA","Upwork":"Up","Fiverr":"Fi","TikTok":"TT","Instagram":"IG","LinkedIn":"in","Facebook":"Fb","YouTube":"YT","Behance":"Bē","X":"X"}
def social_html():
    items=''.join(f'<a href="{e(s["url"])}" target="_blank" rel="noopener me" aria-label="{e(s["name"])}"><span>{ICON.get(s["name"],s["name"][:2])}</span>{e(s["name"])}</a>' for s in social)
    return f'<!--SOCIAL--><div class="coti-social" aria-label="Redes sociales">{items}</div><!--/SOCIAL-->'
def head(title,desc,url,img,typ="website",extra=""):
    return f'''<!doctype html><html lang="es"><head><style>img[width]{{height:auto}}</style><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(title)}</title><meta name="description" content="{e(desc)}"><link rel="canonical" href="{url}"><meta name="robots" content="index,follow,max-image-preview:large">
<meta property="og:type" content="{typ}"><meta property="og:site_name" content="Cotinusa Studio"><meta property="og:locale" content="es_ES"><meta property="og:url" content="{url}"><meta property="og:title" content="{e(title)}"><meta property="og:description" content="{e(desc)}"><meta property="og:image" content="{BASE+img}"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{e(title)}"><meta name="twitter:description" content="{e(desc)}"><meta name="twitter:image" content="{BASE+img}"><link rel="manifest" href="/site.webmanifest">
<link rel="icon" href="/favicon.ico" sizes="any"><link rel="apple-touch-icon" href="/apple-touch-icon.png"><meta name="theme-color" content="#080a10">
<link rel="alternate" type="application/rss+xml" title="Blog Cotinusa Studio" href="/feed.xml">
<link rel="stylesheet" href="/studio-2.css"><link rel="stylesheet" href="/blog.css">{extra}</head><body>'''
NAV='''<header class="nav"><div class="container nav-inner"><a class="brand" href="/"><img src="/assets/cotinusa-logo-supreme.webp" alt="Logo COTINUSA"> COTINUSA <span class="gold">STUDIO</span></a><nav class="links" aria-label="Navegación principal"><a href="/#servicios">Servicios</a><a href="/#proyectos">Proyectos</a><a href="/blog">Blog</a><a href="/#contacto">Contacto</a><a href="/lanzamiento" class="gold" style="font-weight:700">Pack 490 €</a></nav></div></header>'''
def footer():
    return f'''<footer class="footer"><div class="container"><span>© {datetime.date.today().year} COTINUSA STUDIO · Ideas que visten marcas · Cádiz</span>{social_html()}<span><a href="/blog">Blog</a> · <a href="/privacidad">Aviso legal y privacidad</a></span></div></footer><a class="wa-float" href="https://wa.me/34640998402?text=Hola%2C%20vengo%20del%20blog%20de%20Cotinusa%20Studio" target="_blank" rel="noopener">WhatsApp</a></body></html>'''
def body_html(blocks):
    out=[]
    for b in blocks:
        t=b[0]
        if t in('p','h2','h3'): out.append(f'<{t}>{b[1]}</{t}>')
        elif t in('ul','ol'): out.append(f'<{t}>'+''.join(f'<li>{i}</li>' for i in b[1])+f'</{t}>')
    return ''.join(out)
os.makedirs(os.path.join(ROOT,'blog'),exist_ok=True)
for i,p in enumerate(posts):
    url=f"{BASE}/blog/{p['slug']}"
    ld={"@context":"https://schema.org","@type":"BlogPosting","headline":p['title'],"description":p['description'],"image":BASE+p['image'],"datePublished":p['date'],"dateModified":p.get('updated',p['date']),"inLanguage":"es-ES","mainEntityOfPage":url,
        "author":{"@type":"Person","name":"Javier Rugero Gómez","url":BASE+"/#metodo"},"publisher":{"@type":"Organization","name":"Cotinusa Studio","logo":{"@type":"ImageObject","url":BASE+"/assets/cotinusa-logo-supreme.webp"}}}
    bc={"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Inicio","item":BASE+"/"},{"@type":"ListItem","position":2,"name":"Blog","item":BASE+"/blog"},{"@type":"ListItem","position":3,"name":p['title'],"item":url}]}
    extra=f'<meta property="article:published_time" content="{p["date"]}"><script type="application/ld+json">{json.dumps(ld,ensure_ascii=False)}</script><script type="application/ld+json">{json.dumps(bc,ensure_ascii=False)}</script>'
    rel=[q for q in posts if q is not p][:2]
    relh=''.join(f'<a class="post-card" href="/blog/{q["slug"]}"><img loading="lazy" src="{q["image"]}" alt="{e(q["image_alt"])}"><div><span class="pill">{e(q["category"])}</span><h3>{e(q["title"])}</h3></div></a>' for q in rel)
    page=head(p['title']+" | Cotinusa Studio",p['description'],url,p['image'],"article",extra)+NAV+f'''<main class="post container"><nav class="crumbs" aria-label="Migas de pan"><a href="/">Inicio</a> / <a href="/blog">Blog</a> / <span>{e(p["category"])}</span></nav>
<article><header><div class="eyebrow">{e(p["category"])} · <time datetime="{p["date"]}">{fecha(p["date"])}</time> · Por Javier Rugero Gómez</div><h1>{e(p["title"])}</h1><p class="lead">{e(p["description"])}</p></header>
<img class="post-hero" width="1600" height="900" src="{p["image"]}" alt="{e(p["image_alt"])}"><div class="post-body">{body_html(p["body"])}</div>
<aside class="post-cta"><strong>¿Necesitas logo y web para tu negocio?</strong><span>Pack Lanzamiento: logo + web con WhatsApp en 7 días por 490 €.</span><a class="btn btn-primary" href="/lanzamiento">Ver el pack →</a></aside></article>
<section class="related"><h2>Sigue leyendo</h2><div class="post-grid">{relh}</div></section></main>'''+footer()
    open(os.path.join(ROOT,'blog',p['slug']+'.html'),'w',encoding='utf-8').write(page)
cards=''.join(f'<a class="post-card" href="/blog/{p["slug"]}"><img loading="lazy" src="{p["image"]}" alt="{e(p["image_alt"])}"><div><span class="pill">{e(p["category"])} · {fecha(p["date"])}</span><h2>{e(p["title"])}</h2><p>{e(p["description"])}</p></div></a>' for p in posts)
idx=head("Blog de branding, diseño web y SEO | Cotinusa Studio","Consejos prácticos de branding, diseño web, SEO local e inteligencia artificial para negocios. El blog de Cotinusa Studio, estudio creativo en Cádiz.",BASE+"/blog","/assets/og-image.jpg")+NAV+f'''<main class="container blog-index"><div class="eyebrow">COTINUSA / NOTICIAS Y BLOG</div><h1>Ideas para que tu negocio <span class="gold">se vea y venda.</span></h1><p class="lead">Branding, diseño web, SEO local e IA explicados sin tecnicismos.</p><div class="post-grid">{cards}</div></main>'''+footer()
open(os.path.join(ROOT,'blog.html'),'w',encoding='utf-8').write(idx)
# RSS
def rfc(d): return datetime.datetime.strptime(d,'%Y-%m-%d').strftime('%a, %d %b %Y 09:00:00 +0100')
items=''.join(f'<item><title>{e(p["title"])}</title><link>{BASE}/blog/{p["slug"]}</link><guid>{BASE}/blog/{p["slug"]}</guid><pubDate>{rfc(p["date"])}</pubDate><description>{e(p["description"])}</description></item>' for p in posts)
open(os.path.join(ROOT,'feed.xml'),'w',encoding='utf-8').write(f'<?xml version="1.0" encoding="UTF-8"?><rss version="2.0"><channel><title>Blog Cotinusa Studio</title><link>{BASE}/blog</link><description>Branding, diseño web, SEO e IA para negocios</description><language>es-es</language>{items}</channel></rss>\n')
# sitemap
static=[("/","1.0","weekly",None),("/lanzamiento","0.9","weekly",None),("/blog","0.8","weekly",posts[0]['date']),("/origins","0.6","monthly",None),("/cosmic","0.5","monthly",None),("/idea-builder","0.6","monthly",None)]
today=datetime.date.today().isoformat()
urls=[(u,pr,c,lm or today) for u,pr,c,lm in static]+[(f"/blog/{p['slug']}","0.7","monthly",p.get('updated',p['date'])) for p in posts]
open(os.path.join(ROOT,'sitemap.xml'),'w',encoding='utf-8').write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+''.join(f'  <url><loc>{BASE}{u}</loc><lastmod>{lm}</lastmod><changefreq>{c}</changefreq><priority>{pr}</priority></url>\n' for u,pr,c,lm in urls)+'</urlset>\n')
# inyectar redes + enlace Blog en index y lanzamiento
for f in ('index.html','lanzamiento.html'):
    fp=os.path.join(ROOT,f); s=open(fp,encoding='utf-8').read()
    s=re.sub(r'<!--SOCIAL-->.*?<!--/SOCIAL-->','',s,flags=re.S)
    if '<link rel="stylesheet" href="/blog.css">' not in s: s=s.replace('</head>','<link rel="stylesheet" href="/blog.css"></head>',1)
    s=s.replace('</div></footer>',social_html()+'</div></footer>',1) if '</div></footer>' in s else s.replace('</footer>',social_html()+'</footer>',1)
    if f=='index.html' and 'href="/blog"' not in s: s=s.replace('<a href="#preguntas">FAQ</a>','<a href="/blog">Blog</a><a href="#preguntas">FAQ</a>',1)
    if 'alternate" type="application/rss' not in s: s=s.replace('</head>','<link rel="alternate" type="application/rss+xml" title="Blog Cotinusa Studio" href="/feed.xml"></head>',1)
    open(fp,'w',encoding='utf-8').write(s)
# ultimas entradas en la portada
fp=os.path.join(ROOT,'index.html'); s=open(fp,encoding='utf-8').read()
s=re.sub(r'<!--BLOG-->.*?<!--/BLOG-->','',s,flags=re.S)
latest=''.join(f'<a class="post-card" href="/blog/{p["slug"]}"><img loading="lazy" src="{p["image"]}" alt="{e(p["image_alt"])}"><div><span class="pill">{e(p["category"])} · {fecha(p["date"])}</span><h3>{e(p["title"])}</h3></div></a>' for p in posts[:3])
sec=f'<!--BLOG--><section id="blog-home"><div class="container"><div class="intro"><div class="eyebrow">NOTICIAS / BLOG</div><h2>Últimas ideas del <span class="gold">estudio.</span></h2></div><div class="post-grid">{latest}</div><div class="actions"><a class="btn btn-secondary" href="/blog">Ver todo el blog ↗</a></div></div></section><!--/BLOG-->'
s=s.replace('<section id="preguntas"',sec+'<section id="preguntas"',1)
open(fp,'w',encoding='utf-8').write(s)
print(f"Blog generado: {len(posts)} articulos")
