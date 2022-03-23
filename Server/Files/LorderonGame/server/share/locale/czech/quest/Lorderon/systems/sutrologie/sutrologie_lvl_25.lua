quest sutrologie_lvl_25 begin
		state start begin
	end
	
	state run begin
		when login or levelup with pc.level >= 25 begin
			set_state(information)
		end
	end

	state information begin
		when letter begin
			send_letter("�utrologie - ��st 5")		
		end

		when info or button begin
			say_title("�utrologie - ��st 5")
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
			say("Tv�j �kol:")
			say_yellow("Zni� 25x �utr �ernoty")
			pc.setqf("state", 25)
			q.set_counter("�utr �ernoty", 25)
			set_state(kill)
		end
	end
	state kill begin
		when 8005.kill begin
			local count = pc.getqf("state") - 1
			if count <= 25 then
				pc.setqf("state", count)
				q.set_counter("�utr �ernoty", count)
			end
			if count == 0 then
				say_title("�utrologie - ��st 5")
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
				pc.change_money(90000)
				pc.give_item2(39028, 35)
				pc.give_item2(39028, 5)
				pc.give_item2(71027, 2)
				pc.give_item2(71028, 2)
				pc.give_item2(71030, 2)
				pc.give_item2(72314, 3)
				set_quest_state("sutrologie_lvl_30", "run")
				clear_letter()
				set_state(__COMPLETE__)
			end
		end
		when letter begin
			send_letter("�utrologie - ��st 5")
		end
		when info or button begin
			say_title("�utrologie - ��st 5")
			say("Zem� je pohlcena mnoha �utry.")
			say("Jako odm�nu dostane�: ")
			say_reward("90.000 Yang� ")
			say_reward("35x Za�arovat p�edm�t. ")
			say_reward("5x Po�ehnan� pergamen")
			say_reward("2x �tok dra��ho boha")
			say_reward("2x Obrana dra��ho boha")
			say_reward("2x �ivot dra��ho boha")
			say_reward("3x Pergamen draka")
			say("Tv�j �kol:")
			say_yellow("Zb�v� zni�it: "..pc.getqf("state").." �utr�. ")
			local count = pc.getqf("state")
			q.set_counter("�utr �ernoty", count)
		end
	end

	state __COMPLETE__ begin
	end
end