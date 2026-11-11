"""Published NCAA Football 07 articles, separate from CBL numbering."""
from pathlib import Path
ROOT = Path(__file__).parent
ARTICLES = [
    ('001', 'From Childhood Favorite to PC Recompilation', 'PROJECT INTRODUCTION', 'A childhood favorite, original Xbox recompilation, and the long-term Missouri high school football dream.'),
    ('002', 'Cracking Open NCAA Football 07', 'EXECUTABLE RESEARCH', 'Inside the original Xbox game image: file inventory, executable sections, and imported system dependencies.'),
    ('003', 'Mapping the Game: 33,755 Functions and Our First Major Roadblocks', 'FUNCTION AND ABI RESEARCH', 'Mapping 33,755 function candidates and identifying what needs validation before lifting can proceed.'),
]
def build(page, intro, markdown):
    for index, (number, title, category, summary) in enumerate(ARTICLES):
        body=markdown((ROOT/f'content/ncaa-football-07-dev-log-{number}.md').read_text(encoding='utf-8'))
        if number=='001':
            figure='''<figure class="dev-image"><img src="assets/ncaa-football-07-cover.jpg" alt="NCAA Football 07 cover artwork featuring Reggie Bush"><figcaption>NCAA Football 07 cover artwork. Image: EA Sports, via <a href="https://www.ign.com/wikis/ncaa-football-07">IGN</a>. Reference imagery from the original game.</figcaption></figure>'''
            position=body.find('</p>')+4
            body=body[:position]+figure+body[position:]
        previous=f'<a href="ncaa-football-07-dev-log-{ARTICLES[index-1][0]}.html">← Previous entry</a>' if index else '<a href="ncaa-football-07.html">← Project overview</a>'
        following=f'<a href="ncaa-football-07-dev-log-{ARTICLES[index+1][0]}.html">Next entry →</a>' if index<len(ARTICLES)-1 else '<a href="community.html">Join the conversation ↗</a>'
        page(f'ncaa-football-07-dev-log-{number}.html',f'NCAA Football 07 Recomp — Dev Log {number}',f'<section class="article"><a class="back" href="ncaa-football-07-dev-logs.html">← NCAA Football 07 journal</a><p class="eyebrow">NCAA FOOTBALL 07 RECOMP / ORIGINAL XBOX / {number}</p><article>{body}</article><div class="article-nav">{previous}{following}</div></section>','Dev Logs')
    listing='<div class="log-list">'+''.join(f'<a class="log-row" href="ncaa-football-07-dev-log-{number}.html"><span class="log-number">{number}</span><div><p class="eyebrow">NCAA FOOTBALL 07 RECOMP / {category}</p><h3>{title}</h3><p>{summary}</p></div><span class="arrow">↗</span></a>' for number,title,category,summary in reversed(ARTICLES))+'</div>'
    page('ncaa-football-07-dev-logs.html','NCAA Football 07 Recomp — Development Journal',intro('NCAA FOOTBALL 07 RECOMP / ORIGINAL XBOX','The Xbox recompilation journal.','Follow the childhood-favorite origin story and the work toward native Windows. An independent series, beginning at #001.')+'<section><a class="text-link" href="ncaa-football-07.html">← Project overview</a>'+listing+'</section>','Dev Logs')
    for name in ['index.html','dev-logs.html','ncaa-football-07.html']:
        path=ROOT/'site'/name
        text=path.read_text(encoding='utf-8')
        if name=='ncaa-football-07.html':
            text=text.replace('Its development journal will document the story as articles are published.','Our latest development log covers function candidates, calling conventions, and the roadblocks to lifting. <a class="text-link" href="ncaa-football-07-dev-log-003.html">Read Dev Log 003 →</a>')
            text=text.replace('</main>','<section><p class="eyebrow">NCAA FOOTBALL 07 / DEVELOPMENT JOURNAL</p><h2>The journey continues.</h2>'+listing+'</section></main>')
        else:
            text=text.replace('</main>','<section><p class="eyebrow">NCAA FOOTBALL 07 / NEW IN THE JOURNAL</p><h2>Mapping the game.</h2>'+listing+'</section></main>')
        path.write_text(text,encoding='utf-8')
