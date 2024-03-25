from django import urls
import pytest


@pytest.mark.django_db
def test_product_views(client):
    url = urls.reverse("products")  # 獲取獲取所有產品的 URL
    assert client.get(url).status_code == 200
