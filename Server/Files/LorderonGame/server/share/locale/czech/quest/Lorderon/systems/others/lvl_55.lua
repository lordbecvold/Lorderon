quest lvl_55 begin
	state start begin
		when levelup with pc.level == 55 begin
			say_title("Doporu�en�.")
			say("V�born� dos�hl jsi �rovn� 55! ")
			say("Zlep�il jsi se v j�zd� na koni")
			say("Obdr�eno: ")
			say_yellow("Schopnost jezdit na koni �rovn� 21")
			say_yellow("V�echny schopnosti kon� M1")
			pc.set_skill_level(137 ,20)
			pc.set_skill_level(138 ,20)
			pc.set_skill_level(139 ,20)
			pc.set_skill_level(140 ,20)
			pc.set_skill_level(130 ,21)
			
		end
	end
end