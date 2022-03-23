quest item_change_sex begin
	state start begin
		when 71048.use begin 
			if pc.get_level() < 50 then 
				say_title("Zmìna pohlaví ")
				say_reward("Potøebuješ level 50.")
				return;
			end
			
			if pc.is_engaged() then
				say_title("Zmìna pohlaví ")
				say_reward("Nemùeš zmìnit pohlaví.")
				return;
			end

			if pc.is_married() then
				say_title("Zmìna pohlaví ")
				say_reward("Na zmìnu pohlaví musíš bıt svobodnı/á.")
				return;
			end

			if pc.is_polymorphed() then
				say_title("Zmìna pohlaví ")
				say_reward("Nemùeš si zmìnit pohlaví, kdy jsi promìnìnı.")
				say("")
				return;
			end
			say_title("Zmìna pohlaví ")
			say("Chceš zmìnit své pohlaví?")
			say("")
			local s=select("Ano","Ne")
			if 1==s then
				say("Opravdu?")
				say("")
				local s2=select("Ano","Ne")
				if 1==s2 then
				say("Ok, zmìna pohlaví probíhá.")
				say_reward("Zmìna pohlaví probìhla uspìšnì odhlašte se!")
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