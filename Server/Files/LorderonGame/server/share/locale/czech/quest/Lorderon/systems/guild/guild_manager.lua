define __givememoney__ 100000000
quest sample__guild_make begin
    state start begin
		when guild_man1.chat."Založit cech " or guild_man2.chat."Založit cech " or guild_man3.chat."Založit cech " with not pc.hasguild() and not pc.isguildmaster() begin
			say("Chceš si založit cech? .")
			say_reward("Dobøe dej mi: ".. __givememoney__ .." yangù.")
			if select("Ano", "Ne")==2 then return end
			-- let's start!
			say("Zadej jméno tvého Cechu:")
			local guild_name = string.gsub(input(), "[^A-Za-z0-9]", "") -- it also clean non alphanumeric characters
			local guild_len_name = string.len(guild_name)
			if not ((2 < guild_len_name) and (guild_len_name < 12)) then
				say_reward("Jméno by nemìlo mít speciální znaky a jejich délka by mìla být mezi tøemi až jedenácti znaky! ")
				return
			end
			say("Opravdu chceš založit Cech?[ENTER]"..guild_name)
			if select("Ano", "NE")==2 then return end
			-- checks begin
			if not (pc.get_gold() >= __givememoney__ ) then
				say_reward("nemáš dostatek yangù na založení cechu. ")
				return
			end
			if (pc.hasguild() or pc.isguildmaster()) then
				say_reward("Již patøíš k cechu.")
				return
			end
			-- checks end
			-- so many ifs, we can simplify this by using a table
			local ret = pc.make_guild0(guild_name)
			if ret==-2 then
				say_reward("[Ne] Tohle jméno je pøíliš dlouhé ")
			elseif ret==-1 then
				say_reward("[Ne] Ttot jméno obsahuje speciální znaky. ")
			elseif ret==0 then
				say_reward("[Ne] Tento cech je již založen! ")
			elseif ret==1 then
				pc.change_gold(- __givememoney__ )
				say_reward("[Ano] Cech byl úspìšnì vytvoøen. ")
			elseif ret==2 then
				say_reward("[Ne] Hráè je již v cechu. ")
			elseif ret==3 then
				say_reward("[Ne] Hráè je již vùdce cechu. ")
			end
		end
		when guild_man1.chat."Zrušit cech " or guild_man2.chat."Zrušit cech " or guild_man3.chat."Zrušit cech " with not !pc.hasguild() begin
			say("Chceš si Zrušit cech? ")
			if select("Ano", "Ne")==2 then return end
			pc.destroy_guild()
		end
		when guild_man1.chat."Opustit cech " or guild_man2.chat."Opustit cech " or guild_man3.chat."Opustit cech " with not !pc.hasguild() begin
			say("Opravdu chceš opstit svuj cech? ")
			if select("Ano", "Ne")==2 then return end
			pc.remove_from_guild()
		end
	end
end
