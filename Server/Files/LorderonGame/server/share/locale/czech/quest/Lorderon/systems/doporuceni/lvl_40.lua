quest lvl_40 begin
	state start begin
		when levelup with pc.level == 40 begin
			say_title("Doporu�en�.")
			say("Nezapom�nej d�lat �koly bossologie! ")
			say_yellow("Za �koly Bossologie dostane� trval� bonusy, ")
			say_yellow("kter� pos�l� tvou postavu." )
			say(" ")
			say_yellow("Tak� nezapom�nej na Biologick� v�zkum!")
			say_yellow("Najde� ho v invent��i pod tla��tkem �ipky v lev� stran� okna. ")
		end
	end
end