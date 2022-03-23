quest lvl_35 begin
	state start begin
		when levelup with pc.level == 35 begin
			say_title("Doporuèení.")
			say("je èas se pøesunout do nové lokace! ")
			say_yellow("Koukni se do Údolí orkù. ")
		end
	end
end