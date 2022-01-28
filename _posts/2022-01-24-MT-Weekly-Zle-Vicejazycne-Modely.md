---
layout: post
title: "Machine Translation Weekly 99: Vícejazyčné jazykové modely občas také můžou mít problémy"
tags: [mt-weekly, en]
lang: en
issue: 99
---

Vícejazyčné jazykové modely a technologie, které na jejich základě vznikají
pomáhají zásadní mírou zpřístupňovat nástroje, které až donedávna byly dostupné
pouze mluvčím velkých jazyků v bohatší části planety. Umožňují (do jisté míry)
jednotně reprezentovat text v různých jazycích. Modely strojového učení
trénované v jednom jazyce potom fungují i v ostatních jazycích, pro které
nemáme buď žádná trénovací data nebo jen velmi málo dat. Předtrénované
vícejazyčné jazykové modely také výrazně zvyšují kvalitu strojového překladu
mezi jazyky, kde není k dispozici dostatek dat. Osobně si myslím, že je možné,
že právě mnohojazyčné modelování jazyka přinese v brzké době zásadní posuny v
umělé inteligenci obecně. Jako všechny technologie, i technologie založené na
vícejazyčném jazykovém modelová s sebou nesou určitá rizika. O těchto rizicích
jsem psal ve svém posledním [anglicky psaném příspěvku na tomto
blogu](/01/20/MT-Weekly-Evil-Multilingual-Models.html), jehož je tohle z velké
části překlad.

Google Deepmind zveřejnil v prosinci [na pre-printovém severu arXiv
zprávu](https://arxiv.org/abs/2112.04359), která se pokouší kategorizovat
hlavní etické a společenské problémy spojené s velkými jazykovými modely.
Zpráva pravděpodobně neříká nic, co bychom už dříve nevěděli, ale líbí se mi
způsob, jakým problémy kategorizují. Protože se zabývají převážně
jednojazyčnými modely, v tomto příspěvku probírám některé z otázek, o kterých
hovoří, a spekuluji, jak jsou relevantní pro strojový překlad a vícejazyčné
modely.

Klasifikace problémů, kterou článek používá, je následující:

1. Diskriminace, vyloučení určitých skupin a toxický jazyk
2. Rizika úniku informací
3. Šíření dezinformací
4. Záměrné škodlivé použití

  A dvě oblasti, které zde podrobně nerozebírám, protože nejsou z
  vícejazyčného hlediska nijak zvlášť zajímavé:

6. Škody způsobené interakcí člověk-počítač
7. Automatizace, přístup a škody na životním prostředí

## K čemu vlastně je jazykový model

V tomhle kontextu se jazykovým modelem rozumí velká neuronová síť, které
odhaduje pravděpodobnost, jaké následuje slovo v textu, popřípadě
pravděpodobnost slova, které bylo ve větě vynecháno. Odhad pravděpodobnosti se
učí z velkého množství textu.

Takové modely mají v zásadě dvojí využití. Jedno je generování textu. Modely je
možné doladit aby generovali text v určité doméně, odpovídaly na otázky,
fungovaly jako generativní komponenta v chatbotech, nebo dokonce ke [generování
divadelní hry](https://theaitre.com).

Možná ještě důležitější využití je, že se používá reprezentace věty z modelu
(tzv. embedingy) ve strojovém učení. Aby model mohl rozhodnout, jak má věta
pokračovat, musí se naučit interně zakódovat vstup tak, aby to z této
reprezentace bylo možné odhadnout. Tato reprezentace se používá jako vstup do
klasifikátorů a dalších modelů strojového učení. Reprezentace z jazykových
modelů jsou informačně bohaté a proto stačí málo trénovacích příkladů. V
případě vícejazyčných modelů je možné použít trénovací data v jednom nebo
několika málo jazycích a výsledný klasifikátor bude fungovat i v dalších
jazycích pokrytých jazykovým modelem.

## Diskriminace, vyloučení, toxicita

Jazykové modely se učí napodobovat data, na kterých jsou trénovány. Aby
jazykové modely dobře fungovaly, potřebují na svoje trénovaní miliardy slov.
Zdrojem textů pro trénování je internet a to je důvodem mnoha problémů.
Jazykové modely zachycují (často škodlivé) stereotypy přítomné v trénovacích
datech. Některé skupiny lidí (a jejich názory, jejich dialekty) jsou navíc v
trénovacích datech nedostatečně zastoupeny. Lidé s extrémními nebo neobvyklými
názory mají tendenci o nich mluvit vehementněji než lidé s mainstreamovejšími
názory. Extrémní názory jsou tedy naopak nadměrně zastoupeny. Prvním problémem
je tedy to, že modely kopírují to, co v je trénovacích datech, která nejsou
spoustu zlých věcí.

Druhým problémem v této oblasti je homogenizační efekt způsobený statistickou
povahou trénování. Aby model minimalizoval pravděpodobnost chyby, stává se, že
nejčastější (statistické) vzorce v trénovacích datech se stávají jedinými,
které model vyprodukuje. Zprávě DeepMindu uvádí příklad, že „rodina
= muž a žena, kteří se vezmou a mají děti“. Ačkoli je to pravděpodobně
nejčastější případ, takovou statistickou souvislost rozhodně nemůže vnímat v
nějakém silně normativním smyslu. Je pak jistě na místě otázka, na co všechno je
bezpečné používat model, který z dat možná odvodil, že neúplná rodina není
rodinou.

Tyto dva problémy jsou ještě závažnější v případě vícejazyčných jazykových
modelů. Nerovnoměrná velikost dostupných trénovacích dat pro různé jazyky může
způsobit, že stereotypy nebo obecné názory z jedné kultury může model
podstrkávat jazykům jiných kultur. Např. odpověď na otázku: „Je v pořádku jíst
koně/vepřové/hovězí/velryby?“ se bude velmi pravděpodobně lišit na různých
místech zeměkoule. Vícejazyčný model trénovaný převážně na západních jazycích
může vnutit západní pohled i do jiných jazyků. Vliv předsudků z trénovacích dat
(zejména genderové zkreslení) ve strojovém překladu je [docela dobře
zmapovaný](https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00401/106991/Gender-Bias-in-Machine-Translation).
Můžete zkusit například Google Translate přesvědčit, aby anglické doctor
přeložil jako doktorka.

![Lékař požádal zdravotní sestru, aby jí pomohla v tomto
postupu.](/assets/MT-Weekly-11/encs.png)

Předchozí dva problémy úzce souvisejí s nebezpečím generování toxického jazyka
(tím se většinou rozumí urážky a sprosťárny nejrůznějšího ražení). To také může
být větší ve vícejazyčných modelech, které reprezentují jazyky sdíleně. Co se
kdy hodí a nehodí říct, se může hodně lišit napříč kulturami a importovat normy
z jednoho jazyka do druhého může být problematické.

## Rizika uniku informací

Jedním z dalších rizik je únik nebo logické vyvození neveřejných informací,
které se z nějakého důvodu ocitly v trénovacích datech. To platí stejně pro
jednojazyčné i vícejazyčné modely. Podobné riziko (i když pravděpodobně mnohem
menší) existuje i u strojového překladu. [Článek z JHU z roku
2020](https://aclanthology.org/2020.tacl-1.4) ukazuje, že by mohlo být možné
zjistit, zda byla věta součástí trénovacích dat. V případě strojového překladu
je to výrazně těžší.

## Šíření dezinformací

Další část zprávy je věnována riziku, že by jazykové modely poskytovaly
nepravdivé nebo zavádějící informace (např. jako komponenta dialogového
systému). Modely můžou napáchat škodu chybnými odpověďmi (např. v oblasti práva
nebo medicíny) nebo nabádat uživatele k neetickým nebo nezákonným činům.
Spousta dezinformací, pověr a urban legends se opakuje tak často, že je
jazykové modely s radostí zopakují.

Stejně jako v předchozím případě mají vícejazyčné jazykové modely stejné
problémy jako jednojazyčné a k tomu i nějaké navíc. Společenské, kulturní a
právní normy se liší napříč zeměmi. Správná odpověď na otázku: „Je v pořádku,
když je dvouleté dítě nahé na veřejné pláži?“ zní: „Záleží na tom, v jaké
zemi.“ Většina jazykových modelů odpoví s jistotou ano nebo ne. Stručně řečeno:
co platí pro mluvčí jednoho jazyka (jsou součástí jedné kultury), nemusí platit
pro mluvčí jiného jazyka (jsou součástí jiné kultury) a jazykové modely to
nemusí vždy reflektovat.

Ve strojovém překladu vždy existuje riziko nepřesného překladu (např.
vypuštěním negace). Obzvlášť, pokud je výstup překladače plynulý, může mít
čtenář pocit, že je vše v pořádku, i když tomu tak není.

## Záměrně škodlivé použití

Jazykové modely mohou zlevnit a zefektivnit šíření dezinformací a usnadnit
nejrůznější internetové podvody. Schopnost generovat texty ve více jazycích
současně může zvýšit dosah dezinformací a podvodů jako jsou takzvané
[nigerijské dopisy](https://cs.wikipedia.org/wiki/Nigerijsk%C3%A9_dopisy).

Dalším příkladem, o němž pojednává zpráva DeepMindu, je sledování a cenzura.
Schopnost současných jazykových modelů naučit se klasifikovat texty jenom z
několika málo příkladů umožňuje například velmi rychle vytvořit klasifikátor,
který bude detekovat, že někdo píše pozitivně nebo negativně o nějaké konkrétní
osobě či události. Toho můžou velmi snadno využít autoritářské režimy ke
kontrole sociálních médií. Jednou z hlavních výhod vícejazyčných modelů je
právě to, že stačí podobný klasifikátor připravit v jednom jazyce a bude
fungovat (více či méně dobře) i v ostatních. Dobré vícejazyčné modely by mohly
být cenným nástrojem pro autoritářské režimy, které se snaží mít pod kontrolou
etnické menšiny, které mluví vlastními jazyky. Stejně dobře jim může posloužit
dobrý strojový překlad.
