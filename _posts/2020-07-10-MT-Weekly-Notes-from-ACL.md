---
layout: post
title: "Machine Translation Weekly 47: Notes from the ACL"
tags: [mt-weekly, en]
lang: en
---

In this extremely long post, I will not focus on one paper as I usually do, but
instead will show my brief, but still infinitely long notes from this year's
ACL. Many people already commented on the virtual format of the conference. I
will spare you of that and rather talk about the content of the conference
including a list of short summaries of papers.

## Focus on Evaluation

Many papers commented on how we evaluate our models and many of those papers
got awarded. This is great news! Evaluation (and especially the BLEU score in
machine translation) was the elephant in the NLP room for a very long time, but
most people just accepted the evaluation practice as rules of the game. (The
game of getting papers accepted.)

I think it has something to with how competitive the field has become in recent
years. The publication record is one of the main factors influencing
researchers' careers, which may result in pressure to publish as much as
possible, not leaving much time to critically reflect not only the evaluation
but also the broader impact of our work.

The new interest for evaluation is probably also connected with the black-box
aspect of the models: with a rule-based or not so complex statistical model,
you know what the model does, there is no need for a specialized dataset that
will tell you that. I totally welcome this trend.

## Research Ethics & Reviewing

I think this conference also showed that the community is not really able to
deal with ethical issues related to NLP research. I will illustrate that on an
example of one paper from the conference, but there several more papers that
might be similarly controversial (yet did not resonate much in my Twitter
bubble).

There was a very passionate discussion on Twitter about a paper on the gender
gap in NLP. The paper shows that authors with first names stereotypically
associated with male gender publish much more frequently and are more
frequently cited. Even more serious issue is that with the growing academic age
of the other (number years from the first publication) this gap is getting
bigger. This is an alarming message to the community showing how non-inclusive
the NLP research community is.

However, the problem with the paper is that the conceptualization of gender
used through the paper and simplifying assumptions made in the paper can
further deepen the stereotypes about people who identify themselves neither as
male nor female. Many people find the conceptualization offensive and harmful,
especially those who were for the sake of statistical analysis assigned gender
they do not identify with without asking for their consent of being part of the
statistics.

<center>
<blockquote class="twitter-tweet"><p lang="en" dir="ltr">NB folx are **not** a variable that you can just throw away for the sake of simplifying your analysis. <br><br>And don&#39;t get me started of gender labeling individual based on their names. <a href="https://twitter.com/hashtag/acl2020nlp?src=hash&amp;ref_src=twsrc%5Etfw">#acl2020nlp</a></p>&mdash; Luca Soldaini 🏳️‍🌈 (@soldni) <a href="https://twitter.com/soldni/status/1280976612746358784?ref_src=twsrc%5Etfw">July 8, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
</center>

The author took responsibility and very positively reacted to the feedback. The
reason this paper was written is obvious that the author is very concerned
about the inclusivity of the research community and the discussion that
followed the paper clearly shows that. In my view, the story has a happy end,
but it reveals the problems the community has.

The paper went through a peer-review at the most prestigious conference in the
field. This discussion should have happened before the paper appeared at the
conference. The peer review process should have ensured that the message of the
paper is published without making any harm. The reviewers are also to blame.

On the other hand, if I were the reviewer, I would probably be overwhelmed by
the alarming message the paper has about the community and (being myself a
non-empathetic ignorant) I probably would not notice the ethical issues unless
someone would tell me. I believe this is the case for many reviewers in the
field which clearly shows that we need to reform how research ethics is
reviewed. There certainly should be some training for the reviewers. Perhaps,
there should be an additional review for research ethics if the reviewers or
the authors ask for that. Maybe the ethical statements should be published
together with the papers.

## Paper overview

What now follows is my brief (subjective and non-representative) notes about
some of the paper that I met at the conference.

[__Learning to Recover from Multi-Modality Errors for Non-Autoregressive Neural
Machine Translation__](https://www.aclweb.org/anthology/2020.acl-main.277/)

* Partially non-autoregressive architecture: generate sector vectors in
  parallel, then generate autoregressive content of several-word segments.
* The model does not really learn end-to-end. They observe it makes errors and
  modifies training data to simulate the errors.
* I think semi-autoregressive methods are a good future direction, but I always
  imagined it the other way round: generate and few tokens in parallel and
  process them.

[__Modeling Word Formation in English–German Neural Machine
Translation__](https://www.aclweb.org/anthology/2020.acl-main.389/)

* Morphologically motivated segmentation that captures word-formation works
  better than BPE.
* For me, the paper brings arguments for further investigating character-level
  methods that learn their own segmentation, frequency-based heuristics such as
  BPE miss a lot.

[__Climbing towards NLU: On Meaning, Form, and Understanding in the Age of
Data__](https://www.aclweb.org/anthology/2020.acl-main.463/)

* Claim BERT-like models cannot learn meaning from forms only, because there is
  no intention and interaction in the training data. Without intention, there
  is no communication.
* We find responses of GPT-2 and similar meaningful because it is us who
  project meaning in the sentences.
* Pragmatic counter-argument: How can I know that all other people are not just
  GPT-7s and it is me projecting the meaning into what they say? Word forms can
  be observed. Behavior can be observed. Can we observe other intentions?

[__Character-Level Translation with
Self-attention__](https://www.aclweb.org/anthology/2020.acl-main.145)

* Adding CNNs in Transformer blocks narrows to the gap between character-level
  and word-level, but still worse than subwords.

[__End-to-End Neural Word Alignment Outperforms GIZA++__](https://www.aclweb.org/anthology/2020.acl-main.146)

* Attention does not do word alignment very well, we all know that. This paper
  adds a specialized mechanism to work more like alignment (directly uses
  encoder states; forces the alignment matrix to be more contiguous).
* The resulting model translates and generates high-quality alignment at the
  same time, even better than GIZA++.
* I hoped for more explainability of model decisions via alignment. Here, the
  alignment is not an explanation for the generation, but rather an auxiliary
  task parallel to translation.

[__Content Word Aware Neural Machine
Translation__](https://www.aclweb.org/anthology/2020.acl-main.34)

* Distinguish content and non-content words using TF-IDF. Two ways of
  incorporating into MT: separate content word encoder, auxiliary loss in the
  decoder.
* Both seem to get small, but significant improvements in MT quality.
* My takeaway: Transformers do not really know what words are more important
  for sentence meaning. How could they if XENT loss treats all words equally.

[__Language-aware Interlingua for Multilingual Neural Machine
Translation__](https://www.aclweb.org/anthology/2020.acl-main.150)

* Fellow researchers, please do not use word interlingua!
* If someone told me: take what is out there and try to make a single system
  for all languages, this is what I would do (language embedding, translate in
      both directions, autoencoding, force similar encoder representation). I
      am glad I do not have to do it myself and can just have a look at the
      results.
* Pivoting is better than zero-shot! The same was with the [Improving Massively
  Multilingual Neural Machine Translation and Zero-Shot
  Translation](https://www.aclweb.org/anthology/2020.acl-main.148/).

[__Tagged Back-translation Revisited: Why Does It Really
Work?__](https://www.aclweb.org/anthology/2020.acl-main.532)

* A nice empirical analysis that shows that tagged back-translation help
  translating natural sentences.
* Adding the back-translation tag at inference times helps to translate
  translationeese.

[__Language (Technology) is Power: A Critical Survey of "Bias" in NLP__](https://www.aclweb.org/anthology/2020.acl-main.485/)

* Critical is a reference to the [Frankfurt
  School](https://en.wikipedia.org/wiki/Frankfurt_School) in
  philosophy/sociology, it does mean criticizing.
* Main message: NLP literature about bias often comes from an ivory tower, does
  not reflect how social hierarchies are reflected in the language (and how
  language is inherently structured to reinforce existing power hierarchies).
* Removing bias is often taken abstractly without taking into consideration
  those whom the technology might harm, and what the harm is.
* Implicitly claim that fairness is inherently normative and you cannot propose
  methods for mitigation bias without admitting what your normativity (i.e.,
  your ideology) is. I am not sure if it is true, I would rather say, there can
  be agnostic debiasing methods and you can make normative decisions afterward.

[__Towards Transparent and Explainable Attention
Models__](https://www.aclweb.org/anthology/2020.acl-main.387)

* In the beginning, there is an observation that attention does not work as an
  explanation if the state that it attends are too similar to each other (you
  can then permute the distribution and nothing changes).
* Introducing a loss that enforces dissimilarity among the states almost does
  not harm the performance and helps the attention to provide an explanation.

[__On Exposure Bias, Hallucination and Domain Shift in Neural Machine
Translation__](https://www.aclweb.org/anthology/2020.acl-main.326)

* MT models often react to a domain shift by hallucinating fluent but unrelated
  content.
* Exposure bias is partially responsible: minimum risk training can help.
* Beam search size matters! The larger the beam, the more hallucination. That
  confirms what [Felix Stahlberg and Bill
  Byrne](https://www.aclweb.org/anthology/D19-1331) showed that there is
  something wrong in the way we think we model the sequence probabilities (see
  [MT Weekly 20](2019/11/21/MT-Weekly-Search-and-Model-Errors.html)).

[__On the Linguistic Representational Power of Neural Machine Translation
Models__](https://www.mitpressjournals.org/doi/full/10.1162/COLI_a_00367).

* Morphology on lower layers, syntax, and semantics on higher layers.
* Granularity: character-level systems are much more aware of morphology,
  subwords are better for syntax and semantics
* They say character-models are better for Czech-English translation; this is
  opposite to what I found.

[__Returning the N to NLP: Towards Contextually Personalized Classification
Models__](https://www.aclweb.org/anthology/2020.acl-main.700)

* The paper promotes the idea that all NLP tasks should be personalized, it
  should make the NLP systems supposedly more natural and provide a better user
  experience.
* I totally disagree, personalization means collecting private data or
  customization based on stereotypes.
* Research in this area would only support the myth that AI needs personal data
  and companies need our personal data, so we are part of the technological
  progress. This is how we make ourselves colonized by data.
* The paper phrase the best interest of companies as a research program. This
  is probably one of the papers that would deserve a special review for ethics.

[__Tabula nearly Rasa: Probing the linguistic knowledge of character-level neural
language models trained on unsegmented text__](https://www.mitpressjournals.org/doi/full/10.1162/tacl_a_00283)

* Discovering what words are is a big challenge in human language acquisition,
  but in NLP, the models do not have to deal with it, inputs are already
  tokenized.
* They trained character-level LSTM NN and measured what it captures compared
  to word-level: POS tagging worse, lexical semantics worse, grammatical
  agreements approx the same.
* There are neurons that highly correlate with word boundaries.

[__Toward Gender-Inclusive Coreference
Resolution__](https://www.aclweb.org/anthology/2020.acl-main.418)

* Introduce the dataset for coreference resolution in English with all gendered
  stuff removed. The question is: can coreference resolution work without
  gender stereotypes?
* It is an interesting toy problem but does not open really interesting
  research directions. With a gender-free dataset, you can of course learn a
  gender-free model? But what would you do in language with grammatical gender
  that cannot be as easily separated from sociological gender (without e.g.,
  changing gendered declination paradigms)?
* The truly unbiased coreference resolution should be able to learn not to
  stereotype even while having gendered data.

[__Translationese as a Language in "Multilingual"
NMT__](https://www.aclweb.org/anthology/2020.acl-main.691)

* Unsupervised classifier for telling for a translation pair if the sentence is
  original in the language or translationese. Use that to tag training data.
* Pose MT as zero-shot setup and compare modes: original to translationese,
  original-to-original. Human raters preferred the later one both in terms of
  accuracy and fluency.
* BLEU scores on source-original data tell the opposite of human judgment.
* This shows a serious problem for the behaviorist paradigm in MT: what do we
  want to do if we do not want to simulate how people translate?

[__Parallel Sentence Mining by Constrained
Decoding__](https://www.aclweb.org/anthology/2020.acl-main.152)

* Totally elegant: Build trie of target sentences, for each source sentence
  trie to force-decode the entire trie and prune, during the decoding, so you
  end up with the most probable sentence.

[__ENGINE: Energy-Based Inference Networks for Non-Autoregressive Machine
Translation__](https://www.aclweb.org/anthology/2020.acl-main.251)

* I think a more suitable title for the paper would be: more clever knowledge
  distillation for non-autoregressive models using directly an autoregressive
  teacher model.
* The non-autoregressive model is trained to produce tokens that are probable
  under a trained autoregressive model.
* It is actually more knowledge distillation that what is normally called
  knowledge distillation in NAR MT.

[__Learning and Evaluating Emotion Lexicons for 91
Languages__](https://www.aclweb.org/anthology/2020.acl-main.112)

* Translate + classifier and that its. I am not sure if I am disappointed or
  pleasantly surprised. I would expect that cultural differences would make
  such a direct approach impossible.
* Is this paper projecting American values to the entire world? This is another
  paper that would deserve a thorough review of research ethics.

[__On The Evaluation of Machine Translation SystemsTrained With
Back-Translation__](https://www.aclweb.org/anthology/2020.acl-main.253)

* Another paper with a different method, but similar conclusions about
  back-translation. In terms of BLEU score back-translation helps a lot in the
  reverse translation direction (the unrealistic one), but not in the direct
  direction. In human evaluation, back-translation helps in both directions,
  but less in the reverse one.

[__On the Limitations of Cross-lingual Encoders as Exposed by Reference-Free
Machine Translation
Evaluation__](https://www.aclweb.org/anthology/2020.acl-main.151)

* A combination of alignment scores from pre-trained representation and
  language modeling is a good QE metric. Is this a chance for unsupervised MT?

[__Beyond Accuracy: Behavioral Testing of NLP Models with
CheckList__](https://www.aclweb.org/anthology/2020.acl-main.442)

* A well-deserved best paper.
* We all know it, but it is always helpful to remind over and over again.
  Aggregated accuracy hides how buggy our models are, we know structured test
  sets that would tell us more. This paper shows a software engineering like
  methodology to do so.

[__The Unreasonable Volatility of Neural Machine Translation
Models__](https://www.aclweb.org/anthology/2020.ngt-1.10)

* Minor changes in input cause major changes in the output. E.g., changing a number in
  the input which should only cause the same minor change in the output.
