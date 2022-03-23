quest lvl_120_up begin
	state start begin
		when levelup with pc.level == 120 begin
			say_title("Dokázal jsi to!")
			say("Nadešel tvùj èas, Dokázal jsi dokonèit maximální úroveò.")
			say(" ")
			say("Díky tvé vytrvalosti jsi se dostal na úroveò kam málo kdo. ")
			say("Draèí bùh ti gratuluje! ")
			say_yellow("Ovšem tady tvá cesta nekonèí, vìk je pøeci jen èíslo. ")
			say_green(" ")
			say_green(" - Lorderon Team ti Gratuluje - ")
		end
	end
end