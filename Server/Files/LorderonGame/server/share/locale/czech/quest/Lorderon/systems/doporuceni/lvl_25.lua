quest lvl_25 begin
	state start begin
		when levelup with pc.level == 25 begin
			say_title("Doporu�en�.")
			say("Dos�hl jsi �rovn� 25 v�born�! ")
			say("Koukni se do m�sta k postav� Kop��. ")
			say_yellow("M��e� u n�j koupit p�edm�ty kter� ti pomohou ve h�e. ")
		end
	end
end