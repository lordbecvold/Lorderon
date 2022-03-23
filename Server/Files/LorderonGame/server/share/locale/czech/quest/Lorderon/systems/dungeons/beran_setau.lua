quest beran_setau_port begin
	state start begin
		when 30121.chat."Draèí chrám (75-105 Lvl) " begin
		if pc.get_level() < 75 then
			say(" Tvá úroveò je pøíliš nízká ")
		elseif pc.get_level() > 105 then
			say(" Tvá úroveò je pøíliš vysoká ")
		else
			pc.warp(819200, 1049600)	
			end
		end
	end
end

