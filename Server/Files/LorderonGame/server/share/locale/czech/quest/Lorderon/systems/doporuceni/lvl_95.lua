quest lvl_95 begin
	state start begin
		when levelup with pc.level == 95 begin
			say_title("V�born� dos�hl jsi �rovn� 95!")
			say("Otev�ela se ti nov� exp lokace!")
			say_yellow("V tv�m teleporta�n�m syst�mu je dostupn� mapa Zaklet� les. ")
		end
	end
end