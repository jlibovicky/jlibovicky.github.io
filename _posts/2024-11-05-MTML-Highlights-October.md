---
layout: post
title: "Highlights from Machine Translation and Multilinguality in October 2024"
tags: [mtml-highlights, en]
lang: en
---

Here are summaries of a few pre-preprints that I noticed on arXiv during October.

### [LangSAMP: Language-Script Aware Multilingual Pretraining](https://arxiv.org/abs/2409.18199v1)

Folks from LMU Munich try a relatively simple trick to improve multilingual encoder models, particularly non-Latin-script and low-resource languages. They use additional information about the language identity and the script, but only during training, so at the inference, we can still use the model without caring about what language we feed in. They add static language and script embeddings before the langauge modeling head of MLM, which is typically not used at inference time. Presumably, this way, the model does not have to care about what langauge and script the output should be and can focus more on meaning (whatever that is). This, in turn, should make the cross-lingual transfer easier. The finetune XLM-R on the Glot500-c dataset for 500 languages and get decent improvements compared to previous work.

### [Can LLMs Really Learn to Translate a Low-Resource Language from One Grammar Book?]( https://arxiv.org/abs/2409.19151)

Folks from the University of Amsterdam debunk a claim from this year's ICLR spotlight paper that long-context can learn to translate an extremely low-resource language by using a textbook as input. The new experiments show that what matters is the translation examples from the book; anything else confuses the model. They get better results when they extract the examples from the book and do 5-shot in-context learning in the good old way people have used LLMs since GPT-3. Moreover, they try to add information about the target language's grammar in various ways, and it does not help improve the translation.

### [The Fair Language Model Paradox](https://arxiv.org/abs/2410.11985v1)

A preprint from MIT, Texas A&M, and Brown University studies the effect of weight decay (the good old L2 regularization for those who wonder what weight decay is) on the perplexity of tokens from different frequency bins. They show on several smaller LMs (but still too big for me to train) that as the L2 regularization increases, the perplexity of the low-frequency tokens increases. They do not explicitly discuss it, but I think this might have serious consequences for multilinguality because the low-frequency tokens will likely be from less represented languages in the training data mix, and no one would suspect that this good old machine-learning trick could ever influence them.

### [Multilingual Hallucination Gaps in Large Language Models](https://arxiv.org/abs/2410.18270v1)

A study from three Quebecian institutions investigates the factuality of what LLM generates. They use prompts like "Give me a biography of XY," where XY is a person with a sufficiently detailed Wikipedia page. Then, they use FactScore, an LLM-based metric that splits the answer into atomic facts and searches for support of the atomic facts in the Wikipedia article about XY. Even though it is not entirely clear how to do this correctly (prompt in local language/English, do the FactScore in the language, or translate into English first and do the evaluation), different setups with different languages lead to consistent results. The results show that the fewer training data we have for the language, the more the LLMs hallucinate.

### [On Instruction-Finetuning Neural Machine Translation Models](https://arxiv.org/abs/2410.05553v1)

Folks from Microsoft managed to instruction-finetune Transformer Big for machine translation to follow instructions for what the translation should look like. It is good to see that telling models what to do works also on a much smaller scale than we usually see nowadays. (But they generated the training data from an LLM anyway, so it is still, in some sense, a distilled LLM.)