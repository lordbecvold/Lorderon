quest sutrologie_lvl_25 begin
		state start begin
	end
	
	state run begin
		when login or levelup with pc.level >= 25 begin
			set_state(information)
		end
	end

	state information begin
		when letter begin
			send_letter("Šutrologie - Èást 5")		
		end

		when info or button begin
			say_title("Šutrologie - Èást 5")
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
			say("Tvùj úkol:")
			say_yellow("Zniè 25x Šutr èernoty")
			pc.setqf("state", 25)
			q.set_counter("Šutr èernoty", 25)
			set_state(kill)
		end
	end
	state kill begin
		when 8005.kill begin
			local count = pc.getqf("state") - 1
			if count <= 25 then
				pc.setqf("state", count)
				q.set_counter("Šutr èernoty", count)
			end
			if count == 0 then
				say_title("Šutrologie - Èást 5")
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
				pc.change_money(90000)
				pc.give_item2(39028, 35)
				pc.give_item2(39028, 5)
				pc.give_item2(71027, 2)
				pc.give_item2(71028, 2)
				pc.give_item2(71030, 2)
				pc.give_item2(72314, 3)
				set_quest_state("sutrologie_lvl_30", "run")
				clear_letter()
				set_state(__COMPLETE__)
			end
		end
		when letter begin
			send_letter("Šutrologie - Èást 5")
		end
		when info or button begin
			say_title("Šutrologie - Èást 5")
			say("Zemì je pohlcena mnoha Šutry.")
			say("Jako odmìnu dostaneš: ")
			say_reward("90.000 Yangù ")
			say_reward("35x Zaèarovat pøedmìt. ")
			say_reward("5x Poehnanı pergamen")
			say_reward("2x Útok draèího boha")
			say_reward("2x Obrana draèího boha")
			say_reward("2x ivot draèího boha")
			say_reward("3x Pergamen draka")
			say("Tvùj úkol:")
			say_yellow("Zbıvá znièit: "..pc.getqf("state").." Šutrù. ")
			local count = pc.getqf("state")
			q.set_counter("Šutr èernoty", count)
		end
	end

	state __COMPLETE__ begin
	end
end