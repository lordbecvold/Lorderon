quest lvl_25 begin
	state start begin
		when levelup with pc.level == 25 begin
			say_title("Doporuèení.")
			say("Dosáhl jsi úrovnì 25 výbornì! ")
			say("Koukni se do mìsta k postavì Kopáè. ")
			say_yellow("Mùžeš u nìj koupit pøedmìty které ti pomohou ve høe. ")
		end
	end
end