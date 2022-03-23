quest bossologie_lvl_40 begin
	state start begin
		when login or levelup with pc.level >= 40 begin
			set_state(information)
		end
	end

	state information begin
		when letter begin
			send_letter("Bossologie - ��st 1")		
		end

		when info or button begin
			say_title("Bossologie - ��st 1")
			say("Ve vesnic vl�dne temnota! ")
			say("Ve vesnici se usadil brut�ln� velitel, a ohro�uje jej� obyvatelstvo! ")
			say("Pomoz jim a zni� ho! ")
			say("Odm�na t� nemine.")
			say("Tv�j �kol:")
			say_yellow("Zabij 5x Brut�ln�ho velitele")
			pc.setqf("state", 5)
			q.set_counter("Brut�ln�ho velitele", 5)
			set_state(kill)
		end
	end
	state kill begin
		when 591.kill begin
			local count = pc.getqf("state") - 1
			if count <= 5 then
				pc.setqf("state", count)
				q.set_counter("Brut�ln�ho velitele", count)
			end
			if count == 0 then
				say_title("Bossologie - ��st 1")
				say("Dokon�il jsi �kol!")
				say("")
				say_reward("Obdr�� svou odm�nu. ")
				say_reward("20.000 Yang� ")
				say_reward(" +10 Obrany (Permanentn�) ")
				pc.change_money(20000)
				affect.add_collect(apply.DEF_GRADE_BONUS,10,60*60*24*365*60) 	
				set_quest_state("bossologie_lvl_50", "run")
				clear_letter()
				set_state(__COMPLETE__)
			end
		end
		when letter begin
			send_letter("Bossologie - ��st 1")
		end
		when info or button begin
			say_title("Bossologie - ��st 1")
			say("Ve vesnic vl�dne temnota! ")
			say("Ve vesnici se usadil brut�ln� velitel, a ohro�uje jej� obyvatelstvo! ")
			say("Pomoz jim a zni� ho! ")
			say("Odm�na t� nemine.")
			say("Tv�j �kol:")
			say_yellow("Zb�v� zni�it: "..pc.getqf("state").." Velitel�. ")
			local count = pc.getqf("state")
			q.set_counter("Brut�ln�ch velitel� ", count)
		end
	end

	state __COMPLETE__ begin
	end
end