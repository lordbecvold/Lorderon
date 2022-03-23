quest sutrologie_lvl_65 begin
		state start begin
	end
	
	state run begin
		when login or levelup with pc.level >= 65 begin
			set_state(information)
		end
	end

	state information begin
		when letter begin
			send_letter("Šutrologie - Èást 14")		
		end

		when info or button begin
			say_title("Šutrologie - Èást 14")
			say("Zemì je pohlcena mnoha Šutry.")
			say("Pomoz nám jich pár znièit.")
			say("Jako odmìnu dostaneš: ")
			say_reward("5.000.000 Yangù ")
			say_reward("300x Zaèarovat pøedmìt. ")
			say_reward("30x Poehnanı pergamen")
			say_reward("30x Útok draèího boha")
			say_reward("30x Obrana draèího boha")
			say_reward("30x ivot draèího boha")
			say_reward("80x Cor Draconis")
			say("Tvùj úkol:")
			say_yellow("Zniè 65x Šutr smrti")
			pc.setqf("state", 65)
			q.set_counter("Šutr smrti", 65)
			set_state(kill)
		end
	end
	state kill begin
		when 8013.kill begin
			local count = pc.getqf("state") - 1
			if count <= 65 then
				pc.setqf("state", count)
				q.set_counter("Šutr smrti", count)
			end
			if count == 0 then
				say_title("Šutrologie - Èást 14")
				say("Dokonèil jsi úkol!")
				say("")
				say_reward("Obdríš svou odmìnu. ")
				say_reward("5.000.000 Yangù ")
				say_reward("300x Zaèarovat pøedmìt. ")
				say_reward("30x Poehnanı pergamen")
				say_reward("30x Útok draèího boha")
				say_reward("30x Obrana draèího boha")
				say_reward("30x ivot draèího boha")
				say_reward("80x Cor Draconis")
				pc.change_money(5000000)
				pc.give_item2(39028, 300)
				pc.give_item2(39028, 30)
				pc.give_item2(71027, 30)
				pc.give_item2(71028, 30)
				pc.give_item2(71030, 30)
				pc.give_item2(50252, 80)
				set_quest_state("sutrologie_lvl_70", "run")
				clear_letter()
				set_state(__COMPLETE__)
			end
		end
		when letter begin
			send_letter("Šutrologie - Èást 14")
		end
		when info or button begin
			say_title("Šutrologie - Èást 14")
			say("Zemì je pohlcena mnoha Šutry.")
			say("Jako odmìnu dostaneš: ")
			say_reward("5.000.000 Yangù ")
			say_reward("300x Zaèarovat pøedmìt. ")
			say_reward("30x Poehnanı pergamen")
			say_reward("30x Útok draèího boha")
			say_reward("30x Obrana draèího boha")
			say_reward("30x ivot draèího boha")
			say_reward("80x Cor Draconis")
			say("Tvùj úkol:")
			say_yellow("Zbıvá znièit: "..pc.getqf("state").." Šutrù. ")
			local count = pc.getqf("state")
			q.set_counter("Šutr smrti", count)
		end
	end

	state __COMPLETE__ begin
	end
end