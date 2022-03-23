quest sutrologie_lvl_20 begin
		state start begin
	end
	
	state run begin
		when login or levelup with pc.level >= 20 begin
			set_state(information)
		end
	end

	state information begin
		when letter begin
			send_letter("Šutrologie - Èást 4")		
		end

		when info or button begin
			say_title("Šutrologie - Èást 4")
			say("Zemì je pohlcena mnoha Šutry.")
			say("Pomoz nám jich pár znièit.")
			say("Jako odmìnu dostaneš: ")
			say_reward("80.000 Yangù ")
			say_reward("35x Zaèarovat pøedmìt. ")
			say_reward("5x Požehnaný pergamen")
			say_reward("2x Útok draèího boha")
			say_reward("2x Obrana draèího boha")
			say_reward("2x Život draèího boha")
			say("Tvùj úkol:")
			say_yellow("Zniè 20x Šutr laènosti")
			pc.setqf("state", 20)
			q.set_counter("Šutr laènosti", 20)
			set_state(kill)
		end
	end
	state kill begin
		when 8004.kill begin
			local count = pc.getqf("state") - 1
			if count <= 20 then
				pc.setqf("state", count)
				q.set_counter("Šutr laènosti", count)
			end
			if count == 0 then
				say_title("Šutrologie - Èást 4")
				say("Dokonèil jsi úkol!")
				say("")
				say_reward("Obdržíš svou odmìnu. ")
				say_reward("80.000 Yangù ")
				say_reward("35x Zaèarovat pøedmìt. ")
				say_reward("5x Požehnaný pergamen")
				say_reward("2x Útok draèího boha")
				say_reward("2x Obrana draèího boha")
				say_reward("2x Život draèího boha")
				pc.change_money(80000)
				pc.give_item2(39028, 35)
				pc.give_item2(39028, 5)
				pc.give_item2(71027, 2)
				pc.give_item2(71028, 2)
				pc.give_item2(71030, 2)
				set_quest_state("sutrologie_lvl_25", "run")
				clear_letter()
				set_state(__COMPLETE__)
			end
		end
		when letter begin
			send_letter("Šutrologie - Èást 4")
		end
		when info or button begin
			say_title("Šutrologie - Èást 4")
			say("Zemì je pohlcena mnoha Šutry.")
			say("Jako odmìnu dostaneš: ")
			say_reward("80.000 Yangù ")
			say_reward("35x Zaèarovat pøedmìt. ")
			say_reward("5x Požehnaný pergamen")
			say_reward("2x Útok draèího boha")
			say_reward("2x Obrana draèího boha")
			say_reward("2x Život draèího boha")
			say("Tvùj úkol:")
			say_yellow("Zbývá znièit: "..pc.getqf("state").." Šutrù. ")
			local count = pc.getqf("state")
			q.set_counter("Šutr laènosti", count)
		end
	end

	state __COMPLETE__ begin
	end
end