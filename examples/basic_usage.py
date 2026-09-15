from openpromptkit import PromptTemplate


prompt = PromptTemplate(
    """
You are an expert in {{domain}}.

Analyze the following subject:

{{subject}}

Return the answer in this format:

{{format}}
""".strip()
)

result = prompt.render(
    domain="medicine",
    subject="the physiological mechanisms of hypertension",
    format="A concise explanation followed by the main clinical implications.",
)

print(result)
