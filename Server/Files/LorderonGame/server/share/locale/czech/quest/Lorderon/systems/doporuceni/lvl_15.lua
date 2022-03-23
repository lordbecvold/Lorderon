quest lvl_15 begin
	state start begin
		when levelup with pc.level == 15 begin
			say_title("Doporuèení.")
			say("V plnìní úkolù šutrologie ti pomùže mapa Svìt šutrù. ")
			say("Dostaneš se do ní pomocí teleportaèního prstenu. ")
			say("")
			say("Pokud chceš rychleji expit mùžeš se pøesunout do vesnice, ")
			say("najdeš ji také v teleportaèním prstenu. ")
			say_yellow("Pokud chceš lépe bojovat nakup si lepší vìci,")
			say_yellow("u obchodníkù ve mìstì. ")
		end
	end
end