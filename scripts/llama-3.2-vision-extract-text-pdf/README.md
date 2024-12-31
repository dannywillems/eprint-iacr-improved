# Extract text from PDF using llama3.2-vision

This Python script attempts to extract Markdown from a PDF by first
transforming the PDF into images that can be read later by llama3.2-vision.
We do convert first PDF into images instead of reading the text of the PDF to
handle in a better way math equations.

The endgoal is to have a corresponding Markdown version of the paper to be able
to extract information in a more efficient way.

## Setup

First install ollama:

```
curl -fsSL https://ollama.com/install.sh | sh
```

and pull llama3.2-vision:

```
ollama pull llama3.2-vision
```

Install the python library ollama:

```
pip install ollama
```

## Run on an example

The original PlonK paper will be used as an example:

```
wget https://eprint.iacr.org/2019/953.pdf
pdftoppm -png 953.pdf 953
```

## Run the script

