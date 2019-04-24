---
layout: post
title: Tak trochu fake news o umělé inteligenci
categories: [Czech, Popular]
lang: cs
---

__[English version of the post](/2017/11/21/Kind-of-fake-news-on-AI.html)__

Když si v médiích čtu o technologiích, které využívají strojové učení, a o
umělé inteligenci, jak se teď říká, často se divím, jak jsou zprávy nejen
zjednodušující, ale především zavádějící. Určitě se to děje ve všech oborech,
nicméně rozhořčování se nad nepřesností zpráv například z letectví nebo
medicíny přenechám jiným a budu se věnovat strojovému učení a umělé
inteligenci.

Zpravodajské obsahy soutěží o naší pozornost se spoustou jiných zdrojů zábavy
a způsobů trávení času. Abych si vůbec nějakou zprávu přečetl, musí pro mě být
v daný okamžik zajímavější například než práce, kterou bych měl dělat,
procházení Facebooku odshora dolů, povídaní si s kamarády nebo si třeba jít
zaběhat. Mediální odborníci v této souvislosti hovoří o takzvaných
[_zpravodajských
hodnotách_](https://cs.wikipedia.org/wiki/Zpravodajsk%C3%A9_hodnoty), znacích,
které musí zprávy splňovat, aby měly vůbec šanci oslovit čtenáře
mainstreamových médií. V případě zpráv o umělé inteligenci hraje roli především
především to, že technologie mají jasné místo v naší kultuře (kulturní
blízkost), všichni ví, k čemu je pokrok (jednoznačnost), částečně i možnost
personalizace zprávy – vyprávět ji jako příběh jednotlivce nebo malé skupiny
vývojářů nebo příběh uživatelů, kterým se změnil život.

Zprávy se také musí vyhýbat nesrozumitelným vědeckým a technickým termínům.
V případě umělé inteligence pak není daleko k tomu, že si novináři vypomohou
metaforami ze sci-fi literatury a filmů. Nevyslovená souvislost mezi
nejnovějšími technologiemi a sci-fi žánrem určitě dělá takové zprávy v očích
veřejnosti atraktivnější, na druhou stranu vytváří falešné povědomí o
možnostech technologie a o problémech, které mohou být s novými technologiemi
spojeny.

# Strojový překlad od Googlu vytvořil univerzální jazyk

Na konci minulého roku Google publikoval studii, která ukazuje, jak je možné
jednoduše pozměnit neuronový strojový překlad, který používá Google Translate,
tak, aby jeden jediný model zvládal překlad mezi více jazykovými páry. Systém
je údajně schopný překládat nejen mezi dvojicemi jazyků, pro které byl
natrénován, ale i mezi páry jazyků, které systém nikdy předtím neviděl spolu.
Schéma toho, jak systém funguje, ukazuje [Google Research na svém
blogu](https://research.googleblog.com/2016/11/zero-shot-translation-with-googles.html).

![Google's Zero-Shot Translation](/assets/google_zero_shot.gif)

V současnosti je totiž potřeba zvláštní model pro každý jazykový pár. Pro mnoho
dvojic jazyků ani neexistuje dostatečné množství dvojjazyčných textů, s jejichž
pomocí by bylo možné překlad natrénovat. Kdyby něco takového fungovalo dobře,
byl by to pro strojový překlad velký krok dopředu. Bohužel nic takového se
nestalo. Výsledky Googlu jsou nesmírně zajímavé z teoretického hlediska, ale
úspěšnost představených modelů je daleko za tím, na co jsou uživatelé Google
Translate zvyklí.

V mediích se objevily objevily zprávy, které nejenom že chválily, jak systém
dobře funguje, ale obsahovaly i další zavádějící tvrzení – totiž, že překladový
systém si vytvořil vlastní univerzální jazyk, takzvanou _interlinguu_, který
používá při přechodu mezi jazyky. Jako interlingua se v lingvistice označuje
hypotetická (a pravděpodobně nemožná) reprezentace významu, která by měla být
nezávislá na konkrétním jazyce. Zpráva o tom, že překladač od Googlu jaksi sám
vytvořil univerzální jazyk, se objevila v mnoha médiích včetně nejčtenějších
technologických serverů:

* [Respekt, 13.1. 2017: Nový Google Translator chápe vztahy mezi jazyky, které vedle sebe nikdy neviděl](https://www.respekt.cz/denni-menu/novy-google-translator-chape-vztahy-mezi-jazyky-ktere-vedle-sebe-nikdy-nevidel)

* [Wired.com, 23.11. 2017: Google's AI just created its own universal 'language'](http://www.wired.co.uk/article/google-ai-language-create)

* [TechCruch.com, 22.11. 2017: Google’s AI translation tool seems to have invented its own secret internal language](https://techcrunch.com/2016/11/22/googles-ai-translation-tool-seems-to-have-invented-its-own-secret-internal-language/)

Nejenom, že články zapomínají zmínit, že pro praktické použití je takový systém
k ničemu, ale navíc vytváří falešný dojem, že si nějaký model strojového učení
(umělá inteligence!) vytvořil vlastní jazyk. Tím totiž mezi řádky říkají, že
současné neuronové sítě jsou natolik inteligentní objekty, že u nich má smysl
mluvit o tom, že používají lidský jazyk. A nejenom to, dokonce si samy pro sebe
vytváří nové, lepší jazyky. To je něco, co bychom v lidském přisoudili
maximálně napůl autistickým géniům. Stroj s takovými schopnosti tak každému
musí připadat jako děsivá a nepředvidatelná věc. Ve skutečnosti modely
reprezentují vstupní sekvence jako tabulky reálných čísel, které nemají žádnou
přímou interpretaci a nevykazují žádné vlastnosti, které obvykle jazyku
přisuzujeme.

# Experiment s umělou inteligencí se Facebooku vymkl kontrole

Většina modelů strojového učení, které se používají na zpracování přirozeného
jazyka, modeluje pouze, jak jazyk za určitých okolností vypadá, aniž by modely
nějakým způsobem explicitně věděly, k čemu mají jednotlivé promluvy sloužit
(zjistit, kolik je hodin, přesvědčit kamarády, aby volili Stranu zelených,
modlit se, nebo si třeba koupit poštovní známku). Modely, které se používají
například pro strojový překlad, toto neberou (a možná ani nemusí brát) v potaz.
Zdá se, že v případě strojového překladu si vystačíme s tím, že umíme
modelovat, jak vypadá věta v cílovém jazyce, když nám byla ukázána věta ve
zdrojovém jazyce. Pokud bychom ale chtěli vytvořit program, který s někým o
něčem vyjednával, program, který by používal jazyk k tomu, aby dosáhl nějakého
předem daného cíle (třeba sjednat co nejvýhodnější obchod), napodobování toho,
co lidé dělají v podobných situacích, by nejspíše nevedlo k cíli, měl by vědět,
jak se jazyk používá.

Letos v létě provedli výzkumníci ve Facebooku experiment, ve kterém se snažili
vyvinout model, který by měl přesně takovéto vlastnosti. Model, na kterém
pracovali, měl používat přirozený jazyk k tomu, aby vyjednával co nejvýhodnější
směny čepic, míčů a knížek. V experimentu využili stejného principu, který
používal systém [AplhaGo](https://cs.wikipedia.org/wiki/AlphaGo), který jako
první porazil člověka ve hře Go. Program sám sebe zdokonaloval tím, že hrál
miliony partií s různými verzemi sebe sama a metodou pokus–omyl zjišťovat, co
je nejlepší. V případě tohoto experimentu, výzkumníci modely nejprve
předtrénovaly tak, že uměly simulovat, jak vypadají konverzace mezi uživateli
na chatu – vycházely tedy z toho, jak jazyk vypadá. V průběhu dalšího trénování
mezi sebou vyjednávaly o výměnách předmětů tak, že zkoušeli, co je pro ně
nejvýhodnější. Modely si tak vytvořily velmi efektivní kód pro vyjednávání o
výměně předmětů, který ale ani v nejmenší nepřipomínal angličtinu.

Experiment získal překvapivě vysoké mediální pokrytí. Ve většině zpráv
nechybělo, že Facebook byl nucen ukončit experiment, ve kterém se umělá
inteligence začala vymykat kontrole.

* [Forbes.com, 31.7. 2017: Facebook AI creates its own language in creepy preview of our potential future](https://www.forbes.com/sites/tonybradley/2017/07/31/facebook-ai-creates-its-own-language-in-creepy-preview-of-our-potential-future)

* [Independent.co.uk, 31.7. 2017: Facebook's artificial intelligence robots shut down after they start talking to each other in their own language](http://www.independent.co.uk/life-style/gadgets-and-tech/news/facebook-artificial-intelligence-ai-chatbot-new-language-research-openai-google-a7869706.html)

* [Mirror.co.uk, 1.8. 2017: Robot intelligence is dangerous: Expert's warning after Facebook AI develop their own language](http://www.mirror.co.uk/tech/robot-intelligence-dangerous-experts-warning-10908711)

* [Business Insider 21.7. 2017: Facebooks's AI accidentally created its own language](http://uk.businessinsider.com/facebook-chat-bots-created-their-own-language-2017-6?r=US&IR=T)

Na rozdíl od zpráv o domnělém univerzálním jazyce, který měl vzniknout
v Googlu, nejvýznamnější technologické servery se naopak snažily šokující
zprávy o umělé inteligenci uvést na pravou míru.

* [Wired.com, 1.8. 2017: No, Facebook’s chatbots will not take over the world](https://www.wired.com/story/facebooks-chatbots-will-not-take-over-the-world/)

* [Gizmodo, 31.7. 2017: No, Facebook Did Not Panic and Shut Down an AI Program That Was Getting Dangerously Smart](https://gizmodo.com/no-facebook-did-not-panic-and-shut-down-an-ai-program-1797414922)

Když se nad experimentem zamyslíme, není nejspíš velkým překvapením, že
vyjednávací kód, který modely vyvinuly nakonec není podobný přirozenému jazyku.
Ostatně, lidský jazyk pravděpodobně není nejefektivnějším kódem pro vyjednávání
o směně předmětů. Za to má mnoho jiných fascinujících vlastností: můžeme v něm
psát básně, vyprávět vtipy nebo zpívat "Kolo, kolo, mlýnský". Výsledek
experimentu můžeme brát také jako argument pro to, že obchodní jednání není
hlavní funkce jazyka. Facebook experiment zastavil ne proto, že by byl jakkoli
nebezpečný, ale především protože nepřinesl praktické výsledky.

# Co si z toho odnést?

To, jak média informují o umělé inteligenci (už i sám pojem umělá inteligence
je poměrně zavádějící), často připomíná způsob, jakým se o umělé inteligenci
mluví ve sci-fi literatuře, kde toto sousloví obvykle znamená něco úplně
jiného. Média ráda využijí příležitost, jak interpretovat technologické novinky
v tomto duchu. Články na zpravodajských serverech to zatraktivňuje, a to i
v případě, kdy by se měl nakonec čtenář rozčílit, že to, o čem se píše, přece
není žádná inteligence.

Jako největší problém vnímám, že terminologie převzatá z vědecko-fantastických
filmů, obvykle evokuje i problémy a rizika z těchto filmů. Čtenářům vyvstává na
mysli možnost, že se umělá inteligence vymkne kontrole a vzbouří se proti
lidstvu, nebo že se nějaký super-padouch rozhodne s její pomocí ovládnout svět.
Jak by něco takového mohl udělat model, který počítá podmíněnou pravděpodobnost
slov v české větě, je-li dána anglická věta, nemám nejmenší tušení. Jako každá
technologie má umělá inteligence a strojové učení určitá rizika, ale tím, že
bude v médiích mluvit o sci-fi scénářích, se ty opravdové problémy nestanou
součástí veřejné diskuze.
