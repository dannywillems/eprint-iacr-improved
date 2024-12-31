from pathlib import Path
from ollama import chat
from ollama import ChatResponse
import sys

filename = sys.argv[1]

# Temperature determines the randomness of the response.
# 0.0 is deterministic.
# 1.0 is the most random possible.
# We always want the same output.
temperature=0.0

print("Processing %s" % img)
response = chat(model='llama3.2-vision', messages=[
  {
    'role': 'user',
    'content': 'Here is a page of a research paper in cryptography, given as an image extracted from the original PDF. Extract the content into MarkDown, and extract in LaTeX for the equations and mathematical symbols. Keep the exact same content. Do not describe what is in the paper. The paper is splitted in different images, therefore do not add any section.',
    'images': [img],
    'temperature': temperature,
  }],
)

print(response['message']['content'])
# or access fields directly from the response object
print(response.message.content)
md_filename = "%s.md" % img.stem
with open(md_filename, "w") as f:
    print("Writing result in %s" % md_filename)
    f.write(response.message.content)

