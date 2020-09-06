import random
from . import common

last_name_list = [
    '김', '이', '박', '최', '정', '조', '강', '장', '윤', '유', '임', '여'
    , '견', '구', '권', '남', '노', '도', '반s', '방', '배', '서', '석', '성', '소', '신', '심'
    , '안', '양', '엄', '연', '염', '오', '옥', '우', '전', '주', '지', '진', '차', '채', '천'
    , '하', '한', '허', '홍', '황'
]

first_name_list = [
    '가람(강)', '가온(세상의 중심)', '그린(그린 듯, 그리운)', '거늘(출)', '꼬두람이(막내)', '꼬리별(혜성)'
    , '나래(날개)', '나르샤(비상하다)', '나린(하늘이 내린)', '난길(밝고 환한)', '난새(한껏 날아오른 새)', '너비(널리)'
    , '너울(바다의 큰 물결)', '노량(천천히)', '노해(바닷가에 퍼진 들판)', '노고지리(종달새)', '늘찬(늘 옹골찬 아이로 자라라)'
    , '늘해랑(밝고 강한 사람)', '두빛나래(두 개의 빛나는 날개)', '드레(점잖은 무게)', '또바기(언제나 한결같이)'
    , '다소니(사랑하는 사람)', '다소다(애틋하게 사랑하다)', '다흰(세상의 희게 하는 사람)', '다원(모두가 원하는 사람)'
    , '다온(좋은 모든 일들이 다 온다)', '다한(모든 일에 최선을 다하는)', '달보드레(달달하고 부드럽다)'
    , '라온(즐거운)', '로와(슬기로와)', '로운(슬기로운)', '마루(하늘)', '마파람(남풍)', '마루한(으뜸가는 큰 사람)', '마리(으뜸가는 사람)'
    , '매지구름(먹구름)', '맨마루(절정)', '모아(늘 뜻을 모아 사는 삶)', '모은(값진 것을 모은 사람)', '모해(모둥이를 비춰주는 햇빛)'
    , '목새(물결에 밀려 한 곳에 쌓인 보드라운 모래)', '미리내(은하수)', '바오(보기 좋게)', '바림(그라데이션)'
    , '별찌(유성)', '보미(봄에 태어난 아이)', '사나래(천사의 날개)', '산다라(굳세다)', '새라(새롭다)'
    , '새나(새가 나는 것처럼 자유롭게 아름다움)', '새론(늘 새로운 사람)', '소소리바람(차고 음산한 봄바람)'
    , '수피아(숲의 요정)', '숯(신선한 힘)', '아람(탐스러운 가을 햇살을 받아 잘 익어 벌어진 과일)'
    , '아사(아침)', '아스라이(아득히)', '안다로미(그릇에 넘치도록 많이)', '온(100)', '온누리(온세상)', '이든(어진)'
    , '즈믄(1,000)', '파니(하는 일 없이 노는 모양)', '푸실(풀이 우거진 마을)', '하랑(함께 높이 날다)'
    , '한빛(세상을 이끄는 환한 빛)', '한별(크고 밝은 별)', '한울(우주)', '해길(해가 비추는 길을 가듯 평탄하게 살아라)'
    , '해늘(늘 해처럼 밝게)', '해솔(해처럼 밝고 솔처럼 바르게)', '해찬솔(햇빛이 가득 차 더욱 푸른 소나무)'
    , '흰여울(물이 맑고 깨끗한)', '헤움(생각)'
]

birth_month_name_list = [
    '해오름달', '시샘달', '물오름달', '잎새달', '푸른달', '누리달', '비나린달', '타오름달', '열매달', '하늘연달', '미틈달', '매듭달'
]

birth_day_name_list = [
    '하루', '이틀', '사흘', '나흘', '닷새', '엿새', '이레', '여드레', '아흐레'
]

birth_10th_day_name_list = [
    '열흘', '스무날', '서른날'
]

job_list = [
    '정치인', '상인', '부호', ['도둑', '복면'], '건달', '농부', '주막 주인', '도사', '의원', '포졸', '학생'
    , '학자', '귀족', '사냥꾼', '사당패'
]

belonging_list = [
    '없음', '검', '지팡이', '단도', '대마', '약초', '장신구', '활', '삿갓'
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
