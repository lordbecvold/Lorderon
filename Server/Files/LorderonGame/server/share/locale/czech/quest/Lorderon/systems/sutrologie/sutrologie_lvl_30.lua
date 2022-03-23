quest sutrologie_lvl_30 begin
		state start begin
	end
	
	state run begin
		when login or levelup with pc.level >= 30 begin
			set_state(information)
		end
	end

	state information begin
		when letter begin
			send_letter("�utrologie - ��st 6")		
		end

		when info or button begin
			say_title("�utrologie - ��st 6")
			say("Zem� je pohlcena mnoha �utry.")
			say("Pomoz n�m jich p�r zni�it.")
			say("Jako odm�nu dostane�: ")
			say_reward("90.000 Yang� ")
			say_reward("35x Za�arovat p�edm�t. ")
			say_reward("5x Po�ehnan� pergamen")
			say_reward("2x �tok dra��ho boha")
			say_reward("2x Obrana dra��ho boha")
			say_reward("2x �ivot dra��ho boha")
			say_reward("3x Pergamen draka")
			say_reward("10x Cor Draconis")
			say("Tv�j �kol:")
			say_yellow("Zni� 30x �utr tmy")
			pc.setqf("state", 30)
			q.set_counter("�utr tmy", 30)
			set_state(kill)
		end
	end
	state kill begin
		when 8006.kill begin
			local count = pc.getqf("state") - 1
			if count <= 30 then
				pc.setqf("state", count)
				q.set_counter("�utr tmy", count)
			end
			if count == 0 then
				say_title("�utrologie - ��st 6")
				say("Dokon�il jsi �kol!")
				say("")
				say_reward("Obdr�� svou odm�nu. ")
				say_reward("90.000 Yang� ")
				say_reward("35x Za�arovat p�edm�t. ")
				say_reward("5x Po�ehnan� pergamen")
				say_reward("2x �tok dra��ho boha")
				say_reward("2x Obrana dra��ho boha")
				say_reward("2x �ivot dra��ho boha")
				say_reward("3x Pergamen draka")
				say_reward("10x Cor Draconis")
				pc.change_money(90000)
				pc.give_item2(39028, 35)
				pc.give_item2(39028, 5)
				pc.give_item2(71027, 2)
				pc.give_item2(71028, 2)
				pc.give_item2(71030, 2)
				pc.give_item2(72314, 3)
				pc.give_item2(50252, 10)
				set_quest_state("sutrologie_lvl_35", "run")
				clear_letter()
				set_state(__COMPLETE__)
			end
		end
		when letter begin
			send_letter("�utrologie - ��st 6")
		end
		when info or button begin
			say_title("�utrologie - ��st 6")
			say("Zem� je pohlcena mnoha �utry.")
			say("Jako odm�nu dostane�: ")
			say_reward("90.000 Yang� ")
			say_reward("35x Za�arovat p�edm�t. ")
			say_reward("5x Po�ehnan� pergamen")
			say_reward("2x �tok dra��ho boha")
			say_reward("2x Obrana dra��ho boha")
			say_reward("2x �ivot dra��ho boha")
			say_reward("3x Pergamen draka")
			say_reward("10x Cor Draconis")
			say("Tv�j �kol:")
			say_yellow("Zb�v� zni�it: "..pc.getqf("state").." �utr�. ")
			local count = pc.getqf("state")
			q.set_counter("�utr tmy", count)
		end
	end

	state __COMPLETE__ begin
	end
end