import openai
def Textinitiator(value):
    openai.api_key = "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"
    data = openai.Completion.create(
    model="text-davinci-003",
    prompt=value,
    max_tokens=2048,
    temperature=0.9
    )
    return data
def ImageInitiator(value):
    openai.api_key = "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"
    data = openai.Image.create(
    prompt=value,
    n=2,
    size="512x512"
    )
    return data