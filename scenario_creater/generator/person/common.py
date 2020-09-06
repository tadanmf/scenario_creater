from random import choice, choices, sample

nature_list = [
    '용의주도', '상상력 풍부', '사색적', '논리적', '대담한', '도전적', '조용한', '신비로운', '이상주의', '열정적',
    '상냥한', '이타주의', '낭만적', '카리스마', '정의로운', '대중을 압도하는', '재기발랄', '창의적', '활발한',
    '어울리기 좋아하는', '자유로운', '청렴결백한', '현실주의', '용감한', '헌신적', '성실한', '자기방어적', '엄격한',
    '세심한', '사교적', '융통성 있는', '모험을 즐기는', '에너지 넘치는', '즉흥적'
]

desire_list = [
    '식욕', '물욕', '권력욕', '안전욕구', '재물욕', '명예욕', '수면욕', '경쟁욕', '호기심 충족', '영역 보존', '의존 욕구', '성장 욕구', '게으름']

goal_list = ['세계정복', '복수', '업계에서 성공한다', '생존', '직위 탈환', '명예 회복', '혁명', '조직 부강']

body_list = ['왜소', '마름', '표준 체형', '건장', '거대']

clothes_list = ['후줄근', '깔끔', '멋부리다']

secret_list = ['출생', '질환', '목표', '상처', '직업', '출신', '연령', '신체 일부']

person_list = ['상사', '가족', '친구', '동료']

thing_list = ['바다', '물', '불', '날붙이', '음식', '집', '비', '종교', '금', '돈', '보석', '땅']

living_thing_list = ['새', '파충류', '인간', '물고기', '동물']

scale_list = ['초반', '중반', '후반']

origin_list = ['귀족', '범죄계', '지식인', '노동계', '왕족', '정치계', '무예인']

lists = {
    'nature_list': nature_list,
    'desire_list': desire_list,
    'goal_list': goal_list,
    'body_list': body_list,
    'clothes_list': clothes_list,
    'secret_list': secret_list,
    'person_list': person_list,
    'thing_list': thing_list,
    'living_thing_list': living_thing_list
}


def get_common(props_name, cnt):
    if cnt > 1:
        return sample(lists[props_name], cnt)
    else:
        return choice(lists[props_name])


def get_age_group():
    return f'{choices(range(1, 9), weights=[2, 3, 3, 2, 2, 1, 1, 1])[0]}0대 {choice(scale_list)}'


def get_height():
    return f'1{choices(range(5, 10), weights=[1, 2, 2, 1, 1])[0]}0 {choice(scale_list)}'


def get_origin():
    return choice(origin_list)
