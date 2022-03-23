quest lvl_95 begin
	state start begin
		when levelup with pc.level == 95 begin
			say_title("Výbornì dosáhl jsi úrovnì 95!")
			say("Otevøela se ti nová exp lokace!")
			say_yellow("V tvém teleportaèním systému je dostupná mapa Zakletý les. ")
		end
	end
end