quest bossologie_lvl_50 begin
		state start begin
	end
	
	state run begin
		when login or levelup with pc.level >= 50 begin
			set_state(information)
		end
	end

	state information begin
		when letter begin
			send_letter("Bossologie - Èást 2")		
		end

		when info or button begin
			say_title("Bossologie - Èást 2")
			say("Údolí orkù ovládl draèí bùh! ")
			say("V Údolí orkù vládne stoupenec draèího boha Vrchní ork! ")
			say("Jeho zabitím pomùžeš k osvobození orèího údolí. ")
			say("Dostaneš Bohatou odmìnu. ")
			say("Tvùj úkol:")
			say_yellow("Zabij 10x Vrchního orka")
			pc.setqf("state", 10)
			q.set_counter("Vrchního orka", 10)
			set_state(kill)
		end
	end
	state kill begin
		when 691.kill begin
			local count = pc.getqf("state") - 1
			if count <= 10 then
				pc.setqf("state", count)
				q.set_counter("Vrchního orka", count)
			end
			if count == 0 then
				say_title("Bossologie - Èást 2")
				say("Dokonèil jsi úkol!")
				say("")
				say_reward("Obdržíš svou odmìnu. ")
				say_reward("80.000 Yangù ")
				say_reward(" +20 Obrany (Permanentnì) ")
				pc.change_money(80000)
				affect.add_collect(apply.DEF_GRADE_BONUS,20,60*60*24*365*60) 	
				set_quest_state("bossologie_lvl_55", "run")
				clear_letter()
				set_state(__COMPLETE__)
			end
		end
		when letter begin
			send_letter("Bossologie - Èást 2")
		end
		when info or button begin
			say_title("Bossologie - Èást 1")
			say("Údolí orkù ovládl draèí bùh! ")
			say("V Údolí orkù vládne stoupenec draèího boha Vrchní ork! ")
			say("Jeho zabitím pomùžeš k osvobození orèího údolí. ")
			say("Dostaneš Bohatou odmìnu. ")
			say("Tvùj úkol:")
			say_yellow("Zbývá znièit: "..pc.getqf("state").." Vùdcù orkù. ")
			local count = pc.getqf("state")
			q.set_counter("Vùdce orkù ", count)
		end
	end

	state __COMPLETE__ begin
	end
end