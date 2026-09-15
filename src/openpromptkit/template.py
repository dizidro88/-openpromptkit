"""Prompt template utilities."""

from dataclasses import dataclass
import re


_VARIABLE_PATTERN = re.compile(
    r"\{\{\s*([a-zA-Z_][a-zA-Z0-9_]*)\s*\}\}"
)


@dataclass(frozen=True)
class PromptTemplate:
    """A reusable prompt template with named variables."""

    template: str

    def __post_init__(self) -> None:
        """Validate the template when it is created."""
        if not self.template.strip():
            raise ValueError("Template cannot be empty.")

        self.validate()

    @property
    def variables(self) -> tuple[str, ...]:
        """Return the unique variables required by the template."""
        return tuple(dict.fromkeys(_VARIABLE_PATTERN.findall(self.template)))

    def validate(self) -> None:
        """Validate the template structure."""
        if "{{" in self.template or "}}" in self.template:
            matches = list(_VARIABLE_PATTERN.finditer(self.template))

            for match in matches:
                variable = match.group(1)

                if not variable:
                    raise ValueError("Template contains an empty variable.")

            cleaned = _VARIABLE_PATTERN.sub("", self.template)

            if "{{" in cleaned or "}}" in cleaned:
                raise ValueError("Template contains a malformed variable.")

    def render(self, **values: str) -> str:
        """Render the template using the supplied variable values."""
        missing = [name for name in self.variables if name not in values]

        if missing:
            raise ValueError(
                f"Missing template variables: {', '.join(missing)}"
            )

        return _VARIABLE_PATTERN.sub(
            lambda match: str(values[match.group(1)]),
            self.template,
        )
