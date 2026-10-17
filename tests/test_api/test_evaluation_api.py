﻿﻿﻿"""
RAG 评估 API 测试。

Description:
    测试 RAG 效果评估相关 API 端点。
@version 1.0.0
2026-04-05
"""

from collections.abc import Iterator
from unittest.mock import AsyncMock, MagicMock

import pytest
from fastapi.testclient import TestClient

from main import app
from src.db import get_db


@pytest.fixture
def client() -> TestClient:
    """创建测试客户端。"""
    return TestClient(app)


def _make_fake_session() -> MagicMock:
    """构造满足评估接口调用形状的假数据库会话。"""
    result = MagicMock()
    result.scalar.return_value = 0
    result.scalar_one_or_none.return_value = None
    result.scalars.return_value.all.return_value = []
    result.fetchall.return_value = []
    result.all.return_value = []
    result.first.return_value = None

    session = MagicMock()
    session.execute = AsyncMock(return_value=result)
    session.flush = AsyncMock()
    session.commit = AsyncMock()
    session.rollback = AsyncMock()
    session.refresh = AsyncMock()
    session.add = MagicMock()
    session.delete = AsyncMock()
    session.get = AsyncMock(return_value=None)
    return session


@pytest.fixture(autouse=True)
def override_get_db() -> Iterator[None]:
    """用假会话覆盖 get_db 依赖，避免测试连接真实数据库。

    路由通过 ``Depends(get_db)`` 捕获了函数引用，因此必须使用 FastAPI 的
    ``dependency_overrides`` 机制覆盖，且覆盖对象需与路由导入的是同一个函数对象。
    """
    session = _make_fake_session()

    async def _fake_get_db():
        yield session

    app.dependency_overrides[get_db] = _fake_get_db
    try:
        yield
    finally:
        app.dependency_overrides.pop(get_db, None)


class TestHitRateAPI:
    """命中率 API 测试。"""

    def test_get_hit_rate(self, client: TestClient) -> None:
        """测试获取命中率统计。"""
        response = client.get("/api/v1/evaluation/hit-rate?days=7")

        assert response.status_code == 200
        data = response.json()
        assert data["code"] == 200
        assert "data" in data


class TestComparisonAPI:
    """对比评估 API 测试。"""

    def test_compare_rag_vs_non_rag(self, client: TestClient) -> None:
        """测试 RAG 与非 RAG 对比。"""
        response = client.post(
            "/api/v1/evaluation/compare",
            json={},
        )

        assert response.status_code == 200
        data = response.json()
        assert data["code"] == 200
        assert "rag_stats" in data["data"]
        assert "non_rag_stats" in data["data"]


class TestReportAPI:
    """评估报告 API 测试。"""

    def test_get_report(self, client: TestClient) -> None:
        """测试获取评估报告。"""
        response = client.get("/api/v1/evaluation/report?days=30")

        assert response.status_code == 200
        data = response.json()
        assert data["code"] == 200
        assert "summary" in data["data"]
        assert "recommendations" in data["data"]


class TestOptimizeSuggestionsAPI:
    """优化建议 API 测试。"""

    def test_get_optimize_suggestions(self, client: TestClient) -> None:
        """测试获取优化建议。"""
        response = client.get("/api/v1/evaluation/optimize-suggestions")

        assert response.status_code == 200
        data = response.json()
        assert data["code"] == 200
        assert isinstance(data["data"], list)
