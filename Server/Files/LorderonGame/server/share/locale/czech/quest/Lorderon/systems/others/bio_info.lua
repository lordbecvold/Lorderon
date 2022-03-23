quest bio_info begin
	state start begin
		when 20084.chat."Informace o výzkumu " begin
			say_title("Biolog")
			say("Každých 10 úrovní mùže plnit biologocký úkol ")
			say("První úkol dostaneš na úrovni 30")
			say("Za splnìní dostaneš trvalé bonusy ")
			say_yellow("Biologický výzkum najdeš v inventáøi pod tlaèítkem šipky na levé stranì okna. ")
		end
	end
end

