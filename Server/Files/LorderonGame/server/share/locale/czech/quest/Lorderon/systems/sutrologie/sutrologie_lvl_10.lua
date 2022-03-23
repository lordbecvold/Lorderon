quest sutrologie_lvl_10 begin
		state start begin
	end
	
	state run begin
		when login or levelup with pc.level >= 10 begin
			set_state(information)
		end
	end

	state information begin
		when letter begin
			send_letter("Šutrologie - Èást 2")		
		end

		when info or button begin
			say_title("Šutrologie - Èást 2")
			say("Zemì je pohlcena mnoha Šutry.")
			say("Pomoz nám jich pár znièit.")
			say_reward("Kostým pro zaèáteèníky na 7 dnù ")
			say("Tvùj úkol:")
			say_yellow("Zniè 10x Šutr boje")
			pc.setqf("state", 10)
			q.set_counter("Šutr boje", 10)
			set_state(kill)
		end
	end
	state kill begin
		when 8002.kill begin
			local count = pc.getqf("state") - 1
			if count <= 10 then
				pc.setqf("state", count)
				q.set_counter("Šutr boje", count)
			end
			if count == 0 then
				say_title("Šutrologie - Èást 2")
				say("Dokonèil jsi úkol!")
				say("")
				say_reward("Obdržíš svou odmìnu. ")
				say_reward("60.000 Yangù ")
				say_reward("15x Zaèarovat pøedmìt. ")
				say_reward("Kostým pro zaèáteèníky na 7 dnù ")
				pc.change_money(60000)
				pc.give_item2(39028, 10)
				local pohlavi = pc.get_sex()
				if pohlavi == 0 then
					pc.give_item2(41003, 1)
				elseif pohlavi == 1 then
					pc.give_item2(41004, 1)
				end
				set_quest_state("sutrologie_lvl_15", "run")
				clear_letter()
				set_state(__COMPLETE__)
			end
		end
		when letter begin
			send_letter("Šutrologie - Èást 2")
		end
		when info or button begin
			say_title("Šutrologie - Èást2")
			say("Zemì je pohlcena mnoha Šutry.")
			say("Jako odmìnu dostaneš kostým pro zaèáteèníky")
			say("Tvùj úkol:")
			say_yellow("Zbývá znièit: "..pc.getqf("state").." Šutrù. ")
			local count = pc.getqf("state")
			q.set_counter("Šutr boje", count)
		end
	end

	state __COMPLETE__ begin
	end
end