quest lvl_10 begin
	state start begin
		when levelup with pc.level == 10 begin
			say_title("Doporu�en�.")
			say("V�born� dos�hl jsi �rovn� 10! ")
			say("Nezapom�nej d�lat �koly �utrologie! ")
			say("")
			say_blue("Dostane� za n� spousty v�c� kter� ti pom��ou v boji")
		end
	end
end