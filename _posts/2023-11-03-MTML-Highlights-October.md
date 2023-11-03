---
layout: post
title: "Highlights from Machine Translation and Multilinguality in October 2023"
tags: [mtml-highlights, en]
lang: en
---

Here is my monthly summary of what papers on multilinguality and machine
translation I found the most noteworthy during October 2023. There were 2,881
preprints in the computation and language category on arXiv (a new record
number), so there is a big chance that there were preprints I would like to
read that I missed.

### [Navigating Cultural Chasms: Exploring and Unlocking the Cultural POV of Text-To-Image Models](https://arxiv.org/abs/2310.01929v1)

A preprint from Israeli Technion, Google Research, and Cambridge University
studies cultural awareness of text-to-image models. The paper has a very good
related work section that explains necessary concepts from cultural studies (I
learned a lot). Based on the theory and surveys, they collect concepts that
differ the most across cultures (e.g., holiday, teacher, wedding, protest,
king, beauty). Then, they measure the similarity of OpenCLIP representations of
images generated from prompts with the selected concepts. At first glance, the
results show that the models they tested (Stable Diffusion, AltDiffusion,
DALL-E, and DeepFloyd) reasonably capture relatively course-grained cultural
differences. A deeper analysis, however, reveals that switching between
cultural/geographic areas can be triggered just by using characters from the
language-specific alphabet. With one random Arabic character in the prompt, the
models generate Middle Eastern-looking kings instead of medieval European
kings.

### [To token or not to token: A Comparative Study of Text Representations for Cross-Lingual Transfer](https://arxiv.org/abs/2310.08078v1)

A paper from George Mason University that will appear at the Multilingual
Representation Learning Workshop at EMNLP 2023 explores how different
tokenization (subwords, characters, pixels) approaches influence cross-lingual
transfer. The methodology is in many ways problematic: they compare models with
different numbers of parameters trained on very different datasets. However,
some findings are interesting: Pixel-based models (i.e., models relying on
visual representations of the text) work well for transfer between indic
languages, which use visually similar alphabets; however, they have different
UTF8 encodings. Subword tokenization outperforms characters for tasks that rely
more on lexical meaning.

### [xCOMET: Transparent Machine Translation Evaluation through Fine-grained Error Detection](https://arxiv.org/abs/2310.10482v1)

A Portuguese company, Unbabel, introduced xCOMET, a new version of their widely
used machine translation evaluation metric. Instead of predicting one overall
score saying how good a translation is, it does  MQM labeling, i.e., it detects
spans where something went wrong and assigns labels. It is prepared in multiple
stages. First, they finetune XLM-R on direct assessment of machine translation
quality: the way the previous editions of COMET were trained. In stages 2 and
3, it is finetuned on word level annotations, mixed data first, high quality
later. Unfortunately, they only look at translations between English and
German, Russian and Chinese. The results are on par or slightly better than
Microsoft's GEMBA (evaluation by prompting GPT-4), but...

### [GEMBA-MQM: Detecting Translation Quality Error Spans with GPT-4](https://arxiv.org/abs/2310.13988)

Five days later, Microsoft answered with their new version of GEMBA. Similarly
to xCOMET, they also abandoned predicting a single number and used the MQM
scheme for tagging specific problems. They formulated the MQM tagging as a
prompt for GPT-4 and let it do the job. On high-resource languages, it
outperforms xCOMET (and all other metrics). As with xCOMET, we know nothing
about less resource-rich languages. And, of course, a considerable disadvantage
of such evaluation is that it relies on proprietary commercial models, whereas
xCOMET can be run on a Playstation-sized GPU.

### [Cross-Lingual Consistency of Factual Knowledge in Multilingual Language Models](https://arxiv.org/abs/2310.10378v2)

A paper from Groningen and Amsterdam (that will appear at this year's EMNLP)
studies how consistently multilingual langauge models answer factual questions.
They use X-FACTR and MLAMA datasets to check the cross-lingual consistency of
factual knowledge in BLOOM, mT5, and XLM-R (and I miss LLaMA2, but it was not
available at the time of EMNLP submissions). They develop their own consistency
ranking (regardless of accuracy) based on the overlap of top-k prediction. In
general, the consistency is low. They search for factors that influence
consistency: the most important are language similarity in terms of language
family and vocabulary overlap. Based on the results, the authors speculate that
factual knowledge is stored on a rather shallow level in the embeddings
(largely language-specific) and not in the more shared parts of the model.

### [Cross-lingual Prompting: Improving Zero-shot Chain-of-Thought Reasoning across Languages](https://arxiv.org/abs/2310.14799v1)

This EMNLP 2023 paper by authors from several Chinese universities shows a new,
interesting method for chain-of-thought prompting in a multilingual setup. When
they solve a task in a language other than English, they formulate the task in
the original language, then say, let's think step by step in English, and let
the model proceed step-by-step in English. They test first at MGSM
(Multilingual Grade School Math, often used to evaluate chain-of-thought
prompting), then also on XNLI and PAWS-X (where I would not expect
chain-of-thought prompts to make any difference, but it does). This
language-hybrid method is better than chain-of-thought prompting in the
original language and better than translating everything into English. The
results are consistent both for the OpenAI models and open-source ones like
LLaMA and BLOOMZ.
