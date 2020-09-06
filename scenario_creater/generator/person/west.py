import random
from . import common

last_name_list = [
    '모리스', '브라운', '밀러', '화이트', '마틴', '워커', '스콧', '터너', '콜린', '콕', '페리', '시몬스',
    '그리핀', '러셀', '포드', '힉스', '니콜라스', '호킨스'
]

first_name_list = [
    '다리아', '다린', '에보니', '엘로이', '에밀리', '에스테반', '에스더', '글로리아', '빅토리아', '올리비아',
    '헬리아', '재클린', '제시카', '켈리', '클라우스', '루시아'
]

job_list = [
    ['기사', '기사복'], '정치인', '상인', '부호', ['도둑', '복면'], ['신관', '신관복'], '건달', '여관 주인', '농부'
    , '마법사', '정령사', '암살자', '레인저', '학자', '용병', '귀족', '모험가', '사냥꾼', ['의사', '가운']
]

belonging_list = [
    '없음', '검', '안경', '모노클', '지팡이', '회중시계', '단도', '총', '마약', '상비약', '장신구'
]

color_list = [
    '빨간색', '주황색', '노란색', '초록색', '파란색', '보라색', '검은색', '갈색', '금색', '은색', '남색'
]

common_list = [color_list, common.person_list, common.thing_list, common.living_thing_list]


def get_properties():
    name = f'{random.choice(first_name_list)} {random.choice(last_name_list)}'
    age_group = common.get_age_group()
    nature = common.get_common('nature_list', 3)

    job = random.choice(job_list)
    uniform = ''
    if type(job) == list:
        uniform = job[1]
        job = job[0]

    origin = common.get_origin()
    desire = common.get_common('desire_list', 2)
    goal = common.get_common('goal_list', 1)

    wp_num = random.randint(0, 3)
    weakpoint = random.choice(common_list[wp_num])

    secret = common.get_common('secret_list', 1)

    like_dislike = ''
    for i in range(2):
        num = random.randint(0, 3)
        like_dislike += f'{"호: " if i == 0 else ", 불호: "}{random.choice(common_list[num])}'

    relationship = ''
    for i in range(2):
        relationship += f'{"호: " if i == 0 else ", 불호: "}{random.choice(first_name_list)} {random.choice(last_name_list)}'

    appearance = f'{common.get_height()} / {common.get_common("body_list", 1)} / {random.choice(color_list)} 머리 / {random.choice(color_list)} 눈 / {uniform if uniform != "" else common.get_common("clothes_list", 1)} / 소지품 {random.choice(belonging_list)}'

    return {
        'name': name,
        'age_group': age_group,
        'nature': nature,
        'origin': origin,
        'job': job,
        'desire': desire,
        'goal': goal,
        'weakpoint': weakpoint,
        'secret': secret,
        'like_dislike': like_dislike,
        'relationship': relationship,
        'appearance': appearance
    }
