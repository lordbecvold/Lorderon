quest bossologie_lvl_40 begin
	state start begin
		when login or levelup with pc.level >= 40 begin
			set_state(information)
		end
	end

	state information begin
		when letter begin
			send_letter("Bossologie - Èást 1")		
		end

		when info or button begin
			say_title("Bossologie - Èást 1")
			say("Ve vesnic vládne temnota! ")
			say("Ve vesnici se usadil brutální velitel, a ohrožuje její obyvatelstvo! ")
			say("Pomoz jim a zniè ho! ")
			say("Odmìna tì nemine.")
			say("Tvùj úkol:")
			say_yellow("Zabij 5x Brutálního velitele")
			pc.setqf("state", 5)
			q.set_counter("Brutálního velitele", 5)
			set_state(kill)
		end
	end
	state kill begin
		when 591.kill begin
			local count = pc.getqf("state") - 1
			if count <= 5 then
				pc.setqf("state", count)
				q.set_counter("Brutálního velitele", count)
			end
			if count == 0 then
				say_title("Bossologie - Èást 1")
				say("Dokonèil jsi úkol!")
				say("")
				say_reward("Obdržíš svou odmìnu. ")
				say_reward("20.000 Yangù ")
				say_reward(" +10 Obrany (Permanentnì) ")
				pc.change_money(20000)
				affect.add_collect(apply.DEF_GRADE_BONUS,10,60*60*24*365*60) 	
				set_quest_state("bossologie_lvl_50", "run")
				clear_letter()
				set_state(__COMPLETE__)
			end
		end
		when letter begin
			send_letter("Bossologie - Èást 1")
		end
		when info or button begin
			say_title("Bossologie - Èást 1")
			say("Ve vesnic vládne temnota! ")
			say("Ve vesnici se usadil brutální velitel, a ohrožuje její obyvatelstvo! ")
			say("Pomoz jim a zniè ho! ")
			say("Odmìna tì nemine.")
			say("Tvùj úkol:")
			say_yellow("Zbývá znièit: "..pc.getqf("state").." Velitelù. ")
			local count = pc.getqf("state")
			q.set_counter("Brutálních velitelù ", count)
		end
	end

	state __COMPLETE__ begin
	end
end