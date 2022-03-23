quest sutrologie_lvl_45 begin
		state start begin
	end
	
	state run begin
		when login or levelup with pc.level >= 45 begin
			set_state(information)
		end
	end

	state information begin
		when letter begin
			send_letter("�utrologie - ��st 10")		
		end

		when info or button begin
			say_title("�utrologie - ��st 10")
			say("Zem� je pohlcena mnoha �utry.")
			say("Pomoz n�m jich p�r zni�it.")
			say("Jako odm�nu dostane�: ")
			say_reward("200.000 Yang� ")
			say_reward("60x Za�arovat p�edm�t. ")
			say_reward("5x Po�ehnan� pergamen")
			say_reward("5x �tok dra��ho boha")
			say_reward("5x Obrana dra��ho boha")
			say_reward("5x �ivot dra��ho boha")
			say_reward("30x Cor Draconis")
			say_reward("1x N�u�nice z dra�� kosti 2h")
			say("Tv�j �kol:")
			say_yellow("Zni� 45x �utr st�nu")
			pc.setqf("state", 45)
			q.set_counter("�utr st�nu", 45)
			set_state(kill)
		end
	end
	state kill begin
		when 8009.kill begin
			local count = pc.getqf("state") - 1
			if count <= 45 then
				pc.setqf("state", count)
				q.set_counter("�utr st�nu", count)
			end
			if count == 0 then
				say_title("�utrologie - ��st 10")
				say("Dokon�il jsi �kol!")
				say("")
				say_reward("Obdr�� svou odm�nu. ")
				say_reward("200.000 Yang� ")
				say_reward("60x Za�arovat p�edm�t. ")
				say_reward("5x Po�ehnan� pergamen")
				say_reward("5x �tok dra��ho boha")
				say_reward("5x Obrana dra��ho boha")
				say_reward("5x �ivot dra��ho boha")
				say_reward("30x Cor Draconis")
				say_reward("1x N�u�nice z dra�� kosti 2h")
				pc.change_money(200000)
				pc.give_item2(39028, 60)
				pc.give_item2(39028, 5)
				pc.give_item2(71027, 5)
				pc.give_item2(71028, 5)
				pc.give_item2(71030, 5)
				pc.give_item2(50252, 30)
				pc.give_item2(72704, 1)
				set_quest_state("sutrologie_lvl_50", "run")
				clear_letter()
				set_state(__COMPLETE__)
			end
		end
		when letter begin
			send_letter("�utrologie - ��st 10")
		end
		when info or button begin
			say_title("�utrologie - ��st 10")
			say("Zem� je pohlcena mnoha �utry.")
			say("Jako odm�nu dostane�: ")
			say_reward("200.000 Yang� ")
			say_reward("60x Za�arovat p�edm�t. ")
			say_reward("5x Po�ehnan� pergamen")
			say_reward("5x �tok dra��ho boha")
			say_reward("5x Obrana dra��ho boha")
			say_reward("5x �ivot dra��ho boha")
			say_reward("30x Cor Draconis")
			say_reward("1x N�u�nice z dra�� kosti 2h")
			say("Tv�j �kol:")
			say_yellow("Zb�v� zni�it: "..pc.getqf("state").." �utr�. ")
			local count = pc.getqf("state")
			q.set_counter("�utr st�nu", count)
		end
	end

	state __COMPLETE__ begin
	end
end