quest beran_setau_port begin
	state start begin
		when 30121.chat."Dra�� chr�m (75-105 Lvl) " begin
		if pc.get_level() < 75 then
			say(" Tv� �rove� je p��li� n�zk� ")
		elseif pc.get_level() > 105 then
			say(" Tv� �rove� je p��li� vysok� ")
		else
			pc.warp(819200, 1049600)	
			end
		end
	end
end

