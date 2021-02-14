---
layout: post
title: "Machine Translation Weekly 68: Pre-editing of MT inputs"
tags: [mt-weekly, en]
lang: en
---

Today, I am going to comment on a paper that systematically explores something
that probably many MT users do this is pre-editing (editing the source
sentence) to get a better output of an MT that is treated as a black box. The
title of the paper is [Understanding Pre-Editing for Black-Box Neural Machine
Translation](https://arxiv.org/abs/2102.02955) by authors from Nagoya
University and NICT in Japan and will appear at this year's EACL.

Pre-editing is something I often do when I use automatic translation from
English to German. With my level of German, it is often easier for me to use
automatic translation than writing directly in German. On the other hand, I do
understand the target sentences to some extent, so I often search for a better
formulation by alternating the English source. (And then I usually post-edit
the German target anyway.)

The paper presents a user study where the users were instructed to do exactly
this sort of pre-editing – and to keep editing the source until there were
satisfied with the quality of the output. (Which means that the user must have
been speakers of both the source and the target language.) The collected user
edits are thoroughly analyzed in the paper. The wishful thinking of the authors
was probably finding some systematic patterns that could be used in automatic
pre-editing of the inputs or perhaps for pre-processing of the training data.
That did not really work out, but the findings are still pretty interesting.

In all cases, the users succeeded to get a target sentence that they considered
to be of satisfactory quality. However, the edits that they made are sort of
unintuitive. One would expect that the pre-edited sentences would be shorter
and structurally simpler (here measured by the presence of long distant
dependencies, and how deeply nested expressions are in the sentences), but it
did not appear to be the case. The pre-edited sentences that led to the best
translations were in fact on average longer and structurally more complex than
the original ones. The most frequent successful edits were replacing words with
synonyms and changing the content of the source sentence slightly. This is
actually the only really systematic pattern observed: using words that are in
general more frequent leads to better translations. Another very frequent type
of edits was changing punctuation or orthography (in Japanese), which is
according to me a rather sad message about the inconsistency of current neural
machine translation systems.

In the end, it this inconsistency or unpredictability of the systems that make
developing reasonable tips for human pre-editing or an automatic pre-editing
procedure virtually impossible. Thinking of which: finetuning an existing
system to get rid of this property might a good thesis topic.
