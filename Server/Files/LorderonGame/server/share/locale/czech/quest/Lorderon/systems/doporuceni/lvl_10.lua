quest lvl_10 begin
	state start begin
		when levelup with pc.level == 10 begin
			say_title("Doporuèení.")
			say("Výbornì dosáhl jsi úrovnì 10! ")
			say("Nezapomínej dìlat úkoly šutrologie! ")
			say("")
			say_blue("Dostaneš za nì spousty vìcí které ti pomùžou v boji")
		end
	end
end