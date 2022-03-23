quest sash begin
	state start begin
		when 60003.chat."Kombinování šerp" begin
			say_title(mob_name(60003))
			say("Pøi kombinaci šerp je možné že se jedna znièí.")
			local confirm = select("Ano", "Ne")
			if confirm == 2 then
				return
			end
			
			setskin(NOWINDOW)
			pc.open_acce(true)
		end
		when 60003.chat."Co je Šerpa? " begin
			say_title(mob_name(60003))
			say("Šerpa je cást výbavy která do které lze vložit bonusy ")
			say("Šerpa pøebere 100% bonusù v pøedmìtu ")
			say("")
			say_red("Vztahuje se pouze na toèitelné bonusy")
			say("")
			say_yellow("Do šerpy se vkládá brnìní nebo zbraò ")
		end
		
		when 60003.chat."Absorbovat bonus " begin
			say_title(mob_name(60003))
			say("Do šerpy mùžeš absorbovat zbranì a brnìní ")
			say("Chceš to udìlat? ")
			local confirm = select("Ano ", "Ne ")
			if confirm == 2 then
				return
			end		
			setskin(NOWINDOW)
			pc.open_acce(false)
		end
	end
end
