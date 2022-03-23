quest sutrologie_lvl_5 begin
	state start begin
		when login or levelup with pc.level >= 5 begin
			set_state(information)
		end
	end

	state information begin
		when letter begin
			send_letter("Šutrologie - Èást 1")		
		end

		when info or button begin
			say_title("Šutrologie - Èást 1")
			say("Zemì je pohlcena mnoha Šutry.")
			say("Pomoz nám jich pár znièit.")
			say("Odmìna tì nemine.")
			say("Tvùj úkol:")
			say_yellow("Zniè 5x Šutr smutku")
			pc.setqf("state", 5)
			q.set_counter("Šutr smutku", 5)
			set_state(kill)
		end
	end
	state kill begin
		when 8001.kill begin
			local count = pc.getqf("state") - 1
			if count <= 5 then
				pc.setqf("state", count)
				q.set_counter("Šutr smutku", count)
			end
			if count == 0 then
				say_title("Šutrologie - Èást 1")
				say("Dokonèil jsi úkol!")
				say("")
				say_reward("Obdržíš svou odmìnu. ")
				say_reward("60.000 Yangù ")
				say_reward("10x Zaèarovat pøedmìt. ")
				pc.change_money(60000)
				pc.give_item2(39028, 10)
				set_quest_state("sutrologie_lvl_10", "run")
				clear_letter()
				set_state(__COMPLETE__)
			end
		end
		when letter begin
			send_letter("Šutrologie - Èást 1")
		end
		when info or button begin
			say_title("Šutrologie - Èást 1")
			say("Zemì je pohlcena mnoha Šutry.")
			say("Pomoz nám jich pár znièit.")
			say("Odmìna tì nemine.")
			say("Tvùj úkol:")
			say_yellow("Zbývá znièit: "..pc.getqf("state").." Šutrù. ")
			local count = pc.getqf("state")
			q.set_counter("Šutr smutku", count)
		end
	end

	state __COMPLETE__ begin
	end
end