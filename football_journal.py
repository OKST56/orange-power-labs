"""Published NCAA Football 07 articles, separate from CBL numbering."""
from pathlib import Path

ROOT = Path(__file__).parent

def build(page, intro, markdown):
    filename='ncaa-football-07-dev-log-001.html'
    title='From Childhood Favorite to PC Recompilation'
    body=markdown((ROOT/'content/ncaa-football-07-dev-log-001.md').read_text(encoding='utf-8'))
    figure='''<figure class="dev-image"><img src="assets/ncaa-football-07-cover.jpg" alt="NCAA Football 07 cover artwork featuring Reggie Bush"><figcaption>NCAA Football 07 cover artwork. Image: EA Sports, via <a href="https://www.ign.com/wikis/ncaa-football-07">IGN</a>. Reference imagery from the original game.</figcaption></figure>'''
    position=body.find('</p>')+4
    body=body[:position]+figure+body[position:]
    page(filename,'NCAA Football 07 Recomp — Dev Log 001',f'<section class="article"><a class="back" href="ncaa-football-07-dev-logs.html">← NCAA Football 07 journal</a><p class="eyebrow">NCAA FOOTBALL 07 RECOMP / ORIGINAL XBOX / 001</p><article>{body}</article><div class="article-nav"><a href="ncaa-football-07.html">← Project overview</a><a href="community.html">Join the conversation ↗</a></div></section>','Dev Logs')
    listing=f'''<div class="log-list"><a class="log-row" href="{filename}"><span class="log-number">001</span><div><p class="eyebrow">NCAA FOOTBALL 07 RECOMP / PROJECT INTRODUCTION</p><h3>{title}</h3><p>A childhood favorite, original Xbox recompilation, and the long-term Missouri high school football dream.</p></div><span class="arrow">↗</span></a></div>'''
    page('ncaa-football-07-dev-logs.html','NCAA Football 07 Recomp — Development Journal',intro('NCAA FOOTBALL 07 RECOMP / ORIGINAL XBOX','The Xbox recompilation journal.','Follow the childhood-favorite origin story and the work toward native Windows. An independent series, beginning at #001.')+'<section><a class="text-link" href="ncaa-football-07.html">← Project overview</a>'+listing+'</section>','Dev Logs')
    for name in ['index.html','dev-logs.html','ncaa-football-07.html']:
        path=ROOT/'site'/name
        text=path.read_text(encoding='utf-8')
        text=text.replace('A new journal for a childhood favorite. Opening articles are in preparation.','Read our first published article: a childhood favorite becomes a new recompilation project.')
        if name=='ncaa-football-07.html':
            text=text.replace('Its development journal will document the story as articles are published.',f'Our first development log tells the origin story. <a class="text-link" href="{filename}">Read Dev Log 001 →</a>')
            text=text.replace('</main>','<section><p class="eyebrow">NCAA FOOTBALL 07 / DEVELOPMENT JOURNAL</p><h2>The journey begins.</h2>'+listing+'</section></main>')
        else:
            text=text.replace('</main>','<section><p class="eyebrow">NCAA FOOTBALL 07 / NEW IN THE JOURNAL</p><h2>From childhood favorite to PC recompilation.</h2>'+listing+'</section></main>')
        path.write_text(text,encoding='utf-8')
