quest nemere_dung begin
	state start begin
		when 20395.chat."Nemerova pevnost (100-120 Lvl) " begin
		if pc.get_level() < 100 then
			say(" Tvá úroveò je pøíliš nízká ")
		elseif pc.get_level() > 120 then
			say(" Tvá úroveò je pøíliš vysoká ")
		else
			pc.warp(512000, 153600)	
			end
		end
	end
end
