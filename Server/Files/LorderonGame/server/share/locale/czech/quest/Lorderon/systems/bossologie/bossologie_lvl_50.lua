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
			send_letter("Bossologie - ��st 2")		
		end

		when info or button begin
			say_title("Bossologie - ��st 2")
			say("�dol� ork� ovl�dl dra�� b�h! ")
			say("V �dol� ork� vl�dne stoupenec dra��ho boha Vrchn� ork! ")
			say("Jeho zabit�m pom��e� k osvobozen� or��ho �dol�. ")
			say("Dostane� Bohatou odm�nu. ")
			say("Tv�j �kol:")
			say_yellow("Zabij 10x Vrchn�ho orka")
			pc.setqf("state", 10)
			q.set_counter("Vrchn�ho orka", 10)
			set_state(kill)
		end
	end
	state kill begin
		when 691.kill begin
			local count = pc.getqf("state") - 1
			if count <= 10 then
				pc.setqf("state", count)
				q.set_counter("Vrchn�ho orka", count)
			end
			if count == 0 then
				say_title("Bossologie - ��st 2")
				say("Dokon�il jsi �kol!")
				say("")
				say_reward("Obdr�� svou odm�nu. ")
				say_reward("80.000 Yang� ")
				say_reward(" +20 Obrany (Permanentn�) ")
				pc.change_money(80000)
				affect.add_collect(apply.DEF_GRADE_BONUS,20,60*60*24*365*60) 	
				set_quest_state("bossologie_lvl_55", "run")
				clear_letter()
				set_state(__COMPLETE__)
			end
		end
		when letter begin
			send_letter("Bossologie - ��st 2")
		end
		when info or button begin
			say_title("Bossologie - ��st 1")
			say("�dol� ork� ovl�dl dra�� b�h! ")
			say("V �dol� ork� vl�dne stoupenec dra��ho boha Vrchn� ork! ")
			say("Jeho zabit�m pom��e� k osvobozen� or��ho �dol�. ")
			say("Dostane� Bohatou odm�nu. ")
			say("Tv�j �kol:")
			say_yellow("Zb�v� zni�it: "..pc.getqf("state").." V�dc� ork�. ")
			local count = pc.getqf("state")
			q.set_counter("V�dce ork� ", count)
		end
	end

	state __COMPLETE__ begin
	end
end