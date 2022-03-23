quest sutrologie_lvl_45 begin
		state start begin
	end
	
	state run begin
		when login or levelup with pc.level >= 45 begin
			set_state(information)
		end
	end

	state information begin
		when letter begin
			send_letter("Šutrologie - Èást 10")		
		end

		when info or button begin
			say_title("Šutrologie - Èást 10")
			say("Zemì je pohlcena mnoha Šutry.")
			say("Pomoz nám jich pár znièit.")
			say("Jako odmìnu dostaneš: ")
			say_reward("200.000 Yangù ")
			say_reward("60x Zaèarovat pøedmìt. ")
			say_reward("5x Poehnanı pergamen")
			say_reward("5x Útok draèího boha")
			say_reward("5x Obrana draèího boha")
			say_reward("5x ivot draèího boha")
			say_reward("30x Cor Draconis")
			say_reward("1x Náušnice z draèí kosti 2h")
			say("Tvùj úkol:")
			say_yellow("Zniè 45x Šutr stínu")
			pc.setqf("state", 45)
			q.set_counter("Šutr stínu", 45)
			set_state(kill)
		end
	end
	state kill begin
		when 8009.kill begin
			local count = pc.getqf("state") - 1
			if count <= 45 then
				pc.setqf("state", count)
				q.set_counter("Šutr stínu", count)
			end
			if count == 0 then
				say_title("Šutrologie - Èást 10")
				say("Dokonèil jsi úkol!")
				say("")
				say_reward("Obdríš svou odmìnu. ")
				say_reward("200.000 Yangù ")
				say_reward("60x Zaèarovat pøedmìt. ")
				say_reward("5x Poehnanı pergamen")
				say_reward("5x Útok draèího boha")
				say_reward("5x Obrana draèího boha")
				say_reward("5x ivot draèího boha")
				say_reward("30x Cor Draconis")
				say_reward("1x Náušnice z draèí kosti 2h")
				pc.change_money(200000)
				pc.give_item2(39028, 60)
				pc.give_item2(39028, 5)
				pc.give_item2(71027, 5)
				pc.give_item2(71028, 5)
				pc.give_item2(71030, 5)
				pc.give_item2(50252, 30)
				pc.give_item2(72704, 1)
				set_quest_state("sutrologie_lvl_50", "run")
				clear_letter()
				set_state(__COMPLETE__)
			end
		end
		when letter begin
			send_letter("Šutrologie - Èást 10")
		end
		when info or button begin
			say_title("Šutrologie - Èást 10")
			say("Zemì je pohlcena mnoha Šutry.")
			say("Jako odmìnu dostaneš: ")
			say_reward("200.000 Yangù ")
			say_reward("60x Zaèarovat pøedmìt. ")
			say_reward("5x Poehnanı pergamen")
			say_reward("5x Útok draèího boha")
			say_reward("5x Obrana draèího boha")
			say_reward("5x ivot draèího boha")
			say_reward("30x Cor Draconis")
			say_reward("1x Náušnice z draèí kosti 2h")
			say("Tvùj úkol:")
			say_yellow("Zbıvá znièit: "..pc.getqf("state").." Šutrù. ")
			local count = pc.getqf("state")
			q.set_counter("Šutr stínu", count)
		end
	end

	state __COMPLETE__ begin
	end
end