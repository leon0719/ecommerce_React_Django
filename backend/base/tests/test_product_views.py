from django import urls
import pytest


@pytest.mark.parametrize(
    "param",
    [
        ("products"),  # 測試獲取所有產品的路由
    ],
)
@pytest.mark.django_db
def test_product_views(client, param):
    url = urls.reverse("products")  # 獲取獲取所有產品的 URL
    assert client.get(url).status_code == 200
