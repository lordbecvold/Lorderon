quest lvl_75 begin
	state start begin
		when levelup with pc.level == 75 begin
			say_title("V�born� dos�hl jsi �rovn� 75!")
			say("Otev�ela se ti nov� lokace")
			say_yellow("Jeskyn� vyhnanstv� ")
			say(" ")
			say_green("Nov� set zbran�, brn�n� a �perk�, z�sk� ve v�i d�mon� ")
			say_green("Ve� d�mon� najde� v chr�mu hwang. ")
		end
	end
end