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
			send_letter("Bossologie - ��st 6")		
		end

		when info or button begin
			say_title("Bossologie - ��st 6")
			say("V �dol� dra��ho ohn� se nah�z� mocn� Rakshasa! ")
			say("M��e� pomoci j� zab�t? ")
			say("Dostane� Bohatou odm�nu. ")
			say("Tv�j �kol:")
			say_yellow("Zabij 30x Pavou�� Kr�lovna")
			pc.setqf("state", 30)
			q.set_counter("Pavou�� Kr�lovna", 30)
			set_state(kill)
		end
	end
	state kill begin
		when 3290.kill begin
			local count = pc.getqf("state") - 1
			if count <= 30 then
				pc.setqf("state", count)
				q.set_counter("Pavou�� Kr�lovna", count)
			end
			if count == 0 then
				say_title("Bossologie - ��st 6")
				say("Dokon�il jsi �kol!")
				say("")
				say_reward("Obdr�� svou odm�nu. ")
				say_reward("50.000.000 Yang� ")
				say_reward("Kost�m kobry (Permanentn�) ")
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
			send_letter("Bossologie - ��st 6")
		end
		when info or button begin
			say_title("Bossologie - ��st 6")
			say("V �dol� dra��ho ohn� se nah�z� mocn� Rakshasa! ")
			say("M��e� pomoci j� zab�t? ")
			say("Dostane� Bohatou odm�nu. ")
			say("Tv�j �kol:")
			say_yellow("Zb�v� zni�it: "..pc.getqf("state").." Rakshashu ")
			local count = pc.getqf("state")
			q.set_counter("Rakshasa", count)
		end
	end

	state __COMPLETE__ begin
	end
end