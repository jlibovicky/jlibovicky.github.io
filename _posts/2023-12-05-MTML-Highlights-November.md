---
layout: post
title: "Highlights from Machine Translation and Multilinguality in November 2023"
tags: [mtml-highlights, en]
lang: en
---

Here are a couple of articles that caught my attention in November.

### [Narrowing the Gap between Zero- and Few-shot Machine Translation by Matching Styles](https://arxiv.org/abs/2311.02310v1)

A team from Johns Hopkins University published a pre-print that belongs to the
currently trendy genre: stuff we can do with LLMs. This time, it is about how
to use it efficiently for domain-specific machine translation. It is known that
few-shot prompting works much better than zero-shot prompting, but you need to
select proper parallel examples. In other words, you need an in-domain parallel
corpus for domain-specific translation. This paper says that the LLMs already
know how to translate; they only need a hint of style or domain, which can be
monolingual, so no parallel data is required. They propose to do the
translation in two steps: first, they do the usual zero-shot translation. In
the second step, they retrieve similar monolingual sentences in the target
language and add them to the prompt. The results are very similar to doing
few-shot prompts with actual parallel sentences. This supports the author's
hypothesis that the main thing in few-shot prompting for MT is not the
translation but explaining the domain in the target language.

### [There's no Data Like Better Data: Using QE Metrics for MT Data Filtering](https://arxiv.org/abs/2311.05350v1)

Folks from Google show that machine translation quality estimation metrics have
reached such a level that they can be used for training data filtering. They
show promising results in translation between English and German, Japanese and
Chinese, where they can reduce the required training data to one-half only by
selecting suitable training examples.

### [Investigating Multi-Pivot Ensembling with Massively Multilingual Machine Translation Models](https://arxiv.org/abs/2311.07439v1)

Folks from Zurich (University of Zurich and EPFL) explored the ensembling of
differently pivoted translation with multilingual translation models. Pivoted
translation means that instead of translating directly from the source language
to the target language, we first translate from the source language to a pivot
language and then from the pivot language to the target language. For languages
that do not have much direct parallel data, pivoting is usually the best
choice. They do not have to be low-resource languages; for instance, both Czech
and Korean are relatively high-resource languages and have plenty of parallel
data with English, but there is only little direct parallel data. With
multilingual models, we can use multiple languages for pivoting and then
ensemble the translators from the pivot languages to the target language. I
would assume it would help against hallucinated generations; however, the paper
shows that it is untrue. Multilingual models are surprisingly consistent in
hallucination. The remedy is surprisingly simple: do not average the model
outputs, but always take the most confident prediction.

### [To Translate or Not to Translate: A Systematic Investigation of Translation-Based Cross-Lingual Transfer to Low-Resource Languages](https://arxiv.org/abs/2311.09404v1)

Folks from Würzburg empirically compare approaches to cross-lingual model
transfer. First, they compare zero-shot transfer with the translate train and
translate test approaches. They do natural language inference in native
American languages, sentiment classification in East Asian languages, and named
entity recognition in African languages. They claim the winner is the
translate-train approach while keeping the original source language. It is also
the best approach if the MT system does not cover the language of interest (in
that case, they assume it is the most related language for MT). This is a bit
unfair for the translate-test method because it does not consider the
possibility of using additional training data only available in the target
language, which is, in my opinion, the biggest advantage.
