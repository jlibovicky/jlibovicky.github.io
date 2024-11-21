---
layout: post
title: "Notes from EMNLP 2024"
tags: [en]
lang: en
---

Last week, I was at EMNLP in Miami, and here are a few notes about what I saw at the conference.

## Keynotes

The conference had three keynotes: two good and one amazing.

In the first keynote, Percy Liang talked about research on LLMs that they do at Stanford. One topic was LLM-based agents: Percy Liang predicts that LLMs are awaiting their AlphaGo moment so that we will move from coded agents; soon, the big topic will be agents trained with reinforcement learning, in other words, small black boxes operating over big black boxes. I am not completely sure about this.

The second keynote by Anca Dragan discussed reinforcement learning. As always, when talking about reinforcement learning, we saw examples of learning bad objectives that were exploited by the algorithms. An interesting point was 

The third keynote delivered by Tom Griffiths was about Bayesian thinking about LLMs. Initially, I worried about the understandability of the talk because Bayesian typically means plenty of complicated math that I have a hard time understanding, but the talk was excellent. One nice result that he showed in the keynote was that some of the reasoning errors of LLMs (famous example: preferring "A" in multiple-choice QA or being able to decipher substitution ciphers only with popular shifts) can be explained by a high prior from the training data:

$$P(\text{answer}|\text{query}) \propto P(\text{query}|\text{answer})\cdot P(\text{answer}) $$

Compensation for the prior probability of the answer may help. These results might seem trivial at first glance, but what shows is that in many cases (when we accepted the popular approach that LLMs the way of doing intelligence, whatever it is), we do not want the LLM to model what is probable in the language. We want it just to do some reasoning. This decomposition might, in turn, show that we sort of have to choose either model language or intelligence, which might suggest that LLMs are not the way to AGI (not that I ever thought they were).

## Conference papers

On the first day, there were several papers without much empirical content but with interesting ideas.

* [**Pragmatic Norms Are All You Need – Why The Symbol Grounding Problem Does Not Apply to LLMs.**](https://aclanthology.org/2024.emnlp-main.651) Yet another paper that debunks the famous Octopus thought experiment by Bender and Koller (2020). The paper attacks mostly how meaning is defined in the original paper: Even though the octopus paper defines the meaning via intention, the analysis in this paper argues that the underlying assumption is a simple correspondence theory of meaning, which has been criticized many times and better theories exist.
* [**How to Compute the Probability of a Word.**](https://aclanthology.org/2024.emnlp-main.1020) Linguists often need to estimate word probability (e.g. to estimate reading times based on suprisal). With subword-based language models, it is not straightforward and this paper comes with some probability tricks to compensate for that.
* [**Towards similarity-aware Surprisal Theory.**](https://aclanthology.org/2024.emnlp-main.921.pdf) This paper tackles an everlasting problem with neural networks and NLP: in the very last layer, we assume that all vocabulary units are conditionally independent (given the context), which is simply not true because words can have a similar meaning. This paper tries to compensate for this by including a similarity term in surprisal computation and, in turn, gets a better estimation of human reading times.

I was pretty surprised at how many NLP tasks people work on. I remember when most papers concerned core NLP tasks like tagging, parsing, or named entity recognition. Now, plenty of tasks, including unusual ones like fairy tale generation, pedagogical assistants, doing math, fact-checking, etc. Also, retrieval augmented generation was a very popular technique. Often, it seemed to me that from the technical perspective, people did pretty much straightforward things. However, because I have almost zero knowledge about many of the tasks, it was still pretty interesting.

And here is my biased and, to some extent, a random selection of what was, for me, the outstanding papers:

* [**MMTE: Corpus and Metrics for Evaluating Machine Translation Quality of Metaphorical Language.**](https://aclanthology.org/2024.emnlp-main.634) A challenge set for translating metaphors from English to Italian and Chinese.
* [**TEMA: Token Embeddings Mapping for Enriching Low-Resource Language Models.**](https://aclanthology.org/2024.emnlp-main.638) In this paper, they improve BERT-like model in less-resourced languages by giving it transformed embedding mapped token embeddings from better-resourced languages.
* [**The Potential and Challenges of Evaluating Attitudes, Opinions, and Values in Large Language Models.**](https://aclanthology.org/2024.findings-emnlp.513) A survey on how people evaluate values in LMs.
* [**LLM Tropes: Revealing Fine-Grained Values and Opinions in Large Language Models.**](https://aclanthology.org/2024.findings-emnlp.995/) People often evaluate LLMs using sociological surveys and hope that the answers in the survey setup will generalize to free-form generation setups. This paper presents a methodology for evaluating the free-form setup properly.
* [**M5 – A Diverse Benchmark to Assess the Performance of Large Multimodal Models Across Multilingual and Multicultural Vision-Language Tasks.**](https://aclanthology.org/2024.findings-emnlp.250) This paper evaluates many current multimodal LLMs (both closed and open-weight) multilingual vision-language tasks and show that except for GPT 4V most of them are pretty bad.
* [**Pixology: Probing the Linguistic and Visual Capabilities of Pixel-based Language Models.**](https://aclanthology.org/2024.emnlp-main.194) Pixel-based pretrained encoders seem to be as good as subword models, but so far, no one has tried the most classical probing trying to figure out what information is on what model layer. This paper does that and finds out that, unlike subword models that tend to have the most syntactic information in the middle layers, pixel-based models tend to learn this stuff toward the end of the layer stack. Also, pixel models do not seem to like complex semantic tasks. It is hard to say if it is an inherent limitation of the architecture or whether deeper models would help.

## Workshops

Here are some random takeaways from the workshops, too: 

* Most submissions to WMT translation tasks finetuned LLMs.
* An important topic at the panel discussion and BlackboxNLP was that evaluation in interpretability is hard. (My interpretation is that the panelists meant that the credibility of interpretability research is often an issue.)
* Sebastian Ruder and his Cohere colleagues have a dataset for evaluating wrong language generation.

