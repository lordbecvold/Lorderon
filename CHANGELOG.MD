-----------------------------------------------------------------------------------------------------
Lorderon game changelog [CZ]
-----------------------------------------------------------------------------------------------------
22.10.2019
-Obnovena práce na serveru.
-Připraven testovaví server.
-Přepracován Pack v clientu.

23.10.2019
-Optimalizován pack clientu.
-Odstraněny nesmyslné komentáře v codu (Python části clientu).

24.10.2019
-Optimalizován zdrojový kod clientu (Odstraněny nesmyslné komentáře a části kodu).
-Opraveny sysery v clientu.
-Optimalizován client odstraněny záseky při načítání hry.
-Odstraněna hudba z nastavené systému.
-Opraveny chyby pádu hry a ????? chyba.
-Opravena nekompatibilita clientu pro windows 7-SP1
-Odstraněna doba trvání u schopností v popisu v clientu.
-Opraveny brnění pro 105 lvl sury (Ž)
-Kompletně dokončena optimalizace clientu a opraveny všechny známé bugy.
-Dokončen pack systém pro Lorderon obsah clientu.
-Opraveny drobné chyby v interfacu hry (CVBN/Okno cechu).

25.10.2019
-Optimalizace serverfiles (Odstraněny mrtvé časti codu a nesmyslné komentáře).
-Odstraněn kompletní obsah serveru (Mob drop,special_item_g, atd).
-Přepracován systém configu přístupu k databázy atd.
-Nastaven test_server mode pro debug.
-Upraven systém kanálů a jejich jader pro lepší funkčnost a změnšení zátěže na server.
-Odstraněny všechny Questy včetně funkčních scriptů.
-Opravena chyba připojení k databázy po záloze serveru.
-Opravena chyba ztráty spojení serveru a databáze při restartu ch99.
-Odstraněny zbytečné hlášky serveru.
-Ostraněny zbytečné tabulky v databázy.
-Pročištěna databáze kompletně promazány tabulky.
-Smazán itemShop sklad z inventáře.
-Optimalizován zdrojový kod databáze (Odstraněny nesmyslné komentáře a mrtvé části kodu).
-Optimalizován zdrojový kod hry (Odstraněny nesmyslné komentáře a mrtvé části kodu).

26.10.2019
-Nový login select a create interface.
-Efekt označující bosse.
-Systém čtení kamenů duše.
-Ignor low buf systém.
-Odstraněno omezení yangů v obchodování a zvíšeny sloty na 24.
-Oznámení clientu při přijmu pm.
-Při oživení postavy Dostane hráč max_hp
-Nekonečno šípů.
-Nový efekt pro kritický zásah.
-Systém ochrany safezony proti mobům.
-Odstraněny vlajky říše u npc.

25.03.2020
-Nainstalován server na nové vps a compiler.
-Dokončen web + registrace a propojení do databáze

30.03.2020
-Effect otravy u zb hráče a target menu moba
-Nastaveno přídávání bonusu pouze na zesílit předmět
-Opraven bug zasekávání myši při minimalizaci clientu.
-Odstraněny mapy.
-Připraveny předměty pro začátečníky.
-Implementován mount systém.
-Implementován pet systém.
-Implementován skill select systém
-Opraven bug zasekávání myši při minimalizaci clientu.
-Opraveno černání obrazovky v uzavřených mapách.

1.4.2020
-Dokončen systém čtení schopností + nový systém čtení kamenů duše.
-Odstraněny přebytečné npc

2.4.2020
-Nastaveny první mapy
-Nastaveny start itemy
-Nastaveny základní shopy
-Kompletně dokončen web a zabezpečení webu

3.4.2020
-Nastavena dračí alchymie
-Odstraněn expand inventář u opasku
-Nastaven shop s účesy
-Metinland
-nastavená druhá mapa 
-Nastaveno kování
-implementovány questy na metiny 

4.4.2020
-Otestován průběh hrou do lvl 35

5.4.2020
-Opraveny chyby zjištěny při testování
-Implementován systém doporučení (Rady po doexpení určitých úrovní)
-Změněn herní config a konfigurační aplikace.
-Opravena chyba aury meče a čepeke (Po teleportu se aktivuje)
-Přidána možnost nasadat na mounta během útoku.
-Port systém (Tab)

6.4.2020
-Implementován Special storage system (Uppky, knihy, kameny)

8.4.2020
-Snižen regen brutálního velitele.
-Přenastaveny dopy za questy.
-Nastaveny dropy truhly kamenu.
-Zvednut MAX_GOLD
-Implementován switchbot

9.4.2020
-Implementován sash system by LenT(ACCE_SYSTEM)

10.4.2020
-Remove fog settings.
-Chest drop opening.
-Fixed pozadí popisku.
-Přidán target element icon

11.4.2020
-Přidán Obchod na tavby.
-Přidán Quest na brutálního velitele.
-Přidán systém Energie (Krystal energie).
-navýšeny odměny za šutrologii.
-Přeloženo skill_proto.
-Nové vzhledy schopností
-Navýšen max status na 100
-Vylepšeno okno pm.
-Nový systém vylepšování.

12.4.2020
-Automatické přepínání Dne a noci.
-Opraveno vytváření postav CreatePacket.

13.4.2020
-Opraven F4 slot 
-Opravena dračí alcha
-Opravena vesnice
-Odebrán drop orchideomeče
-Dokončen web 
-Přidány HP do target UI

14.4.2020
-Přidány nové mapy (Údolí orků, poušť, Ledová zem)
-Přidány nové questy na šutrologii a bossologii
-Přidán drop k šutrům 40, 45, 50 a 55 lvl
-Přidán drop k bossům Vrchní ork, Pouštní želva a Devítiocas
-Odebrány obrany u Pouštní želvy 
-Po dokončení úrovně 55 hráč dostane MH.
-Přidán drop k mobům do map (Údolí orků, poušť, Ledová zem)
-Navýšen čas u alchymiie dračích kamenů 
-Biolog lvl 30, 40 a 50.
-Přidáno kování šperků a brnění (Překov z ebenů, smrtka železky a štítu 21)
-Opravena průchodnost ve Vesnici.
-Přidán davanced duel system

15.4.2020
-Opraven system šerp
-Odstupňování legendární alchymie podle úrovně 50, 60, 70, 80 a 90

16.4.2020
-Přidáno další kování věcí a drop uppek.
-Přidány nové kameny (legendární stupěn) a jejich kování.
-Nový mounti a peti 35 lvl 55 lvl.
-Implementován opičí dungeon pro drop uppek na mounty a pety.

17.4.2020
-Přidána mapa Chrám-Hwang
-Přidány dropy a spawny metinu pádu
-Přidán quest šutrologie na metiny pádu
-Přidány questy na pavoučí královnu a žlutého tygra
-Přidány kostýmy jako odměnu za quest na metiny pádu.
-Optimalizován teleportační systém.
-Opraven model animace Královské šerpy u postavy ninja(ž)
-Opraven bug zasekávání postavy při relogu
-Implementován systém pro blokaci cheat enginu
-Nové kování věcí pro zbraně a brnění 45 a 55 lvl překov zbraní lvl 30.
-Nastaven drop uppek pro kování věcí 45 a 55lvl do chrámu hwang a k mmetinům 60
-Přidán item_vum do popisku itemu (Pro GM)
-Odebrány obrany pouštním liškám
-Přidány mapy pavoučí dungeon 2 a 3 + Spawn bossů.
-Implementována věž démonů.
-Implementována mapa Ohnivá zem.

18.4.2020
-Přidáno kování věcí zbraně 75, Bska štíty 61 + přidán štít na pvm, Kování helem 60 a šperků krystalu duše + Upraveny bony na pvm
-Nastaven drop předmětů do truhel do věže + drop bossů.
-Nastaven drop k démonům do věže.
-Nastaven drop metinům 65 a 70 + questy na ně (Odměny kostýmy)
-Nastaven drop v ohnivce
-Nastavena mapa Zelený les
-Přidán biolog lvl 60 a 70
-Implementován opičí dungeon 2 55-75 Lvl.
-Nový stupeň petů a mountů od úrovně 75
-Implementován game button sidebar

20.4.2020
-Implementován Maintenance system
-Implementován effect pro pláště statečnosti
-Implementován Profesional Biolog systém 

21.4.2020
-Implementována tabulka bonusů
-Implementováno automatické vylepšování alchymie

22.4.2020
-Implementována rychlá změna výbavy
-Implementováno nastavení pro rychlejší kování věcí 
-Vylepšen button sidebar 
-Nové logo + effect pro GM.
-Přidán GM list do Seznamu prátel
-Přepracován systém šutrologie (Zpracování questu, odměny + musí mít hráč dokončené předchozí questy aby mohl dělat nové)
-Opraveny animace zbraní po minimalizování clientu se resetují.
-Opraven bug aury meče effect se aplikuje při každém použití
-Opraven slot pro kostým (Nepřekrývá se s šerpu v pvp eq systému)

23.4.2020
-Implementován lepší systém bossologie 
-Přidán + nastaven červený les
-Implementovány watery 1 a 2 + nastaven drop 
-Nastaven drop a kování zbraní 65 kování až do 90lvl
-Nastaveno kování wodek
-Dokončen základní postup hrou do úrovně 90.

-25.4.2020
-Register a discord server button v login screenu
-Počet ch nastaven na 6 (Pro test_server pouze na 3)
-Implementována změna ch
-Nový systém ukládání dat (Vše se ukládá do registerů)

26.4.2020
-Nastaven exp na polovinu
-Přidán systém oznámení při přihlášení přítele
-Opravny nevyditelné gui

-27.4.2020
-Opraven slot pro opasek a nastaveno kování opasků
-Přidáno tlačítko pro tabulku bonusů
-Implementován systém pro nákup kuliček proměny.
-Opraveny bugy interfacu hry webu + patcheru

5.5.2020
-Opraven bug přepisování předmětů při nákupu z offline stánků.
-Přidán nový pet a mount od úrovně 90, Opičí dungeon 75-90 Lvl (Obtížnost druhého a třetího dungeonu se bude upravovat podle testování)

7.5.2020
-Implementovány a nastaveny mapy 90 + Zakletý les, Nemere a Razador dungeon
-Nastaveno kování zbraní 105
-Nastaveno kování brnění 105
-Nastaven drop a kování helem na útok a odolnost.
-Nastaveno kování opasků až po úrověn 105
-Nastaveno kování titanu.
-Nastaveno kování pvm šperků a ohnivek
-Nastaveno kování a drop pvp šperků a oceánek + Pvp opasky
-Nastaven drop metinům v mapách 90+
-Nastaven drop příšerám a bossům v mapách úrovně 90.
-Nastaveno kompletní kování drop exp do lvl 120.
-Opraven bug kování šerp.
-Dokončen systém doporučení.
-Implementován pvm set dračího boha (Zbraně od lvlu 105) (Brnění od lvlu 120).

9.5.2020
-Opraveno pár bugů v druhé vesnici.
-Opraveno pozadí pro yang drop okno

10.5.2020
-Nastaven drop tabulek pro biologa 
-Upraven drop pro truhlu perel + kousky kamene se třídí do external invu.
-Opraveno bugování předmětů v iventáři
-Nastaveny úrovně pro dungeony
1)Opičí dung 1 - 35-55 lvl 
2)Opičí dung 2 - 55-75 lvl
3)Opičí dung 3 - 75-95 lvl
4)Modrý drak 75 - 105 lvl
5)Razador 100 - 120 lvl
6)Nemere 100 - 120 lvl
-Možnost procházek skrze offline stánky

12.5.2020
-Upraven systém pro správu cechů.
-Přidány nové informační questy k npc pacholek a biolog.
-Implementován systém titulů 
-barva enemy dropu red
-hide object

-----------------------------------------------------------------------------------------------------