quest lvl_90 begin
	state start begin
		when levelup with pc.level == 90 begin
			say_title("Výbornì dosáhl jsi úrovnì 90!")
			say("Otevøela se ti nová lokace")
			say_yellow("Otevøeli se ti 4 nové mapy na drop. ")
		end
	end
end