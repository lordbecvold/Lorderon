quest kovar_dialog begin
	state start begin
		when 20016.chat."Jak se vylepšují pøedmety?" begin
			say("Pøeješ si Zlepšit nejaký pøedmet? ")
			say("Nu. Dobrá ale mysli na to že se to také nemusí podaøit. ")
			say("Dej mi ho a já se o to za menší poplatek pokusím. ")
			say(" ")
			say("Ale pokud se bojíš je tu druhá možnost, Požehnaný pergamen. ")
			say("Pøi použití pergamenu se pøi neúspìchu pouze sníží úroveò. ")
			say("pøedmetu o jeden bod. ")
			say("Další možnost je pøíruèka, Pøi jejím použítí stoupá šance na úspech o 20%. ")
			say(" ")
			say("Ale pokud se opravdu o svùj pøedmet obáváš mužeš použít     magický kámen. ")
			say("pøi jeho použití nehrozí ani ztráta ani snížení úrovnì. ")
		end
	end
end