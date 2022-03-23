define __givememoney__ 100000000
quest sample__guild_make begin
    state start begin
		when guild_man1.chat."Zalo�it cech " or guild_man2.chat."Zalo�it cech " or guild_man3.chat."Zalo�it cech " with not pc.hasguild() and not pc.isguildmaster() begin
			say("Chce� si zalo�it cech? .")
			say_reward("Dob�e dej mi: ".. __givememoney__ .." yang�.")
			if select("Ano", "Ne")==2 then return end
			-- let's start!
			say("Zadej jm�no tv�ho Cechu:")
			local guild_name = string.gsub(input(), "[^A-Za-z0-9]", "") -- it also clean non alphanumeric characters
			local guild_len_name = string.len(guild_name)
			if not ((2 < guild_len_name) and (guild_len_name < 12)) then
				say_reward("Jm�no by nem�lo m�t speci�ln� znaky a jejich d�lka by m�la b�t mezi t�emi a� jeden�cti znaky! ")
				return
			end
			say("Opravdu chce� zalo�it Cech?[ENTER]"..guild_name)
			if select("Ano", "NE")==2 then return end
			-- checks begin
			if not (pc.get_gold() >= __givememoney__ ) then
				say_reward("nem� dostatek yang� na zalo�en� cechu. ")
				return
			end
			if (pc.hasguild() or pc.isguildmaster()) then
				say_reward("Ji� pat�� k cechu.")
				return
			end
			-- checks end
			-- so many ifs, we can simplify this by using a table
			local ret = pc.make_guild0(guild_name)
			if ret==-2 then
				say_reward("[Ne] Tohle jm�no je p��li� dlouh� ")
			elseif ret==-1 then
				say_reward("[Ne] Ttot jm�no obsahuje speci�ln� znaky. ")
			elseif ret==0 then
				say_reward("[Ne] Tento cech je ji� zalo�en! ")
			elseif ret==1 then
				pc.change_gold(- __givememoney__ )
				say_reward("[Ano] Cech byl �sp�n� vytvo�en. ")
			elseif ret==2 then
				say_reward("[Ne] Hr�� je ji� v cechu. ")
			elseif ret==3 then
				say_reward("[Ne] Hr�� je ji� v�dce cechu. ")
			end
		end
		when guild_man1.chat."Zru�it cech " or guild_man2.chat."Zru�it cech " or guild_man3.chat."Zru�it cech " with not !pc.hasguild() begin
			say("Chce� si Zru�it cech? ")
			if select("Ano", "Ne")==2 then return end
			pc.destroy_guild()
		end
		when guild_man1.chat."Opustit cech " or guild_man2.chat."Opustit cech " or guild_man3.chat."Opustit cech " with not !pc.hasguild() begin
			say("Opravdu chce� opstit svuj cech? ")
			if select("Ano", "Ne")==2 then return end
			pc.remove_from_guild()
		end
	end
end
