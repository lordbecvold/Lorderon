quest lvl_30 begin
	state start begin
		when levelup with pc.level == 30 begin
			say_title("Doporu�en�.")
			say("V�born� dos�hl jsi �rovn� 30! ")
			say("Je �as z�skat novou zbra�, ")
			say("Z�sk� j� z truhly vzestupu. ")
			say_yellow("Ta pad� z Brut�ln�ho velitele ve vesnici. ")
		end
	end
end