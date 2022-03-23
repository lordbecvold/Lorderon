quest sutrologie_lvl_65 begin
		state start begin
	end
	
	state run begin
		when login or levelup with pc.level >= 65 begin
			set_state(information)
		end
	end

	state information begin
		when letter begin
			send_letter("�utrologie - ��st 14")		
		end

		when info or button begin
			say_title("�utrologie - ��st 14")
			say("Zem� je pohlcena mnoha �utry.")
			say("Pomoz n�m jich p�r zni�it.")
			say("Jako odm�nu dostane�: ")
			say_reward("5.000.000 Yang� ")
			say_reward("300x Za�arovat p�edm�t. ")
			say_reward("30x Po�ehnan� pergamen")
			say_reward("30x �tok dra��ho boha")
			say_reward("30x Obrana dra��ho boha")
			say_reward("30x �ivot dra��ho boha")
			say_reward("80x Cor Draconis")
			say("Tv�j �kol:")
			say_yellow("Zni� 65x �utr smrti")
			pc.setqf("state", 65)
			q.set_counter("�utr smrti", 65)
			set_state(kill)
		end
	end
	state kill begin
		when 8013.kill begin
			local count = pc.getqf("state") - 1
			if count <= 65 then
				pc.setqf("state", count)
				q.set_counter("�utr smrti", count)
			end
			if count == 0 then
				say_title("�utrologie - ��st 14")
				say("Dokon�il jsi �kol!")
				say("")
				say_reward("Obdr�� svou odm�nu. ")
				say_reward("5.000.000 Yang� ")
				say_reward("300x Za�arovat p�edm�t. ")
				say_reward("30x Po�ehnan� pergamen")
				say_reward("30x �tok dra��ho boha")
				say_reward("30x Obrana dra��ho boha")
				say_reward("30x �ivot dra��ho boha")
				say_reward("80x Cor Draconis")
				pc.change_money(5000000)
				pc.give_item2(39028, 300)
				pc.give_item2(39028, 30)
				pc.give_item2(71027, 30)
				pc.give_item2(71028, 30)
				pc.give_item2(71030, 30)
				pc.give_item2(50252, 80)
				set_quest_state("sutrologie_lvl_70", "run")
				clear_letter()
				set_state(__COMPLETE__)
			end
		end
		when letter begin
			send_letter("�utrologie - ��st 14")
		end
		when info or button begin
			say_title("�utrologie - ��st 14")
			say("Zem� je pohlcena mnoha �utry.")
			say("Jako odm�nu dostane�: ")
			say_reward("5.000.000 Yang� ")
			say_reward("300x Za�arovat p�edm�t. ")
			say_reward("30x Po�ehnan� pergamen")
			say_reward("30x �tok dra��ho boha")
			say_reward("30x Obrana dra��ho boha")
			say_reward("30x �ivot dra��ho boha")
			say_reward("80x Cor Draconis")
			say("Tv�j �kol:")
			say_yellow("Zb�v� zni�it: "..pc.getqf("state").." �utr�. ")
			local count = pc.getqf("state")
			q.set_counter("�utr smrti", count)
		end
	end

	state __COMPLETE__ begin
	end
end