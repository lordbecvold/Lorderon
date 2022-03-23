quest sutrologie_lvl_15 begin
		state start begin
	end
	
	state run begin
		when login or levelup with pc.level >= 15 begin
			set_state(information)
		end
	end

	state information begin
		when letter begin
			send_letter("�utrologie - ��st 3")		
		end

		when info or button begin
			say_title("�utrologie - ��st 3")
			say("Zem� je pohlcena mnoha �utry.")
			say("Pomoz n�m jich p�r zni�it.")
			say("Jako odm�nu dostane�: ")
			say_reward("70.000 Yang� ")
			say_reward("30x Za�arovat p�edm�t. ")
			say_reward("5x Po�ehnan� pergamen")
			say("Tv�j �kol:")
			say_yellow("Zni� 15x �utr bitvy")
			pc.setqf("state", 15)
			q.set_counter("�utr bitvy", 15)
			set_state(kill)
		end
	end
	state kill begin
		when 8003.kill begin
			local count = pc.getqf("state") - 1
			if count <= 15 then
				pc.setqf("state", count)
				q.set_counter("�utr bitvy", count)
			end
			if count == 0 then
				say_title("�utrologie - ��st 3")
				say("Dokon�il jsi �kol!")
				say("")
				say_reward("Obdr�� svou odm�nu. ")
				say_reward("70.000 Yang� ")
				say_reward("30x Za�arovat p�edm�t. ")
				say_reward("5x Po�ehnan� pergamen")
				pc.change_money(70000)
				pc.give_item2(39028, 30)
				pc.give_item2(39028, 5)
				set_quest_state("sutrologie_lvl_20", "run")
				clear_letter()
				set_state(__COMPLETE__)
			end
		end
		when letter begin
			send_letter("�utrologie - ��st 3")
		end
		when info or button begin
			say_title("�utrologie - ��st3")
			say("Zem� je pohlcena mnoha �utry.")
			say("Jako odm�nu dostane�: ")
			say_reward("70.000 Yang� ")
			say_reward("30x Za�arovat p�edm�t. ")
			say_reward("5x Po�ehnan� pergamen")
			say("Tv�j �kol:")
			say_yellow("Zb�v� zni�it: "..pc.getqf("state").." �utr�. ")
			local count = pc.getqf("state")
			q.set_counter("�utr bitvy", count)
		end
	end

	state __COMPLETE__ begin
	end
end