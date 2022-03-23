quest lvl_20 begin
	state start begin
		when levelup with pc.level == 20 begin
			say_title("Doporuèení.")
			say("Dosáhl jsi úrovnì 20 výbornì! ")
			say("Je èas vydat se do boje proti bossùm ve vesnici. ")
			say("bìž do vesnice a zabijej Mahona, Bo, Go-pae a Chuonga")
			say("Pøedmìty které získáš ti pomohou v dalším rozvoji")
			say_green("Pokud klikneš na ? v menu pøíšery ")
			say_green("zobrazí se ti vìci co mùžeš jejím zabitím získat. ")
		end
	end
end