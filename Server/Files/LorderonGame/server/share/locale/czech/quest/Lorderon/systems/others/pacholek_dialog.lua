quest pacholek_dialog begin
	state start begin
		when 20349.chat."Informace o mountech " begin
			say_title("Pacholek")
			say("Mounta m��e� vylep�ovat pergameny nebo u kov��e. ")
			say(" ")
			say_yellow("Uppky z�sk� v Opi��m dungeonu. ")
		end
		when 20349.chat."Informace o mazl��c�ch " begin
			say_title("Pacholek")
			say("mazl��ka m��e� vylep�ovat pergameny nebo u kov��e. ")
			say(" ")
			say_yellow("Uppky z�sk� v Opi��m dungeonu. ")
		end
	end
end

