---
layout: post
title: "Highlights from Machine Translation and Multilinguality in summer 2023"
tags: [mtml-highlights, en]
lang: en
---

Here are short summaries of the papers I liked the most during the (academic)
summer. Also, this time, I am posting both on GitHub pages and on Medium.

## [mBLIP: Efficient Bootstrapping of Multilingual Vision-LLMs](https://arxiv.org/abs/2307.06930v1)

The preprint from the University of Würzburg presents a recipe for recycling
existing models to create a multilingual vision-language model. They start with
the English-only language model BLIP-2, which allows images to be a part of its
input (the output is always textual). They take the image encoder from this
model and start using it as input to a multilingual model (they experiment with
mT0-XL and mT5-XL) and finetune it to work well with visual inputs. The cool
thing about the method is that because they only train a small part connecting
the visual encoder and LLM (that produces 32 embeddings), most of the backbone
language model can be 8-bit quantized. They evaluate their model on several
tasks, including the IGLUE benchmark (different flavors of visual question
answering and image retrieval) and XM3600 for caption generation and pretty
decent results.

## [SeaEval for Multilingual Foundation Models: From Cross-Lingual Alignment to Cultural Reasoning](https://arxiv.org/abs/2309.04766v1)

A team from A\*STAR and Nanyang University in Singapore collected a benchmark
for multilingual evaluation of large language models. Besides existing
datasets, they created several new ones with questions about local
knowledge in the US, China, and Singapore regions and translated those into
multiple languages. Their evaluations showed that LLaMA 70B Chat is
comparable to ChatGPT in almost all tasks (ChatGPT knows a bit more about
the US), and a relatively smaller Chinese model, Baichuan, matches them in
Chinese, GPT-4 is the best. The most interesting they evaluated in the
paper was cross-lingual consistency, i.e., how often the models answer the
questions in the same way across languages, and the scores are surprisingly
low, with GPT-4 being the best model again. The results suggest that LLMs
tend to represent the languages to some extent separately and that GPT-4
does something differently than the others, but it is hard to say what.

## [MADLAD-400: A Multilingual And Document-Level Large Audited Dataset](https://arxiv.org/abs/2309.04662v1)

Google releases its answer to Meta's NLLB. It is worse both on the WMT
competition test set and Flores 200 datasets but better on the NTREX test set
(an analog to the WMT test sets in 128 languages by Microsoft).

## [ChatGPT MT: Competitive for High- (but not Low-) Resource Languages](https://arxiv.org/abs/2309.07423v1)

Yet another, but this time very systematic, evaluation of ChatGPT for MT from
CMU. They confirm it performs quite poorly for less-resourced and African
languages, much worse than Meta's NLLB (No Language Left Behind). A strong
predictor of the machine translation quality of ChatGPT is the number of
Wikipedia pages in that language.

## [SIB-200: A Simple, Inclusive, and Big Evaluation Dataset for Topic Classification in 200+ Languages and Dialects](https://arxiv.org/abs/2309.07445v1)

Folks from UCL, the University of Toronto, Uni Saarland, and the University of
Ontario created (very cheaply) a dataset for topic classification in 200
languages. They annotated the English part of Flores-200 (a test for machine
translation by Meta for 200 languages) with topic labels and projected it into
the target languages. Not surprisingly, the best baseline is supervised using
based on XLM-R. What was surprising was only a small difference between
supervised learning and zero-shot transfer (from English, French, Chinese, or
Arabic). This small difference makes me wonder to what extent we need the big
contextual models and to what extent the task is solvable, e.g., using aligned
word embeddings only. Asking assistants based on generative models was the
worst method in this case.
