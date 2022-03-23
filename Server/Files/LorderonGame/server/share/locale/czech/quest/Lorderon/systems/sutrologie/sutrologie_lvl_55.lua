quest sutrologie_lvl_55 begin
		state start begin
	end
	
	state run begin
		when login or levelup with pc.level >= 55 begin
			set_state(information)
		end
	end

	state information begin
		when letter begin
			send_letter("Šutrologie - Èást 12")		
		end

		when info or button begin
			say_title("Šutrologie - Èást 12")
			say("Zemì je pohlcena mnoha Šutry.")
			say("Pomoz nám jich pár znièit.")
			say("Jako odmìnu dostaneš: ")
			say_reward("1.000.000 Yangù ")
			say_reward("60x Zaèarovat pøedmìt. ")
			say_reward("5x Poehnanı pergamen")
			say_reward("5x Útok draèího boha")
			say_reward("5x Obrana draèího boha")
			say_reward("5x ivot draèího boha")
			say_reward("30x Cor Draconis")
			say_reward("1x Amulet vìèné lásky 7 dnù ")
			say("Tvùj úkol:")
			say_yellow("Zniè 55x Šutr ïábla")
			pc.setqf("state", 55)
			q.set_counter("Šutr ïábla", 55)
			set_state(kill)
		end
	end
	state kill begin
		when 8011.kill begin
			local count = pc.getqf("state") - 1
			if count <= 55 then
				pc.setqf("state", count)
				q.set_counter("Šutr ïábla", count)
			end
			if count == 0 then
				say_title("Šutrologie - Èást 12")
				say("Dokonèil jsi úkol!")
				say("")
				say_reward("Obdríš svou odmìnu. ")
				say_reward("1.000.000 Yangù ")
				say_reward("60x Zaèarovat pøedmìt. ")
				say_reward("5x Poehnanı pergamen")
				say_reward("5x Útok draèího boha")
				say_reward("5x Obrana draèího boha")
				say_reward("5x ivot draèího boha")
				say_reward("30x Cor Draconis")
				say_reward("1x Amulet vìèné lásky 7 dnù ")
				pc.change_money(1000000)
				pc.give_item2(39028, 60)
				pc.give_item2(39028, 5)
				pc.give_item2(71027, 5)
				pc.give_item2(71028, 5)
				pc.give_item2(71030, 5)
				pc.give_item2(50252, 40)
				pc.give_item2(71145, 1)
				set_quest_state("sutrologie_lvl_60", "run")
				clear_letter()
				set_state(__COMPLETE__)
			end
		end
		when letter begin
			send_letter("Šutrologie - Èást 12")
		end
		when info or button begin
			say_title("Šutrologie - Èást 12")
			say("Zemì je pohlcena mnoha Šutry.")
			say("Jako odmìnu dostaneš: ")
			say_reward("1.000.000 Yangù ")
			say_reward("60x Zaèarovat pøedmìt. ")
			say_reward("5x Poehnanı pergamen")
			say_reward("5x Útok draèího boha")
			say_reward("5x Obrana draèího boha")
			say_reward("5x ivot draèího boha")
			say_reward("30x Cor Draconis")
			say_reward("1x Amulet vìèné lásky 7 dnù ")
			say("Tvùj úkol:")
			say_yellow("Zbıvá znièit: "..pc.getqf("state").." Šutrù. ")
			local count = pc.getqf("state")
			q.set_counter("Šutr ïábla", count)
		end
	end

	state __COMPLETE__ begin
	end
end