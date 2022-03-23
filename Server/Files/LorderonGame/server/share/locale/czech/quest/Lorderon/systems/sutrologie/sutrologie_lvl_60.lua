quest sutrologie_lvl_60 begin
		state start begin
	end
	
	state run begin
		when login or levelup with pc.level >= 60 begin
			set_state(information)
		end
	end

	state information begin
		when letter begin
			send_letter("Šutrologie - Èást 13")		
		end

		when info or button begin
			say_title("Šutrologie - Èást 13")
			say("Zemì je pohlcena mnoha Šutry.")
			say("Pomoz nám jich pár znièit.")
			say("Jako odmìnu dostaneš: ")
			say_reward("2.000.000 Yangù ")
			say_reward("100x Zaèarovat pøedmìt. ")
			say_reward("5x Požehnaný pergamen")
			say_reward("5x Útok draèího boha")
			say_reward("5x Obrana draèího boha")
			say_reward("5x Život draèího boha")
			say_reward("30x Cor Draconis")
			say("Tvùj úkol:")
			say_yellow("Zniè 60x Šutr pádu")
			pc.setqf("state", 60)
			q.set_counter("Šutr pádu", 60)
			set_state(kill)
		end
	end
	state kill begin
		when 8012.kill begin
			local count = pc.getqf("state") - 1
			if count <= 60 then
				pc.setqf("state", count)
				q.set_counter("Šutr pádu", count)
			end
			if count == 0 then
				say_title("Šutrologie - Èást 13")
				say("Dokonèil jsi úkol!")
				say("")
				say_reward("Obdržíš svou odmìnu. ")
				say_reward("2.000.000 Yangù ")
				say_reward("100x Zaèarovat pøedmìt. ")
				say_reward("5x Požehnaný pergamen")
				say_reward("5x Útok draèího boha")
				say_reward("5x Obrana draèího boha")
				say_reward("5x Život draèího boha")
				say_reward("30x Cor Draconis")
				pc.change_money(2000000)
				pc.give_item2(39028, 100)
				pc.give_item2(39028, 5)
				pc.give_item2(71027, 5)
				pc.give_item2(71028, 5)
				pc.give_item2(71030, 5)
				pc.give_item2(50252, 40)
				set_quest_state("sutrologie_lvl_65", "run")
				clear_letter()
				set_state(__COMPLETE__)
			end
		end
		when letter begin
			send_letter("Šutrologie - Èást 13")
		end
		when info or button begin
			say_title("Šutrologie - Èást 13")
			say("Zemì je pohlcena mnoha Šutry.")
			say("Jako odmìnu dostaneš: ")
			say_reward("2.000.000 Yangù ")
			say_reward("100x Zaèarovat pøedmìt. ")
			say_reward("5x Požehnaný pergamen")
			say_reward("5x Útok draèího boha")
			say_reward("5x Obrana draèího boha")
			say_reward("5x Život draèího boha")
			say_reward("30x Cor Draconis")
			say("Tvùj úkol:")
			say_yellow("Zbývá znièit: "..pc.getqf("state").." Šutrù. ")
			local count = pc.getqf("state")
			q.set_counter("Šutr pádu", count)
		end
	end

	state __COMPLETE__ begin
	end
end