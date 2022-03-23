quest sutrologie_lvl_40 begin
		state start begin
	end
	
	state run begin
		when login or levelup with pc.level >= 40 begin
			set_state(information)
		end
	end

	state information begin
		when letter begin
			send_letter("Šutrologie - Èást 8")		
		end

		when info or button begin
			say_title("Šutrologie - Èást 8")
			say("Zemì je pohlcena mnoha Šutry.")
			say("Pomoz nám jich pár znièit.")
			say("Jako odmìnu dostaneš: ")
			say_reward("130.000 Yangù ")
			say_reward("60x Zaèarovat pøedmìt. ")
			say_reward("5x Požehnaný pergamen")
			say_reward("5x Útok draèího boha")
			say_reward("5x Obrana draèího boha")
			say_reward("5x Život draèího boha")
			say_reward("30x Cor Draconis")
			say("Tvùj úkol:")
			say_yellow("Zniè 40x Šutr duše")
			pc.setqf("state", 40)
			q.set_counter("Šutr duše", 40)
			set_state(kill)
		end
	end
	state kill begin
		when 8008.kill begin
			local count = pc.getqf("state") - 1
			if count <= 40 then
				pc.setqf("state", count)
				q.set_counter("Šutr duše", count)
			end
			if count == 0 then
				say_title("Šutrologie - Èást 8")
				say("Dokonèil jsi úkol!")
				say("")
				say_reward("Obdržíš svou odmìnu. ")
				say_reward("130.000 Yangù ")
				say_reward("60x Zaèarovat pøedmìt. ")
				say_reward("5x Požehnaný pergamen")
				say_reward("5x Útok draèího boha")
				say_reward("5x Obrana draèího boha")
				say_reward("5x Život draèího boha")
				say_reward("30x Cor Draconis")
				pc.change_money(130000)
				pc.give_item2(39028, 60)
				pc.give_item2(39028, 5)
				pc.give_item2(71027, 5)
				pc.give_item2(71028, 5)
				pc.give_item2(71030, 5)
				pc.give_item2(50252, 30)
				set_quest_state("sutrologie_lvl_45", "run")
				clear_letter()
				set_state(__COMPLETE__)
			end
		end
		when letter begin
			send_letter("Šutrologie - Èást 8")
		end
		when info or button begin
			say_title("Šutrologie - Èást 8")
			say("Zemì je pohlcena mnoha Šutry.")
			say("Jako odmìnu dostaneš: ")
			say_reward("130.000 Yangù ")
			say_reward("60x Zaèarovat pøedmìt. ")
			say_reward("5x Požehnaný pergamen")
			say_reward("5x Útok draèího boha")
			say_reward("5x Obrana draèího boha")
			say_reward("5x Život draèího boha")
			say_reward("30x Cor Draconis")
			say("Tvùj úkol:")
			say_yellow("Zbývá znièit: "..pc.getqf("state").." Šutrù. ")
			local count = pc.getqf("state")
			q.set_counter("Šutr duše", count)
		end
	end

	state __COMPLETE__ begin
	end
end