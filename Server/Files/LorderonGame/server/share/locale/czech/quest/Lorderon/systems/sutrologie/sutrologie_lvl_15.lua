quest sutrologie_lvl_15 begin
		state start begin
	end
	
	state run begin
		when login or levelup with pc.level >= 15 begin
			set_state(information)
		end
	end

	state information begin
		when letter begin
			send_letter("Šutrologie - Èást 3")		
		end

		when info or button begin
			say_title("Šutrologie - Èást 3")
			say("Zemì je pohlcena mnoha Šutry.")
			say("Pomoz nám jich pár znièit.")
			say("Jako odmìnu dostaneš: ")
			say_reward("70.000 Yangù ")
			say_reward("30x Zaèarovat pøedmìt. ")
			say_reward("5x Požehnaný pergamen")
			say("Tvùj úkol:")
			say_yellow("Zniè 15x Šutr bitvy")
			pc.setqf("state", 15)
			q.set_counter("Šutr bitvy", 15)
			set_state(kill)
		end
	end
	state kill begin
		when 8003.kill begin
			local count = pc.getqf("state") - 1
			if count <= 15 then
				pc.setqf("state", count)
				q.set_counter("Šutr bitvy", count)
			end
			if count == 0 then
				say_title("Šutrologie - Èást 3")
				say("Dokonèil jsi úkol!")
				say("")
				say_reward("Obdržíš svou odmìnu. ")
				say_reward("70.000 Yangù ")
				say_reward("30x Zaèarovat pøedmìt. ")
				say_reward("5x Požehnaný pergamen")
				pc.change_money(70000)
				pc.give_item2(39028, 30)
				pc.give_item2(39028, 5)
				set_quest_state("sutrologie_lvl_20", "run")
				clear_letter()
				set_state(__COMPLETE__)
			end
		end
		when letter begin
			send_letter("Šutrologie - Èást 3")
		end
		when info or button begin
			say_title("Šutrologie - Èást3")
			say("Zemì je pohlcena mnoha Šutry.")
			say("Jako odmìnu dostaneš: ")
			say_reward("70.000 Yangù ")
			say_reward("30x Zaèarovat pøedmìt. ")
			say_reward("5x Požehnaný pergamen")
			say("Tvùj úkol:")
			say_yellow("Zbývá znièit: "..pc.getqf("state").." Šutrù. ")
			local count = pc.getqf("state")
			q.set_counter("Šutr bitvy", count)
		end
	end

	state __COMPLETE__ begin
	end
end