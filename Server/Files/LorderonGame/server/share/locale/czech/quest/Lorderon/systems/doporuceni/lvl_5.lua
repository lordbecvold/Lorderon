quest lvl_5 begin
	state start begin
		when levelup with pc.level == 5 begin
			say_title("Doporu�en�.")
			say("V�born� dos�hl jsi �rovn� 5! ")
			say("Na �rovni 5 si m��e� vybrat schopnosti, ")
			say(" ")
			say_red("Najde� je v �kolu pod tla��tkem N. ")
		end
	end
end