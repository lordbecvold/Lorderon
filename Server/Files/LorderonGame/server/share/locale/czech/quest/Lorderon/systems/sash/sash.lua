quest sash begin
	state start begin
		when 60003.chat."Kombinov�n� �erp" begin
			say_title(mob_name(60003))
			say("P�i kombinaci �erp je mo�n� �e se jedna zni��.")
			local confirm = select("Ano", "Ne")
			if confirm == 2 then
				return
			end
			
			setskin(NOWINDOW)
			pc.open_acce(true)
		end
		when 60003.chat."Co je �erpa? " begin
			say_title(mob_name(60003))
			say("�erpa je c�st v�bavy kter� do kter� lze vlo�it bonusy ")
			say("�erpa p�ebere 100% bonus� v p�edm�tu ")
			say("")
			say_red("Vztahuje se pouze na to�iteln� bonusy")
			say("")
			say_yellow("Do �erpy se vkl�d� brn�n� nebo zbra� ")
		end
		
		when 60003.chat."Absorbovat bonus " begin
			say_title(mob_name(60003))
			say("Do �erpy m��e� absorbovat zbran� a brn�n� ")
			say("Chce� to ud�lat? ")
			local confirm = select("Ano ", "Ne ")
			if confirm == 2 then
				return
			end		
			setskin(NOWINDOW)
			pc.open_acce(false)
		end
	end
end
