quest sutrologie_lvl_70 begin
		state start begin
	end
	
	state run begin
		when login or levelup with pc.level >= 70 begin
			set_state(information)
		end
	end

	state information begin
		when letter begin
			send_letter("�utrologie - ��st 15")		
		end

		when info or button begin
			say_title("�utrologie - ��st 15")
			say("Zem� je pohlcena mnoha �utry.")
			say("Pomoz n�m jich p�r zni�it.")
			say("Jako odm�nu dostane�: ")
			say_reward("10.000.000 Yang� ")
			say_reward("500x Za�arovat p�edm�t. ")
			say_reward("30x Po�ehnan� pergamen")
			say_reward("30x �tok dra��ho boha")
			say_reward("30x Obrana dra��ho boha")
			say_reward("30x �ivot dra��ho boha")
			say_reward("80x Cor Draconis")
			say_reward("5x Magick� k�men")
			say_reward("10x Truhla perel")
			say("Tv�j �kol:")
			say_yellow("Zni� 70x �utr vra�dy")
			pc.setqf("state", 70)
			q.set_counter("�utr vra�dy", 70)
			set_state(kill)
		end
	end
	state kill begin
		when 8014.kill begin
			local count = pc.getqf("state") - 1
			if count <= 70 then
				pc.setqf("state", count)
				q.set_counter("�utr vra�dy", count)
			end
			if count == 0 then
				say_title("�utrologie - ��st 15")
				say("Dokon�il jsi �kol!")
				say("")
				say_reward("10.000.000 Yang� ")
				say_reward("500x Za�arovat p�edm�t. ")
				say_reward("30x Po�ehnan� pergamen")
				say_reward("30x �tok dra��ho boha")
				say_reward("30x Obrana dra��ho boha")
				say_reward("30x �ivot dra��ho boha")
				say_reward("80x Cor Draconis")
				say_reward("5x Magick� k�men")
				say_reward("10x Truhla perel")
				pc.change_money(10000000)
				pc.give_item2(39028, 500)
				pc.give_item2(39028, 30)
				pc.give_item2(71027, 30)
				pc.give_item2(71028, 30)
				pc.give_item2(71030, 30)
				pc.give_item2(50252, 80)
				pc.give_item2(25041, 5)
				pc.give_item2(50135, 10)
				set_quest_state("sutrologie_lvl_75", "run")
				clear_letter()
				set_state(__COMPLETE__)
			end
		end
		when letter begin
			send_letter("�utrologie - ��st 15")
		end
		when info or button begin
			say_title("�utrologie - ��st 15")
			say("Zem� je pohlcena mnoha �utry.")
			say("Jako odm�nu dostane�: ")
			say_reward("10.000.000 Yang� ")
			say_reward("500x Za�arovat p�edm�t. ")
			say_reward("30x Po�ehnan� pergamen")
			say_reward("30x �tok dra��ho boha")
			say_reward("30x Obrana dra��ho boha")
			say_reward("30x �ivot dra��ho boha")
			say_reward("80x Cor Draconis")
			say_reward("5x Magick� k�men")
			say_reward("10x Truhla perel")
			say("Tv�j �kol:")
			say_yellow("Zb�v� zni�it: "..pc.getqf("state").." �utr�. ")
			local count = pc.getqf("state")
			q.set_counter("�utr vra�dy", count)
		end
	end

	state __COMPLETE__ begin
	end
end