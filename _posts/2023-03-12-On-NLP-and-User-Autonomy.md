---
layout: post
title: "Few words on Natural Language Processing and User Autonomy"
tags: [en]
lang: en
---

As natural language processing (NLP) finds its way from university labs and
becomes a crucial element of many user-facing technologies (machine
translation, search, language-model-based assistants), people start to get
concerned about the ethics of this technology. When people talk about NLP
ethics, the main topics are: biases that the models get from training data,
replication of toxic behavior found on the Internet, underrepresentation of
already underprivileged groups, differences between the technology availability
between the global north and global south.

There are many good articles on this topic, and I don't have much to add, but I
want to tackle this from a slightly different angle. Most work on this topic
views the technology creators as the active ones. The potential technology
users are passive, and the research community's task is to protect them from
unintentional or intentional harm, taking a sort of paternalist stance toward
the users. I was thinking about this already in 2021 when Covid vaccination was
a big topic, and some governments were considering compulsory vaccination,
which many people opposed as a lack of respect for patient autonomy.
Fundamental issues of medical ethics: informed consent, and patient autonomy,
were suddenly in the mainstream discourse. I was surprised that in NLP,
informed consent and autonomy are not a concern at all. The release of ChatGPT
and what followed made me think about user autonomy again.

## Basic concepts (as I see them) and what ethics is NLP ethics

First, I try to summarize the main theoretical concept here. I do not mean to
educate the readers but rather show how limited (and perhaps naive) my
understanding is. Two major theoretical frameworks are typically considered
when discussing ethics of technology: consequentialist ethics and rule-driven
deontology. Several more potentially relevant theoretical frameworks exist,
such as virtue or care ethics.

In the consequentialist view, a good action is an action that maximizes the
overall happiness or welfare or, negatively defined, minimizes harm. In other
words, it optimizes some utility functions.

The apparent advantage of such thinking is that it provides clear guidelines,
given the utility of decisions if well-defined, i.e., saving the maximum number
of lives given limited resources. Consequentialism's main problem is ultimately
to define the utility, which must be a universal moral "currency" to compare
possible consequences of a very different kind objectively. Although defining a
good utility in a limited domain might be feasible, a global and universal
moral utility seems impossible. Even if the utility seems commensurable, such
as the number of saved human lives, it can be problematic if taken too
literally. In an extreme case, killing someone to use their organs to save a
dozen others might be moral.

Deontology considers an action moral if it is justified by following ethical
rules, regardless of the consequences. In deontological thinking, we attempt to
have a small set of initial principles (such as Kant's categorical imperative)
for inferring rules for specific situations. E.g., ethics in biomedical
research stabilized on the following principles ([Gillon,
1994](https://www.bmj.com/content/309/6948/184); [Beauchamp and Childress,
2009](https://books.google.de/books?id=xg8iwAEACAAJ)):

* **Respect for autonomy.** Every person should be able to provide informed consent
  with the research or use of technology.

* **Beneficence.** The goal of any action should be the welfare of those directly
  affected and the whole society.  Non-maleficence. The goal of any action
  should be to avoid causing harm. It typically includes thinking of dual
  effects of actions, where harm can be a side effect of otherwise beneficent
  actions.

* **Justice.** Limited resources must be distributed fairly.

The beneficence of NLP research is rather implicit: the newly invented methods
are always beneficial to at least someone; otherwise, there is no reason to
publish such work. Avoiding causing harm is intensively studied in the context
of societal biases replicated by NLP models (e.g., [Bender and Friedman,
2018](https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00041/43452/Data-Statements-for-Natural-Language-Processing);
[Blodgett et al., 2020](https://doi.org/10.18653/v1/2020.acl-main.485)) or
dual-use ([Leins et al., 2020](https://aclanthology.org/2020.acl-main.261);
[Zellers et al.,
2019](https://proceedings.neurips.cc/paper/2019/hash/3e9f0fc9b2f89e043bc6233994dfcf76-Abstract.html)).
The NLP community also discusses justice: the biggest injustice is the impact
of the carbon footprint of the NLP technology that affects mainly different
populations than those that benefit from its existence (e.g., [Strubell et al.,
2019](https://doi.org/10.18653/v1/P19-1355)). User autonomy as a value is
rarely discussed.

Not respecting autonomy does not necessarily mean treating people as means to
ends. If the motivation is care or protection from harm, people talk about
paternalism. The common consensus is that it is desirable under some
circumstances, e.g., when states prohibit the use of some drugs. In the
consequentialist view, we can justify it by increasing the total welfare of all
people. In the deontology view, we can argue that this restricts short-term
autonomy for the sake of long-term autonomy (by preventing addiction), which is
a value in itself regardless of consequences (example from [Stanford
Encyclopedia of Philosophy](https://plato.stanford.edu/entries/paternalism)).
Paternalism is not a priori morally wrong but needs to be adequately justified.

NLP ethics focusing on mitigating biases and preventing harmful consequences
without viewing the affected people as relevant actors who should make informed
decisions seems to be unjustified paternalism.

## User Interface and no Space for Autonomy

Many complex technological artifacts inform users about their internal states:
cars have speedos, revolution counters, and dozens of warning lights for
various things that might have gone wrong with the engine. Smartphones say how
many percent of the battery capacity is left, what are the GSM and WiFi signal
strength and many other potentially helpful information. This information helps
users to make informed decisions on how they use the technology.

User interfaces of the most recent NLP tools are different, even though there
are complex artifacts too. No matter if it is Google Translate, DeepL, ChatGPT,
You.com, or the brand-new Bing search. There is a text input box, and the user
gets some text back, and that is it. Users have no idea what the internal state
of the system is.

Machine translation could provide a quality estimation. It could show what
training data instances the translation is likely based on. It can give several
translation variants and highlight the differences (e.g., more or less formal,
assuming some gender or gender-neutral). Similar things could be done with
writing assistants or search as well. The outputs are presented to users
without any additional information. The users do not get any information to
make a qualified and informed decision about what to do with the output.

I am not sure if this is not a priority or if the system authors think the
users would not use this information anyway, but for me, this is a clear sign
of a lack of respect for user autonomy.

## Ethics Statements at ACL 2021

In 2021, the separate ethics statement for ACL papers was new. Back then, I
read all 129 statements from ACL 2021 papers, tried to categorize their values,
and made some notes. (Now, I do not even remember what I hoped to discover in
the statements.)

Most often, the ethics statements focus on the consequences of the presented
method if it was deployed in the real world, most frequently via replicating or
amplifying societal biases or through unintended use of the methods (most
frequently disinformation generation). Only six statements (5%) mention the
lack of transparency or interpretability as a potential ethical issue. The
authors also often express concerns about the actual research process, mainly
in cases where data collection was a part of the research process. Most
frequently, the statements mention compensation to annotators and the privacy
of the annotators. Almost a quarter of the statements explicitly stated that
there were no issues.

Four papers view the lack of transparency for users as an ethical issue
(without explicitly appealing to the principle of autonomy). Three of them
targeted professional users ([Malik et al.,
2021](https://doi.org/10.18653/v1/2021.acl-long.313) legal text processing;
[Chen et al., 2021](https://doi.org/10.18653/v1/2021.acl-long.473) scientific
text processing; [Qiu et al.,
2021](https://doi.org/10.18653/v1/2021.acl-long.54) tools for robot
developers). [Fung et al.
(2021)](https://doi.org/10.18653/v1/2021.acl-long.133) are the only ones
presenting methods that might find users among the general public who mentions
interpretability as an ethical issue. There are another five papers explicitly
mentioning professionals in the ethics statements and ten that explicitly
mention end-users (in different roles, e.g., patients, parents, specific
platform users), and around 30 that probably have end users in mind when
talking about biases.

Although this is a tiny sample, the ratios show that the research community
tends to value the autonomy of professionals more than abstract and anonymous
end users of the technologies (3 out of 5 papers for professionals vs. 1 out of
10–30 users from the general public).

## Conclusions

Both the look and feel of user interfaces of current NLP applications and the
values reflected in the ethics statements made me think that NLP, as a field,
unwittingly takes a paternalist stance towards the end users of NLP
technologies. It seems to me that the value set in the community is that
technology should deliver good results (when they are good, there is no reason
to inform anyone about anything). We should protect those who might be harmed
by unintended or intended harm caused by the technology—no need to inform the
user about anything.

This is a pity. It would be great if we could change the mindset and keep in
mind that not only the system designers but also the system user should be able
to make informed decisions. It would undoubtedly lead to much exciting research
that we are now deprived of.
