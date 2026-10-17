﻿﻿﻿"""
知识库 API 测试。

Description:
    测试知识库管理相关 API 端点。
@version 1.0.0
2026-04-05
"""

from collections.abc import Iterator
from unittest.mock import AsyncMock, MagicMock

import pytest
from fastapi.testclient import TestClient

from main import app
from src.db import get_db
from src.db.models import KnowledgeDoc


@pytest.fixture
def client() -> TestClient:
    """创建测试客户端。"""
    return TestClient(app)


@pytest.fixture
def mock_session() -> MagicMock:
    """创建模拟数据库会话。"""
    session = MagicMock()
    session.execute = AsyncMock()
    session.flush = AsyncMock()
    session.commit = AsyncMock()
    session.rollback = AsyncMock()
    return session


def _make_fake_session() -> MagicMock:
    """构造满足知识库接口调用形状的假数据库会话。"""
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


class TestKnowledgeDocumentAPI:
    """知识库文档 API 测试。"""

    def test_list_documents(self, client: TestClient) -> None:
        """测试获取文档列表。"""
        response = client.get("/api/v1/knowledge/documents")

        assert response.status_code == 200
        data = response.json()
        assert data["code"] == 200

    def test_get_stats(self, client: TestClient) -> None:
        """测试获取统计信息。"""
        response = client.get("/api/v1/knowledge/stats")

        assert response.status_code == 200
        data = response.json()
        assert data["code"] == 200


class TestKnowledgeSearchAPI:
    """知识库检索 API 测试。"""

    def test_search_knowledge(self, client: TestClient) -> None:
        """测试知识检索。"""
        response = client.post(
            "/api/v1/knowledge/search",
            json={
                "query": "品牌规范",
                "top_k": 5,
            },
        )

        assert response.status_code == 200
        data = response.json()
        assert data["code"] == 200
