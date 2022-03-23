quest bossologie_lvl_55 begin
		state start begin
	end
	
	state run begin
		when login or levelup with pc.level >= 55 begin
			set_state(information)
		end
	end

	state information begin
		when letter begin
			send_letter("Bossologie - Èást 3")		
		end

		when info or button begin
			say_title("Bossologie - Èást 3")
			say("V poušti není bezpeèno! ")
			say("Velká pouštní želva dìlá problémy v poušti! ")
			say("Zrodila se želva a bere potravu pouštním živoèíchùm. ")
			say("Mùžeš pomoci pouštím živoèíchùm? ")
			say("Dostaneš Bohatou odmìnu. ")
			say("Tvùj úkol:")
			say_yellow("Zabij 10x Velkou pouštní želvu")
			pc.setqf("state", 10)
			q.set_counter("Velkou pouštní želvu", 10)
			set_state(kill)
		end
	end
	state kill begin
		when 2191.kill begin
			local count = pc.getqf("state") - 1
			if count <= 10 then
				pc.setqf("state", count)
				q.set_counter("Velkou pouštní želvu", count)
			end
			if count == 0 then
				say_title("Bossologie - Èást 3")
				say("Dokonèil jsi úkol!")
				say("")
				say_reward("Obdržíš svou odmìnu. ")
				say_reward("80.000 Yangù ")
				say_reward(" +10 útok (Permanentnì) ")
				pc.change_money(80000)
				affect.add_collect(apply.POINT_ATT_BONUS,10,60*60*24*365*60) 	
				set_quest_state("bossologie_lvl_60", "run")
				clear_letter()
				set_state(__COMPLETE__)
			end
		end
		when letter begin
			send_letter("Bossologie - Èást 3")
		end
		when info or button begin
			say_title("Bossologie - Èást 3")
			say("V poušti není bezpeèno! ")
			say("Velká pouštní želva dìlá problémy v poušti! ")
			say("Zrodila se želva a bere potravu pouštním živoèíchùm. ")
			say("Mùžeš pomoci pouštím živoèíchùm? ")
			say("Dostaneš Bohatou odmìnu. ")
			say("Tvùj úkol:")
			say_yellow("Zbývá znièit: "..pc.getqf("state").." Velkou pouštní želvu. ")
			local count = pc.getqf("state")
			q.set_counter("Velkou pouštní želvu ", count)
		end
	end

	state __COMPLETE__ begin
	end
end