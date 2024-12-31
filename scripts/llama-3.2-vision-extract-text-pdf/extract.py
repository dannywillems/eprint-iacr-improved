from pathlib import Path
from ollama import chat
from ollama import ChatResponse
import sys

filename = Path(sys.argv[1])

# Temperature determines the randomness of the response.
# 0.0 is deterministic.
# 1.0 is the most random possible.
# We always want the same output.
temperature=0.0

prompt = """
I have a PDF document. Please extract the text from the PDF and convert it into Markdown format. Use the following guidelines:
1. Exact text:
    - Extract the text exactly as it appears in the PDF, without summarizing or rephrasing.
2. Markdown Structure:
    - Use Markdown for headings, lists, and text formatting.
    - Format author names, titles, and affiliations with appropriate heading levels (#, ##, ###, etc.).
    - For emphasis, use * for italics and ** for bold text.
3. LaTeX for Mathematical Content:
    - Convert all mathematical symbols, formulas, and equations to LaTeX.
    - Use single $...$ for inline math and $$...$$ or a math code block for block math.
4. Maintain Formatting:
    - Preserve the layout, such as bullet points, numbered lists, and sections.
    - Reproduce section headers, labels, and any special text formatting.
5. Meta Information:
    - Include footnotes, author contact information, and dates as shown in the document.
"""

print("Processing %s" % filename)
response = chat(
        model='llama3.2-vision',
        messages=[{
            'role': 'user',
            'content': prompt,
            'images': [filename],
            'temperature': temperature,
        }],
    )

# or access fields directly from the response object
print(response.message.content)
md_filename = "%s.md" % filename.stem
with open(md_filename, "w") as f:
    print("Writing result in %s" % md_filename)
    f.write(response.message.content)

