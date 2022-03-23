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
			send_letter("Bossologie - ��st 3")		
		end

		when info or button begin
			say_title("Bossologie - ��st 3")
			say("V pou�ti nen� bezpe�no! ")
			say("Velk� pou�tn� �elva d�l� probl�my v pou�ti! ")
			say("Zrodila se �elva a bere potravu pou�tn�m �ivo��ch�m. ")
			say("M��e� pomoci pou�t�m �ivo��ch�m? ")
			say("Dostane� Bohatou odm�nu. ")
			say("Tv�j �kol:")
			say_yellow("Zabij 10x Velkou pou�tn� �elvu")
			pc.setqf("state", 10)
			q.set_counter("Velkou pou�tn� �elvu", 10)
			set_state(kill)
		end
	end
	state kill begin
		when 2191.kill begin
			local count = pc.getqf("state") - 1
			if count <= 10 then
				pc.setqf("state", count)
				q.set_counter("Velkou pou�tn� �elvu", count)
			end
			if count == 0 then
				say_title("Bossologie - ��st 3")
				say("Dokon�il jsi �kol!")
				say("")
				say_reward("Obdr�� svou odm�nu. ")
				say_reward("80.000 Yang� ")
				say_reward(" +10 �tok (Permanentn�) ")
				pc.change_money(80000)
				affect.add_collect(apply.POINT_ATT_BONUS,10,60*60*24*365*60) 	
				set_quest_state("bossologie_lvl_60", "run")
				clear_letter()
				set_state(__COMPLETE__)
			end
		end
		when letter begin
			send_letter("Bossologie - ��st 3")
		end
		when info or button begin
			say_title("Bossologie - ��st 3")
			say("V pou�ti nen� bezpe�no! ")
			say("Velk� pou�tn� �elva d�l� probl�my v pou�ti! ")
			say("Zrodila se �elva a bere potravu pou�tn�m �ivo��ch�m. ")
			say("M��e� pomoci pou�t�m �ivo��ch�m? ")
			say("Dostane� Bohatou odm�nu. ")
			say("Tv�j �kol:")
			say_yellow("Zb�v� zni�it: "..pc.getqf("state").." Velkou pou�tn� �elvu. ")
			local count = pc.getqf("state")
			q.set_counter("Velkou pou�tn� �elvu ", count)
		end
	end

	state __COMPLETE__ begin
	end
end