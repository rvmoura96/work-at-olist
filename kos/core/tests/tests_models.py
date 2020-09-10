from django.test import TestCase
import pytest

from core.models import Author


@pytest.mark.django_db
def test_create_and_validate_author_creation():
    author_data = {'name': 'Plato'}
    Author.objects.create(**author_data)
    expected_total_records = 1
    result = Author.objects.count()
    assert expected_total_records == result
