quest lvl_35 begin
	state start begin
		when levelup with pc.level == 35 begin
			say_title("Doporu�en�.")
			say("je �as se p�esunout do nov� lokace! ")
			say_yellow("Koukni se do �dol� ork�. ")
		end
	end
end