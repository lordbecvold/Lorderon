quest lvl_5 begin
	state start begin
		when levelup with pc.level == 5 begin
			say_title("Doporuèení.")
			say("Výbornì dosáhl jsi úrovnì 5! ")
			say("Na úrovni 5 si mùžeš vybrat schopnosti, ")
			say(" ")
			say_red("Najdeš je v úkolu pod tlaèítkem N. ")
		end
	end
end