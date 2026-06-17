from typing import Literal

from fastapi import FastAPI
from pydantic import BaseModel, Field

from app.recommender import RecommendationInput, TeamRecommendation, build_recommendations


RegionPreference = Literal[
    "서울",
    "경기/인천",
    "충청",
    "호남",
    "대구/경북",
    "부산/경남",
    "지역 상관없음",
]
MainAttraction = Literal[
    "지금 잘하는 팀",
    "역사와 전통",
    "우승 명문 이미지",
    "뜨거운 응원",
    "지역색 강한 팀",
    "반등을 기다리는 재미",
    "젊고 새로운 팀",
    "선수 성장/분석 재미",
]
CheerStyle = Literal[
    "압도적인 떼창 응원",
    "지역 팬덤이 강한 응원",
    "수도권에서 편하게 입문",
    "조용히 경기 분석",
    "가족/친구와 직관하기 좋음",
]
StadiumPreference = Literal[
    "잠실",
    "돔구장",
    "신축/현대적 구장",
    "지역 명물 구장",
    "야외 구장",
    "상관없음",
]
RiskPreference = Literal[
    "상위권 팀이 좋음",
    "중위권이어도 매력 있으면 좋음",
    "성적 기복도 감수 가능",
    "리빌딩/언더독도 좋음",
]


class RecommendationRequest(BaseModel):
    region_preference: RegionPreference = Field(description="선호 지역")
    main_attraction: MainAttraction = Field(description="가장 끌리는 팀 이미지")
    cheer_style: CheerStyle = Field(description="응원 스타일")
    stadium_preference: StadiumPreference = Field(description="구장 선호")
    risk_preference: RiskPreference = Field(description="성적 리스크 성향")

    def to_recommendation_input(self) -> RecommendationInput:
        return {
            "region_preference": self.region_preference,
            "main_attraction": self.main_attraction,
            "cheer_style": self.cheer_style,
            "stadium_preference": self.stadium_preference,
            "risk_preference": self.risk_preference,
        }


class RecommendationResponse(BaseModel):
    top_team: str
    summary: str
    recommendations: list[TeamRecommendation]
    scoring_note: str


app = FastAPI(
    title="KBO Team Finder API",
    description="사용자 취향을 바탕으로 KBO 입덕팀을 추천하는 FastAPI 백엔드",
)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "service": "kbo-team-finder-back"}


@app.post("/recommend", response_model=RecommendationResponse)
def recommend_team(request: RecommendationRequest) -> RecommendationResponse:
    recommendations = build_recommendations(request.to_recommendation_input())
    top = recommendations[0]
    return RecommendationResponse(
        top_team=top["team"],
        summary=top["image"],
        recommendations=recommendations,
        scoring_note="입력 항목과 팀별 이미지 태그의 일치 여부에 가중치를 적용했습니다.",
    )

