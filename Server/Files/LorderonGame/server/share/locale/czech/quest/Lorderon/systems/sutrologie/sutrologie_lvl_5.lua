quest sutrologie_lvl_5 begin
	state start begin
		when login or levelup with pc.level >= 5 begin
			set_state(information)
		end
	end

	state information begin
		when letter begin
			send_letter("�utrologie - ��st 1")		
		end

		when info or button begin
			say_title("�utrologie - ��st 1")
			say("Zem� je pohlcena mnoha �utry.")
			say("Pomoz n�m jich p�r zni�it.")
			say("Odm�na t� nemine.")
			say("Tv�j �kol:")
			say_yellow("Zni� 5x �utr smutku")
			pc.setqf("state", 5)
			q.set_counter("�utr smutku", 5)
			set_state(kill)
		end
	end
	state kill begin
		when 8001.kill begin
			local count = pc.getqf("state") - 1
			if count <= 5 then
				pc.setqf("state", count)
				q.set_counter("�utr smutku", count)
			end
			if count == 0 then
				say_title("�utrologie - ��st 1")
				say("Dokon�il jsi �kol!")
				say("")
				say_reward("Obdr�� svou odm�nu. ")
				say_reward("60.000 Yang� ")
				say_reward("10x Za�arovat p�edm�t. ")
				pc.change_money(60000)
				pc.give_item2(39028, 10)
				set_quest_state("sutrologie_lvl_10", "run")
				clear_letter()
				set_state(__COMPLETE__)
			end
		end
		when letter begin
			send_letter("�utrologie - ��st 1")
		end
		when info or button begin
			say_title("�utrologie - ��st 1")
			say("Zem� je pohlcena mnoha �utry.")
			say("Pomoz n�m jich p�r zni�it.")
			say("Odm�na t� nemine.")
			say("Tv�j �kol:")
			say_yellow("Zb�v� zni�it: "..pc.getqf("state").." �utr�. ")
			local count = pc.getqf("state")
			q.set_counter("�utr smutku", count)
		end
	end

	state __COMPLETE__ begin
	end
end