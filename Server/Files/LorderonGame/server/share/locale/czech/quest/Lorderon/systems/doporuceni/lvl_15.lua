quest lvl_15 begin
	state start begin
		when levelup with pc.level == 15 begin
			say_title("Doporu�en�.")
			say("V pln�n� �kol� �utrologie ti pom��e mapa Sv�t �utr�. ")
			say("Dostane� se do n� pomoc� teleporta�n�ho prstenu. ")
			say("")
			say("Pokud chce� rychleji expit m��e� se p�esunout do vesnice, ")
			say("najde� ji tak� v teleporta�n�m prstenu. ")
			say_yellow("Pokud chce� l�pe bojovat nakup si lep�� v�ci,")
			say_yellow("u obchodn�k� ve m�st�. ")
		end
	end
end