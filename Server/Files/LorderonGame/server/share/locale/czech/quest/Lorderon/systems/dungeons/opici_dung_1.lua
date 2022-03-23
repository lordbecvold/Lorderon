quest opici_dung_port begin
	state start begin
		when 20369.chat."Opièí jeskynì (30-55 Lvl) " begin
		if pc.get_level() < 30 then
			say_title(" Stráce opièí jeskynì ")
			say(" Tvá úroveò je pøíliš nízká ")
		elseif pc.get_level() > 55 then
			say_title(" Stráce opièí jeskynì ")
			say(" Tvá úroveò je pøíliš vysoká ")
		else
			pc.warp(768000, 435200)	
			end
		end
		when 20369.chat."Opièí jeskynì 2 (55-75 Lvl) " begin
		if pc.get_level() < 55 then
			say_title(" Stráce opièí jeskynì ")
			say(" Tvá úroveò je pøíliš nízká ")
		elseif pc.get_level() > 75 then
			say_title(" Stráce opièí jeskynì ")
			say(" Tvá úroveò je pøíliš vysoká ")
		else
			pc.warp(128000, 640000)	
			end
		end
		when 20369.chat."Opièí jeskynì 3 (75-95 Lvl) " begin
		if pc.get_level() < 75 then
			say_title(" Stráce opièí jeskynì ")
			say(" Tvá úroveò je pøíliš nízká ")
		elseif pc.get_level() > 95 then
			say_title(" Stráce opièí jeskynì ")
			say(" Tvá úroveò je pøíliš vysoká ")
		else
			pc.warp(128000, 716800)	
			end
		end
	end
end
