quest change_empire begin
	state start begin
		when 71054.click."Zmìnit øíši" with game.get_event_flag("c_e") > 0 begin

			local count = pc.get_change_empire_count() ;
			if count >= 1 then
				say("Nemùeš zmìnit øíši.")
				say("")
				return
			end
			say_reward("Zmìnit øíši")
			say("Zmìna øíše stojí 500.000 Yangù,")
			say("i pøesto chceš zmìnit øíši?")
			say("")
			
			local s = select("Ano", "Ne")

			if s == 1 then
				change_empire.move_pc()
			elseif s == 2 then
				return
			end
		end

		when 71054.use begin
			say_reward("Zmìnit øíši")

			if get_time() < pc.getqf("next_use_time") then
				say("Nemùeš zmìnit øíši!")
				say("")

				if pc.is_gm() then
					say("Chceš urychlit èas pro")
					say("zmìnìní øíše?")
					say("")
					local s = select("Ano", "Ne")
					if s == 1 then
						say("Èas byl urychlen.")
						say("Pokud chceš zmìnit øíši,")
						say("vyber poloku znovu.")
						pc.setqf("next_use_time", 0)
					end
				end

				return
			end

			if change_empire.move_pc() == true then
				pc.setqf("next_use_time", get_time() + 86400 * 7)
			end
		end



		function move_pc()
			if pc.is_engaged() then
				say("Nemùeš zmìnit øíši,")
				say("protoe jsi enatı!")
				say("")
				return false
			end

			if pc.is_married() then
				say("Nemùeš zmìnit øíši,")
				say("protoe jsi enatı!")
				say("")
				return false
			end

			if pc.is_polymorphed() then
				say("Nemùeš zmìnit øíši!")
				say("")
				return false
			end

			if pc.has_guild() then
				say("Nemùzeš zmìnit øíši,")
				say("protoe jsi v cechu.")
				say("")
				return false
			end
			if pc.money < 500000 then
				say("Nemáš dostatek yangù.")
				say("")
				return false
			end
			local s = select("Èervená øíše", "lutá øíše", "Zavøít")
			if 3==s then
				return false 
			end
			say("")
			say_reward("Chceš opravdu zmìnit øíši?")
			say("")
			local a = select("Ano", "Ne")
			if 2== a then
				return false
			end

			local ret = pc.change_empire(s)
			local oldempire = pc.get_empire()
			if ret == 999 then
				say("Uspìsnì jsi si zmìnil øíši.")
				say("Odhlaš se a potom se hned pøihlaš.")
				say("")
				pc.change_gold(-500000)
				pc.remove_item(71054) ;

				char_log(0, "CHANGE_EMPIRE",string.format("%d -> %d", oldempire, s)) 
			
				return  true
			else
				if ret == 1 then
					say("Zvolil jsi øíši, ve které jsi.")
					say("")
				elseif ret == 2 then
					say("Nemùeš zmìnit øíši, protoe")
					say("jsi byl v nedávné dobì v cechu.")
					say("")
					say("")
				elseif ret == 3 then
					say("Nemùeš zmenit øíši, protoe")
					say("jsi byl v nedávné dobì v páru.")
					say("")
				end
			end
			return false
		end

	end
end