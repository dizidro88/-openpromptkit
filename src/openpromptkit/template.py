"""Prompt template utilities."""

from dataclasses import dataclass
import re


_VARIABLE_PATTERN = re.compile(r"\{\{\s*([a-zA-Z_][a-zA-Z0-9_]*)\s*\}\}")


@dataclass(frozen=True)
class PromptTemplate:
    """A reusable prompt template with named variables."""

    template: str

    @property
    def variables(self) -> tuple[str, ...]:
        """Return the variables required by the template."""
        return tuple(dict.fromkeys(_VARIABLE_PATTERN.findall(self.template)))

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
