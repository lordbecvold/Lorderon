quest sutrologie_lvl_10 begin
		state start begin
	end
	
	state run begin
		when login or levelup with pc.level >= 10 begin
			set_state(information)
		end
	end

	state information begin
		when letter begin
			send_letter("�utrologie - ��st 2")		
		end

		when info or button begin
			say_title("�utrologie - ��st 2")
			say("Zem� je pohlcena mnoha �utry.")
			say("Pomoz n�m jich p�r zni�it.")
			say_reward("Kost�m pro za��te�n�ky na 7 dn� ")
			say("Tv�j �kol:")
			say_yellow("Zni� 10x �utr boje")
			pc.setqf("state", 10)
			q.set_counter("�utr boje", 10)
			set_state(kill)
		end
	end
	state kill begin
		when 8002.kill begin
			local count = pc.getqf("state") - 1
			if count <= 10 then
				pc.setqf("state", count)
				q.set_counter("�utr boje", count)
			end
			if count == 0 then
				say_title("�utrologie - ��st 2")
				say("Dokon�il jsi �kol!")
				say("")
				say_reward("Obdr�� svou odm�nu. ")
				say_reward("60.000 Yang� ")
				say_reward("15x Za�arovat p�edm�t. ")
				say_reward("Kost�m pro za��te�n�ky na 7 dn� ")
				pc.change_money(60000)
				pc.give_item2(39028, 10)
				local pohlavi = pc.get_sex()
				if pohlavi == 0 then
					pc.give_item2(41003, 1)
				elseif pohlavi == 1 then
					pc.give_item2(41004, 1)
				end
				set_quest_state("sutrologie_lvl_15", "run")
				clear_letter()
				set_state(__COMPLETE__)
			end
		end
		when letter begin
			send_letter("�utrologie - ��st 2")
		end
		when info or button begin
			say_title("�utrologie - ��st2")
			say("Zem� je pohlcena mnoha �utry.")
			say("Jako odm�nu dostane� kost�m pro za��te�n�ky")
			say("Tv�j �kol:")
			say_yellow("Zb�v� zni�it: "..pc.getqf("state").." �utr�. ")
			local count = pc.getqf("state")
			q.set_counter("�utr boje", count)
		end
	end

	state __COMPLETE__ begin
	end
end