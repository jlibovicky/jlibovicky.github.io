---
layout: post
title: Spellchecking of y and in Czech using deep learning
---

It this post we will have a closer look how can be deep learning used for spell
checking of a particular phenomenon in the Czech language - choosing whether to
write 'i' or 'y'. I have chosen this phenomenon becase even native speaker
sometimes tend make errors in this.  I will try show how we can at least
attempt to solve it using deep learning and demonstrate how a computer
scientist (or a computational linguist) would think about developing a solution
for this problem.

# Jak se to vlastně píše

At the elemntary school, children are tought many more or less complicated
rules of how we choose whether to write 'y' or 'i'. The problem is they are
pronounced in the exactly same way (although it wasn't always the case in the
history). Southern slavic languages as Slovene has reflected that in their
spelling and use 'i' wherever possible. Although it might seem tempting to
simplify the spelling in this way, it has also some unexpected consequences.
This decision some words which are pronounced the same became spelled the same
way and this additional need for disambiguation made reading slower.

The rules Czech children need to acquire are:

* After some consonants, only 'y' or only 'i' can be written. The problem with
  this rule is that sometimes placing 'i' changes the pronounciation of the
  previous consonant, so you need to know in advance how the word is
  pronounced.

* For some words you just need to remember the stem of the word.

* For nouns and adjectives, you need to know to which declination paradigm they
  belong and remember the endings for different grammatical cases in all the
  paradigms.

* shoda podmětu s přísudkem (k tomu musíme umět alespoň základním způsobem umět
  větný rozbor a poznat, co je podmět a co je přísudek),

* vyznat se v tom, kdy pravidla kolidují (píšeme _tácy_, přestože _c_ je měkká
  souhláska, protože skloňujeme podle vzoru _hrad_).

Abychom mohli taková pravidla naprogramovat, museli bychom umět nejdřív udělat
automaticky větný rozbor včetně všech pádů, rodů a čísel, abychom mohli všechna
pravidla použít. Pro představu, jak může větný rozbor fungovat, si můžete
vyzkoušet napříkald
[Treex](https://lindat.mff.cuni.cz/services/treex-web/result/2HfygMLDnvZm63ZX4EF).

Automatické větné analyzátory obvykle spoléhají na to, že věty jsou gramaticky
správně a pokud nejsou, dělá chyby. Vzhledem k tomu, že chceme věty opravovat
je to poměrně nepříjemná vlastnost.

# Trénovací a testovací data

Jakékoli strojové učení vždy potřebuje nějaká data, ze kterých se bude učit. V
případě této úlohy můžeme trénovací data získat velmi snadno tak, že stáhneme z
Internetu větší množství českého textu a budeme doufat, že je z většiny
gramaticky správně. Jednoduše dá stáhnout najednou například celá [česká
Wikipedie](https://dumps.wikimedia.org/cswiki/latest/) v XML formátu.

Text z Wikipedie je ještě potřeba trochu upravit a pročistit. Text se dá
například automaticky rozdělit na věty (knihovna [NLTK](http://www.nltk.org/)
obsahuje i modely pro češtinu). Pro jednoduchost ještě nahradíme všechny znaky,
které nejsou z české abecedy nějakým speciálním symbolem (třeba `_`) —
Wikipedie obsahuje spoustu útržků textů v jiných abecedách. Pro větší
jednoduchost ještě převedeme veškerý text převedeme na malá písmena.

Nyní už zbývá jenom změnit všechna i na měkká a zapamatovat si, kde se mají
změnit na tvrdá. Výsledek může vypadat nějak takto:

*Vstup:*

```txt
aristotelés dále určil poloměr země, kterí ale odhadl na dvojnásobek...
v aristotelovském modelu země stojí a měsíc se sluncem a hvězdami krouží...
mišlenki aristotelovi rozvinul ve 2. století našeho letopočtu klaudios...
```

*Výstup*

```txt
00001000000000000000000000000000001000000100000000000000000000001000000100000...
02000002000100000000200000100000000000000001000000000000000000000001000000000...
00000000000000000010000000000001000002000000000000000000020000000000000000000...
```

V tomu výstupu jednička značí měkké i, dvojka značí y a nula všechny ostatní
znaky. Můžete si prohlédnout kód pro [rozdělení textu na
věty](/assets/code/yi/sentence_split.py) a [přípravu
dat](/assets/code/yi/format_data.py). V době stahování bylo na české Wikipedie
přibližně 5 milionů českých vět.

Když řešíme nějaký problém pomocí strojového učení — a je jedno jestli je to
dnes tak populární hluboké učení nebo jiné metody, je potřeba striktně
oddělovat trénovací a testovací data. Trénovací používáme k naučení modelu.
Když nějaký model vyvíjíme, mělo by nás spíše zajímat, jak si povede, až uvidí
nějaká data, která při trénování neviděl. To se obvykle řeší tak, že si necháme
část dat stranou, model na nich netrénujeme a tato data používáme pouze k tomu,
abychom porovnali, který model je lepší a který je horší. Pro naše další
experimenty si odložíme stranou tisíc vět a ty budeme používat pro testování
našich metod.

# Jednoduchá řešení

Triviálním řešením by bylo všude nechat měkká i. Tímto přístupem se na našich
testovacích dostaneme na krásných __76.4 %__. V počítačové lingvistice (a umělé
inteligenci obecně) se tomu obvykle říká _stanovení baseline_. Aby řešení
nějaké úlohy bylo vůbec nějak zajímavé, je potřeba, aby bylo výrazně lepší, než
nějaké triviální řešení.

Zkusíme se ještě na chvíli u těchto jednoduchých řešení zastavit. Můžeme
například zkusit dávat tvrdé y po tvrdých souhláskách _h_, _ch_ (tedy zase
vlastně _h_), _k_ a _r_. U hlásek _d_, _t_ a _n_ ale nemáme možnost jednoduše
poznat, jestli se mají vyslovovat měkce a má za nimi následovat _i_ nebo tvrdě.

Další pozorování, které můžeme udělat je, že pokud slovo začíná na _vi_/_vy_,
většinou se jedná o předponu _vy_ (Vikingové a lama vikuňa prominou).

|                     |  přesnost |
|:--------------------|----------:|
|všechna měkká        |    76.4 % |
| + tvrdé souhlásky   |    77.5 % |
| + předpona _vy_     |    80.0 % |

S řešením, které se dá napsat na jeden řádek pomocí dvou regulárních výrazů
jsme se dostali na úspěšnost 80.0 %. Kdybychom se nad skupinami hlásek
zamysleli důkladněji a pomohli bychom si důkladnější statistickou analýzou,
zvládli bychom se dostat ještě o několik procent výše.

Místo toho se zastavíme u jiného velmi jednoduchého řešení. Z předchozí části
víme, že máme k dispozici celou Wikipedii jako trénovací data. Můžeme si zkusit
pro každé slovo zaznamenat, kolikrát se vyskytlo s jakým pravopisem. Později,
při testování, použijeme pro každé slovo jeho nejčastější pravopis. Následující
tabulka ukazuje, jaké přesnosti dosáhneme po zpracování určitého množství vět.

| počet přečtených vět  |  přesnost |
|----------------------:|----------:|
|                   500 |    77.9 % |
|                 5 000 |    85.3 % |
|                50 000 |    88.6 % |
|               500 000 |    90.4 % |
|             5 000 000 |    90.8 % |


Vidíme, že s rostoucím množstvím zpracovaného textu roste i úspěšnost modelu.
Není to nic překvapivého. Čím více textu vidíme, tím menší pravděpodobnost je,
že v něm uvidíme nějaká slova, která jsme ještě neviděli.

# Model

Než se dostaneme k podrobnostem, jak takový model funguje, rozmyslíme si, co po
něm vlastně chceme. Určitě po něm chceme, aby pracoval s větší úspěšností než
91% — potom by bylo poměrně zbytečné se s něčím takovým vůbec ztrácet čas.
Jenže také víme, že okolo těch 91% bude ležet hranice, na kterou je možné se
dostat tak, že si zapamatujeme, jak se píše většina slov. Abychom se dostali za
tuto hranici, je nutné, aby se naše neuronová síť naučila alespoň základní
pravidla shody podmětu s přísudkem, kde se lidé neobejdou bez větného rozboru.

Na naši úlohu použijeme rekurentní neuronovou síť. Rekurentní neuronová síť
funguje tak, že pokaždé, když dostane nějaký vstup, provede update svého
vnitřního stavu a vydá nějaký výstup. Schéma kousku sítě rozvinuté v čase
vidíme na následujícím obrázku.

![sequence-labeling](/assets/rnn_cs.svg)

Rekurentní síť dělá v každém kroku (tedy s každým písmenkem) tu samou operaci.
To se může zdát na první pohled zvláštní, ale je to přesně to, co naší síti
chceme. Každé písmeno má jinou naučenou vektoru reprezentaci, a když ji síť
obdrží, rozhodne, co udělá. Vnitřní stav rekurentní sítě je vlastně paměť, kde
si ukládá, jaké vstupy viděla v minulosti a co to znamená pro vstupy, které
mají teprve přijít.

Síť se učí především reprezentovat vstupní písmena a už viděný text takovým
způsobem, aby dokázala dobře plnit svůj úkol. Učení vhodné reprezentace se
často zdůrazňuje jako jedna z nejdůležitějších vlastností hlubokého učení. V
textu nijak nezdůrazňujeme lingvistické koncepty, které nám pomáhají pravopis
nějakým způsobem pojmově uchopit. Je to prostě proud znaků a neuronová síť s
ním musí nějakým způsobem poradit.

Síť ještě vylepšíme jednoduchým trikem. Použijeme nezávisle dvě rekurentní
neuronové sítě. Jedna bude číst text odpředu a bude se snažit odhadnout
pravopis podle toho, co bylo ve větě nalevo od posledního písmene, druhá síť
bude používat to, co bylo napravo od něj.

# Trénování

Rekurentní síť vydává nějaký výstup po přečtení každého z písmen, ale nás zde
zajímají jenom, kde je na vstupu i a máme rozhodnout, jestli je měkké nebo
tvrdé. Výstupy na ostatních místech sítě můžeme ignorovat a zjednodušit si tím
práci.

Na začátku trénování jsou váhy v síti náhodné. V průběhu učení síť vždy přečte
větu, provede svůj odhad a ten porovnáme s tím, co by měla síť vydat do opravdu
a váhy sítě se drobně upraví tak, aby byly blíže tomu, co by síť měla skutečně
vydat.

Pouze z této základní informace se neuronová síť postupně naučí, reprezentovat
vstupní věty tak, aby snadno mohla rozhodovat. Při trénování se nikdy výslovně
neobjevuje pojem slova, souhlásky a samohlásky. Síti nikdo neříká: "Toto je
podmět, protože je v prvním pádě," nepracuje se slovesným rodem, s pády, čísly
a skloňovacími vzory. Všechno to, k čemu jako lidé potřebuje složitá explicitní
pravidla, je schopna během trénování odvodit ze samotných dat.

Naše síť trénovaná na ne příliš výkonné grafické kartě zpracovala 5 milionů vět
za 8 hodin a nakonec dosáhla úspěšnosti __98 %__.


|metoda               |  přesnost |
|:--------------------|----------:|
|všechna měkká        |    70.4 % |
|jednoduchá pravidla  |    80.0 % |
|nejčastější pravopis |    90.8 % |
|neuronová síť        |    98.3 % |

# Co se síť naučila

Nevýhodou neuronových sítí je to, že nemáme možnost nějak jednoduše zjistit, co
se vlastně naučila. Jakousi základní představu si můžeme udělat z takzvaných
učících křivek. To je graf, který má na ose *x* počet použitých trénovacích dat
a na ose *y* úspěšnost modelu.

![sequence-labeling](/assets/rnn_learning_curve_cs.svg)

Z grafu na první pohled vidíme, že neuronová síť potřebovala poměrně dost
trénovacích příkladů na to, aby se naučila dělat něco lepšího, než všude dávat
měkké i. Potřebovala k tomu 13 tisíc vět.

Zatímco algoritmus, který si pamatuje nejčastější pravopis každého slova
potřeboval 1 500 vět k tomu, aby byl úspěšnější, než naše jednoduchá pravidla,
neuronová síť k tomu potřebovala 33 000 trénovacích vět - to je 2200 normostran
textu, více než trojnásobek délky Dostojevského Zločinu a trestu. Síť překonala
pamatování si nejčastějšího pravopisu až po 300 000 větách. Ty by při průměrné
rychlosti čtení 200 slov za minutu trvalo přečíst 17 dní bez přestávky (29
Zločinech a trestech).

Další možností, jak zjistit, co se naše síť naučila, je provést ručně rozbor
chyb na nějakých zajímavých příkladech. My se podíváme na několik vět z
[televizního diktátu Zdeňka Svěráka z roku
2008](http://zpravy.idnes.cz/umite-pravopis-vyplnte-si-sverakuv-diktat-na-idnes-cz-ppd-/domaci.aspx?c=A080829_111241_studium_bar).

* Děti se jako vždycky nejvíc těšily na slavnou velrybí kostru.

|:----------------------|:-------------------------------------------------------------|
|*pravidla*             |Děti se jako vždicky nejvíc těšili na slavnou velrybí kostru. |
|*nejčastější*          |Děti se jako vždycky nejvíc těšili na slavnou velrybí kostru. |
|*neuronová síť (83 %)* |Děti se jako vždicky nejvíc těšili na slavnou velribý kostru. |
|*neuronová síť (92 %)* |Děty se jako vždicky nejvíc těšily na slavnou velribý kostru. |
|*neuronová síť (96 %)* |Děti se jako vždicky nejvíc těšily na slavnou velrybí kostru. |

* Rodiče zase lákaly archeologické nálezy kostěných nástrojů starých kultur.

|:----------------------|:--------------------------------------------------------------------------|
|*pravidla*             |Rodiče zase lákali archeologické nálezi kostěních nástrojů starých kultur. |
|*nejčastější*          |Rodiče zase lákaly archeologické nálezy kostěných nástrojů starých kultur. |
|*neuronová síť (83 %)* |Rodiče zase lákali archeologické nálezi kostěních nástrojů starích kultur. |
|*neuronová síť (92 %)* |Rodiče zase lákaly archeologické nálezi kostěných nástrojů starých kultur. |
|*neuronová síť (96 %)* |Rodiče zase lákaly archeologické nálezy kostěných nástrojů starých kultur. |

* V oddělení nerostů pak byli zaujati třpytivými drahokamy, hýřícími kouzelnými
  barvami.

|:----------------------|:--------------------------------------------------------------------------------------|
|*pravidla*             |V oddělení nerostů pak bili zaujati třpitivími drahokami, hýřícími kouzelními barvami. |
|*nejčastější*          |V oddělení nerostů pak byly zaujati třpytivými drahokamy, hýřícími kouzelnými barvami. |
|*neuronová síť (83 %)* |V oddělení nerostů pak byli zaujati třpitivími drahokami, hířícími kouzelními barvami. |
|*neuronová síť (92 %)* |V oddělení nerostů pak byly zaujati třpitivými drahokami, hýřícími kouzelnými barvami. |
|*neuronová síť (96 %)* |V oddělení nerostů pak byly zaujaty třpitivými drahokami, hířícími kouzelnými barvami. |

* Mezi plazy vás určitě zaujmou krokodýli.

|:----------------------|:----------------------------------------|
|*pravidla*             |Mezi plazi vás určitě zaujmou krokodíli. |
|*nejčastější*          |Mezi plazy vás určitě zaujmou krokodýli. |
|*neuronová síť (83 %)* |Mezi plazi vás určitě zaujmou krokodíli. |
|*neuronová síť (92 %)* |Mezi plazy vás určitě zaujmou krokodíli. |
|*neuronová síť (96 %)* |Mezi plazy vás určitě zaujmou krokodíly. |

Na těchto pár příkladech vidíme, že pravidla, která fungují na 80 % dobře stále
produkují text, který vypadá jako by ho psal téměř analfabet. Deset procent,
které od sebe dělí jednoduchá pravidla a používání nejčastějšího pravopisu na
druhou stranu vytváří dojem, že je text téměř bez chyby. Chyby jsou na místech,
kde je skutečně potřeba využít pravidel o gramatické shodě.

Zkusit nějak interpretovat chování neuronové sítě je podstatně náročnější. V
době, kdy dosahovala úspěšnosti okolo 83 %, dávala na skoro všechna místa měkké
i, kromě dvou případů (*byli* a *velribý*). Za situace, kdy model na větách z
Wikipedie dosahoval úspěšnosti 92 %, vypadají jeho výstupy na našich ukázkových
větách poněkud zmateně. Přestože se jedná o kvantitativně lepší výsledek, než
pamatovat si pro každé slovo nejčastější pravopis, příklady působí jako, že si
model počíná dost náhodně.

Znatelně lepší je situace ve stavu, kdy model dosahoval úspěšnosti 96 %.
Vidíme, že v teno okamžik zvládá shodu podmětu s přísudkem a první dvě věty
jsou bez chyby.  V třetí větě je hned několik chyb, které je nejspíš možné
přisoudit tomu, že slova *třpytivý* a *hýřivý* a jim příbuzná se vyskytují
poměrně řídce a model neměl možnost se je dobře naučit. Potom může chybně
reprezentovat celou větu a dělat chyby i na jiných místech. Z chyby ve slově
*hýřivý* můžeme usuzovat také na to, že spíš než, že by se model naučil seznam
tvrdých souhlásek, spíše bude sám pro sebe učit něco jako vyjmenovaná slova.
Naznačuje to i *krokodíly*, které se v tomto případě tváří podobně jako třeba
slovo *světadíly*.
