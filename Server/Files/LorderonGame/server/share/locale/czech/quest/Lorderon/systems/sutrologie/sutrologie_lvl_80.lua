quest sutrologie_lvl_80 begin
		state start begin
	end
	
	state run begin
		when login or levelup with pc.level >= 80 begin
			set_state(information)
		end
	end

	state information begin
		when letter begin
			send_letter("Šutrologie - Èást 17")		
		end

		when info or button begin
			say_title("Šutrologie - Èást 17")
			say("Zemì je pohlcena mnoha Šutry.")
			say("Pomoz nám jich pár znièit.")
			say("Jako odmìnu dostaneš: ")
			say_reward("20.000.000 Yangù ")
			say_reward("500x Zaèarovat pøedmìt. ")
			say_reward("30x Požehnaný pergamen")
			say_reward("30x Útok draèího boha")
			say_reward("30x Obrana draèího boha")
			say_reward("30x Život draèího boha")
			say_reward("80x Cor Draconis")
			say_reward("4x Rituální kámen")
			say_reward("10x Truhla perel")
			say("Tvùj úkol:")
			say_yellow("Zniè 80x Šutr Ma-An")
			pc.setqf("state", 80)
			q.set_counter("Šutr Ma-An", 80)
			set_state(kill)
		end
	end
	state kill begin
		when 8025.kill begin
			local count = pc.getqf("state") - 1
			if count <= 80 then
				pc.setqf("state", count)
				q.set_counter("Šutr Ma-An", count)
			end
			if count == 0 then
				say_title("Šutrologie - Èást 17")
				say("Dokonèil jsi úkol!")
				say("")
				say_reward("20.000.000 Yangù ")
				say_reward("500x Zaèarovat pøedmìt. ")
				say_reward("30x Požehnaný pergamen")
				say_reward("30x Útok draèího boha")
				say_reward("30x Obrana draèího boha")
				say_reward("30x Život draèího boha")
				say_reward("80x Cor Draconis")
				say_reward("4x Rituální kámen")
				say_reward("10x Truhla perel")
				pc.change_money(20000000)
				pc.give_item2(39028, 500)
				pc.give_item2(39028, 30)
				pc.give_item2(71027, 30)
				pc.give_item2(71028, 30)
				pc.give_item2(71030, 30)
				pc.give_item2(50252, 80)
				pc.give_item2(25042, 4)
				pc.give_item2(50135, 10)
				set_quest_state("sutrologie_lvl_85", "run")
				clear_letter()
				set_state(__COMPLETE__)
			end
		end
		when letter begin
			send_letter("Šutrologie - Èást 16")
		end
		when info or button begin
			say_title("Šutrologie - Èást 17")
			say("Zemì je pohlcena mnoha Šutry.")
			say("Jako odmìnu dostaneš: ")
			say_reward("20.000.000 Yangù ")
			say_reward("500x Zaèarovat pøedmìt. ")
			say_reward("30x Požehnaný pergamen")
			say_reward("30x Útok draèího boha")
			say_reward("30x Obrana draèího boha")
			say_reward("30x Život draèího boha")
			say_reward("80x Cor Draconis")
			say_reward("4x Rituální kámen")
			say_reward("10x Truhla perel")
			say("Tvùj úkol:")
			say_yellow("Zbývá znièit: "..pc.getqf("state").." Šutrù. ")
			local count = pc.getqf("state")
			q.set_counter("Šutr Ma-An", count)
		end
	end

	state __COMPLETE__ begin
	end
end