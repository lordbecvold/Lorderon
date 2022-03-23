quest sutrologie_lvl_75 begin
		state start begin
	end
	
	state run begin
		when login or levelup with pc.level >= 75 begin
			set_state(information)
		end
	end

	state information begin
		when letter begin
			send_letter("�utrologie - ��st 16")		
		end

		when info or button begin
			say_title("�utrologie - ��st 16")
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
			say_reward("5x Ritu�ln� k�men")
			say_reward("10x Truhla perel")
			say("Tv�j �kol:")
			say_yellow("Zni� 75x �utr Pung-ma")
			pc.setqf("state", 75)
			q.set_counter("�utr Pung-ma", 75)
			set_state(kill)
		end
	end
	state kill begin
		when 8024.kill begin
			local count = pc.getqf("state") - 1
			if count <= 75 then
				pc.setqf("state", count)
				q.set_counter("�utr Pung-ma", count)
			end
			if count == 0 then
				say_title("�utrologie - ��st 16")
				say("Dokon�il jsi �kol!")
				say("")
				say_reward("10.000.000 Yang� ")
				say_reward("500x Za�arovat p�edm�t. ")
				say_reward("30x Po�ehnan� pergamen")
				say_reward("30x �tok dra��ho boha")
				say_reward("30x Obrana dra��ho boha")
				say_reward("30x �ivot dra��ho boha")
				say_reward("80x Cor Draconis")
				say_reward("5x Ritu�ln� k�men")
				say_reward("10x Truhla perel")
				pc.change_money(10000000)
				pc.give_item2(39028, 500)
				pc.give_item2(39028, 30)
				pc.give_item2(71027, 30)
				pc.give_item2(71028, 30)
				pc.give_item2(71030, 30)
				pc.give_item2(50252, 80)
				pc.give_item2(25042, 2)
				pc.give_item2(50135, 10)
				set_quest_state("sutrologie_lvl_80", "run")
				clear_letter()
				set_state(__COMPLETE__)
			end
		end
		when letter begin
			send_letter("�utrologie - ��st 16")
		end
		when info or button begin
			say_title("�utrologie - ��st 16")
			say("Zem� je pohlcena mnoha �utry.")
			say("Jako odm�nu dostane�: ")
			say_reward("10.000.000 Yang� ")
			say_reward("500x Za�arovat p�edm�t. ")
			say_reward("30x Po�ehnan� pergamen")
			say_reward("30x �tok dra��ho boha")
			say_reward("30x Obrana dra��ho boha")
			say_reward("30x �ivot dra��ho boha")
			say_reward("80x Cor Draconis")
			say_reward("2x Ritu�ln� k�men")
			say_reward("10x Truhla perel")
			say("Tv�j �kol:")
			say_yellow("Zb�v� zni�it: "..pc.getqf("state").." �utr�. ")
			local count = pc.getqf("state")
			q.set_counter("�utr Pung-ma", count)
		end
	end

	state __COMPLETE__ begin
	end
end