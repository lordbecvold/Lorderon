quest sutrologie_lvl_20 begin
		state start begin
	end
	
	state run begin
		when login or levelup with pc.level >= 20 begin
			set_state(information)
		end
	end

	state information begin
		when letter begin
			send_letter("�utrologie - ��st 4")		
		end

		when info or button begin
			say_title("�utrologie - ��st 4")
			say("Zem� je pohlcena mnoha �utry.")
			say("Pomoz n�m jich p�r zni�it.")
			say("Jako odm�nu dostane�: ")
			say_reward("80.000 Yang� ")
			say_reward("35x Za�arovat p�edm�t. ")
			say_reward("5x Po�ehnan� pergamen")
			say_reward("2x �tok dra��ho boha")
			say_reward("2x Obrana dra��ho boha")
			say_reward("2x �ivot dra��ho boha")
			say("Tv�j �kol:")
			say_yellow("Zni� 20x �utr la�nosti")
			pc.setqf("state", 20)
			q.set_counter("�utr la�nosti", 20)
			set_state(kill)
		end
	end
	state kill begin
		when 8004.kill begin
			local count = pc.getqf("state") - 1
			if count <= 20 then
				pc.setqf("state", count)
				q.set_counter("�utr la�nosti", count)
			end
			if count == 0 then
				say_title("�utrologie - ��st 4")
				say("Dokon�il jsi �kol!")
				say("")
				say_reward("Obdr�� svou odm�nu. ")
				say_reward("80.000 Yang� ")
				say_reward("35x Za�arovat p�edm�t. ")
				say_reward("5x Po�ehnan� pergamen")
				say_reward("2x �tok dra��ho boha")
				say_reward("2x Obrana dra��ho boha")
				say_reward("2x �ivot dra��ho boha")
				pc.change_money(80000)
				pc.give_item2(39028, 35)
				pc.give_item2(39028, 5)
				pc.give_item2(71027, 2)
				pc.give_item2(71028, 2)
				pc.give_item2(71030, 2)
				set_quest_state("sutrologie_lvl_25", "run")
				clear_letter()
				set_state(__COMPLETE__)
			end
		end
		when letter begin
			send_letter("�utrologie - ��st 4")
		end
		when info or button begin
			say_title("�utrologie - ��st 4")
			say("Zem� je pohlcena mnoha �utry.")
			say("Jako odm�nu dostane�: ")
			say_reward("80.000 Yang� ")
			say_reward("35x Za�arovat p�edm�t. ")
			say_reward("5x Po�ehnan� pergamen")
			say_reward("2x �tok dra��ho boha")
			say_reward("2x Obrana dra��ho boha")
			say_reward("2x �ivot dra��ho boha")
			say("Tv�j �kol:")
			say_yellow("Zb�v� zni�it: "..pc.getqf("state").." �utr�. ")
			local count = pc.getqf("state")
			q.set_counter("�utr la�nosti", count)
		end
	end

	state __COMPLETE__ begin
	end
end