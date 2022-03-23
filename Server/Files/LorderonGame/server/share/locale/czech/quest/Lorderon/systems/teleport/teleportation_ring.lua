quest teleportation_ring begin
	state start begin
		when 70007.use or 9012.click or 20009.click begin
			say_size(350, 380)
			say_title("Teleportace")
			local map = pc.get_map_index()
			local level = pc.get_level()
			local empire = pc.get_empire()
			say("Tak kam chceš cestovat?")
			say("Èím vıší úrovnì dosáhneš, tím více lokací bude v nabídce.")
			if level >= 1 and level < 25 then
				sub_set = select(
				"Svìt šutrù 1-90 Lvl. ", 
				"Oblast Joan 1-15 Lvl. ", 
				"Oblast Yayang 1-15 Lvl. ", 
				"Vesnice 15-35 Lvl. ", 
				"Asi se mi nikam nechce")
				if sub_set == 5 then
					return
				end
			elseif level >= 25 and level < 35 then
				sub_set = select(
				"Svìt šutrù 1-90 Lvl. ", 
				"Oblast Joan 1-15 Lvl. ", 
				"Oblast Yayang 1-15 Lvl. ", 
				"Vesnice 15-35 Lvl. ", 
				"Pouš 30-50 Lvl", 
				"Údolí orkù 30-45 Lvl", 
				"Ledová zem 30-55 Lvl", 
				"Asi se mi nikam nechce")
				if sub_set == 8 then
					return
				end
			elseif level >= 35 and level < 45 then
				sub_set = select(
				"Svìt šutrù 1-90 Lvl. ", 
				"Oblast Joan 1-15 Lvl. ", 
				"Oblast Yayang 1-15 Lvl. ", 
				"Vesnice 15-35 Lvl. ", 
				"Pouš 30-50 Lvl", 
				"Údolí orkù 30-45 Lvl", 
				"Ledová zem 30-55 Lvl", 
				"Pavouèí Dungeon 35-55 Lvl", 
				"Asi se mi nikam nechce")
				if sub_set == 9 then
					return
				end
			elseif level >= 45 and level < 55 then
				sub_set = select(
				"Svìt šutrù 1-90 Lvl. ", 
				"Oblast Joan 1-15 Lvl. ", 
				"Oblast Yayang 1-15 Lvl. ", 
				"Vesnice 15-35 Lvl. ", 
				"Pouš 30-50 Lvl", 
				"Údolí orkù 30-45 Lvl", 
				"Ledová zem 30-55 Lvl", 
				"Pavouèí Dungeon 35-55 Lvl", 
				"Chrám-Hwang 45-55 Lvl", 
				"Asi se mi nikam nechce")
				if sub_set == 10 then
					return
				end
			elseif level >= 55 and level < 75 then
				sub_set = select(
				"Svìt šutrù 1-90 Lvl. ", 
				"Oblast Joan 1-15 Lvl. ", 
				"Oblast Yayang 1-15 Lvl. ", 
				"Vesnice 15-35 Lvl. ", 
				"Pouš 30-50 Lvl", 
				"Údolí orkù 30-45 Lvl", 
				"Ledová zem 30-55 Lvl", 
				"Pavouèí Dungeon 35-55 Lvl", 
				"Chrám-Hwang 45-55 Lvl", 
				"Ohnivá zem (65-75) Lvl",
				"Zelenı les (65-75) Lvl",
				"Asi se mi nikam nechce")
				if sub_set == 12 then
					return
				end
			elseif level >= 75 and level < 90 then
				sub_set = select(
				"Svìt šutrù 1-90 Lvl. ", 
				"Oblast Joan 1-15 Lvl. ", 
				"Oblast Yayang 1-15 Lvl. ", 
				"Vesnice 15-35 Lvl. ", 
				"Pouš 30-50 Lvl", 
				"Údolí orkù 30-45 Lvl", 
				"Ledová zem 30-55 Lvl", 
				"Pavouèí Dungeon 35-55 Lvl", 
				"Chrám-Hwang 45-55 Lvl", 
				"Ohnivá zem (65-75) Lvl",
				"Zelenı les (65-75) Lvl",
				"Èervenı les (75-90) Lvl",
				"Jeskynì vyhnanství (75-90) Lvl",
				"Asi se mi nikam nechce")
				if sub_set == 14 then
					return
				end
			elseif level >= 90 and level < 95 then
				sub_set = select(
				"Svìt šutrù 1-90 Lvl. ", 
				"Oblast Joan 1-15 Lvl. ", 
				"Oblast Yayang 1-15 Lvl. ", 
				"Vesnice 15-35 Lvl. ", 
				"Pouš 30-50 Lvl", 
				"Údolí orkù 30-45 Lvl", 
				"Ledová zem 30-55 Lvl", 
				"Pavouèí Dungeon 35-55 Lvl", 
				"Chrám-Hwang 45-55 Lvl", 
				"Ohnivá zem (65-75) Lvl",
				"Zelenı les (65-75) Lvl",
				"Èervenı les (75-90) Lvl",
				"Jeskynì vyhnanství (75-90) Lvl",
				"Záliv draèího ohnì (90-105) Lvl",
				"Bouøné hory (90-105) Lvl",
				"Nefritovı záliv (90-105) Lvl",
				"Útes guatama (90-105) Lvl",
				"Asi se mi nikam nechce")
				if sub_set == 18 then
					return
				end
			elseif level >= 95 then
				sub_set = select(
				"Svìt šutrù 1-90 Lvl. ", 
				"Oblast Joan 1-15 Lvl. ", 
				"Oblast Yayang 1-15 Lvl. ", 
				"Vesnice 15-35 Lvl. ", 
				"Pouš 30-50 Lvl", 
				"Údolí orkù 30-45 Lvl", 
				"Ledová zem 30-55 Lvl", 
				"Pavouèí Dungeon 35-55 Lvl", 
				"Chrám-Hwang 45-55 Lvl", 
				"Ohnivá zem (65-75) Lvl",
				"Zelenı les (65-75) Lvl",
				"Èervenı les (75-90) Lvl",
				"Jeskynì vyhnanství (75-90) Lvl",
				"Záliv draèího ohnì (90-105) Lvl",
				"Bouøné hory (90-105) Lvl",
				"Nefritovı záliv (90-105) Lvl",
				"Útes guatama (90-105) Lvl",
				"Zakletı les (95-120) Lvl",
				"Asi se mi nikam nechce")
				if sub_set == 19 then
					return
				end
			end

			local warplist = 
			{
				{{256000, 665600}, {256000, 665600}, {256000, 665600},},
				{{63800, 166400}, {63800, 166400}, {63800, 166400},},
				{{474300, 954800}, {474300, 954800}, {474300, 954800},},
				{{819200, 204800}, {819200, 204800}, {819200, 204800},},
				{{204800, 486400}, {204800, 486400}, {204800, 486400},},
				{{634800, 843600}, {634800, 843600}, {634800, 843600},},
				{{358400, 153600}, {358400, 153600}, {358400, 153600},},
				{{51200, 486400}, {51200, 486400}, {51200, 486400},},
				{{537600, 51200}, {537600, 51200}, {537600, 51200},},
				{{588800, 614400}, {588800, 614400}, {588800, 614400},},
				{{281600, 0}, {281600, 0}, {281600, 0},},
				{{1049600, 0}, {1049600, 0}, {1049600, 0},},
				{{153600, 1203200}, {153600, 1203200}, {153600, 1203200},},
				{{1024000, 1664000}, {1024000, 1664000}, {1024000, 1664000},},
				{{1126400, 1510400}, {1126400, 1510400}, {1126400, 1510400},},
				{{1049600, 1510400}, {1049600, 1510400}, {1049600, 1510400},},
				{{1177600, 1664000}, {1177600, 1664000}, {1177600, 1664000},},
				{{768000, 1408000}, {768000, 1408000}, {768000, 1408000},},
			}
			pc.warp(warplist[sub_set][empire][1], warplist[sub_set][empire][2])
		end
	end
end
