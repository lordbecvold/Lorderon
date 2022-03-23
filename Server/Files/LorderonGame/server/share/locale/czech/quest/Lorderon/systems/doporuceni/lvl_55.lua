quest lvl_55 begin
	state start begin
		when levelup with pc.level == 55 begin
			say_title("Výbornì dosáhl jsi úrovnì 55!")
			say("Získal jsi")
			say_yellow("Schopnosti konì M1")
			say_yellow("Schopnosti jízdy na koni 21")
			pc.set_skill_level(138,20)
			pc.set_skill_level(139,20)
			pc.set_skill_level(140,20)
			pc.set_skill_level(130,20)
			pc.set_skill_level(137,21)
		end
	end
end