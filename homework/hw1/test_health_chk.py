import pytest
import requests


class TestRoutesHealthCheck:

    @pytest.mark.smoke
    @pytest.mark.parametrize("url", open("urls.txt").readlines())
    def test_health_check(self, url):
        response = requests.session().get(url.strip())          # Делаем запрос по указанному url
        assert response.status_code == 200                      # Проверяем успешную загрузку страницы
        assert response.url.startswith("https://")              # Проверяем использование HTTPS
        assert response.elapsed.total_seconds() < 5             # Проверяем время ответа на запрос
        assert "text/html" in response.headers['Content-Type']  # Проверяем на наличие нужных заголовков в ответе