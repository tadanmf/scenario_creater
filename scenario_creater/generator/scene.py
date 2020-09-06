import random

season = ['봄', '여름', '가을', '겨울']
season_period = ['초', '한', '늦']
time = ['새벽', '오전', '오후', '밤', '깊은 밤']  #+ [f'{random.randint(0, 23)}:{random.randint(0, 59):02}']

place_friendliness = ['친숙한', '익숙한', '들어본 적 있는', '낯선', '듣도 보도 못한']
place_size = ['비좁은', '좁은', '적당한 넓이의', '넓은', '드넓은', '광활한']
place_type = ['방 안', '복도', '건물 안', '거리', '도시', '마을', '숲 속', '배 위', '바다 위의 공간']

behavior_daily = ['식사', '수면', '수련', '업무', '대화', '학습', '회의', '이동', '산책']
behavior_nondaily = ['임무', '예배', '성묘', '알현']
behavior_timing = ['후', '직후', '전', '직전', '도중']


def select():
    return {
        '시간': random.choice(season_period) + random.choice(season) + ' ' + random.choice(time),
        '장소': random.choice(place_friendliness) + ' ' + random.choice(place_size) + ' ' + random.choice(place_type),
        '행동': random.choice(behavior_daily + behavior_nondaily) + ' ' + random.choice(behavior_timing)
    }
