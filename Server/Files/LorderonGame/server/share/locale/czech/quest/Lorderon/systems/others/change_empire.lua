quest change_empire begin
	state start begin
		when 71054.click."Zm�nit ��i" with game.get_event_flag("c_e") > 0 begin

			local count = pc.get_change_empire_count() ;
			if count >= 1 then
				say("Nem��e� zm�nit ��i.")
				say("")
				return
			end
			say_reward("Zm�nit ��i")
			say("Zm�na ��e stoj� 500.000 Yang�,")
			say("i p�esto chce� zm�nit ��i?")
			say("")
			
			local s = select("Ano", "Ne")

			if s == 1 then
				change_empire.move_pc()
			elseif s == 2 then
				return
			end
		end

		when 71054.use begin
			say_reward("Zm�nit ��i")

			if get_time() < pc.getqf("next_use_time") then
				say("Nem��e� zm�nit ��i!")
				say("")

				if pc.is_gm() then
					say("Chce� urychlit �as pro")
					say("zm�n�n� ��e?")
					say("")
					local s = select("Ano", "Ne")
					if s == 1 then
						say("�as byl urychlen.")
						say("Pokud chce� zm�nit ��i,")
						say("vyber polo�ku znovu.")
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
				say("Nem��e� zm�nit ��i,")
				say("proto�e jsi �enat�!")
				say("")
				return false
			end

			if pc.is_married() then
				say("Nem��e� zm�nit ��i,")
				say("proto�e jsi �enat�!")
				say("")
				return false
			end

			if pc.is_polymorphed() then
				say("Nem��e� zm�nit ��i!")
				say("")
				return false
			end

			if pc.has_guild() then
				say("Nem�ze� zm�nit ��i,")
				say("proto�e jsi v cechu.")
				say("")
				return false
			end
			if pc.money < 500000 then
				say("Nem� dostatek yang�.")
				say("")
				return false
			end
			local s = select("�erven� ��e", "�lut� ��e", "Zav��t")
			if 3==s then
				return false 
			end
			say("")
			say_reward("Chce� opravdu zm�nit ��i?")
			say("")
			local a = select("Ano", "Ne")
			if 2== a then
				return false
			end

			local ret = pc.change_empire(s)
			local oldempire = pc.get_empire()
			if ret == 999 then
				say("Usp�sn� jsi si zm�nil ��i.")
				say("Odhla� se a potom se hned p�ihla�.")
				say("")
				pc.change_gold(-500000)
				pc.remove_item(71054) ;

				char_log(0, "CHANGE_EMPIRE",string.format("%d -> %d", oldempire, s)) 
			
				return  true
			else
				if ret == 1 then
					say("Zvolil jsi ��i, ve kter� jsi.")
					say("")
				elseif ret == 2 then
					say("Nem��e� zm�nit ��i, proto�e")
					say("jsi byl v ned�vn� dob� v cechu.")
					say("")
					say("")
				elseif ret == 3 then
					say("Nem��e� zmenit ��i, proto�e")
					say("jsi byl v ned�vn� dob� v p�ru.")
					say("")
				end
			end
			return false
		end

	end
end