quest lvl_20 begin
	state start begin
		when levelup with pc.level == 20 begin
			say_title("Doporu�en�.")
			say("Dos�hl jsi �rovn� 20 v�born�! ")
			say("Je �as vydat se do boje proti boss�m ve vesnici. ")
			say("b� do vesnice a zabijej Mahona, Bo, Go-pae a Chuonga")
			say("P�edm�ty kter� z�sk� ti pomohou v dal��m rozvoji")
			say_green("Pokud klikne� na ? v menu p��ery ")
			say_green("zobraz� se ti v�ci co m��e� jej�m zabit�m z�skat. ")
		end
	end
end