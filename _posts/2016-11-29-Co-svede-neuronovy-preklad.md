---
layout: post
title: Co dovede neuronový překlad?
---

Před rokem jsem na konferenci [EMNLP v Lisabonu](http://www.emnlp2015.org/)
zahlédl článek, který se jmenoval [On Statistical Machine Translation and
Translation
Theory](http://www.emnlp2015.org/proceedings/DiscoMT/pdf/DiscoMT22.pdf) (O
statistickém strojovém překladu a teorii překladu) od Christiana Hardmeiera.
    Stál před svým posterem a každému, kdo se u jeho posteru zastavil se skoro
omlouval, že jeho příspěvek není o nějaké metodě, která zlepšuje stávají
statistický strojový překlad — a je to _pouhá_ reflexe toho, co dělá
statistický překlad z pohledu translatologie. Bohužel tento zajímavý článek
vyšel v momentě, kdy se začalo ukazovat, že statistický strojový překlad bude
brzy nahrazen překladači založenými na neuronových sítích. Je to jen pár dní,
co Google oznámil, že ve svém [Google Translate nasazuje neuronový strojový
překlad](https://research.googleblog.com/2016/09/a-neural-network-for-machine.html).

V tomto příspěvku se tedy společně podíváme na to, co se změnilo z hlediska
teorie překladu s příchodem neuronového strojového překladu, a na to, co by to
pro neuronový strojový překlad mohlo znamenat do budoucna.

## Nakládáme s významem

Na překlad se tradičně pohlíží jako na nějaký proces, při kterém se zachovává
význam, ať je význam cokoli. Díváme se na text jako na něco, co má význam samo
o sobě a význam celku postupně skládáme z významu jednolitých částí textu (slov
či víceslovných ustálených frází). Tváříme se, že význam je _kompozicionální_.

Pokud by to tak skutečně bylo, byl by statistický frázový strojový překlad
(způsob, jakým se strojový překlad dělal doteď), pravděpodobně nejlepším možným
způsobem, jak k automatickému překladu přistoupit. Pro statistický strojový
překlad je ústředním pojmem slovní zarovnání (word alignment). Z velkých
paralelních korpusů extrahujeme, jak se slova nebo celé skupiny slov nejčastěji
překládají do druhého jazyka. To je takzvaný _překladový model_, dovede slovům
a frázím přiřadit jejich pravděpodobné překlady. Úkolem překladového modelu je
zachovat význam stavebních prvků textu.

Kromě překladového modelu používají statistické překladové systémy ještě další
model, takzvaný _jazykový model_. Jeho úkolem je zajistit, aby se z překladů
jednotlivých slov a frází nakonec sestavila gramaticky správná a plynulá věta.
Úkolem jazykového modelu je postarat se o kompozici významu.

K významu lze ale přistoupit jaksi z druhé strany — často nazývané _kulturální
pohled_. Každý text je nějakým pokusem o komunikaci. Autor textu se snaží něco
říct svým čtenářům, nějak na něj působí (informuje ho, chce změnit jeho
chování, pobavit atd.). Text sám o sobě žádný význam nemá (není to koneckonců
nic než dlouhá série podivných obrázků, kterým říkáme písmena), svůj význam
dostává až tehdy, když ho někdo čte — a právě v tento moment se komunikace
završuje. Na rozdíl od představy, že slova mají význam sama o sobě a jejich
skládáním dostaneme skutečný význam celého textu, komunikace se vždy odehrává
v nějakém kontextu — fyzickém, psychologickém, sociálním. Je to v konečném
důsledku sám čtenář, kdo vytváří význam toho, co čte. Záměr autora se buď
uskuteční nebo také ne.

Překlad z jazyka do jazyka je potom také určitým způsobem komunikace.
Překladatel vezme (zkonstruuje ve svém vlastním kontextu) význam věty ve
zdrojovém jazyce (komunikace s původním autorem) a přepíše jej do cílového
jazyka, kdy mu čtenář opět přiřadí nějaký význam. Statistický strojový překlad
něco takového ani vzdáleně nedělá — ale ten neuronový by to mohl alespoň
simulovat.

Tento zajímavý pohled na význam pochází z knihy _How to do Things with Words_
z roku 1955 od britského filozofa Johna Austina. Jeho myšlenky zásadním
způsobem ovlivnily pohled na význam a komunikaci a stály například u zrodu
takzvaných kulturálních studií v šedesátých letech, která se zaměřovala
především na masovou komunikaci.

## Neuronový překlad je jiný

Klasický statistický strojový překlad nejprve odhadne překlady pro slova a
víceslovné fráze ve zdrojové větě (slova s pokud možno stejným významem).
V dalším kroku se z nich snaží vybudovat smysluplnou větu, kdy se snaží co
nejlépe vyvážit mnoho protichůdných podmínek: vybrat nejadekvátnější překlady;
každé slovo by mělo být přeloženo právě jednou; slova ve výsledné větě by měla
být přibližně v podobném pořadí jako ve zdrojové větě; věta by měla být co
nejplynulejší; a takto bychom mohli vymyslet ještě celou řadu dalších kritérií.
Tímto způsobem se automatický překlad prováděl od konce devadesátých let do
dneška.

Tento přístup byl v nedávné době překonán překladem založeným na neuronových
sítích. Překladač větu ve zdrojovém jazyce pomocí jedné rekurentní neuronové sítě,
enkodéru, zakóduje do vektoru reálných čísel. Následně z této reprezentace
pomocí další rekurentní neuronové sítě, dekodéru, vygeneruje větu v cílovém
jazyce. Můžeme si to představit jako jeden stroj, který postupně čte slova
vstupní věty a při tom mění svůj vnitřní stav, který je reprezentovaný vektorem
reálných čísel. Potom, co skončí, předá informaci o svém vnitřním stavu druhému
stroji, který postupně vydává slova v cílovém jazyce a s každým slovem také
změní svůj vnitřní stav (ten tedy vždy kóduje zbytek věty). V praxi je postup
generování o něco složitější — používá se takzvaný beam search. To si můžeme
představit tak, že spustíme několik dekodérů paralelně a v průběhu generování
cílové věty vždy pracujeme s několika hypotézami současně a nakonec z nich
vybereme tu nejlepší. Pokročilejší neuronové modely používají ještě takzvaný
_attention model_. S jeho pomocí se může dekodér v průběhu dekódovaní zaměřovat
na konkrétní slova ze vstupní věty.

![Neural translation animation](/assets/nmt.gif)

Při uvažování o fungování neuronových překladových systémů se můžeme zcela
obejít bez pojmu významové ekvivalence slov a frází napříč jazyky a představy
kompozicionality významů. Obsah vstupní věty se celý zakóduje do číselného
vektoru, který se potom použije k vygenerování věty v cílovém jazyce.

V předchozí části jsem psal o tom, že význam není vytvářen pouze tím, co je
v textu napsáno, ale také kontextem, v jakém se nachází. I to je možné
v neuronových systémech zohlednit. Už teď existují metody, jak lze číselnými
vektory reprezentovat celé texty (používají se například pro podobnostní
vyhledávání nebo analýzu sentimetu). Pokud bychom například dávali takový
vektor jako další vstup neuronovému překladači, dokázal by se s dostatkem dat
naučit využívat i lingvistický kontext jednotlivých vět, v kterém se nutně
odráží i psychologický a sociální kontext textů. Jednotlivé sociální skupiny
používají jazyk odlišně (mají své sociolekty), různé způsoby vyjádření se
používají při různých příležitostech — to vše se v textech jaksi jen mimochodem
odráží. Způsob, jak se vypořádat s různými kontexty vznikl i v rámci
statistického strojového překladu — říká se mu doménová adaptace. V tomto
případě je ale nutné mít samostatné systémy pro každou z domén (např. sportovní
zpravodajství, odborné texty pro lékaře atd.).

## A co dál?

Neuronový strojový překlad je stále velice mladý a pravděpobně existuje velký
prostor pro zlepšení. Podobně jako v předchozím paradigmatu, lidé přicházejí se
stále novými triky, jak systém lépe trénovat. Výzkumníci a vývojáři každý rok
poměřují síly na soutěži [Workshop on Machine
Translation](http://www.statmt.org/wmt16/).

Jako velice slibný směr ve výzkumu strojového překladu se jeví vícejazyčné
metody. [Google nedávno publikoval metodu](https://arxiv.org/abs/1611.04558),
jak lze naučit strojový překlad pro jazykový pár, pro který je velmi málo
trénovacích dat, ale bylo možné je propojit přes jiné jazykové páry. V konečném
důsledku by potom data jakákoli dvojjazyčná data mohlo být použita ku prospěchu
překladu mezi všemi jazyky navzájem.
