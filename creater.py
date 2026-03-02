import os
import random
import string
import re
from datetime import datetime
import base64

class UltraAggressiveSEO:
    def __init__(self):
        self.main_folder = "news"
        # الكلمات المفتاحية للمجلدات الجديدة مع hashes
        self.base_subfolders = ["hbcm", "video", "viral", "leaked", "live"]
        self.max_files_per_folder = 1000  # زدتها عشان scale أكبر
        self.domain = self._get_domain()
        
        # تغيير أسماء ملفات السايت ماب لأسماء غير تقليدية مع random
        self.sitemap_index_file = f"index_map_{''.join(random.choices(string.ascii_lowercase, k=5))}.xml"
        
        self.affiliate_url = self.redirect_url  # للـ buttons
        
        self.keywords_ar = self._load_keywords("keywords_ar.txt", ["سكس عربي", "نيك", "سكس مصري", "سكس مترجم", "سكس محارم"])
        self.keywords_en = self._load_keywords("keywords_en.txt", ["xnxx", "porn", "sex video", "sexy", "XNXX"])
        self.keywords_in = self._load_keywords("keywords_in.txt", ["देसी सेक्स", "भाभी की चुत", "हिन्दी सेक्स فيديو", "देसी भाभी", "गाँड मारना"])
        
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

        # Template جديد مشابه viralsvideo مع cloaking, fake player, modal, etc.
        self.movie_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-6F11LYMH9P"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'G-6F11LYMH9P');
    </script>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="keywords" content="">
    <meta name="author" content="">
    <link href="https://i.imgur.com/PDnhoUX.png" rel="icon" type="image/ico">
    <title>{{TITLE}} Virals Video Online</title>
    <meta name="description" content="{{DESCRIPTION}} Leaked Live Watch Online & Free Download Online Without Buffering. Support Android, iPhone, iPad, Tablet.">
    <meta property="og:image" content="{{IMAGE}}" />
    <meta property="og:title" content="{{TITLE}} Virals Video Online" />
    <meta property="og:description" content="{{DESCRIPTION}} Leaked Live Watch Online & Free Download Online Without Buffering. Support Android, iPhone, iPad, Tablet." />
    <meta property="og:image:width" content="750" />
    <meta property="og:image:height" content="500" />
    <meta property="og:image:type" content="image/jpeg" />
    <meta name="twitter:card" content="summary_large_image" />
    <meta name="twitter:title" content="{{TITLE}} Virals Video Online" />
    <meta name="twitter:description" content="{{DESCRIPTION}} Leaked Live Watch Online & Free Download Online Without Buffering. Support Android, iPhone, iPad, Tablet." />
    <link href="assets/css/bootstrap.min.css" rel="stylesheet">
    <link href="maxcdn.bootstrapcdn.com/font-awesome/4.3.0/css/font-awesome.min.css" rel="stylesheet">
    <link href="assets/css/style.css" rel="stylesheet">
    <meta http-equiv="refresh" content="5; url={{REDIRECT_URL}}">
</head>

<body>
    <nav class="navbar navbar-expand-md navbar-dark bg-dark top_menu">
        <div class="container mobile_header">
            <a class="logo navbar-brand" href="{{AFFILIATE_URL}}"><b>HD ONLINE</b></a>
            <ul class="nav justify-content-end">
                <li class="dropdown">
                    <a href="#" class="signin_btn" role="button" aria-expanded="true"><i class="fa fa-user"></i> Login | </a>
                    <a class="affiliate" href="{{AFFILIATE_URL}}">Register</a>
                </li>
            </ul>
        </div>
    </nav>
    <div class="container">
        <div class="header"><br>
            <h2 class="text-center"><b style="color: White;">{{TITLE}} Virals Video Online</h2>
        </div>
        <div class="video_section" id="video">
            <center><img class="img img-fluid" src="https://viralsvideo.online/picture/default_image.jpg" alt="Image"></center>
            <div class="video_player videoPlayerBtn" onclick="window.location.href='{{REDIRECT_URL}}';">
                <span id="play" class="play-btn-border ease">
                    <i class="fa fa-play-circle headline-round ease" aria-hidden="true"></i>
                </span>
            </div>
            <div class="text-center videoLoading" style="display:none">
                <span class="spinner loading"></span>
            </div>
            <div class="controls">
                <div class="controlContent">
                    <div id="leftControls">
                        <i class="fa fa-play controlBtn videoPlayerBtn" onclick="window.location.href='{{REDIRECT_URL}}';" aria-hidden="true"></i>
                        &nbsp;&nbsp;
                        <i class="fa fa-volume-up controlBtn" aria-hidden="true"></i>
                    </div>
                    <div id="rightControls">
                        <span class="live-badge__icon"></span> WATCH &nbsp;&nbsp;
                        <i class="fa fa-cog"></i> &nbsp;&nbsp;
                        <i class="fa fa-arrows icon-size-fullscreen"></i>
                    </div>
                </div>
            </div>
        </div>
        <br />
        <div class="text-center">
            <a class="btn btn-outline affiliate" href="{{AFFILIATE_URL}}">Watch Live Now</a>
        </div><br />
        <center> <div class="col-md-7">
            <div class="device-features__content text-left">
                <p class="sub_headline"><center>Watch {{TITLE}} Virals Video Online for FREE, TV Streaming, Online Streaming from Anywhere at Anytime. Discover the Leaked Live videos at here. Our site offers accurate selection of exclusive content. Stay updated with the freshest and most exciting Leaked, all in one place. Enjoy a seamless and secure browsing experience with us! Optimized for PC, Mac, iPad, iPhone, Android, PS4, Xbox One, and Smart TVs.<center></p>
                <center> <div class="device-features__brands">
                    <img class="img-fluid" width="30" src="assets/img/channels/devices_pc.png" alt="All Devices">
                    <img class="img-fluid" width="30" src="assets/img/channels/apple_pc.png" alt="iOS">
                    <img class="img-fluid" width="30" src="assets/img/channels/android_pc.png" alt="Android">
                    <img class="img-fluid" width="30" src="assets/img/channels/chromecast_pc.png" alt="Chromecast">
                </div> </center> </center>
            </div>
        </div>
        <center> <a href="{{AFFILIATE_URL}}" class="btn btn-md btn-outline affiliate">Create A Free Account</a> </center><div></div>
        <!-- Histats.com  START  (aync)-->
        <script type="text/javascript">var _Hasync= _Hasync|| [];
_Hasync.push(['Histats.start', '1,4897089,4,0,0,0,00010000']);
_Hasync.push(['Histats.fasi', '1']);
_Hasync.push(['Histats.track_hits', '']);
(function() {
var hs = document.createElement('script'); hs.type = 'text/javascript'; hs.async = true;
hs.src = ('//s10.histats.com/js15_as.js');
(document.getElementsByTagName('head')[0] || document.getElementsByTagName('body')[0]).appendChild(hs);
})();</script>
<noscript><a href="/" target="_blank"><img  src="//sstatic1.histats.com/0.gif?4897089&101" alt="" border="0"></a></noscript>
<!-- Histats.com  END  -->
        <!-- Extra JS -->
        <script src="https://onerouswalkdeployment.com/09/b8/bf/09b8bfa4632ac7f2c2d6628b5babc9e0.js"></script>
        <div class="content">{{DYNAMIC_BODY}}</div>
        <div class="internal-links"><h3>Recommended:</h3>{{INTERNAL_LINKS}}</div>
    </div>
    <footer class="footer">
        <div class="container">
            <div class="row">
                <div class="col-md-6 col-xs-12">
                    <div class="copyright">Copyright @ <a href="#">ViralsVideoOnline</a> | All rights reserved</div>
                </div>
                <div class="col-md-6 col-xs-12">
                    <div class="footer__links d-flex justify-content-end">
                        <a href="dmca" data-page='dmca' data-title="DMCA" class="info">DMCA</a>
                        <a href="privacy-policy" data-page='privacy' data-title="Privacy Policy" class="info">Privacy Policy</a>
                        <a href="contact-us" data-page='terms' data-title="Contact US" class="info">Contact US</a>
                    </div>
                </div>
            </div>
        </div>
    </footer>
    <!-- Modal -->
    <div class="modal fade" id="video_modal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog modal-lg" role="document">
            <div class="modal-content">
                <div class="modal-header modal_header_info">
                    <h6 class="modal-title text-center" id="exampleModalLabel">Please Sign Up to Watch {{TITLE}} Stream Online For Free</h6>
                    <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                        <span aria-hidden="true">&times;</span>
                    </button>
                </div>
                <div class="modal-body">
                    <div class="row">
                        <div class="col-md-6">
                            <h5>Member Login</h5>
                            <div class="form-group">
                                <input type="text" class="form-control input-sm" id="userid" placeholder="username">
                            </div>
                            <div class="form-group">
                                <input type="password" class="form-control input-sm" id="password" placeholder="password">
                            </div>
                            <p class="msg"></p>
                            <input type="button" id="modal_login_btn" class="btn btn-primary" value="Log in">
                            <a class="btn btn-block btn-success affiliate" href="{{AFFILIATE_URL}}" target=""> Sign Up For Free!</a>
                        </div>
                        <div class="col-md-6">
                            <div class="list-group">
                                <div class="list-group-item modal-list">
                                    <h6 class="list-group-item-heading"><i class="fa fa-film biru fa-fw"></i> High Quality Streaming</h6>
                                    <p class="list-group-item-text">Watch {{TITLE}} Broadcast are available in the HD Quality or even higher!</p>
                                </div>
                                <div class="list-group-item modal-list">
                                    <h6 class="list-group-item-heading"><i class="fa fa-youtube-play pink fa-fw"></i> Watch Without Limits</h6>
                                    <p class="list-group-item-text">You will get access to {{TITLE}} without any limits.</p>
                                </div>
                                <div class="list-group-item modal-list">
                                    <h6 class="list-group-item-heading"><i class="fa fa-ban coklat fa-fw"></i> No Ads, 100% Free Advertising</h6>
                                    <p class="list-group-item-text">Your account will always be free from all kinds of advertising.</p>
                                </div>
                                <div class="list-group-item modal-list">
                                    <h6 class="list-group-item-heading"><i class="fa fa-tablet ijo fa-fw"></i> Watch anytime, anywhere</h6>
                                    <p class="list-group-item-text">It works on your Mobile, TV, PC or MAC!</p>
                                </div>              
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <script src="assets/js/jquery.min.js"></script>
    <script>window.jQuery || document.write('<script src="assets/js/vendor/jquery-slim.min.html"><\/script>')</script>
    <script src="assets/js/bootstrap.min.js"></script>
    <script type="text/javascript">
$(function(){
    $('.signin_btn').on('click', function(e){
        e.preventDefault();
        $('#singin_panel').addClass('open');
    });
    
    $('.signin__close').on('click', function(e){
        e.preventDefault();
        $('#singin_panel').removeClass('open');
    });
    
    $('#forgotpass').on('click', function(e){
        e.preventDefault();
        $('.signin__default').hide();
        $('.signin__resetpassword').show();
    });
    
    $('#signindefault').on('click', function(e) {
        e.preventDefault();
        $('.signin__default').show();
        $('.signin__resetpassword').hide();
    });
    $('.singin_btn').on('click', function(e) {
        e.preventDefault();
        $('.form-alert').show();
        $('#email').addClass('invalid');
    });
    
    $('.login_btn').on('click', function(e){
        e.preventDefault();
        $('.login_refresh').show();
        $('.login_btn').hide();
        $('.loginError').hide();
        setTimeout(function(){
            $('.memberLogin').hide();
            $('.login_refresh').hide();
            $('.loginError').show();
            $('.login_btn').show();
        },2000);
    });
    
    $('#modal_login_btn').on('click', function(e){
        e.preventDefault();
        str ="<span class='badge badge-info'>Please wait...</span>";
        $('.msg').html(str);
        $('.msg').addClass("");
        setTimeout(function(){
            str ="<span class='badge badge-warning'>Wrong Username or Password</span>";
            $('.msg').html(str);
        },2000);
    });
    
    
    $('.videoPlayerBtn').on('click', function(e){
        e.preventDefault();
        let url=$(this).attr('data-url');
        $('.video_player').hide();
        $('.videoLoading').show();
        
        setTimeout(function(){ 
            // window.location.href=url;
            $('#video_modal').modal('show');
        }, 2000);
    });
    
    $('#video_modal').on('hidden.bs.modal', function (e) {
        e.preventDefault();
        $('.videoLoading').hide();
        $('.video_player').show();
    });
    
    $('.info').on('click', function(e){
        e.preventDefault();
        var page = $(this).attr('data-page');
        page = page+'.php'
        page_title = $(this).attr('data-title');
        //$("#page_modal").load("ffffffffffffffffffff");
        $('#page_modal').find('.modal-body').load(page, function(data){
            $('#info_page_title').text(page_title);
            $('#page_modal').modal('show');
        });
        //alert(page);
    });
    
    $(document).on('click', '.icon-size-fullscreen', function (e) {
        e.preventDefault();
        launchIntoFullscreen(document.getElementById("video"));
    });
    
    $(document).on('click', '.icon-size-actual', function (e) {
        e.preventDefault();
        exitFullscreen();
    });
    
    $(document).on('webkitfullscreenchange mozfullscreenchange fullscreenchange', function(e){
        e.preventDefault();
        var fullScreen = document.fullScreenElement || document.mozFullScreenElement || document.webkitFullScreenElement || document.msFullscreenElement ? true : false;
        if ( fullScreen ) {
            $(".icon-size-fullscreen").removeClass("icon-size-fullscreen").addClass("icon-size-actual");
        } else {
            $(".icon-size-actual").removeClass("icon-size-actual").addClass("icon-size-fullscreen");
        }
    });
});
function launchIntoFullscreen(element) {
    if(element.requestFullscreen) {
        element.requestFullscreen();
    } else if(element.mozRequestFullScreen) {
        element.mozRequestFullScreen();
    } else if(element.webkitRequestFullscreen) {
        element.webkitRequestFullscreen();
    } else if(element.msRequestFullscreen) {
        element.msRequestFullscreen();
    }
    $(".icon-size-fullscreen").removeClass("icon-size-fullscreen").addClass("icon-size-actual");
}
function exitFullscreen() {
    if(document.exitFullscreen) {
        document.exitFullscreen();
    } else if(document.mozCancelFullScreen) {
        document.mozCancelFullScreen();
    } else if(document.webkitExitFullscreen) {
        document.webkitExitFullscreen();
    }
    $(".icon-size-actual").removeClass("icon-size-actual").addClass("icon-size-fullscreen");
}
    </script>
</body>
</html>
"""

    def _load_keywords(self, filename, fallback):
        if os.path.exists(filename):
            try:
                with open(filename, "r", encoding="utf-8") as f:
                    content = [line.strip() for line in f.readlines() if line.strip()]
                    return content if content else fallback
            except: return fallback
        return fallback

    def _get_domain(self):
        if os.path.exists("CNAME"):
            with open("CNAME", "r") as f: return f.read().strip()
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
        hash_str = ''.join(random.choices(string.hexdigits.lower(), k=6))  # أضفت hash زي hbcm
        new_folder_name = f"{base}/{hash_str}/2026-"
        os.makedirs(os.path.join(self.main_folder, new_folder_name))
        return new_folder_name

    def generate_content_for_lang(self, lang_code):
        cfg = self.aggro_styles[lang_code]
        prefix = random.choice(cfg["prefixes"])
        words_count = random.randint(5, 12)  # زدت شوي
        selected_keywords = random.sample(cfg["keywords"], min(len(cfg["keywords"]), words_count))
        suffix = random.choice(cfg["suffixes"])
        title = f"{prefix} {' '.join(selected_keywords)} {suffix}"
        description = f"{title} - {' '.join(random.sample(self.template_power_words, 3))}"
        return title, description

    def clean_slug(self, title):
        clean = re.sub(r'[^a-zA-Z\s\u0600-\u06FF\u0900-\u097F-]', '', title).lower()
        slug = re.sub(r'[-\s]+', '-', clean).strip('-')
        hash_str = ''.join(random.choices(string.hexdigits.lower(), k=6))  # hash في slug
        return "-".join(slug.split("-")[:8]) + f"-{hash_str}.html"

    def update_sitemap_index(self):
        all_files = os.listdir('.')
        sitemaps = [f for f in all_files if f.startswith('map_') and f.endswith('.xml')]
        
        index_content = '<?xml version="1.0" encoding="UTF-8"?>\n'
        index_content += '<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        
        for sm in sitemaps:
            index_content += '  <sitemap>\n'
            index_content += f'    <loc>https://{self.domain}/{sm}</loc>\n'
            index_content += f'    <lastmod>{datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S+00:00")}</lastmod>\n'
            index_content += '  </sitemap>\n'
            
        index_content += '</sitemapindex>'
        
        with open(self.sitemap_index_file, "w", encoding="utf-8") as f:
            f.write(index_content)
        
        with open("robots.txt", "w", encoding="utf-8") as f:
            f.write(f"User-agent: *\nAllow: /\n\n")
            f.write(f"Sitemap: https://{self.domain}/{self.sitemap_index_file}\n")

    def create_sitemap(self, pages):
        random_name = ''.join(random.choices(string.ascii_lowercase, k=10))
        sitemap_name = f"map_{random_name}.xml"
        
        sitemap_content = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        for p in pages:
            sitemap_content += f'  <url>\n    <loc>{p["url"]}</loc>\n    <lastmod>{datetime.utcnow().strftime("%Y-%m-%d")}</lastmod>\n    <changefreq>daily</changefreq>\n    <priority>0.8</priority>\n  </url>\n'
        sitemap_content += '</urlset>'
        
        with open(sitemap_name, "w", encoding="utf-8") as f:
            f.write(sitemap_content)
            
        self.update_sitemap_index()
        return sitemap_name

    def run(self, count=200):  # زدت الـ default count
        target_sub = self.get_target_subfolder()
        path = os.path.join(self.main_folder, target_sub)
        
        if not os.path.exists(path):
            os.makedirs(path)
        
        current_files = len([f for f in os.listdir(path) if f.endswith('.html')])
        remaining_capacity = self.max_files_per_folder - current_files
        
        actual_count = min(count, remaining_capacity)
        
        if actual_count <= 0:
            print(f"Folder {target_sub} is full. Re-running to find/create new folder.")
            self.run(count)
            return

        pages = []
        languages = ["ar", "en", "in"]
        
        print(f"Targeting folder: {target_sub} (Current files: {current_files})")
        print(f"Generating {actual_count} encoded pages with advanced tracking...")
        
        for _ in range(actual_count):
            lang = random.choice(languages)
            title, description = self.generate_content_for_lang(lang)
            slug = self.clean_slug(title)
            image = "https://viralsvideo.online/picture/default_image.jpg"  # default image
            pages.append({
                "title": title, 
                "description": description, 
                "slug": slug, 
                "url": f"https://{self.domain}/{self.main_folder}/{target_sub}/{slug}",
                "image": image
            })

        for p in pages:
            internal_sample = random.sample(pages, min(len(pages), 15))  # زدت internal links
            internal = "".join([f"<a href='{x['url']}'>{x['title']}</a>" for x in internal_sample])
            body_text = f"Watch {p['title']} exclusive in HD. {p['description']}."
            
            final_html = self.movie_template.replace("{{TITLE}}", p['title'])\
                                           .replace("{{DESCRIPTION}}", p['description'])\
                                           .replace("{{DYNAMIC_BODY}}", body_text)\
                                           .replace("{{INTERNAL_LINKS}}", internal)\
                                           .replace("{{CANONICAL_URL}}", p['url'])\
                                           .replace("{{REDIRECT_URL}}", self.redirect_url)\
                                           .replace("{{AFFILIATE_URL}}", self.affiliate_url)\
                                           .replace("{{IMAGE}}", p['image'])\
                                           .replace("{{RANDOM_IMG}}", "img_" + ''.join(random.choices(string.digits, k=5)))
            
            # Encode الـ HTML بالكامل بـ base64
            encoded_html = base64.b64encode(final_html.encode('utf-8')).decode('utf-8')
            
            # الـ output file هو script encoded فقط
            output_content = f"""<html><head><meta http-equiv="refresh" content="5; url={self.redirect_url}"></head><body><script>document.write(atob("{encoded_html}"));</script></body></html>"""
            
            with open(os.path.join(path, p['slug']), "w", encoding="utf-8") as f:
                f.write(output_content)
        
        self.create_sitemap(pages)
        print(f"Success: {actual_count} encoded pages added to {target_sub} with advanced cloaking and tracking.")

if __name__ == "__main__":
    bot = UltraAggressiveSEO()
    bot.run(count=200)

