import random
from scenario_creater.generator.resource.twenty_master_plots import plots

time_period_historical = [
    u'신화',
    u'고대',
    u'중세',
    u'근대',
    u'현대',
]
time_period_fictional = [
    u'판타지',
    u'무협',
    u'스팀펑크',
    u'SF',
]
time_period = time_period_historical + time_period_fictional

mood = [
    u'공포',
    u'스릴러',
    u'느와르',
    u'액션',
    u'드라마',
    u'로맨스',
    u'코미디',
]
tag = [
    u'게임',
    u'군대',
    u'다큐',
    u'로맨스',
    u'로봇',
    u'미술',
    u'생존',
    u'성장',
    u'스포츠',
    u'역사',
    u'요리',
    u'음악',
    u'의료',
    u'일상',
    u'재난',
    u'전쟁',
    u'추리',
    u'학교',
    u'회사',
]


def select():
    return {
        u'시대': random.choice(time_period),
        u'분위기': random.choice(mood),
        u'태그': '#' + ', #'.join(random.sample(tag, k=3)),
        u'플롯': ' - '.join(random.choice(list(plots.items()))),
    }
