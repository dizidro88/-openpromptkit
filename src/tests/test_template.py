import pytest

from openpromptkit import PromptTemplate


def test_template_detects_variables():
    prompt = PromptTemplate(
        "You are a {{role}}. Analyze {{subject}}."
    )

    assert prompt.variables == ("role", "subject")


def test_template_renders_values():
    prompt = PromptTemplate(
        "You are a {{role}}. Analyze {{subject}}."
    )

    result = prompt.render(
        role="medical expert",
        subject="hypertension",
    )

    assert result == (
        "You are a medical expert. Analyze hypertension."
    )


def test_template_rejects_missing_variables():
    prompt = PromptTemplate("Analyze {{subject}}.")

    with pytest.raises(ValueError):
        prompt.render()


def test_empty_template_is_rejected():
    with pytest.raises(ValueError):
        PromptTemplate("")


def test_whitespace_only_template_is_rejected():
    with pytest.raises(ValueError):
        PromptTemplate("   ")


def test_malformed_template_is_rejected():
    with pytest.raises(ValueError):
        PromptTemplate("Analyze {{subject.")


def test_duplicate_variables_are_unique():
    prompt = PromptTemplate(
        "{{role}} analyzes {{subject}} as a {{role}}."
    )

    assert prompt.variables == ("role", "subject")
