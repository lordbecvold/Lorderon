quest pacholek_dialog begin
	state start begin
		when 20349.chat."Informace o mountech " begin
			say_title("Pacholek")
			say("Mounta mùeš vylepšovat pergameny nebo u kováøe. ")
			say(" ")
			say_yellow("Uppky získáš v Opièím dungeonu. ")
		end
		when 20349.chat."Informace o mazlíècích " begin
			say_title("Pacholek")
			say("mazlíèka mùeš vylepšovat pergameny nebo u kováøe. ")
			say(" ")
			say_yellow("Uppky získáš v Opièím dungeonu. ")
		end
	end
end

