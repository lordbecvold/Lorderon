quest item_change_sex begin
	state start begin
		when 71048.use begin 
			if pc.get_level() < 50 then 
				say_title("Zm�na pohlav� ")
				say_reward("Pot�ebuje� level 50.")
				return;
			end
			
			if pc.is_engaged() then
				say_title("Zm�na pohlav� ")
				say_reward("Nem��e� zm�nit pohlav�.")
				return;
			end

			if pc.is_married() then
				say_title("Zm�na pohlav� ")
				say_reward("Na zm�nu pohlav� mus� b�t svobodn�/�.")
				return;
			end

			if pc.is_polymorphed() then
				say_title("Zm�na pohlav� ")
				say_reward("Nem��e� si zm�nit pohlav�, kdy� jsi prom�n�n�.")
				say("")
				return;
			end
			say_title("Zm�na pohlav� ")
			say("Chce� zm�nit sv� pohlav�?")
			say("")
			local s=select("Ano","Ne")
			if 1==s then
				say("Opravdu?")
				say("")
				local s2=select("Ano","Ne")
				if 1==s2 then
				say("Ok, zm�na pohlav� prob�h�.")
				say_reward("Zm�na pohlav� prob�hla usp�n� odhla�te se!")
				say("")
				pc.remove_item(71048,1)
				pc.change_sex()
				local m_sex = pc.get_sex()
				if m_sex == 0 then
				    char_log(0, "CHANGE_SEX", "F -> M")
				else
				    char_log(0, "CHANGE_SEX", "M -> F")
				end
			end
			elseif 2==s then
				return
			end
		end
	end
end