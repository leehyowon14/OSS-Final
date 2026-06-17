from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_health_returns_ok() -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_recommend_returns_samsung_for_history_and_daegu_input() -> None:
    response = client.post(
        "/recommend",
        json={
            "region_preference": "대구/경북",
            "main_attraction": "역사와 전통",
            "cheer_style": "압도적인 떼창 응원",
            "stadium_preference": "지역 명물 구장",
            "risk_preference": "상위권 팀이 좋음",
        },
    )

    body = response.json()

    assert response.status_code == 200
    assert body["top_team"] == "삼성 라이온즈(Samsung Lions)"
    assert body["recommendations"][0]["score"] == 100
    assert "압도적인 응원" in body["recommendations"][0]["tags"]


def test_recommend_returns_lotte_for_busan_cheer_input() -> None:
    response = client.post(
        "/recommend",
        json={
            "region_preference": "부산/경남",
            "main_attraction": "뜨거운 응원",
            "cheer_style": "지역 팬덤이 강한 응원",
            "stadium_preference": "지역 명물 구장",
            "risk_preference": "성적 기복도 감수 가능",
        },
    )

    body = response.json()

    assert response.status_code == 200
    assert body["top_team"] == "롯데 자이언츠(Lotte Giants)"
    assert len(body["recommendations"]) == 3


def test_recommend_rejects_unknown_choice() -> None:
    response = client.post(
        "/recommend",
        json={
            "region_preference": "서울",
            "main_attraction": "아무 팀",
            "cheer_style": "조용히 경기 분석",
            "stadium_preference": "돔구장",
            "risk_preference": "리빌딩/언더독도 좋음",
        },
    )

    assert response.status_code == 422

