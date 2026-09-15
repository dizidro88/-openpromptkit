Getting Started

Installation

Once OpenPromptKit is published, it will be installable with:

pip install openpromptkit

For development, clone the repository and install it locally:

git clone https://github.com/dizidro88/openpromptkit.git
cd openpromptkit
pip install -e .

Install the test dependency:

pip install pytest

Creating a prompt template

from openpromptkit import PromptTemplate
prompt = PromptTemplate(
    "You are an expert in {{domain}}. Analyze {{subject}}."
)

Inspecting variables

Templates expose their required variables:

print(prompt.variables)

Output:

('domain', 'subject')

Rendering a template

Provide values for the variables:

result = prompt.render(
    domain="medicine",
    subject="hypertension",
)

The resulting string can then be passed to an AI model or used by another application.

Missing variables

OpenPromptKit validates required variables before rendering.

For example:

prompt.render(domain="medicine")

will raise a ValueError because subject was not supplied.

Current scope

The initial release focuses on a simple and predictable template abstraction.

Future versions may introduce:

* template validation;
* template composition;
* reusable prompt collections;
* version management;
* workflow definitions;
* additional testing utilities.
