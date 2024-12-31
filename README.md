# eprint-iacr-improved

An attempt to build an improved version of eprint.iacr.org.

Features we want to provide:
- on the paper page, list all the references and check that the links are up-to-date
- transform each paper into a corresponding Markdown file to provide a more
convenient way to copy definitions, lemmas, propositions, etc. This way, we
can provide a database of definitions, proven lemmas/propositions/theorems,
etc. From there, we can try to translate it into a programming language like
Coq or Lean for formal reasoning.
- cross-reference reg. proofs of lemmas/propositions. For instance, if paper X
  mentions that paper Y proved a lemma that paper X uses, provide a check.

