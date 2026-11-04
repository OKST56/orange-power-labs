from pathlib import Path
import re, html

ROOT = Path(__file__).parent
OUT = ROOT / 'site'
NAV = [('Home','index.html'),('Projects','projects.html'),('Dev Logs','dev-logs.html'),('Media','media.html'),('Downloads','downloads.html'),('Community','community.html')]
def page(file,title,body,active=None):
    nav=''.join(f'<a href="{url}"'+(' aria-current="page"' if (active or title)==name else '')+f'>{name}</a>' for name,url in NAV)
    text=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="theme-color" content="#181818"><meta name="description" content="Orange Power Labs: independent sports game development, native recompilation, and ambitious mods. Follow College Baseball Legacy and Missouri High School Football."><title>{html.escape(title)} | Orange Power Labs</title><link rel="icon" href="assets/logo.png"><link rel="stylesheet" href="assets/style.css"></head><body><a class="skip" href="#main">Skip to content</a><header><a class="brand" href="index.html"><img src="assets/logo.png" alt=""><span>ORANGE POWER <b>LABS</b><small>GAME DEVELOPMENT & MODDING</small></span></a><button class="menu" aria-expanded="false" aria-controls="navigation">Menu <span>+</span></button><nav id="navigation" aria-label="Main navigation">{nav}</nav></header><main id="main">{body}</main><footer><a class="brand" href="index.html">ORANGE POWER <b>LABS</b></a><p>Independent spirit. Big-league ambition.</p><div><span>© 2026 Orange Power Labs</span><a href="community.html">Find your community ↗</a></div><small>Independent fan projects. Not affiliated with or endorsed by Sony Interactive Entertainment, MLB, the NCAA, EA Sports, or their respective organizations.</small></footer><script src="assets/app.js"></script></body></html>'''
    (OUT/file).write_text(text,encoding='utf-8')
def intro(kicker,title,desc):
    return f'<section class="intro"><p class="eyebrow">{kicker}</p><h1>{title}</h1><p class="lead">{desc}</p></section>'
def cards():
    return '''<div class="project-grid"><a class="project baseball" href="college-baseball-legacy.html"><div class="field" aria-hidden="true"><i></i></div><div class="project-copy"><span class="status">● Active development</span><p class="eyebrow">01 / BASEBALL</p><h3>College Baseball<br>Legacy</h3><p>A new chapter for college baseball on PC. Native Windows recompilation meets an ambitious NCAA conversion.</p><span class="text-link">Explore the project ↗</span></div></a><a class="project football" href="missouri-high-school-football.html"><div class="yard-lines" aria-hidden="true"></div><div class="project-copy"><span class="status muted">● Research & development</span><p class="eyebrow">02 / FOOTBALL</p><h3>Missouri High<br>School Football</h3><p>Friday night ambition. Exploring a Missouri high school football experience built on NCAA Football 14.</p><span class="text-link">Explore the project ↗</span></div></a></div>'''

titles=['The Beginning of College Baseball Legacy','Recompiling an Entire Baseball Game','Bringing the Game Engine to Life','Breaking Through the Graphics Barrier','We Have a Title Screen!']
dates=['October 16–23, 2026','October 24–26, 2026','October 26–29, 2026','October 29 – November 2, 2026','November 2–3, 2026']
summaries=['The vision, the tools, and the first native Windows build.','15,768 function entry points. 129 generated C++ files. A major step toward Windows.','Tracing an animation stall back to memory allocation—and restoring 7,083 clips.','Command buffers, synchronization, and the path to visible progress.','A correctly rendered title screen and the first steps into a partially rendered main menu.']
def rows(indices):
    return '<div class="log-list">'+''.join(f'<a class="log-row" href="dev-log-{i+1:03}.html"><span class="log-number">{i+1:03}</span><div><p class="eyebrow">{dates[i]}</p><h3>{titles[i]}</h3><p>{summaries[i]}</p></div><span class="arrow">↗</span></a>' for i in indices)+'</div>'

page('index.html','Home','''<section class="hero"><div class="hero-copy"><p class="eyebrow"><span class="dot"></span> ORANGE POWER LABS / INDEPENDENT DEVELOPMENT</p><h1>Classic games.<br>New possibilities.<br><em>All heart.</em></h1><p class="lead">Bringing classic sports games into a new era. Native recompilation, ambitious mods, and the future of college sports gaming.</p><div class="actions"><a class="button" href="projects.html">Explore our projects ↗</a><a class="secondary" href="dev-logs.html">Read the dev logs →</a></div></div><div class="hero-art"><div class="orbit"></div><img src="assets/logo.png" alt="Orange Power Labs orange OP lightning bolt and cowboy hat logo"><p>BUILT WITH GRIT.<br><b>POWERED BY POSSIBILITY.</b></p></div></section><div class="ticker"><span>INDEPENDENT DEVELOPMENT</span><b>✳</b><span>SPORTS GAMING</span><b>✳</b><span>REWRITING WHAT’S POSSIBLE</span><b>✳</b></div><section><div class="section-heading"><div><p class="eyebrow">THE WORK</p><h2>Big ideas. Real progress.</h2></div><a href="projects.html">All projects ↗</a></div>'''+cards()+'''</section><section><div class="section-heading"><div><p class="eyebrow">FROM THE LAB</p><h2>Every breakthrough has a story.</h2></div><a href="dev-logs.html">All dev logs ↗</a></div>'''+rows([4,3,2])+'''</section><section class="community-banner"><p class="eyebrow">PULL UP A CHAIR</p><h2>Follow the build.<br>Be part of what comes next.</h2><p>Join the community for project discussion and a closer look at the journey.</p><a class="button" href="community.html">Find the community ↗</a></section>''')
page('projects.html','Projects',intro('THE WORK','Projects with a purpose.','Reimagining the sports games we love, one milestone at a time.')+'<section>'+cards()+'</section>')
page('college-baseball-legacy.html','College Baseball Legacy',intro('PROJECT 01 / ACTIVE DEVELOPMENT','College Baseball Legacy','A long-term vision for college baseball on PC, built on the foundation of MLB The Show 16.')+'''<section class="split"><div><h2>First, bring the game to Windows.</h2><p>The first challenge is static recompilation: translating the original PS3 executable into code that can run as a native Windows application, supported by a compatible runtime.</p><p>The longer-term goal is an NCAA baseball conversion with college programs, conferences, schedules, and a road to Omaha.</p><a class="button" href="dev-logs.html">Follow the development →</a></div><aside><p class="eyebrow">STATUS / NOVEMBER 3, 2026</p><h3>A title screen.<br>A major first.</h3><p>The original title screen has rendered in the native build. Startup navigation has reached a partially rendered main menu.</p><p>Playable baseball remains a future milestone. No public build is available.</p></aside></section><section><div class="section-heading"><h2>The journey so far</h2></div>'''+rows(range(4,-1,-1))+'</section>','Projects')
page('missouri-high-school-football.html','Missouri High School Football',intro('PROJECT 02 / RESEARCH & DEVELOPMENT','Friday nights.<br>Missouri roots.','Exploring a Missouri high school football experience through NCAA Football 14.')+'''<section class="split"><div><h2>Local pride. A bigger stage.</h2><p>This project explores expanding NCAA Football 14 with Missouri high school programs. It is in research and development.</p><p>Confirmed scope, media, and release details will be shared here as development progresses.</p><a class="button" href="community.html">Follow future updates ↗</a></div><aside><p class="eyebrow">PROJECT STATUS</p><h3>Early days.<br>Big ambitions.</h3><p>No release date or public download has been announced.</p></aside></section>''','Projects')
page('dev-logs.html','Dev Logs',intro('THE DEVELOPMENT JOURNAL','From the first build<br>to the next breakthrough.','Five updates from October 16 to November 3, 2026. The community story, with the engineering behind it.')+'<section>'+rows(range(4,-1,-1))+'</section>')

def inline(s):
    s=html.escape(s)
    s=re.sub(r'\*\*(.+?)\*\*',r'<strong>\1</strong>',s)
    return re.sub(r'\*([^*]+)\*',r'<em>\1</em>',s)
def markdown(s):
    result=[]; paragraph=[]; list_type=None
    def flush():
        if paragraph: result.append('<p>'+inline(' '.join(paragraph))+'</p>'); paragraph.clear()
    for line in s.splitlines()+['']:
        line=line.strip()
        match=re.match(r'^(?:- |\d+\. )(.+)',line)
        if match:
            flush(); kind='ul' if line.startswith('-') else 'ol'
            if list_type!=kind:
                if list_type: result.append(f'</{list_type}>')
                result.append(f'<{kind}>'); list_type=kind
            result.append('<li>'+inline(match[1])+'</li>'); continue
        if list_type: result.append(f'</{list_type}>'); list_type=None
        if line.startswith('#'):
            flush(); level=min(len(line)-len(line.lstrip('#')),4); result.append(f'<h{level}>'+inline(line.lstrip('# '))+f'</h{level}>')
        elif not line: flush()
        else: paragraph.append(line)
    return ''.join(result)
raw=(ROOT/'content/recovered-dev-logs.txt').read_text(encoding='utf-8')
blocks=re.findall(r':::writing[^\n]*\n(.*?)(?=\n:::|\Z)',raw,re.S)
blocks[4]=(ROOT/'content/dev-log-005.md').read_text(encoding='utf-8')
for i,block in enumerate(blocks):
    body=markdown(block)
    figures={
        0: '<figure class="dev-image"><img src="assets/mlb-the-show-16-ortiz.png" alt="David Ortiz batting for Boston in MLB The Show 16, with a Baltimore catcher behind home plate"><figcaption>MLB The Show 16 — David Ortiz. Reference imagery from the original game. Image: Sony / San Diego Studio, via <a href="https://www.gamespot.com/wp-content/uploads/original/536/5360430/3009525-ortiz.jpg">GameSpot</a>.</figcaption></figure>',
        4: '<figure class="dev-image"><img src="assets/native-title-screen.png" alt="Orange Power Labs native Windows build displaying the MLB The Show 16 title screen with Josh Donaldson"><figcaption>Our native Windows build displaying the MLB The Show 16 title screen. Actual development capture supplied by Orange Power Labs.</figcaption></figure>'
    }
    if i in figures:
        # Insert the image beneath the existing title and date; preserve all original prose.
        position=body.find('</p>')+4
        body=body[:position]+figures[i]+body[position:]
    warning=''
    page(f'dev-log-{i+1:03}.html',f'Dev Log {i+1:03} — {titles[i]}',f'<section class="article"><a class="back" href="dev-logs.html">← All dev logs</a><p class="eyebrow">FROM THE LAB / {i+1:03}</p>{warning}<article>{body}</article><div class="article-nav">'+(f'<a href="dev-log-{i:03}.html">← Previous entry</a>' if i else '<span></span>')+(f'<a href="dev-log-{i+2:03}.html">Next entry →</a>' if i<4 else '<a href="community.html">Join the conversation ↗</a>')+'</div></section>','Dev Logs')
page('media.html','Media',intro('A LOOK INSIDE','The work, in focus.','A home for development captures, screenshots, and videos.')+'''<section class="empty"><span class="large-number">REC / 001</span><h2>Our first visual milestone.</h2><p>The native title screen is documented in Dev Log 005. Verified development screenshots and videos will appear here when they are ready to share.</p><a class="button" href="dev-log-005.html">Read the milestone →</a></section>''')
page('downloads.html','Downloads',intro('WHEN IT’S READY','Good things<br>take development.','Future public releases and project tools will live here.')+'''<section class="empty"><span class="status muted">● No public releases yet</span><h2>Still in the lab.</h2><p>College Baseball Legacy is working toward a functional native runtime. Missouri High School Football is in research and development. Neither project has a public download or an announced release date.</p><a class="button" href="dev-logs.html">See the latest progress →</a></section>''')
page('community.html','Community',intro('THE PEOPLE BEHIND THE PROGRESS','Come for the games.<br>Stay for the journey.','Follow the experiments, talk sports games, and be there for the next breakthrough.')+'''<section class="split"><div><p class="eyebrow">DISCORD</p><h2>The lab is open.</h2><p>Join the Orange Power Labs community to discuss the projects and follow development.</p><a class="button" href="https://discord.gg/mByxc7QGq" target="_blank" rel="noopener noreferrer">Join us on Discord ↗</a><p class="fine">This is a temporary invite and may expire. If it no longer works, check back here for a refreshed link.</p></div><aside><p class="eyebrow">MORE FROM THE LAB</p><h3>Keep up with the build.</h3><p>The development journal is the home for our published milestones.</p><a class="text-link" href="dev-logs.html">Read the journal →</a><hr><a class="text-link" href="https://github.com/OKST56" target="_blank" rel="noopener noreferrer">OKST56 on GitHub ↗</a></aside></section>''')
page('404.html','Page not found',intro('404 / OUT OF PLAY','That page is out of bounds.','Let’s get you back to the lab.')+'<section><a class="button" href="https://okst56.github.io/orange-power-labs/">Back to home →</a></section>')
(OUT/'.nojekyll').touch()
print(f'Built {len(list(OUT.glob("*.html")))} pages.')
