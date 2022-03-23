quest bossologie_lvl_95 begin
		state start begin
	end
	
	state run begin
		when login or levelup with pc.level >= 95 begin
			set_state(information)
		end
	end

	state information begin
		when letter begin
			send_letter("Bossologie - Èást 6")		
		end

		when info or button begin
			say_title("Bossologie - Èást 6")
			say("V údolí draèího ohnì se nahází mocnı Rakshasa! ")
			say("Mùeš pomoci jí zabít? ")
			say("Dostaneš Bohatou odmìnu. ")
			say("Tvùj úkol:")
			say_yellow("Zabij 30x Pavouèí Královna")
			pc.setqf("state", 30)
			q.set_counter("Pavouèí Královna", 30)
			set_state(kill)
		end
	end
	state kill begin
		when 3290.kill begin
			local count = pc.getqf("state") - 1
			if count <= 30 then
				pc.setqf("state", count)
				q.set_counter("Pavouèí Královna", count)
			end
			if count == 0 then
				say_title("Bossologie - Èást 6")
				say("Dokonèil jsi úkol!")
				say("")
				say_reward("Obdríš svou odmìnu. ")
				say_reward("50.000.000 Yangù ")
				say_reward("Kostım kobry (Permanentní) ")
				local pohlavi = pc.get_sex()
				if pohlavi == 0 then
					pc.give_item2(41309, 1)
				elseif pohlavi == 1 then
					pc.give_item2(41310, 1)
				end
				pc.change_money(50000000)
				set_quest_state("bossologie_lvl_100", "run")				
				clear_letter()
				set_state(__COMPLETE__)
			end
		end
		when letter begin
			send_letter("Bossologie - Èást 6")
		end
		when info or button begin
			say_title("Bossologie - Èást 6")
			say("V údolí draèího ohnì se nahází mocnı Rakshasa! ")
			say("Mùeš pomoci jí zabít? ")
			say("Dostaneš Bohatou odmìnu. ")
			say("Tvùj úkol:")
			say_yellow("Zbıvá znièit: "..pc.getqf("state").." Rakshashu ")
			local count = pc.getqf("state")
			q.set_counter("Rakshasa", count)
		end
	end

	state __COMPLETE__ begin
	end
end