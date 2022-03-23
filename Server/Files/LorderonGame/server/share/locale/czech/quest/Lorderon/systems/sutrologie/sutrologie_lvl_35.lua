quest sutrologie_lvl_35 begin
		state start begin
	end
	
	state run begin
		when login or levelup with pc.level >= 35 begin
			set_state(information)
		end
	end

	state information begin
		when letter begin
			send_letter("Šutrologie - Èást 7")		
		end

		when info or button begin
			say_title("Šutrologie - Èást 7")
			say("Zemì je pohlcena mnoha Šutry.")
			say("Pomoz nám jich pár znièit.")
			say("Jako odmìnu dostaneš: ")
			say_reward("100.000 Yangù ")
			say_reward("60x Zaèarovat pøedmìt. ")
			say_reward("5x Požehnaný pergamen")
			say_reward("2x Útok draèího boha")
			say_reward("2x Obrana draèího boha")
			say_reward("2x Život draèího boha")
			say_reward("2x Energetický krystal")
			say_reward("10x Cor Draconis")
			say("Tvùj úkol:")
			say_yellow("Zniè 35x Šutr žárlivosti")
			pc.setqf("state", 35)
			q.set_counter("Šutr žárlivosti", 35)
			set_state(kill)
		end
	end
	state kill begin
		when 8007.kill begin
			local count = pc.getqf("state") - 1
			if count <= 35 then
				pc.setqf("state", count)
				q.set_counter("Šutr žárlivosti", count)
			end
			if count == 0 then
				say_title("Šutrologie - Èást 7")
				say("Dokonèil jsi úkol!")
				say("")
				say_reward("Obdržíš svou odmìnu. ")
				say_reward("100.000 Yangù ")
				say_reward("60x Zaèarovat pøedmìt. ")
				say_reward("5x Požehnaný pergamen")
				say_reward("2x Útok draèího boha")
				say_reward("2x Obrana draèího boha")
				say_reward("2x Život draèího boha")
				say_reward("2x Energetický krystal")
				say_reward("10x Cor Draconis")
				pc.change_money(100000)
				pc.give_item2(39028, 60)
				pc.give_item2(39028, 5)
				pc.give_item2(71027, 2)
				pc.give_item2(71028, 2)
				pc.give_item2(71030, 2)
				pc.give_item2(51002, 2)
				pc.give_item2(50252, 10)
				set_quest_state("sutrologie_lvl_40", "run")
				clear_letter()
				set_state(__COMPLETE__)
			end
		end
		when letter begin
			send_letter("Šutrologie - Èást 7")
		end
		when info or button begin
			say_title("Šutrologie - Èást 7")
			say("Zemì je pohlcena mnoha Šutry.")
			say("Jako odmìnu dostaneš: ")
			say_reward("100.000 Yangù ")
			say_reward("60x Zaèarovat pøedmìt. ")
			say_reward("5x Požehnaný pergamen")
			say_reward("2x Útok draèího boha")
			say_reward("2x Obrana draèího boha")
			say_reward("2x Život draèího boha")
			say_reward("2x Energetický krystal")
			say_reward("10x Cor Draconis")
			say("Tvùj úkol:")
			say_yellow("Zbývá znièit: "..pc.getqf("state").." Šutrù. ")
			local count = pc.getqf("state")
			q.set_counter("Šutr žárlivosti", count)
		end
	end

	state __COMPLETE__ begin
	end
end