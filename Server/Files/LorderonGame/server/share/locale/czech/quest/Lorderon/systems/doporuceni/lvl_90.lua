quest lvl_90 begin
	state start begin
		when levelup with pc.level == 90 begin
			say_title("V�born� dos�hl jsi �rovn� 90!")
			say("Otev�ela se ti nov� lokace")
			say_yellow("Otev�eli se ti 4 nov� mapy na drop. ")
		end
	end
end