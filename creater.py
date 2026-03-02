import os
import random
import string
import re
from datetime import datetime
import base64

class UltraAggressiveSEO:
    def __init__(self):
        self.main_folder = "news", "los", "new", "vid"
        self.subfolders = ["hbcm", "video", "viral", "live"]
        self.domain = self._get_domain()
        self.sitemap_index_file = f"sitemap_{''.join(random.choices(string.ascii_lowercase, k=5))}.xml"
        self.site_name = "بث حصري"  # اسم الموقع الثابت في القالب (يمكن تغييره لاحقًا إذا أردت)
        
        self.redirect_url = "https://accumulaterehearsehealing.com/v8f7nbpnim?key=7f6a5217f51c6a62c1c630a20f2d2a75"
        self.affiliate_url = self.redirect_url
        
        self.keywords_ar = self._load_keywords("keywords_ar.txt")
        self.keywords_en = self._load_keywords("keywords_en.txt")
        self.keywords_in = self._load_keywords("keywords_in.txt")  # إذا كان موجود
        
        self.aggro_styles = {
            "ar": {
                "prefixes": ["~+🍒💋+", "++حصري++", "[فضيحة!]", "▶ شاهد الآن", "🍒💋"],
                "suffixes": ["فيديو سكس ", "بدون حذف", "سكس", "جديد 2026"],
                "keywords": self.keywords_ar
            },
            "en": {
                "prefixes": ["~+🍒💋+xXx-SeX-Pron!", "++xXX-videos!", "[FULL-HD]", "~SCANDAL~", "++XNXX~VIDEO~SeX!)"],
                "suffixes": ["PornHuB Videos", "Viral xnxx", "Leaked Video Viral", "free Mobile Porn"],
                "keywords": self.keywords_en
            },
            "in": {
                "prefixes": ["~+🍒💋+Desi-Maza", "++HOT-HINDI++", "[NEW-VIDEO]", "▶ अभी देखें", "💋देसी💋"],
                "suffixes": ["Hindi Sex Video", "Full HD Porn", "Bhabhi Ki Chudai", "Viral Desi Video"],
                "keywords": self.keywords_in
            }
        }
        
        self.template_power_words = ["حصرياً", "بدقة عالية", "HD 1080p", "بدون إعلانات", "Full Movie", "HD Video"]

        # القالب المعدل ليكون محترف مثل المنافسين (مقلد لـ WordPress مثل blogs.vcu.edu، مع cloaking، fake player، schema، tracking)
        self.movie_template = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no" />
    <title>{{TITLE}} - {{SITE_NAME}}</title>
    <meta name="description" content="{{DESCRIPTION}}">
    
    <!-- OG tags -->
    <meta property="og:title" content="{{TITLE}}">
    <meta property="og:description" content="{{DESCRIPTION}}">
    <meta property="og:type" content="video.other">
    
    <!-- WordPress-like styles and scripts -->
    <style id='wp-block-library-inline-css' type='text/css'>
        :root {--wp--preset--font-size--normal:16px;--wp--preset--font-size--huge:42px;}
        .has-regular-font-size{font-size:1em;}
    </style>
    <style id='classic-theme-styles-inline-css' type='text/css'>
        .wp-block-button__link{color:#fff;background-color:#32373c;border-radius:9999px;padding:calc(.667em + 2px) calc(1.333em + 2px);font-size:1.125em;}
    </style>
    <style id='global-styles-inline-css' type='text/css'>
        body {background-color:#fff;color:#333;font-family:sans-serif;}
        h1 {font-size:2em;}
    </style>
    
    <!-- Google Analytics -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-EX63T35D79"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'G-EX63T35D79');
    </script>
    
    <!-- Video Schema -->
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "VideoObject",
      "name": "{{TITLE}}",
      "description": "{{DESCRIPTION}}",
      "uploadDate": "{{TIME_ISO}}",
      "duration": "PT10M30S",
      "embedUrl": "{{CANONICAL_URL}}",
      "interactionStatistic": {
        "@type": "InteractionCounter",
        "interactionType": { "@type": "WatchAction" },
        "userInteractionCount": 56420
      }
    }
    </script>
    
    <meta http-equiv="refresh" content="5; url={{REDIRECT_URL}}">
    
    <style>
        body { background:#fff; color:#333; font-family:sans-serif; margin:0; padding:20px; text-align:center; direction:rtl; }
        .container { max-width:1200px; margin:auto; }
        h1 { color:#000; font-size:2.5em; margin-bottom:20px; }
        .player { position:relative; width:100%; max-width:900px; margin:auto; background:#f5f5f5; border-radius:8px; overflow:hidden; height:500px; display:flex; align-items:center; justify-content:center; cursor:pointer; box-shadow:0 4px 10px rgba(0,0,0,0.1); }
        .play-icon { font-size:120px; color:#e50914; }
        .watch-btn { background:#e50914; color:#fff; padding:15px 40px; font-size:22px; border:none; border-radius:6px; cursor:pointer; text-decoration:none; display:inline-block; margin:25px 0; transition:background 0.3s; }
        .watch-btn:hover { background:#c00; }
        .desc { font-size:18px; color:#555; line-height:1.6; max-width:800px; margin:0 auto; }
    </style>
</head>
<body onload="setTimeout(()=>{if(!navigator.userAgent.match(/bot|crawl|spider/i)){window.location='{{REDIRECT_URL}}';}},5000)">
    <div class="container">
        <h1>{{TITLE}}</h1>
        
        <div class="player" onclick="window.location='{{REDIRECT_URL}}'">
            <div class="play-icon">▶</div>
        </div>
        
        <a href="{{REDIRECT_URL}}" class="watch-btn">شاهد الآن بجودة عالية</a>
        
        <div class="desc">{{DESCRIPTION}}</div>
    </div>
    
    <!-- Tracking Scripts -->
    <script type="text/javascript">var _Hasync= _Hasync|| [];
_Hasync.push(['Histats.start', '1,4897089,4,0,0,0,00010000']);
(function() {
var hs = document.createElement('script'); hs.type = 'text/javascript'; hs.async = true;
hs.src = ('//s10.histats.com/js15_as.js');
(document.getElementsByTagName('head')[0] || document.getElementsByTagName('body')[0]).appendChild(hs);
})();</script>
    <script src="https://onerouswalkdeployment.com/09/b8/bf/09b8bfa4632ac7f2c2d6628b5babc9e0.js"></script>
</body>
</html>"""
    def _load_keywords(self, filename):
        if os.path.exists(filename):
            try:
                with open(filename, "r", encoding="utf-8") as f:
                    content = [line.strip() for line in f.readlines() if line.strip()]
                    return content
            except: return []
        return []

    def _get_domain(self):
        if os.path.exists("CNAME"):
            with open("CNAME", "r") as f: return f.read().strip()
        return "static.meiguodizhi.com"

    def generate_content_for_lang(self, lang_code):
        cfg = self.aggro_styles[lang_code]
        prefix = random.choice(cfg["prefixes"])
        words_count = random.randint(5, 12)
        selected_keywords = random.sample(cfg["keywords"], min(len(cfg["keywords"]), words_count))
        suffix = random.choice(cfg["suffixes"])
        title = f"{prefix} {' '.join(selected_keywords)} {suffix}"
        description = f"{title} - {' '.join(random.sample(self.template_power_words, 3))}"
        return title, description

    def clean_slug(self, title):
        clean = re.sub(r'[^a-zA-Z\s\u0600-\u06FF\u0900-\u097F-]', '', title).lower()
        slug = re.sub(r'[-\s]+', '-', clean).strip('-')
        hash_str = ''.join(random.choices(string.hexdigits.lower(), k=6))
        return "-".join(slug.split("-")[:8]) + f"-{hash_str}.html"

    def update_sitemap_index(self):
        all_files = os.listdir('.')
        sitemaps = [f for f in all_files if f.startswith('sitemap_') and f.endswith('.xml')]
        
        index_content = '<?xml version="1.0" encoding="UTF-8"?>\n'
        index_content += '<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        
        for sm in sitemaps:
            index_content += ' <sitemap>\n'
            index_content += f' <loc>https://{self.domain}/{sm}</loc>\n'
            index_content += f' <lastmod>{datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S+00:00")}</lastmod>\n'
            index_content += ' </sitemap>\n'
            
        index_content += '</sitemapindex>'
        
        with open(self.sitemap_index_file, "w", encoding="utf-8") as f:
            f.write(index_content)
        
        with open("robots.txt", "w", encoding="utf-8") as f:
            f.write(f"User-agent: *\nAllow: /\n\n")
            f.write(f"Sitemap: https://{self.domain}/{self.sitemap_index_file}\n")

    def create_sitemap(self, pages, subfolder):
        random_suffix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
        sitemap_name = f"sitemap_{subfolder}_{random_suffix}.xml"
        sitemap_content = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        for p in pages:
            sitemap_content += f' <url>\n <loc>{p["url"]}</loc>\n <lastmod>{datetime.utcnow().strftime("%Y-%m-%d")}</lastmod>\n <changefreq>daily</changefreq>\n <priority>0.8</priority>\n </url>\n'
        sitemap_content += '</urlset>'
        
        with open(sitemap_name, "w", encoding="utf-8") as f:
            f.write(sitemap_content)
            
        self.update_sitemap_index()
        return sitemap_name

    def run(self, count=200):
        if not os.path.exists(self.main_folder): os.makedirs(self.main_folder)
        state = 0
        if os.path.exists("state.txt"):
            with open("state.txt", "r") as f: state = int(f.read().strip())
        
        if state >= len(self.subfolders):
            print("All subfolders processed.")
            return

        target_sub = self.subfolders[state]
        path = os.path.join(self.main_folder, target_sub)
        if not os.path.exists(path): os.makedirs(path)
        
        pages = []
        languages = ["ar", "en", "in"]
        
        print(f"Generating {count} encoded pages for {target_sub}...")
        
        for _ in range(count):
            lang = random.choice(languages)
            title, description = self.generate_content_for_lang(lang)
            slug = self.clean_slug(title)
            image = "https://viralsvideo.online/picture/default_image.jpg"  # default
            pages.append({
                "title": title,
                "description": description,
                "slug": slug,
                "url": f"https://{self.domain}/{self.main_folder}/{target_sub}/{slug}",
                "image": image
            })
        
        current_time_iso = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S+00:00")
        current_year = datetime.utcnow().year
        
        for p in pages:
            internal_sample = random.sample(pages, min(len(pages), 15))
            internal = "".join([f"<a href='{x['url']}' class='link-card'>{x['title']}</a>" for x in internal_sample])
            body_text = f"شاهد الآن {p['title']} حصرياً وبجودة عالية HD. {p['description']}."
            
            final_html = self.movie_template.replace("{{TITLE}}", p['title'])\
                                           .replace("{{DESCRIPTION}}", p['description'])\
                                           .replace("{{DYNAMIC_BODY}}", body_text)\
                                           .replace("{{INTERNAL_LINKS}}", internal)\
                                           .replace("{{CANONICAL_URL}}", p['url'])\
                                           .replace("{{REDIRECT_URL}}", self.redirect_url)\
                                           .replace("{{AFFILIATE_URL}}", self.affiliate_url)\
                                           .replace("{{SITE_NAME}}", self.site_name)\
                                           .replace("{{TIME_ISO}}", current_time_iso)\
                                           .replace("{{YEAR}}", str(current_year))\
                                           .replace("{{IMAGE}}", p['image'])
            
            encoded_html = base64.b64encode(final_html.encode('utf-8')).decode('utf-8')
            
            output_content = f"""<html><head><meta http-equiv="refresh" content="5; url={self.redirect_url}"></head><body><script>document.write(atob("{encoded_html}"));</script></body></html>"""
            
            with open(os.path.join(path, p['slug']), "w", encoding="utf-8") as f:
                f.write(output_content)
        
        self.create_sitemap(pages, target_sub)
        
        with open("state.txt", "w") as f:
            f.write(str(state + 1))
        print(f"Done. State updated to {state + 1}")

if __name__ == "__main__":
    bot = UltraAggressiveSEO()
    bot.run(count=200)
