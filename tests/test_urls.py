import pytest
from django.test import Client


@pytest.mark.django_db
def test_form_check(client: Client) -> None:
    """This test ensures that health check is accessible."""
    response = client.get("/form")

    assert response.status_code == 200


def test_admin_unauthorized(client: Client) -> None:
    """This test ensures that admin panel requires auth."""
    response = client.get("/admin/")

    assert response.status_code == 302


def test_admin_authorized(admin_client: Client) -> None:
    """This test ensures that admin panel is accessible."""
    response = admin_client.get("/admin/")

    assert response.status_code == 200
