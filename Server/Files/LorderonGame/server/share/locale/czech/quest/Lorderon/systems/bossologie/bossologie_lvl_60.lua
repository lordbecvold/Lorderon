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
			send_letter("Bossologie - ��st 5")		
		end

		when info or button begin
			say_title("Bossologie - ��st 5")
			say("V pavou��m dunegonu se nach�z� Kr�lovna pavouk�! ")
			say("M��e� pomoci j� zab�t? ")
			say("Dostane� Bohatou odm�nu. ")
			say("Tv�j �kol:")
			say_yellow("Zabij 5x Pavou�� Kr�lovna")
			pc.setqf("state", 5)
			q.set_counter("Pavou�� Kr�lovna", 5)
			set_state(kill)
		end
	end
	state kill begin
		when 2091.kill begin
			local count = pc.getqf("state") - 1
			if count <= 5 then
				pc.setqf("state", count)
				q.set_counter("Pavou�� Kr�lovna", count)
			end
			if count == 0 then
				say_title("Bossologie - ��st 5")
				say("Dokon�il jsi �kol!")
				say("")
				say_reward("Obdr�� svou odm�nu. ")
				say_reward("8.000.000 Yang� ")
				say_reward(" +30 �tok (Permanentn�) ")
				pc.change_money(8000000)
				affect.add_collect(apply.POINT_ATT_BONUS,30,60*60*24*365*60) 
				set_quest_state("bossologie_lvl_95", "run")				
				clear_letter()
				set_state(__COMPLETE__)
			end
		end
		when letter begin
			send_letter("Bossologie - ��st 5")
		end
		when info or button begin
			say_title("Bossologie - ��st 5")
			say("V pavou��m dunegonu se nach�z� Kr�lovna pavouk�! ")
			say("M��e� pomoci j� zab�t? ")
			say("Dostane� Bohatou odm�nu. ")
			say("Tv�j �kol:")
			say_yellow("Zb�v� zni�it: "..pc.getqf("state").." Pavou�� Kr�lovna ")
			local count = pc.getqf("state")
			q.set_counter("Pavou�� Kr�lovna", count)
		end
	end

	state __COMPLETE__ begin
	end
end