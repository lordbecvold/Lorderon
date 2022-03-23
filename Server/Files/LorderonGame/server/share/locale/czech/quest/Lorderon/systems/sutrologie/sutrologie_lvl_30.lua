quest sutrologie_lvl_30 begin
		state start begin
	end
	
	state run begin
		when login or levelup with pc.level >= 30 begin
			set_state(information)
		end
	end

	state information begin
		when letter begin
			send_letter("Šutrologie - Èást 6")		
		end

		when info or button begin
			say_title("Šutrologie - Èást 6")
			say("Zemì je pohlcena mnoha Šutry.")
			say("Pomoz nám jich pár znièit.")
			say("Jako odmìnu dostaneš: ")
			say_reward("90.000 Yangù ")
			say_reward("35x Zaèarovat pøedmìt. ")
			say_reward("5x Poehnanı pergamen")
			say_reward("2x Útok draèího boha")
			say_reward("2x Obrana draèího boha")
			say_reward("2x ivot draèího boha")
			say_reward("3x Pergamen draka")
			say_reward("10x Cor Draconis")
			say("Tvùj úkol:")
			say_yellow("Zniè 30x Šutr tmy")
			pc.setqf("state", 30)
			q.set_counter("Šutr tmy", 30)
			set_state(kill)
		end
	end
	state kill begin
		when 8006.kill begin
			local count = pc.getqf("state") - 1
			if count <= 30 then
				pc.setqf("state", count)
				q.set_counter("Šutr tmy", count)
			end
			if count == 0 then
				say_title("Šutrologie - Èást 6")
				say("Dokonèil jsi úkol!")
				say("")
				say_reward("Obdríš svou odmìnu. ")
				say_reward("90.000 Yangù ")
				say_reward("35x Zaèarovat pøedmìt. ")
				say_reward("5x Poehnanı pergamen")
				say_reward("2x Útok draèího boha")
				say_reward("2x Obrana draèího boha")
				say_reward("2x ivot draèího boha")
				say_reward("3x Pergamen draka")
				say_reward("10x Cor Draconis")
				pc.change_money(90000)
				pc.give_item2(39028, 35)
				pc.give_item2(39028, 5)
				pc.give_item2(71027, 2)
				pc.give_item2(71028, 2)
				pc.give_item2(71030, 2)
				pc.give_item2(72314, 3)
				pc.give_item2(50252, 10)
				set_quest_state("sutrologie_lvl_35", "run")
				clear_letter()
				set_state(__COMPLETE__)
			end
		end
		when letter begin
			send_letter("Šutrologie - Èást 6")
		end
		when info or button begin
			say_title("Šutrologie - Èást 6")
			say("Zemì je pohlcena mnoha Šutry.")
			say("Jako odmìnu dostaneš: ")
			say_reward("90.000 Yangù ")
			say_reward("35x Zaèarovat pøedmìt. ")
			say_reward("5x Poehnanı pergamen")
			say_reward("2x Útok draèího boha")
			say_reward("2x Obrana draèího boha")
			say_reward("2x ivot draèího boha")
			say_reward("3x Pergamen draka")
			say_reward("10x Cor Draconis")
			say("Tvùj úkol:")
			say_yellow("Zbıvá znièit: "..pc.getqf("state").." Šutrù. ")
			local count = pc.getqf("state")
			q.set_counter("Šutr tmy", count)
		end
	end

	state __COMPLETE__ begin
	end
end