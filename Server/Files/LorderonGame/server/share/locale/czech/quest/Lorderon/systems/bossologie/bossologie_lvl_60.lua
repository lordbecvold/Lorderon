quest bossologie_lvl_60 begin
		state start begin
	end
	
	state run begin
		when login or levelup with pc.level >= 60 begin
			set_state(information)
		end
	end

	state information begin
		when letter begin
			send_letter("Bossologie - Èást 5")		
		end

		when info or button begin
			say_title("Bossologie - Èást 5")
			say("V pavouèím dunegonu se nachází Královna pavoukù! ")
			say("Mùeš pomoci jí zabít? ")
			say("Dostaneš Bohatou odmìnu. ")
			say("Tvùj úkol:")
			say_yellow("Zabij 5x Pavouèí Královna")
			pc.setqf("state", 5)
			q.set_counter("Pavouèí Královna", 5)
			set_state(kill)
		end
	end
	state kill begin
		when 2091.kill begin
			local count = pc.getqf("state") - 1
			if count <= 5 then
				pc.setqf("state", count)
				q.set_counter("Pavouèí Královna", count)
			end
			if count == 0 then
				say_title("Bossologie - Èást 5")
				say("Dokonèil jsi úkol!")
				say("")
				say_reward("Obdríš svou odmìnu. ")
				say_reward("8.000.000 Yangù ")
				say_reward(" +30 útok (Permanentnì) ")
				pc.change_money(8000000)
				affect.add_collect(apply.POINT_ATT_BONUS,30,60*60*24*365*60) 
				set_quest_state("bossologie_lvl_95", "run")				
				clear_letter()
				set_state(__COMPLETE__)
			end
		end
		when letter begin
			send_letter("Bossologie - Èást 5")
		end
		when info or button begin
			say_title("Bossologie - Èást 5")
			say("V pavouèím dunegonu se nachází Královna pavoukù! ")
			say("Mùeš pomoci jí zabít? ")
			say("Dostaneš Bohatou odmìnu. ")
			say("Tvùj úkol:")
			say_yellow("Zbıvá znièit: "..pc.getqf("state").." Pavouèí Královna ")
			local count = pc.getqf("state")
			q.set_counter("Pavouèí Královna", count)
		end
	end

	state __COMPLETE__ begin
	end
end