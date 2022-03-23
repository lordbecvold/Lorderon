quest yang_shin begin
	state start begin
		when 20019.chat."Opièí jeskynì (30-55 Lvl) " begin
		if pc.get_level() < 30 then
			say_title(" Strážce opièí jeskynì ")
			say(" Tvá úroveò je pøíliš nízká ")
		elseif pc.get_level() > 55 then
			say_title(" Strážce opièí jeskynì ")
			say(" Tvá úroveò je pøíliš vysoká ")
		else
			pc.warp(768000, 435200)	
			end
		end
		when 20019.chat."Opièí jeskynì 2 (55-75 Lvl) " begin
		if pc.get_level() < 55 then
			say_title(" Strážce opièí jeskynì ")
			say(" Tvá úroveò je pøíliš nízká ")
		elseif pc.get_level() > 75 then
			say_title(" Strážce opièí jeskynì ")
			say(" Tvá úroveò je pøíliš vysoká ")
		else
			pc.warp(128000, 640000)	
			end
		end
		when 20019.chat."Opièí jeskynì 3 (75-95 Lvl) " begin
		if pc.get_level() < 75 then
			say_title(" Strážce opièí jeskynì ")
			say(" Tvá úroveò je pøíliš nízká ")
		elseif pc.get_level() > 95 then
			say_title(" Strážce opièí jeskynì ")
			say(" Tvá úroveò je pøíliš vysoká ")
		else
			pc.warp(128000, 716800)	
			end
		end
		when 20019.chat."Draèí chrám (75-105 Lvl) " begin
		if pc.get_level() < 75 then
			say(" Tvá úroveò je pøíliš nízká ")
		elseif pc.get_level() > 105 then
			say(" Tvá úroveò je pøíliš vysoká ")
		else
			pc.warp(819200, 1049600)	
			end
		end
		when 20019.chat."Vìž démonù (40-105 Lvl) " begin
		if pc.get_level() < 40 then
			say(" Tvá úroveò je pøíliš nízká ")
		elseif pc.get_level() > 105 then
			say(" Tvá úroveò je pøíliš vysoká ")
		else
			pc.warp(590500, 110500)	
			end
		end
		when 20019.chat."Razadorova pevnost (100-120 Lvl) " begin
		if pc.get_level() < 100 then
			say(" Tvá úroveò je pøíliš nízká ")
		elseif pc.get_level() > 120 then
			say(" Tvá úroveò je pøíliš vysoká ")
		else
			pc.warp(742400, 614400)	
			end
		end
		when 20019.chat."Nemerova pevnost (100-120 Lvl) " begin
		if pc.get_level() < 100 then
			say(" Tvá úroveo je poíliš nízká ")
		elseif pc.get_level() > 120 then
			say(" Tvá úroveo je poíliš vysoká ")
		else
			pc.warp(512000, 153600)	
			end
		end
	end
end