quest lvl_75 begin
	state start begin
		when levelup with pc.level == 75 begin
			say_title("Výbornì dosáhl jsi úrovnì 75!")
			say("Otevøela se ti nová lokace")
			say_yellow("Jeskynì vyhnanství ")
			say(" ")
			say_green("Nový set zbraní, brnìní a šperkù, získáš ve vìži démonù ")
			say_green("Vež démonù najdeš v chrámu hwang. ")
		end
	end
end