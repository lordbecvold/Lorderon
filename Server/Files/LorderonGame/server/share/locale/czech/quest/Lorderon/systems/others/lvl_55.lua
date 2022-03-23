quest lvl_55 begin
	state start begin
		when levelup with pc.level == 55 begin
			say_title("Doporuèení.")
			say("Výbornì dosáhl jsi úrovnì 55! ")
			say("Zlepšil jsi se v jízdì na koni")
			say("Obdrženo: ")
			say_yellow("Schopnost jezdit na koni úrovnì 21")
			say_yellow("Všechny schopnosti konì M1")
			pc.set_skill_level(137 ,20)
			pc.set_skill_level(138 ,20)
			pc.set_skill_level(139 ,20)
			pc.set_skill_level(140 ,20)
			pc.set_skill_level(130 ,21)
			
		end
	end
end