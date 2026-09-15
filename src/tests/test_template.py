import pytest

from openpromptkit.template import PromptTemplate


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
