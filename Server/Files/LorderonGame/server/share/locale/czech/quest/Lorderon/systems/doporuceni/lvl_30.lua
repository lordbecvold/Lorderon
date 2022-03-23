quest lvl_30 begin
	state start begin
		when levelup with pc.level == 30 begin
			say_title("Doporuèení.")
			say("Výbornì dosáhl jsi úrovnì 30! ")
			say("Je èas získat novou zbraò, ")
			say("Získáš jí z truhly vzestupu. ")
			say_yellow("Ta padá z Brutálního velitele ve vesnici. ")
		end
	end
end