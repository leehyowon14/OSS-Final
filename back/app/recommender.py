from typing_extensions import TypedDict


class TeamProfile(TypedDict):
    team: str
    city: str
    stadium: str
    image: str
    tags: list[str]
    matches: dict[str, list[str]]


class RecommendationInput(TypedDict):
    region_preference: str
    main_attraction: str
    cheer_style: str
    stadium_preference: str
    risk_preference: str


class TeamRecommendation(TypedDict):
    rank: int
    team: str
    score: int
    city: str
    stadium: str
    image: str
    tags: list[str]
    reasons: list[str]


WEIGHTS: dict[str, int] = {
    "region_preference": 3,
    "main_attraction": 3,
    "cheer_style": 2,
    "stadium_preference": 2,
    "risk_preference": 2,
}


REASON_LABELS: dict[str, str] = {
    "region_preference": "선호 지역",
    "main_attraction": "가장 끌리는 팀 이미지",
    "cheer_style": "응원 스타일",
    "stadium_preference": "구장 선호",
    "risk_preference": "성적 리스크 성향",
}


TEAM_PROFILES: list[TeamProfile] = [
    {
        "team": "엘지 트윈스(LG Twins)",
        "city": "서울",
        "stadium": "잠실야구장",
        "image": "서울 잠실에서 입문하기 좋은 현재 상위권 인기팀",
        "tags": ["서울", "잠실", "현재 상위권", "입문 쉬움"],
        "matches": {
            "region_preference": ["서울", "지역 상관없음"],
            "main_attraction": ["지금 잘하는 팀"],
            "cheer_style": ["수도권에서 편하게 입문", "가족/친구와 직관하기 좋음"],
            "stadium_preference": ["잠실", "야외 구장", "상관없음"],
            "risk_preference": ["상위권 팀이 좋음"],
        },
    },
    {
        "team": "케이티 위즈(KT Wiz)",
        "city": "수원",
        "stadium": "수원 KT 위즈파크",
        "image": "짧은 역사 안에서 우승과 상위권 경쟁을 만든 젊은 강팀",
        "tags": ["경기", "젊은 강팀", "수원", "체계적인 팀"],
        "matches": {
            "region_preference": ["경기/인천", "지역 상관없음"],
            "main_attraction": ["지금 잘하는 팀", "젊고 새로운 팀"],
            "cheer_style": ["가족/친구와 직관하기 좋음"],
            "stadium_preference": ["야외 구장", "상관없음"],
            "risk_preference": ["상위권 팀이 좋음", "중위권이어도 매력 있으면 좋음"],
        },
    },
    {
        "team": "삼성 라이온즈(Samsung Lions)",
        "city": "대구",
        "stadium": "대구 삼성 라이온즈 파크",
        "image": "역사와 전통, 왕조 이미지, 라팍의 뜨거운 응원을 가진 팀",
        "tags": ["역사와 전통", "왕조 이미지", "대구", "압도적인 응원"],
        "matches": {
            "region_preference": ["대구/경북", "지역 상관없음"],
            "main_attraction": ["역사와 전통", "우승 명문 이미지", "뜨거운 응원"],
            "cheer_style": ["압도적인 떼창 응원", "지역 팬덤이 강한 응원"],
            "stadium_preference": ["지역 명물 구장", "야외 구장"],
            "risk_preference": ["상위권 팀이 좋음", "중위권이어도 매력 있으면 좋음"],
        },
    },
    {
        "team": "한화 이글스(Hanwha Eagles)",
        "city": "대전",
        "stadium": "대전 한화생명 볼파크",
        "image": "충청 팬덤, 긴 기다림, 뜨거운 응원, 반등 서사가 강한 팀",
        "tags": ["충청", "뜨거운 응원", "반등 서사", "강한 팬덤"],
        "matches": {
            "region_preference": ["충청", "지역 상관없음"],
            "main_attraction": ["뜨거운 응원", "반등을 기다리는 재미", "지역색 강한 팀"],
            "cheer_style": ["압도적인 떼창 응원", "지역 팬덤이 강한 응원"],
            "stadium_preference": ["신축/현대적 구장", "야외 구장"],
            "risk_preference": [
                "중위권이어도 매력 있으면 좋음",
                "성적 기복도 감수 가능",
            ],
        },
    },
    {
        "team": "기아 타이거즈(KIA Tigers)",
        "city": "광주",
        "stadium": "광주-KIA 챔피언스 필드",
        "image": "최다 우승 명문, 호남 지역색, 강한 팬덤을 가진 팀",
        "tags": ["호남", "우승 명문", "지역색", "강한 팬덤"],
        "matches": {
            "region_preference": ["호남", "지역 상관없음"],
            "main_attraction": ["우승 명문 이미지", "지역색 강한 팀", "뜨거운 응원"],
            "cheer_style": ["지역 팬덤이 강한 응원", "압도적인 떼창 응원"],
            "stadium_preference": ["야외 구장", "지역 명물 구장"],
            "risk_preference": ["상위권 팀이 좋음", "중위권이어도 매력 있으면 좋음"],
        },
    },
    {
        "team": "두산 베어스(Doosan Bears)",
        "city": "서울",
        "stadium": "잠실야구장",
        "image": "잠실 접근성과 과거 왕조 서사가 있는 반등 기대 팀",
        "tags": ["서울", "잠실", "과거 왕조 서사", "반등 기대"],
        "matches": {
            "region_preference": ["서울", "지역 상관없음"],
            "main_attraction": ["반등을 기다리는 재미"],
            "cheer_style": ["수도권에서 편하게 입문", "가족/친구와 직관하기 좋음"],
            "stadium_preference": ["잠실", "야외 구장"],
            "risk_preference": [
                "중위권이어도 매력 있으면 좋음",
                "성적 기복도 감수 가능",
            ],
        },
    },
    {
        "team": "엔씨 다이노스(NC Dinos)",
        "city": "창원",
        "stadium": "창원 NC 파크",
        "image": "젊은 구단, 깔끔한 구장 경험, 새 팬이 들어가기 쉬운 팀",
        "tags": ["창원", "젊은 구단", "분석형", "입문 쉬움"],
        "matches": {
            "region_preference": ["부산/경남", "지역 상관없음"],
            "main_attraction": ["젊고 새로운 팀", "선수 성장/분석 재미"],
            "cheer_style": ["가족/친구와 직관하기 좋음", "조용히 경기 분석"],
            "stadium_preference": ["신축/현대적 구장", "야외 구장"],
            "risk_preference": ["중위권이어도 매력 있으면 좋음"],
        },
    },
    {
        "team": "에스에스지 랜더스(SSG Landers)",
        "city": "인천",
        "stadium": "인천 SSG 랜더스필드",
        "image": "인천 기반, 현대적 브랜딩, 우승 경험이 있는 수도권 서부 팀",
        "tags": ["인천", "수도권 서부", "현대적 브랜딩", "우승 경험"],
        "matches": {
            "region_preference": ["경기/인천", "지역 상관없음"],
            "main_attraction": ["우승 명문 이미지", "지금 잘하는 팀"],
            "cheer_style": ["수도권에서 편하게 입문", "가족/친구와 직관하기 좋음"],
            "stadium_preference": ["야외 구장", "상관없음"],
            "risk_preference": ["중위권이어도 매력 있으면 좋음"],
        },
    },
    {
        "team": "롯데 자이언츠(Lotte Giants)",
        "city": "부산",
        "stadium": "사직야구장",
        "image": "역사와 전통, 부산 지역색, 사직의 압도적인 응원과 낭만",
        "tags": ["역사와 전통", "부산", "사직", "압도적인 응원"],
        "matches": {
            "region_preference": ["부산/경남", "지역 상관없음"],
            "main_attraction": [
                "역사와 전통",
                "뜨거운 응원",
                "지역색 강한 팀",
                "반등을 기다리는 재미",
            ],
            "cheer_style": ["압도적인 떼창 응원", "지역 팬덤이 강한 응원"],
            "stadium_preference": ["지역 명물 구장", "야외 구장"],
            "risk_preference": ["성적 기복도 감수 가능"],
        },
    },
    {
        "team": "키움 히어로즈(Kiwoom Heroes)",
        "city": "서울",
        "stadium": "고척스카이돔",
        "image": "고척돔, 선수 성장, 분석형 팬에게 맞는 리빌딩/언더독 팀",
        "tags": ["서울", "고척돔", "선수 성장", "언더독"],
        "matches": {
            "region_preference": ["서울", "지역 상관없음"],
            "main_attraction": ["선수 성장/분석 재미", "젊고 새로운 팀"],
            "cheer_style": ["조용히 경기 분석"],
            "stadium_preference": ["돔구장"],
            "risk_preference": ["리빌딩/언더독도 좋음", "성적 기복도 감수 가능"],
        },
    },
]


def build_recommendations(
    user_input: RecommendationInput,
    limit: int = 3,
) -> list[TeamRecommendation]:
    total_weight = sum(WEIGHTS.values())
    scored_teams: list[tuple[int, TeamProfile, list[str]]] = []

    for profile in TEAM_PROFILES:
        raw_score = 0
        reasons: list[str] = []

        for field, selected_value in user_input.items():
            matched_values = profile["matches"][field]
            if selected_value in matched_values:
                raw_score += WEIGHTS[field]
                label = REASON_LABELS[field]
                reasons.append(f"{label} '{selected_value}' 항목과 잘 맞습니다.")

        if not reasons:
            reasons.append("입력값과 일부만 맞지만, 비교 후보로 함께 볼 만한 팀입니다.")

        scored_teams.append((raw_score, profile, reasons))

    scored_teams.sort(
        key=lambda item: (
            item[0],
            len(item[1]["matches"]["main_attraction"]),
            item[1]["team"],
        ),
        reverse=True,
    )

    recommendations: list[TeamRecommendation] = []
    for rank, (raw_score, profile, reasons) in enumerate(scored_teams[:limit], start=1):
        score = round(raw_score / total_weight * 100)
        recommendations.append(
            {
                "rank": rank,
                "team": profile["team"],
                "score": score,
                "city": profile["city"],
                "stadium": profile["stadium"],
                "image": profile["image"],
                "tags": profile["tags"],
                "reasons": reasons,
            }
        )

    return recommendations
