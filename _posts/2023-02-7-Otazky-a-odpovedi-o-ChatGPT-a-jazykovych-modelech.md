---
layout: post
title: Otázky a odpovědi o ChatGPT a velkých jazykových modelech
lang: cs
tags: [popularization, cs]
---

Poslední dobou se v médiích poměrně často píše o ChatGPT a jazykových modelech
a mám pocit, že ne úplně všechno se říká úplně správně. Proto jsem připravil
několik otázek a odpovědí, které snad pomůžou vyjasnit, o čem se to vlastně
mluví.

Otázky:

1. [Co je to (velký) jazykový model?](#co-je-lm)
2. [Co je to ChatGPT?](#co-je-chatgpt)
3. [Je GPT-3.5 a ChatGPT to nejlepší, co existuje?](#gpt-nejlepsi)
4. [Jsou nějaké dostupné alternativy, ideálně open source?](#open-source)
5. [Jaktože umí ChatGPT česky, používá strojový překlad?](#je-to-mt)
6. [Kde se berou znalosti, které má ChatGPT? Používá nějaký vyhledávač?](#znalosti)
7. [Co dělat s tím, že to používají žáci ve školách?](#skoly)
8. [Jazykové modely mají své odpůrce, kteří je považují za nebezpečnou technologii. V čem je to nebezpečí?](#nebezpeci)

## Co je to (velký) jazykový model? {#co-je-lm}

Matematicky vzato je jazykový model nějaká funkce nebo algoritmus, který pro
nějaký text (dokončený nebo nedokončený) odhaduje pravděpodobnost, jaké slovo
bude v textu následovat. Je to základní nástroj, který se ve zpracování
přirozeného jazyka používá od 90. let, původně hlavně k tomu, aby při
rozpoznávání řeči a automatickém překladu vybíral varianty, které jsou
plynulejší a dávají lepší smysl v daném kontextu.

Jazykový modely se učí z dat, z prostého textu, dnes nejčastěji tak, jak se
stáhne z internetu. Od 90. let se několikrát zásadně proměnil způsob, jakým se
jazykové modely trénují. Dramaticky se navýšil dostupný výpočetní výkon a
množství dostupných trénovacích dat. Současné jazykové modely jsou neuronové
sítě založené na [architektuře
Transformer](https://papers.nips.cc/paper/2017/file/3f5ee243547dee91fbd053c1c4a845aa-Paper.pdf).
To je architektura, která reprezentuje vstupní slova jako posloupnosti vektorů
spojitých čísel. Střídá klasické dopředné vrstvy s něčím, čemu se říká
_attention mechanism_. V těchto vrstvách model jakoby „vyzobává“ z textu na
vstupu (nerozlišuje se mezi zadaným vstupem a vygenerovaným textem) relevantní
informace pro předpovězení dalšího slova.

Samotné učení nebo trénování probíhá tak, že se modelu předkládají reálné lidmi
napsané texty. Model dostává trénovací data po dávkách o délce řádově
desetitisíce slov. S každou dávkou se upraví parametry modelu tak, aby model
považoval poslední dávku dat za trochu pravděpodobnější než předtím. V
závislosti na velikosti dat a velikosti modelu může trénování trvat od řádově
hodin po měsíce.

V poslední době se hodně mluví o velkých jazykových modelech, které vykazují
pozoruhodné schopnosti, které by se daly popsat jako inteligentní chování.
Kromě schopnosti kreativně a zajímavě pokračovat v textech, je to schopnost
pochytit komplexní vzorce z několika málo příkladů, které se odborně říká
few-shot learning. Při něm se nějaká úloha (např. rozhodnout, jestli se jedná o
nenávistný příspěvek, zkrátit větu, opravit pravopisné chyby atd.) formuluje v
přirozeném jazyce a na vstup se dá několik příkladů vstupů a výstupů. Model pak
dál pokračuje ve vzorci, který pochytil ze vstupu. Překvapivé je to, že
jazykové modely takto zvládají řešit úlohy, které od člověka vyžadují nemalé
intelektuální úsilí.

Nejznámější jsou velké jazykové modely GPT od společnosti (původně nadace)
OpenAI. Pro představu, co znamená velké: Pro [trénování
GPT-3](https://papers.nips.cc/paper/2020/file/1457c0d6bfcb4967418bfb8ac142f64a-Paper.pdf)
zveřejněného v květnu 2020) se použilo 45TB textu, to odpovídá například 37
milionům výtisků Dostojevského Zločinu a trestu (kdybychom je vyskládali na
fotbalové hřiště, sahaly by do výšky 4.5 metru). GPT-3 má 175 miliard
trénovatelných parametrů. Každý parametr je reálné číslo, na jehož uložení jsou
potřeba 4 byty. Takže jen pro uložení modelu je potřeba 561 GiB paměti. Další
paměť je pak potřeba pro samotné výpočty.

## Co je to ChatGPT? {#co-je-chatgpt}

ChatGPT je chatbot – program, který komunikuje s člověkem v přirozeném jazyce.
Společnost OpenAI v prosinci 2022 spustila [veřejnou demo
verzi](https://openai.com/blog/chatgpt), která je zatím dostupná zdarma.
Plánuje se [její
zpoplatnění](https://www.nytimes.com/2023/02/01/technology/openai-chatgpt-plus-subscription.html).

Technicky vzato je ChatGPT dotrénovaný model GPT 3.5 (vylepšená verze GPT 3, ke
které OpenAI nezveřejnilo příliš detailů) tak, aby pro plnění úloh nepotřeboval
uvádět příklady, ale řešil je rovnou na základě instrukcí od uživatele. Podobný
princip využilo OpenAI ve svém modelu InstuctGPT, ke kterému vyšel [v dubnu
2022 preprint](https://arxiv.org/abs/2203.02155), který zatím nevyšel v žádném
recenzovaném sborníku.

Trénování ChatGPT probíhá ve dvou fázích: v první fázi anotátoři (tak se
obvykle říká pracovníkům, kteří připravují trénovací data pro strojové učení) s
pomocí modelu GPT vytvářely ukázkové dialogy, jak by se měl chatbot chovat. V
druhé fázi, už systém nedostával přímo ukázky správných dialogů, ale učil se
pouze pomocí jednoduché zpětné vazby: anotátoři odpovědi označovali jako dobré
nebo špatné a na základě toho se systém zlepšoval bez přímých ukázek správných
odpovědí. Aby se snížila potřeba lidských anotací, autoři systému natrénovali
další neuronové sítě, které simulují lidské hodnocení. Celý systém se pak může
dále trénovat s pomocí simulované zpětné vazby bez nutnosti lidských vstupů.
Odborníci odhadují, že pro vývoj ChatGPT bylo potřeba statisíce až miliony
anotací. Podle [zjištění amerického časopisu
Time](https://time.com/6247678/openai-chatgpt-kenya-workers) k tomu OpenAI
najímalo agentury v anglicky mluvících zemí třetího světa. Například v keňském
Nairobi platili anotátorům v přepočtu mezi 20 a 40 korun na hodinu.

ChatGPT umí odpovídat na otázky a generovat text podle instrukcí uživatele v
přirozeném jazyce. Vykazuje rozsáhlé encyklopedické znalosti, a protože
součástí trénovacích dat bylo i hodně zdrojového kódu a informatických textů,
zdá se, že umí i poměrně dobře programovat. Je to nejspíš poprvé v dějinách
informatiky, kdy nějaký počítačový systém do velké míry splňuje lidové
představy o tom, jak by mohla nebo měla vypadat umělá umělá inteligence.
Největším problémem systému je, že informace, které podává sice zní velmi
věrohodně, ale neuvádí k nim žádné zdroje a často jsou fakticky špatně. Při
práci s ChatGPT je potřeba vždy důsledně ověřovat všechna fakta ve spolehlivých
zdrojích.

## Je GPT-3.5 a ChatGPT to nejlepší, co existuje? {#gpt-nejlepsi}

GPT-3.5 a ChatGPT pravděpodobně nejlepší modely, které jsou snadno dostupné pro
širší veřejnost. Nejsou to ale největší a nejlepší modely, které existují.
Google má k dispozici model PaLM
([preprint](https://arxiv.org/abs/2204.02311), který ho popisuje vyšel v dubnu
2022, doposud nevyšel žádný recenzovaný článek), který údajně vykazuje zajímavé
schopnosti, které GPT-3 nemá. Na sociálních sítích nejvíc rezonovala údajná
[schopnost vysvětlovat
vtipy](https://ai.googleblog.com/2022/04/pathways-language-model-palm-scaling-to.html).
V podstatě stejné modely jako GPT-3 s názvem OPT (Open Pretrained Transformer)
[kompletně zveřejnila včetně technických
detailů](https://ai.facebook.com/blog/democratizing-access-to-large-scale-language-models-with-opt-175b)
trénovaní společnost Meta (provozovatel Facebooku, Instagramu a WhatsAppu) dva
roky po GPT-3 v květnu 2022.

Google má také chatbot LaMDA ([preprint z ledna
2022](https://ai.googleblog.com/2022/04/pathways-language-model-palm-scaling-to.html),
recenzovaný článek dosud nevyšel), který se trénoval trochu jinak než ChatGPT.
Je to čistý jazykový model trénovaný ale pouze na konverzacích, tedy bez
dotrénování na zpětné vazbě. Chatbot LaMDA vzbudil rozruch v první polovině
roku 2022, kdy jeden z jeho vývojářů [tvrdil, že LaMDA je cítící
bytost](https://www.washingtonpost.com/technology/2022/06/11/google-ai-lamda-blake-lemoine)
a mělo by s ním podle toho zacházet. V lednu 2023, po více než půl roce od této
kauzy Google oznámil [veřejné testování tohoto
chatbota](https://blog.google/technology/ai/join-us-in-the-ai-test-kitchen).

## Jsou nějaké dostupné alternativy, ideálně open source? {#open-source}

OpenAI se chová poměrně tajnůstkářsky. Model GPT 3 nedala k dispozici ani
odborné veřejnosti s vysvětlením, že se obává zneužití. Model je ale k
dispozici prostřednictvím webového rozhraní a OpenAI si [za něj účtuje nemalé
poplatky](https://openai.com/api/pricing).

Existují open-source alternativy. Společnost Meta připravila modely OPT, které
jsou velmi podobné GPT-3 a dala je volně k dispozici ke stažení. Iniciativa
[Big Science Workshop](https://bigscience.huggingface.co), za kterou stojí
newyorský startup [HuggingFace](https://huggingface.co) a konsorcium evropských
a amerických univerzit, připravila [vícejazyčný model
BLOOM](https://bigscience.huggingface.co/blog/bloom), který ovládá přibližně 40
jazyků. Vývoj velkých jazykových modelů pro evropské podporuje v rámci několika
projektů i Evropská Unie – součástí jednoho z nich
([HTLP](https://cordis.europa.eu/project/id/101070350)) je i Ústav formální a
aplikované lingvistiky MFF UK.

Vznikla také open source iniciativa
[Open-Assistant](https://github.com/LAION-AI/Open-Assistant) vedená německou
neziskovou organizací [LAION](https://laion.ai). Jejím cílem je vytvořit model,
který má obdobné schopnosti jako ChatGPT, ale je open source a je možné ho
používat na běžně dostupném hardwaru. Je to sice ambiciózní cíl, ale pokud se
do projektu podaří zapojit ve velkém univerzity, má rozumnou šanci uspět.

V komerčním prostředí nabízí podobný nástroj jako ChatGPT [vyhledávač
You.com](https://you.com/search?q=who+are+you&tbm=youchat&cfr=chat) od
kalifornského AI startupu, který má původ ve společnosti Salesforce a na
Stanfordské univerzitě. Subjektivně se zdá, že funguje hůře, než ChatGPT. Na
rozdíl od něj, ale pracuje s vyhledávačem a generuje odpovědi z výsledků
vyhledávání. Uživatel si tak může ověřit, z jakých zdrojů odpověď pochází.

## Jaktože umí ChatGPT česky, používá strojový překlad? {#je-to-mt}

Česky a dalšími jazyky se ChatGPT naučil jaksi mimochodem z trénovacích dat, do
kterých byly kromě angličtiny zamíchané i další jazyky. Není to tedy tak, že by
se jednalo o chatbot a překladač zapojený za sebe.

Čím větší je digitální stopa nějakého jazyka, tím lépe ho ChatGPT ovládá. Jak
dobře které jazyky ovládá se odhadnout pomocí, jak dobře je ChatGPT schopné
provádět samotný překlad. Nedávný [preprint od čínské společnosti
Tencent](https://arxiv.org/abs/2301.08745), který hodnotil schopnosti
strojového překladu ChatGPT, ukazuje, že pro jazyky s velkou digitální stopou
(velké světové jazyky, ale třeba i čeština) funguje poměrně dobře: srovnatelně
asi jako strojové překladače před pěti lety. Naopak pro jazyky s malou
digitální stopou funguje zásadně hůře, než dnešní automatické překladače.

To, že se v systému není zapojený samostatný překladač, je vidět také na tom,
jak se postupně objevuje generovaný text. Anglicky obvykle přibývá po celých
slovech, česky přibývá po mnohem menších kouscích, po dvojicích až trojicích
písmen. Důvodem je, že jazykové modely mohou pracovat jen s omezeným množstvím
jazykových jednotek, řádově desetitisící, maximálně statisíci. Častá slova tak
zůstávají vcelku – v tomto případě nejčastější slova jsou anglická. Čím méně je
časté slovo v trénovacích datech, na tím více jednotek se rozpadne. Kdyby se
jednalo o automatický překlad, na české straně by byly delší jednotky. Navíc by
ChatGPT v češtině delší odezvu: nejprve by text generoval a teprve potom
překládal.

## Kde se berou znalosti, které má ChatGPT? Používá nějaký vyhledávač? {#znalosti}

Všechno, co ChatGPT a všechny jazykové modely vědí o světě, je zakódované v
naučených parametrech modelu, žádný vyhledávač se používá. To je problematické
v mnoha ohledech. Jedním problémem je to, že nevíme, z jakého zdroje se
konkrétní informace vzala. Další problém je, že není úplně snadné znalosti v
modelu editovat a tak například selektivně odstraňovat dezinformace. S tím
souvisí další problém a to, že celý systém se trénoval v nějaké době a
neexistuje přímočarý způsob, jak ho aktualizovat. ChatGPT tak nemá znalosti o
tom, co se stalo pro roce 2020.

Neuronové sítě jsou v obecnosti obtížně interpretovatelné a vysvětlení, jak
věci uvnitř sítě po jejím trénování, se typicky hledají dodatečně. Nedávné
[experimenty s jazykovými modely na MIT ukázaly](https://rome.baulab.info), že
faktické znalosti se ukládají distribuovaně do dopředných vrstev. Některá fakta
je možné lokalizovat a editovat, jiná nikoli. Jak tuto metodu aplikovat ve
větším měřítku a jestli funguje i pro opravdu velké jazykové modely není jasné.

Existují systémy, které kombinují [vyhledávání s generováním
odpovědí](https://aclanthology.org/2021.findings-acl.374). Ty dokážou říct, na
základě čeho text vznikl. Ani zde ale neexistuje záruka, že nalezené zdroje
jsou věrohodné a že z věrohodných zdrojů jazykový model zvládne extrahovat
pravdivé informace.

## Co dělat s tím, že to používají žáci ve školách? {#skolky}

[Studie provedená se staršími jazykovými
modely](https://aclanthology.org/2020.acl-main.164) z roku 2020 z Googlu a
University of Pennsylvania, ale i velmi čerstvý [preprint ze Stanfordské
university](https://arxiv.org/abs/2301.11305) ukazují, že strojově odhalit
generovaný text je poměrně jednoduché, zatímco lidé s tím mají velké obtíže.
Pro jednodušší rozpoznání generovaného textu se dá používat technika, které se
říká _watermarking_, kdy se do generovaného textu přidává _virtuální vodotisk_.
Tuto metodu velmi dobře shrnuje nedávný [preprint z University of
Maryland](https://arxiv.org/abs/2301.10226). V praxi to znamená to, že
pravděpodobnosti v modelu upraví tak, že některá slova nebo posloupnosti slov
se vyskytují signifikantně častěji, než v přirozeném textu, ale pro člověka je
to nepostřehnutelné. Dá se pak relativně snadno testovat, jestli text vodotisk
obsahuje nebo ne. OpenAI dalo na konci ledna k dispozici [svůj vlastní detektor
generovaného textu](https://platform.openai.com/ai-text-classifier).

Pokud se nástroje na detekci automaticky generovaného textu rozšíří, může to
odstartovat nikdy nekončící hru na kočku a myš. Ten, kdo má k dispozici
detektor generovaného textu a může ho donekonečna pouštět, ho také může použít
pro trénování dalšího, menšího jazykového modelu, který bude parafrázovat
původní text, tak aby neměnil obsah a obelhal detektor.

Podle mého názoru je snaha omezovat používání jazykových modelů předem
odsouzená k neúspěchu. Nemá smysl nic zakazovat, ale je potřeba žáky připravit
na svět s umělou inteligencí. Technologie jako ChatGPT do budoucna změní
způsob, jakým se pracuje se znalostmi a školy by na to měly žáky a studující
připravit.

## Jazykové modely mají své odpůrce, kteří je považují za nebezpečnou technologii. V čem je to nebezpečí? {#nebezpeci}

U velkých jazykových modelů hrozí stejně jako u jakékoli jiné technologie
zneužití. Schopnost generovat podle příkladů nebo podle instrukcí autenticky
znějící plynulý text se dá zneužít ke generování nepravdivých zpráv. Schopnost
vést konverzaci s nějakým cílem se dá využít k automatizaci podvodných emailů,
k neférovým obchodním praktikám nebo v politické propagandě.

Kromě přímého zneužití jsou ale i jiné problematické aspekty, které jsou mnohem
nenápadnější. Jazykové modely se trénují na velkém množství dat, které nutně
obsahují velké množství patologií a toxického chování (sexismus, rasismus,
politický extremismus). Protože se model učí napodobovat trénovací data, učí se
nevyhnutelně napodobovat i toto chování, které není žádoucí.
[Studie](https://aclanthology.org/2021.acl-long.416), které zkoumají menší
jazykové modely v reáliích USA, došly k velmi znepokojivým výsledkům. Když to
spojíme s dalším problematickou vlastností všech neuronových sítí, a to je
neprůhlednost modelů, kdy nevíme, proč došlo k nějakému rozhodnutí, dostáváme
se do situace, kdy nevíme, jestli model negeneruje nějaký výstup na základě
rasistických nebo sexistických předsudků, které byly v trénovacích datech.

V odborné komunitě proti používání jazykových modelů hlasitě vystupuje
profesorka Emily Bender z University of Washington. Její argumenty vycházejí z
předpokladu, že jazykový význam je vlastně záměr člověka, který něco říká nebo
píše. Jazykové modely nemají žádný záměr nemají a jenom sofistikovaně v různých
variacích papouškují, co bylo v trénovacích datech. Podle tohoto argumentu pak
není možné bezpečně jazykové modely použít, protože model nemůže vědět, co se
_má nebo nemá_, ale jenom co se _dělá nebo nedělá_. To navíc často čerpá z
toxického prostředí internetu. Svoje argumenty shrnuje v [článku z roku
2020](https://dl.acm.org/doi/10.1145/3442188.3445922). Větší kontroverze než
samotný obsah článku vyvolalo to, že spoluautoři z Googlu, kteří článek
publikovali v rozporu s interními procesy (v jiné verzi v rozporu s obchodními
zájmy) Googlu, [museli firmu
opustit](https://www.wired.com/story/behind-paper-led-google-researchers-firing).
Na základě těchto argumentů dochází k názoru, že jazykové modely a technologie
na nich založené jsou nebezpečné a neměly by se vůbec používat.

Většina odborné komunity tuto radikální kritiku odmítá, a to z různých důvodů.
Například proto, že nesouhlasí s pojetím významu, který profesorka Bender
používá. Jsou ale i [empirické
studie](https://aclanthology.org/2022.findings-emnlp.423), které ukazují, že
některé modely dovedou částečně simulovat vlastnosti, které by při tomto pojetí
významu měly být nedosažitelné. Dalším argumentem je to, že ChatGPT se [nesnaží
jenom papouškovat text z
internetu](https://gist.github.com/yoavg/59d174608e92e845c8994ac2e234c8a9), ale
prostřednictvím zpětnovazebního učení dostat co nejvíce palců nahoru od
anotátorů.

To ale nic nemění na tom, že jazykové modely často velmi nenápadně replikují
rasové, genderové a jiné předsudky z trénovacích dat, a že generují velmi
věrohodně znějící nepravdivé texty. Pokud se s tím nic neudělá a pokud si to
uživatelé nebudou uvědomovat, může to způsobit nemalé společenské škody.
