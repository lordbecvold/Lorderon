quest lvl_40 begin
	state start begin
		when levelup with pc.level == 40 begin
			say_title("Doporuèení.")
			say("Nezapomínej dìlat úkoly bossologie! ")
			say_yellow("Za úkoly Bossologie dostaneš trvalé bonusy, ")
			say_yellow("které posílí tvou postavu." )
			say(" ")
			say_yellow("Také nezapomínej na Biologický výzkum!")
			say_yellow("Najdeš ho v inventáøi pod tlaèítkem šipky v levé stranì okna. ")
		end
	end
end