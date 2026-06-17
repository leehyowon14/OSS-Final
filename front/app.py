import os
from typing import Any

import requests  # type: ignore[import-untyped]
import streamlit as st


API_BASE_URL = os.getenv("API_BASE_URL", "http://localhost:8000")


REGION_OPTIONS = [
    "서울",
    "경기/인천",
    "충청",
    "호남",
    "대구/경북",
    "부산/경남",
    "지역 상관없음",
]
MAIN_ATTRACTION_OPTIONS = [
    "지금 잘하는 팀",
    "역사와 전통",
    "우승 명문 이미지",
    "뜨거운 응원",
    "지역색 강한 팀",
    "반등을 기다리는 재미",
    "젊고 새로운 팀",
    "선수 성장/분석 재미",
]
CHEER_STYLE_OPTIONS = [
    "압도적인 떼창 응원",
    "지역 팬덤이 강한 응원",
    "수도권에서 편하게 입문",
    "조용히 경기 분석",
    "가족/친구와 직관하기 좋음",
]
STADIUM_OPTIONS = [
    "잠실",
    "돔구장",
    "신축/현대적 구장",
    "지역 명물 구장",
    "야외 구장",
    "상관없음",
]
RISK_OPTIONS = [
    "상위권 팀이 좋음",
    "중위권이어도 매력 있으면 좋음",
    "성적 기복도 감수 가능",
    "리빌딩/언더독도 좋음",
]


def request_recommendation(payload: dict[str, str]) -> dict[str, Any]:
    response = requests.post(
        f"{API_BASE_URL}/recommend",
        json=payload,
        timeout=5,
    )
    response.raise_for_status()
    data: dict[str, Any] = response.json()
    return data


def render_result_card(recommendation: dict[str, Any]) -> None:
    rank = recommendation["rank"]
    team = recommendation["team"]
    score = recommendation["score"]
    city = recommendation["city"]
    stadium = recommendation["stadium"]
    image = recommendation["image"]
    tags = recommendation["tags"]
    reasons = recommendation["reasons"]

    tag_html = "".join(f"<span>{tag}</span>" for tag in tags)
    reasons_html = "".join(f"<li>{reason}</li>" for reason in reasons)

    st.markdown(
        f"""
        <section class="result-card rank-{rank}">
            <div class="result-header">
                <div class="rank-badge">{rank}위</div>
                <div>
                    <h3>{team}</h3>
                    <p>{image}</p>
                </div>
                <strong class="score">{score}<small>/100</small></strong>
            </div>
            <div class="tags">{tag_html}</div>
            <div class="meta-grid">
                <div><b>연고지</b><br>{city}</div>
                <div><b>홈구장</b><br>{stadium}</div>
            </div>
            <ul class="reasons">{reasons_html}</ul>
        </section>
        """,
        unsafe_allow_html=True,
    )


st.set_page_config(
    page_title="KBO Team Finder",
    page_icon="KBO",
    layout="wide",
)

st.markdown(
    """
    <style>
    .block-container {
        padding-top: 2rem;
        max-width: 1180px;
    }
    h1, h2, h3 {
        color: #10213f;
        letter-spacing: 0;
    }
    .app-subtitle {
        margin-top: -0.75rem;
        color: #536071;
        font-size: 1.05rem;
    }
    .result-card {
        border: 1px solid #d6dfeb;
        border-radius: 8px;
        padding: 1rem;
        margin-bottom: 0.9rem;
        background: #ffffff;
        box-shadow: 0 1px 8px rgba(15, 32, 64, 0.06);
    }
    .rank-1 {
        border-color: #184c96;
        box-shadow: 0 2px 12px rgba(24, 76, 150, 0.12);
    }
    .result-header {
        display: grid;
        grid-template-columns: auto 1fr auto;
        gap: 0.85rem;
        align-items: start;
    }
    .rank-badge {
        min-width: 44px;
        text-align: center;
        border-radius: 6px;
        padding: 0.35rem 0.45rem;
        background: #123f7a;
        color: #ffffff;
        font-weight: 800;
    }
    .result-card h3 {
        margin: 0;
        font-size: 1.2rem;
    }
    .result-card p {
        margin: 0.15rem 0 0;
        color: #56657a;
    }
    .score {
        color: #123f7a;
        font-size: 1.6rem;
        line-height: 1;
        white-space: nowrap;
    }
    .score small {
        font-size: 0.8rem;
        color: #67758a;
        margin-left: 0.1rem;
    }
    .tags {
        margin: 0.8rem 0;
    }
    .tags span {
        display: inline-block;
        border: 1px solid #cad6e6;
        border-radius: 6px;
        padding: 0.22rem 0.45rem;
        margin: 0 0.35rem 0.35rem 0;
        color: #1d4d86;
        background: #f2f7ff;
        font-size: 0.86rem;
    }
    .meta-grid {
        display: grid;
        grid-template-columns: repeat(2, minmax(0, 1fr));
        gap: 0.7rem;
        margin: 0.5rem 0;
    }
    .meta-grid div {
        border-left: 3px solid #d62032;
        padding-left: 0.6rem;
        color: #334155;
    }
    .reasons {
        margin-bottom: 0;
        color: #263548;
    }
    .stButton > button {
        width: 100%;
        border-radius: 8px;
        border: 1px solid #d62032;
        background: #d62032;
        color: white;
        font-weight: 700;
    }
    .stButton > button:hover {
        border-color: #b81425;
        background: #b81425;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("KBO Team Finder")
st.markdown(
    "<p class='app-subtitle'>나에게 맞는 KBO 입덕팀 추천</p>",
    unsafe_allow_html=True,
)

left, right = st.columns([0.9, 1.35], gap="large")

with left:
    st.subheader("나의 취향 입력")

    region_preference = st.selectbox("지역 선호", REGION_OPTIONS, index=4)
    main_attraction = st.selectbox("가장 끌리는 팀 이미지", MAIN_ATTRACTION_OPTIONS, index=1)
    cheer_style = st.radio("응원 스타일", CHEER_STYLE_OPTIONS, index=0)
    stadium_preference = st.selectbox("구장 선호", STADIUM_OPTIONS, index=3)
    risk_preference = st.radio("성적 리스크 성향", RISK_OPTIONS, index=0)

    payload = {
        "region_preference": region_preference,
        "main_attraction": main_attraction,
        "cheer_style": cheer_style,
        "stadium_preference": stadium_preference,
        "risk_preference": risk_preference,
    }

    recommend_clicked = st.button("추천받기", type="primary")

with right:
    st.subheader("추천 결과")

    if recommend_clicked:
        try:
            result = request_recommendation(payload)
            st.session_state["last_result"] = result
        except requests.RequestException as exc:
            st.error(f"FastAPI 추천 요청에 실패했습니다: {exc}")

    result_data = st.session_state.get("last_result")
    if result_data is None:
        st.info("왼쪽에서 취향을 선택하고 추천받기 버튼을 눌러주세요.")
    else:
        st.success(f"가장 잘 맞는 팀: {result_data['top_team']}")
        st.caption(result_data["scoring_note"])

        for item in result_data["recommendations"]:
            render_result_card(item)

        with st.expander("FastAPI 응답 JSON 확인", expanded=True):
            st.json(result_data)
